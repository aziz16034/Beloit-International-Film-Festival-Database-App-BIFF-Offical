from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .forms import RegisterForm
from .models import Post
from django.contrib import messages
from .filters import orderfilter


# Create your views here.




def home (request):

    return render(request, 'home.html')



def login (request):
    return render(request, 'login.html')



def about (request):
    return render(request, 'About.html')

def contact (request):
    return render(request, 'contact.html')

def signout (request):
    return render(request, 'logout.html')

def database (request):
    return render(request, 'database.html')


def signup (response):

    if response.method =="POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('home')



    else:
        form = RegisterForm()

    return render(response, 'signup.html', {"form": form})



def profile(request):
    return render(request, 'profile.html')


def database(request):

    
   data = Post.objects.all() 
   myfilter = orderfilter(request.GET, queryset=data)

   data = myfilter.qs
   context = { "student_number": data, 'myfilter': myfilter} 
   return render(request, "database.html", context)









# def database(request):
#     if request.method == 'POST':
#         person_resource = DataSheet()
#         dataset = Dataset()
#         new_persons = request.FILES['myfile']

#         imported_data = dataset.load(new_persons.read(),format='xlsx')
#         #print(imported_data)
#         for data in imported_data:
#         	print(data[1])
#         	value = Post(
#         		data[0],
#         		data[1],
#         		 data[2],
#         		 data[3]
#         		)
#         	value.save()
#         #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

#         #if not result.has_errors():
#         #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

#     return render(request, 'input.html')



# class UploadFileForm(forms.Form):
#     file = forms.FileField()

# def upload(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             filehandle = request.FILES['file']
#             return excel.make_response(filehandle.get_sheet(), "csv")
#         else:
#             return HttpResponseBadRequest()
#     else:
#         form = UploadFileForm()
#     return render_to_response('upload_form.html',
#                               {'form': form},
#                               context_instance=RequestContext(request))

# def download(request):
#     sheet = excel.pe.Sheet([[1, 2],[3, 4]])
#     return excel.make_response(sheet, "csv")






    
    

