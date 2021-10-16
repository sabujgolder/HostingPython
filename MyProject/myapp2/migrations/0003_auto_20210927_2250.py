# Generated by Django 3.2.7 on 2021-09-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_auto_20210926_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuserform',
            name='city',
        ),
        migrations.RemoveField(
            model_name='newuserform',
            name='name',
        ),
        migrations.AddField(
            model_name='newuserform',
            name='vmail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='newuserform',
            name='District',
            field=models.CharField(choices=[('', 'SELECT OPTIONS'), ('Dh', 'Dhaka'), ('kh', 'Khulna'), ('Jess', 'Jessore')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='newuserform',
            name='Radio',
            field=models.CharField(choices=[('', 'SELECT OPTIONS'), ('Dh', 'Dhaka'), ('kh', 'Khulna'), ('Jess', 'Jessore')], default='Dh', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='newuserform',
            name='cc_myself',
            field=models.BooleanField(default=True),
        ),
    ]
