from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.template import loader
from .forms import RegisterForm
from .models import Post, Contact
from django.contrib import messages
from .filters import orderfilter
from django.core.mail import send_mail, BadHeaderError




# Create your views here.




def home (request):

    return render(request, 'home.html')



# def login (request):
#     used_method = str(request.method)

#     return render(request, 'Log-In.html', {'test': used_method})
#         # return render(request, 'Log-In.html', {'test': used_method})

# def login(request, method='POST'):
#     '''Shows a login form and a registration link.'''

#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)

#         if user is not None and user.is_active:
#             auth.login(request, user)
#             return HttpResponseRedirect("/home")

#         else:
#             return HttpResponse("Invalid login. Please try again.")

#     # if not POST then return login form    
#     return render(request, "Log-In.html", {'next':'/home'})

def login (request):
    return render(request, 'Log-In.html')


def about (request):
    return render(request, 'About.html')

# def contact (request):
#     return render(request, 'Contact.html')


# def contact(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "Contact.html", {'form': form})

# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')


def contact(request):
    if request.method=="POST":
        contact =Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        
        contact.save()
        return HttpResponse("THANKS FOR CONTACTING US")
        
    return render(request, 'Contact.html')



def log_out (request):
    return render(request, 'Log-out.html')

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

    return render(response, 'Sign-Up.html', {"form": form})



def profile(request):
    return render(request, 'profile.html')


def database2(request):

    
   data = Post.objects.all() 
   myfilter = orderfilter(request.GET, queryset=data)


   data = myfilter.qs
   context = { "student_number": data, 'myfilter': myfilter} 

   
   return render(request, "Database2.html", context)




# def detail(request, id):
    
 

#     obj= get_object_or_404(Post, pk=id)
    
#     context= {'obj':obj
#               }
    
#     return render(request, 'Detail.html', context)

# def detail(request, pk):

#     return render(request, 'Detail.html', {
#     'post': get_object_or_404(Post, id=pk)
#   })

def detail(request, id):

    post = Post.objects.all(id =id) 
    context= {'post':post
              }
    return render(request, 'Detail.html', context)




def dashboard(request):
    return render(request, 'dashboard.html')




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






    

