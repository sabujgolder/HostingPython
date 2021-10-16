from django import forms
from django.core import validators
from myapp2 import models

def even_checker(value):
    if value % 2 == 1:
        raise forms.ValidationError("Please Insert an even number")



class validator_form(forms.Form):

    name = forms.CharField(validators = [validators.MaxLengthValidator(10)])
    any_id = forms.IntegerField(validators = [validators.MaxValueValidator(500)])
    number = forms.IntegerField(validators=[even_checker])

    email = forms.EmailField()
    vmail = forms.EmailField()

    def clean(self):

        all_cleaned_data = super().clean()

        email = all_cleaned_data['email']
        vmail = all_cleaned_data['vmail']

        if email != vmail :
            raise forms.ValidationError("Emails Doesn't Match")

class FormForNewUser(forms.ModelForm):
    class Meta:
        model = models.NewUserForm
        fields = '__all__'
        widgets = {
            # 'username': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'comment' : forms.Textarea,
            'city' : forms.RadioSelect,
            'Birthday' : forms.TextInput(attrs={'type':'date'}),
            'Radio' : forms.RadioSelect()
        }
        labels = {
            'username': 'Full Name',
            'city' : ' Whats Your CIty',
            'captcha_answer' : ' 2 + 2 ',
        }
        help_texts = {
            'comment': "What's in your mind!!",
            'Another_comment':'Enter Your Comment'
        }

        def clean(self):

            all_cleaned_data = super().clean()

            email = all_cleaned_data['email']
            vmail = all_cleaned_data['vmail']
            if email != vmail :
                raise forms.ValidationError("Emails Doesn't Match")
