from django.shortcuts import render,redirect
from .models import Member
from .forms import Memberform
from django.contrib import messages

# Create your views here.
def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all':all_members})

def join(request) :
    if request.method == 'POST':
        form =  Memberform(request.POST or None)
        if form.is_valid():
            form.save()

        else :
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']
            messages.success(request,("Tente novamente !"))
            #return redirect('join')
            return render(request, 'join.html', {'fname': fname,
                'lname': lname,
                'age': age,
                'email': email,
                'passwd': passwd,
                })

        messages.success(request, ('Seu formulário foi enviado com sucesso !'))
        return redirect('home')
    else :
        return render(request, 'join.html', {})




    
