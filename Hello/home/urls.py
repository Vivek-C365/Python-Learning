
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [ 
    path("", views.login_view, name = 'Login'),
    path("ad/", views.ad, name = 'ad'),
    path("404/", views.error_view, name = '404_Page'),
    path("dashboard/", views.dashboard, name = 'Dashboard'),
    path("job_list/", views.job_list, name = 'Job_List'),
    path("indeed_job/", views.indeed_job, name = 'Indeed_Job'),
    path("Logout/", views.LogoutPage, name = 'Logout'),
    path("test/", views.test, name = 'test'),
    path("source/", views.Source_view, name ='source'),
    
]
