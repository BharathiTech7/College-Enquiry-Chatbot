from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_recaptcha import ReCaptcha
from markupsafe import Markup
import flask_recaptcha
import mysql.connector
import os
# === Chatbot + Gemini Integration ===
from chatterbot import ChatBot
import google.generativeai as genai
from dotenv import load_dotenv

# --- Fix for flask_recaptcha missing Markup ---
flask_recaptcha.Markup = Markup

load_dotenv()

# === Flask App Setup ===
app = Flask(__name__)
recaptcha = ReCaptcha(app=app)
app.secret_key = os.getenv("SECRET_KEY")
app.static_folder = "static"

# ReCaptcha config
app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY=os.getenv("RECAPTCHA_SITE_KEY"),
    RECAPTCHA_SECRET_KEY=os.getenv("RECAPTCHA_SECRET_KEY")
))
recaptcha.init_app(app)

# Secret key for sessions
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


# === Database Connection Function ===
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB"),
        port=int(os.getenv("MYSQL_PORT", 3306)),
        ssl_disabled=os.getenv("MYSQL_SSL_DISABLED", "False") == "True"
    )



# === Routes ===
@app.route("/")
def login():
    return render_template("login.html")


@app.route("/index")
def home():
    if "id" in session:
        return render_template("index.html")
    else:
        return redirect("/")


@app.route("/register")
def about():
    return render_template("register.html")


@app.route("/forgot")
def forgot():
    return render_template("forgot.html")


# Login validation
@app.route("/login_validation", methods=["POST"])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        users = cur.fetchall()
        cur.close()
        conn.close()

        if len(users) > 0:
            session["id"] = users[0][0]
            flash("You were successfully logged in", "success")
            return redirect("/index")
        else:
            flash("Invalid credentials !!!", "danger")
            return redirect("/")
    except Exception as e:
        print("DB Error:", e)
        flash("Database connection failed", "danger")
        return redirect("/")


# Register new user
@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("uemail")
    password = request.form.get("upassword")

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s)", (name, email, password))
        conn.commit()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        myuser = cur.fetchall()
        cur.close()
        conn.close()

        flash("You have successfully registered!")
        session["id"] = myuser[0][0]
        return redirect("/index")
    except Exception as e:
        print("DB Error:", e)
        flash("Registration failed", "danger")
        return redirect("/register")


# Suggestion form
@app.route("/suggestion", methods=["POST"])
def suggestion():
    email = request.form.get("uemail")
    suggesMess = request.form.get("message")

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO suggestion(email, message) VALUES(%s, %s)", (email, suggesMess))
        conn.commit()
        cur.close()
        conn.close()

        flash("Your suggestion is successfully sent!")
        return redirect("/index")
    except Exception as e:
        print("DB Error:", e)
        flash("Failed to send suggestion", "danger")
        return redirect("/index")


# Recaptcha test route
@app.route('/add_user', methods=['POST'])
def register():
    if recaptcha.verify():
        flash("New User Added Successfully")
        return redirect("/register")
    else:
        flash("Error Recaptcha")
        return redirect("/register")


@app.route("/logout")
def logout():
    session.pop("id", None)
    return redirect("/")


# Forgot password update
@app.route("/forgot_password", methods=["POST"])
def forgot_password():
    email = request.form.get("uemail")
    new_password = request.form.get("upassword")

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE users SET password=%s WHERE email=%s", (new_password, email))
        conn.commit()
        cur.close()
        conn.close()

        flash("Password updated successfully!", "success")
        return redirect("/")
    except Exception as e:
        print("DB Error:", e)
        flash("Password reset failed", "danger")
        return redirect("/forgot")


# === Gemini + Chatbot Setup ===
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Import trained chatbot from chatbot.py
from chatbot import chatbot


@app.route("/chat")
def chat():
    if "id" in session:
        return render_template("index.html")  # chatbot page
    else:
        return redirect("/")


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    bot_response = chatbot.get_response(userText)

    if float(bot_response.confidence) > 0.6:
        return str(bot_response)

    # Gemini fallback with context
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(
        f"You are an assistant for Rajeev Gandhi Memorial College of Engineering & Technology (RGMCET), Nandyal, Andhra Pradesh. "
        f"Always give correct and helpful information about RGMCET only. "
        f"Question: {userText}"
    )
    return response.text


# === Run App ===
if __name__ == "__main__":
    app.run(debug=False)
