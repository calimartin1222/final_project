from django.shortcuts import render
from tools.forms import per_day_form, grade_recieved_form
from datetime import datetime, date

# Create your views here.
def home(request):
    return render(request, 'tools/home.html')

def per_day(request):
    #checks the way the user got to the page
    #if it was a POST method, execute the following code
    if request.method == "POST":
        #creates a new form object that is based off of a custom form called
        #per_day_form from forms.py
        form = per_day_form(request.POST)
        if form.is_valid():
            #checks if there's anything wrong with the user input (ex. SQL inserts)
            #sets the various user inputs to useful variables
            amt = int(form['amount'].value())
            m = int(form['due_date_month'].value())
            d = int(form['due_date_day'].value())-1
            y = int(form['due_date_year'].value())
            #gets current date
            now = date.today()
            #sets variable due_date as a datetime object the curent year, but the
            #month and date of the user input
            due_date = date(y, m, d)
            #gets the difference between the current date and the due date
            delta = due_date - now
            #divides amount user has included by days until due date to get a per day
            #amount they must do
            per = amt/(delta.days)
            #sets variable result as message with the result of the operations above
            result = f'You must do {per} per day, starting today, to finish in time'
            #passes the variable result to the html template
            button = 'Calculate another assignment!'

            args = {'form': '',
                'result': result,
                'button' : button,
                'button_link': '/per_day',
                'button_type': 'button',
            }

            return render(request, 'tools/per_day.html', args)
    #if the request was not a POST method (GET), execute the following code
    else:
        #creates a new, blank per day form for the user to fill out
        form = per_day_form()
        #renders per_day.html in the tools folder in the templates
        #folder, and passes the variable form as an argument
        args = {'form': form,
            'result': '',
            'button' : 'Calculate!',
            'button_link': '',
            'button_type': 'submit',
        }
        return render(request, 'tools/per_day.html', args)

def grade_recieved(request):
    #checks the way the user got to the page
    #if it was a POST method, execute the following code
    if request.method == 'POST':
        #creates a new form object that is based off of a custom form called
        #grade_recieved_form from forms.py
        form = grade_recieved_form(request.POST)
        #checks if there's anything wrong with the user input (ex. SQL inserts)
        if form.is_valid():
            #sets the various user inputs to useful variables
            percent = int(form['grade'].value())
            total = int(form['points_possible'].value())
            #divides the user input grade by 100 to get decimal equivalent
            grade = percent/100
            #mutiplies the grade as a decimal by the total possible questions
            missed = total - (grade * total)
            #sets variable result as message with the result of the operations above
            result = f'You missed {missed} question(s)'
            #passes the variable result to the html template
            return render(request, 'tools/results.html', {'result': result})
    #if the request was not a POST method (GET), execute the following code
    else:
        #creates a new, blank grade recieved form for the user to fill out
        form = grade_recieved_form()
        #renders grade_recieved.html in the tools folder in the templates
        #folder, and passes the variable form as an argument
        return render(request, 'tools/grade_recieved.html', {'form': form})

def semester_grade(request):
    #renders the semester_grade.html file
    return render(request, 'tools/semester_grade.html')

def tasklist(request):
    #renders the tasklist.html file
    return render(request, 'tools/tasklist.html')

def timer(request):
    #renders the timer.html file
    return render(request, 'tools/timer.html')