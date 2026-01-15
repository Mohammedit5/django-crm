from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout 
from .form import SignUpForm , AddRecordForm
#from django.contrib.auth import messages
from .models import Record

# where to impoort messages from
from django.contrib import messages
# Create your views here.

#check the form fileds for login and logout

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')  # Redirect to home on failed login
        
    else:
        
        return render(request, 'home.html' , {'records': records} ) 


#def login_user(request):
   # pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

 #   pass

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('home')
       # else:

            #form = SignUpForm()

           # return render(request, 'register.html' , {'form': form} )    
    else:

        form = SignUpForm()

        return render(request, 'register.html' , {'form': form} )
    



    return render(request, 'register.html' , {'form': form} )    



def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record deleted successfully.")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete records.")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = Record(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    phone_number=form.cleaned_data['phone'],
                    address=form.cleaned_data['address'],
                    city=form.cleaned_data['city'],
                    state=form.cleaned_data['state'],
                    zip_code=form.cleaned_data['zip_code']
                )
                add_record.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add records.")
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, initial={
            'first_name': record.first_name,
            'last_name': record.last_name,
            'email': record.email,
            'phone': record.phone_number,
            'address': record.address,
            'city': record.city,
            'state': record.state,
            'zip_code': record.zip_code
        })
        if request.method == 'POST':
            if form.is_valid():
                record.first_name = form.cleaned_data['first_name']
                record.last_name = form.cleaned_data['last_name']
                record.email = form.cleaned_data['email']
                record.phone_number = form.cleaned_data['phone']
                record.address = form.cleaned_data['address']
                record.city = form.cleaned_data['city']
                record.state = form.cleaned_data['state']
                record.zip_code = form.cleaned_data['zip_code']
                record.save()
                messages.success(request, "Record updated successfully.")
                return redirect('home')
        return render(request, 'update_record.html', {'form': form, 'record': record})
    else:
        messages.success(request, "You must be logged in to update records.")
        return redirect('home')

