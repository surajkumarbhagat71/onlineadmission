from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),

    ##############################################  director ######################################

    path('director/add_cat',views.addcategory,name="add_category"),
    path('director/add_course',views.addcourse,name="add_course"),
    path('director/login',views.login,name="login"),
    path('director/dashabord',views.dashabord,name= "dashabord"),
    path('director/add college',views.addcollege,name="add_col"),
    path('logout',views.logout,name="logout"),
    path('director/all_category',views.all_category,name="all_category"),
    path('director/all_course',views.all_course,name="all_course"),
    path('director/all_college',views.all_college,name="all_college"),
    path('delete_college/<int:id>',views.dcollege,name="dcollege"),
    path('delete_course/<int:co_id>',views.dcourse,name="dcourse"),
    path('delete_category/<int:ca_id>',views.dcategory,name="dcategory"),

    #########################################  Student #################################################

    path('student/admission',views.admission,name="admission"),
    path('student/document',views.documtnt,name="document"),
    path('student/registation',views.registation,name="registation"),
    path('slogin',views.slogin,name="slogin"),
    path('student/profile',views.profile,name="profile"),
    path('slogout',views.slogout,name="slogout"),

    ]