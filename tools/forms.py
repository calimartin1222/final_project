from django import forms
import datetime

class per_day_form(forms.Form):

    amount = forms.IntegerField(required=True)
    due_date = forms.DateField(auto_now=False)

    def save(self, commit=True):
        per_day = super(per_day_form, self).save(commit = False)

        amount = self.cleaned_data['amount']
        due_date = self.cleaned_data['due_date']

        if commit:
            user.save()

        args = {
            'amount': amount,
            'due_date': due_date,
        }

        return args