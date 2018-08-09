# Final Project

Web Programming with Python and JavaScript

Description:

This web app is a collection of tools that allows users to log in or register
if they don't have an account, edit their 'profile', and log out. The tools
include a way to calculate their semester grade (this is based on my home
county's, Broward County in Florida, grading scale), a time manager that allows
the user to input a due date and number of tasks they must accomplish (i.e.
math problems or pages to read) and outputs how many they should do a day as
milestones to avoid last minute cramming. Some other tools are a pomodoro timer
(study timer with breaks built in), a task list specific to the currently logged
in user, a calculator that tells the user how many questions they missed on an
test or quiz based on a percentage grade and total number of questions possible
(This could also be used by the student to find out how many questions they can
miss to get a certain grade before taking the actual test), and a calendar to
make notes on. Most of these tools already exist in one capacity or another on
other seperate websites. My goal with this website is to have all of these
features in one place and make it more efficient for students to succeed in school.

File Descriptions:

Account App:

account/static/aplus_logo.png - simple vector I made for favicon and navbar logo

account/templates/account/index.html - the page the user is brought to when they login;
a simple profile page with a link to edit some information

account/templates/account/edit.html - the page the user is brought to when they edit
their profile with a simple form

account/templates/account/login.html - shows user login form

account/templates/account/logout.html - logs the user out and shows user a goodbye message

account/templates/account/register.html - shows user registration form

account/templates/account/base.html - base template all html files extend from;
includes navbar and basic page body setup

account/admin.py - logs the model to be accessed via /admin

account/forms.py - pesonalized forms extending django registration and login forms

account/models.py - user database set up

account/urls.py - sets up url paths

account/views.py - defines functions that are called in urls.py when the user visits certain urls

Tools App:

tools/templates/tools/calendar.html - shows user a calendar that they can add notes to

tools/templates/tools/home.html - homepage of the web app

tools/templates/tools/grade_recieved.html - shows user form to input information and they get a result
back based on a calculation for grade recieved

tools/templates/tools/per_day.html - shows user form to input information and they get a result
back based on a calculation for per day

tools/templates/tools/semester_grade.html - simple but dynamic semester grade calculator
based on Broward County schools grade points

tools/templates/tools/results.html - shows user form a result back based on a calculation

tools/templates/tools/tasklist.html - allows the user to make a list of tasks and check
them off and delete when done

tools/templates/tools/timer.html - allows the user to time themselves studying and
taking breaks using the pomodoro technique

tools/forms.py - per-day and grade-recieved forms set up

tools/urls.py - sets up url paths

tools/views.py - defines functions that are called in urls.py when the user visits certain urls