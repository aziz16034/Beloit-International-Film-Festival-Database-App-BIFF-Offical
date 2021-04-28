from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin 
from .models import Post

# Register your models here.


@admin.register(Post)
class Postdata(ImportExportModelAdmin):
    list_display = ('id','Title', 'Synopsis', 'Judging','Year_Submitted', 'Duration','Category','Language','Genre','Subtitles','Student_Project','Completion_Date','Submission_Name','Submission_email','Director_first_name','Director_email','Director_phone','Producer_first_name','Producer_email','Distributor_name','Distributor_phone','Distributor_email','Key_cast','Screenwriters','Composer_name','Cinematographer_name','Rating','Production_budget','First_time_filmmakers','Physical_copy', 'Submission_Phone', 'Producer_Phone')