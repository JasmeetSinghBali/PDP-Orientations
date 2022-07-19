from turtle import home
from django.urls import path
from .views import lead_create, lead_list, lead_detail, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('',lead_list),
    # the pk in the leads will help to dynamically navigate to specific route and show that lead detail
    # 📝: IMP int datatype specified so django do not confuses the path after <pk> routes expecting primary key in the create route
    path('<int:pk>/',lead_detail),
    path('create/',lead_create),
    path('<int:pk>/update/',lead_update),
    path('<int:pk>/delete/',lead_delete),
]