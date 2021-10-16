# Generated by Django 3.2.7 on 2021-09-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, null=True)),
                ('comment', models.CharField(max_length=128, null=True)),
                ('city', models.CharField(choices=[('Dh', 'Dhaka'), ('kh', 'Khulna'), ('Jess', 'Jessore')], default='Dh', max_length=4)),
            ],
        ),
    ]
