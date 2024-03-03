from django.urls import path
from hw6app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tree/', views.tree_main, name='tree_main'),
    path('tree/<str:pk>/', views.tree_by_id, name='tree_by_id'),
    path('tree/delete/<str:pk>/', views.tree_delete, name='tree_by_id'),
    path('<path:wrong_url>', views.handle_wrong_url),
]
