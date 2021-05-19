import django_filters
from .models import Post
from django_filters import DateFilter 


class orderfilter(django_filters.FilterSet):
    start_date = django_filters.NumberFilter(field_name="Rating", lookup_expr='gt')
    end_date = django_filters.NumberFilter(field_name="Rating", lookup_expr='lt')
    release_year = django_filters.NumberFilter(field_name='Year_Submitted', lookup_expr='gt')
    release_yearlow = django_filters.NumberFilter(field_name='Year_Submitted', lookup_expr='lt')
    # student_project = django_filters.CharFilter(field_name='Student_Project',  look ='Yes' l)





    class Meta:
        model = Post
        fields = ['Title', 'Title_in_Original_Language']