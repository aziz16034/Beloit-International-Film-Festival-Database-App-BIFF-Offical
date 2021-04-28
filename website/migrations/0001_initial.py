# Generated by Django 3.2 on 2021-04-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=100000)),
                ('Synopsis', models.CharField(default='', max_length=100000)),
                ('Judging', models.CharField(default='SOME STRING', max_length=100000)),
                ('Country_of_Origin', models.CharField(default='SOME STRING', max_length=100000)),
                ('Year_Submitted', models.CharField(default='SOME STRING', max_length=100000)),
                ('Duration', models.CharField(default='SOME STRING', max_length=100000)),
                ('Category', models.CharField(default='SOME STRING', max_length=100000)),
                ('Language', models.CharField(default='', max_length=100000)),
                ('Genre', models.CharField(default='', max_length=100000)),
                ('Subtitles', models.CharField(default='', max_length=100000)),
                ('Student_Project', models.CharField(default='', max_length=100000)),
                ('Completion_Date', models.CharField(default='', max_length=100000)),
                ('Submission_Name', models.CharField(default='', max_length=100000)),
                ('Submission_email', models.CharField(default='', max_length=100000)),
                ('Director_first_name', models.CharField(default='', max_length=100000)),
                ('Director_email', models.CharField(default='', max_length=100000)),
                ('Director_phone', models.CharField(default='', max_length=100000)),
                ('Producer_first_name', models.CharField(default='', max_length=100000)),
                ('Producer_email', models.CharField(default='', max_length=100000)),
                ('Distributor_name', models.CharField(default='', max_length=100000)),
                ('Distributor_phone', models.CharField(default='', max_length=100000)),
                ('Distributor_email', models.CharField(default='', max_length=100000)),
                ('Key_cast', models.CharField(default='', max_length=100000)),
                ('Screenwriters', models.CharField(default='', max_length=100000)),
                ('Composer_name', models.CharField(default='', max_length=100000)),
                ('Cinematographer_name', models.CharField(default='', max_length=100000)),
                ('Rating', models.CharField(default='', max_length=100000)),
                ('Production_budget', models.CharField(default='', max_length=100000)),
                ('First_time_filmmakers', models.CharField(default='', max_length=100000)),
                ('Physical_copy', models.CharField(default='', max_length=100000)),
                ('Submission_Phone', models.CharField(default='', max_length=100000)),
                ('Producer_Phone', models.CharField(default='', max_length=100000)),
            ],
        ),
    ]
