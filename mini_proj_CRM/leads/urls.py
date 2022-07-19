from turtle import home
from django.urls import path
from .views import lead_create, lead_list, lead_detail, lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('',lead_list, name='lead-list'),
    # the pk in the leads will help to dynamically navigate to specific route and show that lead detail
    # 📝: IMP int datatype specified so django do not confuses the path after <pk> routes expecting primary key in the create route
    # 📝: IMP the name passed as third param can be used to refference to the path by using the names instead of passing harcoded url path
    path('<int:pk>/',lead_detail, name='lead-detail'),
    path('create-a-lead/',lead_create, name='lead-create'),
    path('<int:pk>/update/',lead_update, name='lead-update'),
    path('<int:pk>/delete/',lead_delete, name='lead-delete'),
]