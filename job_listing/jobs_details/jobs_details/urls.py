
from django.contrib import admin
from django.urls import path , include

admin.site.site_header = "Project Admin"
admin.site.site_title = "Project Admin Portal"
admin.site.index_title = "Welcome to My Project"

urlpatterns = [
    path('',include('jobs_list.urls')),
    path('admin/', admin.site.urls),
]
