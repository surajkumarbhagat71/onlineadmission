from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('product/product',views.product,name="product"),
    path('emplyee/emp_profile',views.emp_profile,name="emp_profile"),
    path('emplyee/login',views.login,name="login"),
    path('logout',views.logout,name="logout"),

    path('director/emp_manage',views.emp_manage,name="emp_manage"),
    path('director/pro_manage',views.pro_manage,name="pro_manage"),
    path('director/insert_emp',views.insert_emp,name="insert_emp"),
    path('director/insert_pro',views.insert_pro,name="insert_pro"),
    path('delete/<int:id>',views.delete_pro,name="delete_pro"),
    path('update/<int:id>',views.update_pro,name="update_pro"),
    path('search',views.search,name="search"),
    path('contact',views.contact,name="contact"),
    path('search_pro',views.search_pro,name="search_pro"),
    path('login_dir',views.login_dir,name="login_dir"),
    path('logout_dir',views.logout_dir,name="logout_dir"),
    path('emp_detail/<int:id>/',views.emp_detail,name="emp_detail"),
    path('update_emp/<int:id>/',views.update_emp,name="update_emp"),
    path('delete_emp/<int:id>/',views.delete_emp,name="delete_emp"),


]