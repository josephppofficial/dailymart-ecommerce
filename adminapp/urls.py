from django.urls import path
from . import views

urlpatterns = [
    path('adminapp', views.adminapp, name='adminapp'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('category_data', views.category_data, name='category_data'),
    path('viewcategory', views.viewcategory, name='viewcategory'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('addproduct', views.addproduct, name='addproduct'),
    path('product_data', views.product_data, name='product_data'),
    path('viewproduct', views.viewproduct, name='viewproduct'),
    path('clear/<int:id>', views.clear, name='clear'),
    path('editproduct/<int:id>', views.editproduct, name='editproduct'),
    path('updation/<int:id>', views.updation, name='updation'),
    path('contact_table', views.contact_table, name='contact_table'),
    path('table_registration', views.table_registration, name='table_registration'),
    path('order', views.order, name='order')
    
    

]