"""competetion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webelopers.views import *

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', index, name='homePage'),
	path('register/', registering, name='register'),
	path('contact/', contact, name='contact_us'),
	path('contact/confirmed/', confirmation, name='confirmed'),
	path('login/', Login, name='login'),
	path('logout/', logout_view, name = 'logout'),
	path('profile/',profile,name='profile'),
	path('panel/',panel,name='panel'),
	path('add_course/', add_course, name='add_course'),
	path('courses/', courses, name='courses'),
	path('edit/', edit, name='edit')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
