from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Krishna Tanmayi'})

def add(request):
    # val1 = int(request.GET['num1'])
    # val2 = int(request.GET['num2'])
    # we are using post method instead of get method in home.html(form tag method ='post')so we have to use post here too
    # when we are using post method our num1,num2 values won't be seen in our url
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    # Here GET is a dictionary so we have to use square brackets 
    # or we can use int(request.GET.get('num1'))
    sum = val1 + val2
    return render(request,'result.html',{'result': sum})