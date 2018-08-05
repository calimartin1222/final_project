from django.shortcuts import render
from tools.forms import per_day_form, grade_recieved_form
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'tools/home.html')

def per_day(request):
    if request.method == 'POST':
        form = per_day_form(request.POST)
        if form.is_valid():
            amt = int(form['amount'].value())
            m = int(form['due_date_month'].value())
            d = int(form['due_date_day'].value())
            y = int(form['due_date_year'].value())

            now = datetime.now()
            due_date = datetime(now.year, m, d)
            delta = due_date - now


            per = amt/delta

            result = f'You must do {per.days} per day to finish in time'

            #f"{m}/{d}/{y}"

            return render(request, 'tools/results.html', {'result': result})
    else:
        form = per_day_form()
        return render(request, 'tools/per_day.html', {'form': form})

def grade_recieved(request):
    if request.method == 'POST':
        form = grade_recieved_form(request.POST)
        if form.is_valid():
            percent = int(form['grade'].value())
            total = int(form['points_possible'].value())

            grade = percent/100

            missed = total - (grade * total)

            result = f'You missed {missed} question(s)'

            return render(request, 'tools/results.html', {'result': result})
    else:
        form = grade_recieved_form()
        return render(request, 'tools/grade_recieved.html', {'form': form})
