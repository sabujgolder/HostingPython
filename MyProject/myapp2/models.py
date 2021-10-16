from django.db import models

# Create your models here.

class NewUserForm(models.Model):
        Dhaka = 'Dh'
        Khulna = 'kh'
        Jessore = 'Jess'
        choices = (
                    ('','SELECT OPTIONS'),
                    ('1','Dhaka'),
                    ('2','Khulna')
        )

        cho = (
                    ('','SELECT OPTIONS'),
                    (Dhaka,'Dhaka'),
                    (Khulna,'Khulna'),
                    (Jessore,'Jessore')
        )

        username = models.CharField(max_length=128,null=True,blank=True)
        comment = models.CharField(max_length=128,null=True,blank=True)

        Another_comment = models.CharField(max_length=100,null=True,blank=True)
        cc_myself = models.BooleanField(default=True,blank=True)

        Birthday = models.DateField(null=True,blank=True)
        captcha_answer = models.IntegerField(null=True,blank=True)

        Radio = models.CharField(choices= cho,max_length=4,null=True,default = Dhaka,blank=True)
        # Multiple_Choice = models.ManyToManyField(choices=cho)


        email = models.EmailField(null=True)
        vmail = models.EmailField(null=True)
        District = models.CharField(choices=cho,max_length=10,null=True)

        def __str__(self):

            return self.username
