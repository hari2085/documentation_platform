from django.contrib import admin
from django.urls import path

from . import views
admin.site.site_header='Documentation admin'
admin.site.site_title='Documentation admin'

urlpatterns = [
    # path('<str:product_name>/<str:project_name>/', views.detail, name='detail'),
    # path('<str:tag_name>/',views.page,name='page'),
    # path('<str:product_name>/',views.detailproduct,name='detailproduct'),

    
]