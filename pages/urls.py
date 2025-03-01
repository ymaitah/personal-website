# pages/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page_view, experience_page_view, other_page_view, resume_view # new

urlpatterns = [
    path("other/", other_page_view),
    path("experience/", experience_page_view),  # new
    path("resume/", resume_view, name="resume"),
    path("", home_page_view), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 