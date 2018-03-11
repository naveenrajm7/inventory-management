from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login,
    get_user_model,
    logout,
    )
from .forms import UserLoginForm
from .forms import UserRegisterForm
from django.views.generic import View
# Create your views here.

def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/home/')
    return render(request,"webapp/form.html",{"form":form, "title":title})

# to register user
class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'webapp/registration_form.html'

    #display blank form
    def get(self, request):
        print("got GET")
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        print("got POST")
        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)
            print(user.is_authenticated)
            if user is not None:
                login(request, user)
                return redirect('/home/')
        print("form invalid")
        return render(request, self.template_name, {'form':form})

def logout_view(request):
    title = 'Logout'
    logout(request)
    return render(request,"webapp/logout.html",{'title':title})
