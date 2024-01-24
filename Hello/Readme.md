***To create project***

- django-admin startproject (***projectname***)

***To run server***

- python manage.py runserver

**After Poject create we have to create app in project**

- To create app - python manage.py startapp home


# File changes


1. After create app we have add ***urls.py*** file in ***App folder***. 

    -   In **urls.py file**

            from django.contrib import admin
            from django.urls import path
            from home import views 
            <!-- (import view file from the project folder into app file) -->

            urlpatterns = [ 
                path("", views.index, name = 'home'),
                path("about/", views.about, name = 'about'),
            ]
    And in this file all urls for website get added. Like **about** when we click on about then url shift to about url

2. Changes in ***setting.py** file of App File

    - To link **static file**
        
            import os

            <!-- added manually -->

            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, "static")
            ]
    - To call **Templates file** - In setting files of project at Template section we have to add ***template base directory in DIRS***

            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [os.path.join(BASE_DIR, "templates")],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.debug',
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ]



3. When there is a empty url then they call Project urls.py file

    -   Project ***urls.py*** files
            <!-- by defalut admin url is present and if we want to enter any url to work as default urls we have to add here -->

            from django.contrib import admin
            from django.urls import path , include


            urlpatterns = [
                path('',include('home.urls')),
                path('admin/', admin.site.urls),
            ]


# Website urls and File calling

1. To Call static file in website manually

    - We type **url/static/(***file name***)**

2. Now we calling html file from ***view.py*** file which is present in App folder(home)

        from django.shortcuts import render

        # Create your views here.
        def index(request):
            return render(request,'index.html' )
    
    <!-- they return the html file which is present in template file with name of index.html -->

3. Now we have to create a html file in template folder with **index.html**
