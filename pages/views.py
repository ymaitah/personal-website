from django.http import HttpResponse
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os


def home_page_view(request):
    return render(request, "pages/home.html")

def other_page_view(request):
    return render(request, "pages/other.html")

def resume_view(request):
    resume_path = os.path.join(settings.BASE_DIR, 'static', 'YousefMaitahResumeR5.pdf')
    return FileResponse(open(resume_path, 'rb'), content_type='application/pdf') 

def coursework_page_view(request):
    return render(request, "pages/coursework.html")
