from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class registration_form(UserCreationForm):
    #adds email field to default registration form
    email = forms.EmailField(required=True)
    #other details about the modified form
    class Meta:
        #the model the class is referencing is the default django 'User' model
        model = User
        #specifies exactly what fields to use from UserCreationForm
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        #sets variable user equal to a registration that has not been saved
        user = super(registration_form, self).save(commit = False)

        #makes sure the info from the user input is safe to put into databases
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']

        #checks if the form has been committed
        if commit:
            user.save()
        #returns user information to use later
        return user

class edit_profile_form(UserChangeForm):

    class Meta:
        #the model the class is referencing is the default django 'User' model
        model = User
        #specifies what fields to that the user can edit from UserCreationForm
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )