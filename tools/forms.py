from django import forms

class per_day_form(forms.Form):
    #sets different field for per_day_form
    amount = forms.IntegerField(max_value=200, min_value=0)
    due_date_month = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)], label='Due Date')
    due_date_day = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)], label='/   ', label_suffix="")
    due_date_year = forms.ChoiceField(choices=[(x, x) for x in range(2018, 2051)], label='/   ', label_suffix="")
    # gets clean data from field user inputs
    def clean(self):
        cleaned_data = super(per_day_form, self).clean()
        amount = cleaned_data.get('amount')
        due_date_month = cleaned_data.get('due_date_month')
        due_date_day = cleaned_data.get('due_date_day')
        due_date_year = cleaned_data.get('due_date_year')
        # raise error if user did not fill in one or more fields
        if not due_date_month and not due_date_day and not due_date_year and not amount:
            raise forms.ValidationError('Please enter all fields')

class grade_recieved_form(forms.Form):
    #sets different field for grade_recieved_form
    grade = forms.IntegerField(label='Percent', max_value=100, min_value=0)
    points_possible = forms.IntegerField(label='Points Possible', max_value=200, min_value=0)
    # gets clean data from field user inputs
    def clean(self):
        cleaned_data = super(grade_recieved_form, self).clean()
        grade = cleaned_data.get('grade')
        points_possible = cleaned_data.get('points_possible')
        # raise error if user did not fill in one or more fields
        if not points_possible and not grade:
            raise forms.ValidationError('Please enter all fields')
