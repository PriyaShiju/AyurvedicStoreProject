from django.urls import path,re_path
from . import views
from .views import *    

urlpatterns = [
    path("", views.index, name="indexurl"),
    #path("1", views.productdetail, name = "productdetailurl")
    re_path(r'^\d+', views.productdetail, name = "productdetailurl"),
    re_path(r'^oil', views.relatedproducts, name ="relatedproducturl"),
    #re_path(r'^oil', ProductView.as_view(), name ="products"),
    #re_path(r'^oil', ProductViewAll.as_view(), name="productallurl")
    #re_path(r'^oil', ListAllItems.as_view(), name="productallurl")
    re_path(r'^logout',views.logout, name="logouturl")
]

