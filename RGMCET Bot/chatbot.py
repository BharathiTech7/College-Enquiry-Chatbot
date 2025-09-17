from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Creating ChatBot Instance with SQLite
chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to RGMCET! 👋 If you need any assistance, I'm always here. Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(chatbot)

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"Helloo!",
"Hey",

"Who are you?",
"I am your friendly College Enquiry Chatbot 🤖✨. I can help you with information about RGMCET, like courses, fees, hostel, scholarships, and more.",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br>1.&emsp;Student's Section Enquiry.</br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"You're Welcome 😄",

"Thanks",
"You're Welcome 😄",

"Bye",
"Thank You for visiting!..",

"Is there a hostel available in RGMCET?",
"Yes, RGMCET provides separate hostels for boys and girls with good facilities.",

"Is there Wi-Fi in the hostel rooms?",
"Yes, Wi-Fi is available in both hostel rooms and common areas.",

"Are visitors allowed in the hostel?",
"Visitors are allowed during specified visiting hours with proper permissions from hostel authorities.",

"Is there a mess in the hostel? What are the timings?",
"Yes, the hostel has a mess. Breakfast: 7-9 AM, Lunch: 12-2 PM, Dinner: 7-9 PM (timings may vary).",


"What are the hostel rules and regulations?",
"Students must maintain discipline, follow mess timings, keep rooms clean, and adhere to hostel rules. Violations may lead to strict action.",

"Tell me about RGMCET college",
"Rajeev Gandhi Memorial College of Engineering and Technology (RGMCET) is an autonomous institution located in Nandyal, Andhra Pradesh. It offers UG, PG, and Ph.D. programs in engineering, management, and sciences. The college is accredited by NAAC and NBA.",

"What do you do?",
"I am made to give Information about RGMCET college.",

"Give me details about RGMCET",
"Rajeev Gandhi Memorial College of Engineering and Technology (RGMCET) is an autonomous institution located in Nandyal, Andhra Pradesh. It offers UG, PG, and Ph.D. programs in engineering, management, and sciences. The college is accredited by NAAC and NBA.",

"Where is RGMCET located?",
"RGMCET is located in Nandyal, Andhra Pradesh, India.",

"Who is the chairman of RGMCET?",
"The Chairman of Rajeev Gandhi Memorial College of Engineering and Technology (RGMCET) is **Dr. M. Santhiramudu**, who is also the founder of the institution.",

"Tell me the chairman of RGMCET",
"The Chairman of RGMCET is **Dr. M. Santhiramudu**.",

"Chairman of RGMCET?",
"The current Chairman of RGMCET is **Dr. M. Santhiramudu**.",

"Is bus facility available for RGMCET?",
"Yes , RGMCET provides bus facilities for students and staff. The college operates a fleet of buses covering Nandyal and nearby towns for convenient and safe transportation.",

"Does RGMCET provide transport facility?",
"Yes , RGMCET offers transport facilities with buses covering Nandyal and nearby areas for students and staff.",

"Bus facility in RGMCET?",
"Yes, the college provides well-maintained bus services to various routes around Nandyal.",


# Principal
"who is the principal of RGMCET?",
"The principal is Dr. T. Jayachandra Prasad. You can contact him at principal.9@jntua.ac.in",

# Courses Offered
"what courses does RGMCET offer?",
"RGMCET offers undergraduate courses in Engineering like CSE, ECE, EEE, ME, Civil, and postgraduate courses like M.Tech and MBA.",

# Fee Structure
"what is the fee structure of RGMCET?",
"The fee structure at RGMCET varies per course. For example, B.Tech courses are around ₹1,00,000 per year. Exact fees can be checked on the official website.",

# Scholarships
"Does RGMCET provide scholarships?",
"Yes, RGMCET offers scholarships for meritorious students and government scholarship schemes.",

# Hostel
"Does RGMCET have a hostel?",
"Yes, RGMCET has hostel facilities for both boys and girls with mess and other amenities.",
# Library
"Does RGMCET have a library?",
"Yes, RGMCET has a well-equipped library with books, journals, and digital resources.",
# Contact Info
"What is the contact information of RGMCET?",
"You can contact RGMCET at +91-9866308422 or email info@rgmcet.edu.in.",
# Website
"What is the official website of RGMCET?",
"The official website of RGMCET is https://www.rgmcet.edu.in/",

