from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def signup(request):

    return render(request, "customers/signup.html", { "signup_form": UserForm() })
