# data_analysis_project/urls.py
from django.contrib import admin
from django.urls import include, path
from data_analysis_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('data-analysis/', include('data_analysis_app.urls')),
]