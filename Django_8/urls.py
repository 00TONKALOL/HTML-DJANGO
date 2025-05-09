"""
URL configuration for Django_8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Django_8 import settings
from app_101 import views

urlpatterns = [
    path('api/people', views.api_people , name='api_people'),
    path('api/person/add' , views.api_add , name='api_people'),
    path('api/person/delete/<int:id>' , views.api_delete , name='api_delete'),
    path('api/person/put/<int:id>' , views.api_update , name='api_delete'),
    path('api/person/<int:id>', views. single_person , name='single_person'),
    path('login', views.login_user , name='login-page'),
    path('signout' , views.signin , name='login-page'),
    path('signout', views.signout , name='login-page'),
    path('', views.home,name='home-page'),
    path('add-person', views.add_person, name='add-person-page'),
    path('people', views.people, name='people-page'),
    path('submit', views.submit, name='submit-page'),
    path('admin/', admin.site.urls),
    path('details/<int:id>', views.details, name='details-page'),
    path('details/<int:id>', views.delete, name='delete-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
