from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

@login_required
def all_subs(request):

