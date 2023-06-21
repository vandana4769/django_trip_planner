from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from travello.models import Destination

# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials!! Try Again.")
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken!")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken!")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,email=email,password = password1,first_name=first_name, last_name = last_name)
                user.save()
                return redirect('login')
                           
        else:
            messages.info(request,"Password mismatch!")
            return redirect('register')

        return redirect('/')
    else:
        return render(request,'register.html')


# Add Destination

def addDest(request):
    if(request.method == 'POST'):
        name = request.POST["name"]
        desc = request.POST["desc"]
        price = request.POST["price"]

        # In our addDest.html we have used input type=file for uploading image.
        # So we have to use request.FILES instead request.POST
        imgfile = request.FILES["img"]  

        # In our addDest.html we have used checkbox for offer.
        # But when it checked only it will be shown on the form but if it is unchecked it won't appear on the form.
        if 'offer' in request.POST :
            offer = True
        else:
            offer = False
        
        if Destination.objects.filter(name=name).exists():
            messages.info(request,'Destination already added !')
            return redirect('addDest')
        else:
            new_dest = Destination.objects.create(name=name, desc = desc, price = price, img = imgfile , offer = offer )
            new_dest.save()
            return redirect("/")
    else:
        return render(request,"addDest.html")
