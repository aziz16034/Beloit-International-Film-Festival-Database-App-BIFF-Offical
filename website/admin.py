from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Contact
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Post)
class Postdata(ImportExportModelAdmin):
    list_display = ('id','Title', 'Synopsis', 'Judging','Year_Submitted', 'Duration','Category','Language','Genre','Subtitles','Student_Project','Completion_Date','Submission_Name','Submission_email','Director_first_name','Director_email','Director_phone','Producer_first_name','Producer_email','Distributor_name','Distributor_phone','Distributor_email','Key_cast','Screenwriters','Composer_name','Cinematographer_name','Rating','Production_budget','First_time_filmmakers','Physical_copy', 'Submission_Phone', 'Producer_Phone')

    search_fields =('Title', 'Year_Submitted')
    readonly_fielfs=('Completion_Date')
    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(Contact)