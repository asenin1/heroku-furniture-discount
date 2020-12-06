from django.urls import path
from furnitures.views import FurnitureList, FurnitureDetail, UserFurnitureList, Create, Edit, Delete

urlpatterns = [
    path('', FurnitureList.as_view(), name='furniture'),
    path('details/<int:pk>/', FurnitureDetail.as_view(), name='furniture-detail'),
    path('mine/', UserFurnitureList.as_view(), name='user-furniture'),
    path('create/', Create.as_view(), name='create'),
    path('edit/<int:pk>/', Edit.as_view(), name='edit'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
