from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name = 'signup'),
    path('logout/',views.signout,name = 'logout'),
    path('addTask/',views.addTask,name = 'addTask'),
    path('deleteTodo/<int:id>',views.deleteTodo,name ='deleteTodo' ),
    path('change-status/<int:id>/<str:status>',views.changestatus,name ='changestatus' ),

]