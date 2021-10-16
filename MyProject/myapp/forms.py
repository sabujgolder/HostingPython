from django import forms

class UserForm(forms.Form):

    choices = (
                ('','SELECT OPTIONS'),
                ('1','Dhaka'),
                ('2','Khulna')
    )

    cho = (
                ('Dhaka','Dhaka'),
                ('Khulna','Khulna'),
                ('Jessore','Jessore')
    )
    username = forms.CharField(label="Full Name",initial="Type Username",required=False)
    comment = forms.CharField(widget=forms.Textarea,required=False)

    Another_comment = forms.CharField(max_length=100, help_text='100 characters max.',widget=forms.TextInput(attrs={'placeholder':'Enter Your Comment'}),required=False)
    cc_myself = forms.BooleanField(required=False)

    Birthday = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}),required=False)
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =',required=False)

    Radio = forms.ChoiceField(choices= cho,widget = forms.RadioSelect,required=False)
    Multiple_Choice = forms.MultipleChoiceField(choices=cho,required=False)

    name = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(required=False)

    District = forms.ChoiceField(choices=choices,label="Select Your District",required=False)
