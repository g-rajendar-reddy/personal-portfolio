from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Registration View
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('/reg')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('/reg')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('/reg')

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        messages.success(request, "User registered successfully!")
        return redirect('/login')

    else:
        return render(request, 'testapp/register.html')


def login(self):
    if self.method== 'POST':
        username = self.POST.get('username')
        password = self.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(self, user)
            return redirect("/port")
        else:
            messages.info(self,'Invalid credentials!')
            return redirect('/login')

    else:    
        return render(self,'testapp/login.html')



def portfolio(self):
    return render(self,'testapp/portfolio.html')



from .models import Contact

def contact(self):
    if self.method == 'POST':
        name = self.POST.get('name')
        email = self.POST.get('email')
        subject = self.POST.get('subject')
        message = self.POST.get('message')

        form = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        form.save()
        messages.success(self, "Your contact details have been sent successfully!")
        return redirect('/contact')
    
    else:
        return render(self,'testapp/portfolio.html')
