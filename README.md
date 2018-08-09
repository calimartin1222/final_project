# Final Project

Web Programming with Python and JavaScript

Description:

This web app is a collection of tools that allows users to log in or register
if they don't have an account, edit their 'profile', and log out. The tools
include a way to calculate
their semester grade (this is based on my home county's, Broward County in
Florida, grading scale), a time manager that allows the user to input a due date
and number of tasks they must accomplish (i.e. math problems or pages to read) and
outputs how many they should do a day as milestones to avoid last minute cramming.
Some other tools are a pomodoro timer (study timer with breaks built in), a task list
specific to the currently logged in user, a calculator that tells the user how many
questions they missed on an test or quiz based on a percentage grade and total number
of questions possible (This could also be used by the student to find out how many
questions they can miss to get a certain grade before taking the actual test),


Most of these tools already exist in one capacity or another on
other seperate websites. My goal with this website is to have all of these features in one
place and make it more efficient for students to succeed in school.

File Descriptions:

Account App:

account/static/account/menu.js - javascript that manipulates the elements on and keeps
track of Events on the order.html page

account/static/account/style.css - makes a couple elements more aesthetically pleasing

account/templates/account/index.html - the page the user is brought to when they login;
a simple welcome page

account/templates/account/directions, hours, sicilianVSreg, contact.html - these are
multiple html pages that just extend base.html and display simple information taken
from Pinocchio's website

account/templates/account/login.html - shows user login form

account/templates/account/logout.html - logs the user out and shows user a goodbye message

account/templates/account/registerForm.html - shows user registration form

account/templates/account/base.html - base template all html files extend from;
includes banner, navbar, and basic page body setup

account/admin.py - logs all the models to be accessed via /admin

account/forms.py - pesonalized forms extending django registration and login forms

account/models.py - user database set up

account/urls.py - sets up url paths

account/views.py - defines functions that are called in urls.py when the user visits certain urls

Orders App:

orders/templates/orders/cart.html - shows user's cart

orders/templates/orders/index.html - actual homepage of the web app

orders/templates/orders/order.html - shows user ordering form

orders/admin.py - logs all the models to be accessed via /admin

orders/models.py - Order, toppings and menu_item database set up

orders/urls.py - sets up url paths

orders/views.py - defines functions that are called in urls.py when the user visits certain urls