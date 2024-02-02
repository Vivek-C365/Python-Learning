from django.contrib import admin
from django.urls import path
from .views import ad, login_view, error_view, dashboard, job_list, indeed_job, LogoutPage, test, Source_view


urlpatterns = [
    path("", login_view, name = 'Login'),
    path("ad/", ad, name = 'ad'),
    path("404/", error_view, name = '404_Page'),
    path("dashboard/", dashboard, name = 'Dashboard'),
    path("job_list/", job_list, name = 'Job_List'),
    path("indeed_job/", indeed_job, name = 'Indeed_Job'),
    path("Logout/", LogoutPage, name = 'Logout'),
    path("test/", test, name = 'test'),
    path("source/",Source_view, name ='source'),
    
]
