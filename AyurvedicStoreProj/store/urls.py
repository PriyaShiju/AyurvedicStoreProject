from django.urls import path,re_path
from . import views
  

urlpatterns = [
    
    path("customerfeedback", views.customerfeedback, name = "customerfeedbackurl"), # http://127.0.0.1:8000/Ayurstores/customerfeedback
    path("feedbacks", views.feedbacks, name = "feedbacksurl"), # http://127.0.0.1:8000/Ayurstores/feedbacks
    path("feedback/<int:feedback_id>",views.viewfeedback , name = "feedbackurl"),
    #path("1", views.productdetail, name = "productdetailurl")
    re_path(r'^\d+', views.relatedproducts, name = "productdetailurl"),
    re_path(r'^oil', views.relatedproducts, name ="relatedproducturl"),
    #re_path(r'^oil', ProductView.as_view(), name ="products"), # http://127.0.0.1:8000/Ayurstores/oil
    #re_path(r'^oil', ProductViewAll.as_view(), name="productallurl")
    #re_path(r'^oil', ListAllItems.as_view(), name="productallurl")
    re_path(r'^logout',views.logout, name="logouturl"),
]

