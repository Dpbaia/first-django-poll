"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

"""
    The idea behind include() is to make it easy to plug-and-play URLs. 
    Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, 
    or under “/content/polls/”, or any other path root, and the app will still work.
"""

urlpatterns = [
    path('polls/', include('polls.urls')), # The include() function allows referencing other URLconfs.
    path('admin/', admin.site.urls)
]

"""
    path() takes 4 arguments, 2 required: route and view, then kwargs and name
    route: the URL pattern
    view: when it finds the route, it calls the specified view witha  HttpRequest object as the first argument
    kwargs: arbitrary keyword arguments
    name: naming url makes it easier to refer to it 
"""
