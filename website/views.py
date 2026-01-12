from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout 

#from django.contrib.auth import messages

# where to impoort messages from
from django.contrib import messages
# Create your views here.

#check the form fileds for login and logout

def home(request):

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
        
        return render(request, 'home.html') 


#def login_user(request):
   # pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

 #   pass

def register_user(request):
     return render(request, 'register.html')    



   