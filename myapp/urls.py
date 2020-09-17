
from django.urls import path, include
from myapp import views



urlpatterns = [
    path('', views.index, name = "index"),
    path('my_index/', views.my_index, name = "my_index"),
    path('create/', views.create, name = "create"),
    path('detail/<int:blog_id>', views.detail, name = "detail"),
    path('delete/<int:blog_id>', views.delete, name = "delete"),
    path('update/<int:blog_id>', views.update, name = "update"),

    # commment#
    path('create_comment/<int:blog_id>/', views.create_comment, name = "create_comment"),
    path('delete_comment/<int:blog_id>/<int:comment_id>', views.delete_comment , name = "delete_comment"),
    path('intro/', views.intro, name = "intro"),
    
    
]