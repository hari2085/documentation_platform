"""doc_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from documentation import views,urls
from django.contrib.auth import views as auth_views

admin.site.site_header = "Documentation Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    path('<str:product_id>/<str:project_id>/<str:version_no>/', views.detailproject, name='detailproject'),
    path('/tag/<str:tag_id>/',views.page,name='page'),
    path('<str:product_id>/',views.detailproduct,name='detailproduct'),

    

    url(r'^chaining/', include('smart_selects.urls')),
]