"What else can you do?",
"I can help you know more about RGMCET",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Academic Calendar <br>1.1.2 Syllabus </b>",
    "1.1.1",
    "<b> 1.1.1 Academic Calendar<br>The link to Academic Calendar 👉 <a href='https://rgmexams.co.in/Examinations.php'>Click Here</a> </b>",
    "1.1.2",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href='https://www.rgmcet.edu.in/academics'>Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 Student Chapters <br> 1.2.3 Student's Council</b>",
    "1.2.1",
    "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'https://www.rgmcet.edu.in/TAP_newsevents' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 Student Chapters<br>The link to Student Chapters👉<a href=" 'https://www.rgmcet.edu.in/media' ">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 Student's Council <br>The link to Student's Council👉 <a href=" 'https://www.rgmcet.edu.in/student%20clubs' ">Click Here</a> </b>",

    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Portal<br> 1.3.2 Notices </b>",
    "1.3.1",
    "<b> 1.3.1 Students Portal<br>The link to Students Portal👉 <a href=" 'https://rgmexams.co.in/Login.php' ">Click Here</a> </b>",
    "1.3.2",
    "<b> 1.3.2 Notices<br>The link to Notices👉 <a href=" 'https://rgmexams.co.in/Examinations.php' ">Click Here</a> </b>",

    "1.4",
    "<b> EXAMINATION <br>These are the top results:<br> 1.4.1 Notices<br> 1.4.2 Examination Process <br> 1.4.3 Results <br></b>",
    "1.4.1",
    "<b > 1.4.1 Notices<br>The link to Notices👉 <a href=" 'https://rgmexams.co.in/Examinations.php' ">Click Here</a> </b>",
    "1.4.2",
    "<b > 1.4.2 Examination Process<br>The link to Examination Process👉<a href=" 'https://www.rgmcet.edu.in/exams-section' ">Click Here</a> </b>",
    "1.4.3",
    "<b> 1.4.3 Results<br>The link to Results 👉 <a href='https://rgmexams.co.in/Login.php'>Click Here</a> </b>",
    
    "1.5",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Our Recruiters <br> 1.5.3 Placement Statistics </b>",
    "1.5.1",
    "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'https://www.rgmcet.edu.in/about_tap' ">Click Here</a> </b>",
    "1.5.2",
    "<b> 1.5.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://www.rgmcet.edu.in/Placement_Records' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 1.5.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://www.rgmcet.edu.in/Placement_Records' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2 Staff Bus Registration Fee<br>2.3  Examination </b>",
    
    "2.1",
    "<b > PORTALS & ADMINISTRATION These are the top results:<br> 2.1.1 Faculty Login <br>2.1.2 Departments </b>",
    "2.1.1",
    "<b> 2.1.1 Faculty Login<br>The link to Faculty Login👉<a href=" 'https://www.rgmcet.edu.in/rgmwebsite/index.php' ">Click Here</a> </b>",
    "2.1.2",
    "<b> 2.1.2 Departments<br>The link to all departments 👉 <a href=" 'https://www.rgmcet.edu.in/department-of-ce' ">Click Here</a> </b>",

    "2.2",
    "<b > STAFF BUS REGISTRATION FEE These are the top results:<br> <br> 2.2.1 Site Login <br> </b>",
    "2.2.1",
    "<b> 2.2.1 Site Login<br>The link to Site Login👉<a href=" 'https://administration.rgmcet.edu.in/Bus_Application_StaffNew.php' ">Click Here</a> </b>",
   
    "2.3",
    "<b > EXAMINATION <br>These are the top results:<br> <br> 2.3.1 Notices<br> ",
    "2.3.1",
    "<b> 2.3.1 Notices <br>The link to Notices 👉 <a href=" 'https://rgmexams.co.in/Examinations.php' ">Click Here</a> </b>",
      
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements <br>3.5 Anti-Ragging <br>3.6 Results</b> " ,

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About RGMCET<br> 3.1.2 Management <br> 3.1.3 Contact Us </b>",
    "3.1.1",
    "<b > 3.1.1 About RGMCET<br>The link to About RGMCET👉 <a href=" 'https://www.rgmcet.edu.in/about-us' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Management <br>The link to Management👉<a href='https://www.rgmcet.edu.in/ugc'>Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Contact Us <br>The link to Contact Us👉 <a href=" 'https://www.rgmcet.edu.in/contact' ">Click Here</a> </b>",

    "3.2",
    "<b > TRANSPORTATION<br>These are the top results:<br> <br> 3.2.1 Transportation Details </b>",
    "3.2.1",
    "<b > 3.2.1 Transportation Details <br>The link to Transportation Details👉 <a href=" 'https://www.rgmcet.edu.in/transportation' ">Click Here</a> </b>",

    "3.3",
    "<b > BUS FEE PAYMENT<br>These are the top results:<br> <br>3.3.1 Bus Application <br> 3.3.2 Online Payment Portal </b>",
    "3.3.1",
    "<b > 3.3.1 Bus Application<br>The link to Payment Details 👉 <a href=" 'https://administration.rgmcet.edu.in/Bus_Application.php' ">Click Here</a> </b>",
    "3.3.2",
    "<b > 3.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://administration.rgmcet.edu.in/' ">Click Here</a> </b>",

    "3.4",
    "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
    "3.4.1",
    "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'https://www.rgmcet.edu.in/about_tap' ">Click Here</a> </b>",
    "3.4.2",
    "<b> 3.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://www.rgmcet.edu.in/Placement_Records' ">Click Here</a> </b>",
    "3.4.3",
    "<b > 3.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://www.rgmcet.edu.in/Placement_Records' ">Click Here</a> </b>",

    "3.5",
    "<b > ANTI-RAGGING<br>These are the top results:<br> <br>3.5.1 Anti-Ragging Committee </b>",
    "3.5.1",
    "<b > 3.5.1 Anti-Ragging Committee<br>The link 👉 <a href=" 'https://www.rgmcet.edu.in/anti-ragging' ">Click Here</a> </b>",
    
    "3.6",
    "<b> 3.6 Results<br>The link to Student Results 👉 <a href='https://rgmexams.co.in/Login.php'>Click Here</a> </b>",

    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular <br>4.5 Careers @ RGMCET </b>",
    
    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About RGMCET<br> 4.1.2 Our History <br> 4.1.3 Contact Us </b>",
    "4.1.1",
    "<b > 4.1.1 About RGMCET<br>The link to About RGMCET👉 <a href=" 'https://www.rgmcet.edu.in/about-us' ">Click Here</a> </b>",
    "4.1.2",
    "<b > 4.1.2 Our History <br>The link to Director's Address👉<a href=" 'https://www.rgmcet.edu.in/about-us' ">Click Here</a> </b>",
    "4.1.3",
    "<b > 4.1.3 Contact Us <br>The link to Contact Us👉 <a href=" 'https://www.rgmcet.edu.in/contact' ">Click Here</a> </b>",

    "4.2",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Ph.D </b>",
    "4.2.1",
    "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://www.rgmcet.edu.in/courses_offered1' ">Click Here</a> </b>",
    "4.2.2",
    "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://www.rgmcet.edu.in/courses_offered1' ">Click Here</a> </b>",
    "4.2.3",
    "<b > 4.2.3 Ph.D <br>The link to Ph.D👉 <a href=" 'https://www.rgmcet.edu.in/courses_offered1' ">Click Here</a> </b>",

    "4.3",
    "<b > STUDENT BODIES <br>These are the top results:<br> <br>4.3.1 Students Council  <br> 4.3.2 Students Chapter <br> 4.3.3 Students Project Groups </b>",
    "4.3.1",
    "<b > 4.3.1 Students Council  <br>The link to Students Council  👉 <a href=" 'https://www.rgmcet.edu.in/student%20clubs' ">Click Here</a> </b>",
    "4.3.2",
    "<b > 4.3.2 Students Chapter <br>The link to Students Chapter 👉<a href=" 'https://www.rgmcet.edu.in/media' ">Click Here</a> </b>",
    "4.3.3",
    "<b > 4.3.3 Rgmcet Project  <br>The link to Rgmcet Project 👉 <a href=" 'https://www.rgmcet.edu.in/projects' ">Click Here</a> </b>",

    "4.4",
    "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 RGMECT RAYS  <br> 4.4.2 Women Empowerment Cell </b>",
    "4.4.1",
    "<b > 4.4.1 RGMECT RAYS <br>The link to Events   👉 <a href=" 'https://www.rgmcet.edu.in/magazine' ">Click Here</a> </b>",
    "4.4.2",
    "<b > 4.4.2 Women Empowerment  Cell <br>The link to Institute Innovation Cell 👉<a href=" 'https://www.rgmcet.edu.in/women' ">Click Here</a> </b>",

    "4.5",
    "<b > CAREERS @ RGMCET<br>These are the top results:<br> <br>4.5.1 Job Openings <br> 4.5.2 Apply Online </b>",
    "4.5.1",
    "<b > 4.5.1 Job Openings<br>The link 👉 <a href="'https://www.rgmcet.edu.in/careers'">Click Here</a> </b>",
    "4.5.2",
    "<b > 4.5.2 Apply Online<br>The link 👉 <a href=" 'https://www.rgmcet.edu.in/careers' ">Click Here</a> </b>",

]

trainer.train(conversation)
