from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name = "home"),
    path('people/',views.people,name = "people"),
    path('profile/<int:pk>',views.profile, name = "profile"),
    path('createprofile',views.createprofile, name = "createprofile"),
    path('update_profile',views.update_profile, name = "update_profile"),
    path('writetalks/',views.write, name = "writetalks"),
    path('login/',views.login_user, name = "login"),
    path('signup/',views.Signup, name = "signup"),
    path('logout/',views.logout_user, name = "logout"),
    path('likes/<int:pk>',views.likes , name = "likes"),
    path('delete/<int:pk>',views.Delete , name = "delete"),
    path('delete_user/<int:pk>',views.Delete_user , name = "delete_user"),
    path('edit/<int:pk>',views.Edit , name = "edit"),
    path('search/',views.search,name = "search"),
]
