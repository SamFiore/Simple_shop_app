from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView

# Create your views here.
class UserRegistraterForm(UserCreationForm):
    usable_password = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username here'})
        # self.fields['password'].widget.attrs.update({'placeholder':'Password here'})

class SingUpView(CreateView):
    form_class = UserRegistraterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'

class LoginAuthForm(AuthenticationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username here'})
        self.fields['password'].widget.attrs.update({'placeholder':'Password here'})

class LoginUpView(FormView):
    form_class = LoginAuthForm
    success_url = reverse_lazy('index')
    template_name = 'registration/login.html'

    def form_valid(self,form):
        user = form.get_user()
        login(self.request,user)
        return super().form_valid(form)

