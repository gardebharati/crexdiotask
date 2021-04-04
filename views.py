from django.shortcuts import render
from django.http import HttpResponse


all_posts=[
    {
        'student':
    }
]
# Create your views here.
def index(request):
    return render(request, 'home.html')
