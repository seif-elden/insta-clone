from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'account'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html' , redirect_authenticated_user=True ),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name='signup'),
    path('myprofile/',views.profile,name='profile'),
    path('myprofile/followers',views.profile_follower,name='profile_follower'),
    path('myprofile/following',views.profile_following,name='profile_following'),
    path('myprofile/add_post',views.add_post,name='add_post'),
    path('myprofile/edit',views.profile_edit,name='profile_edit'),
    path('profile/<user_name>',views.other_user_profile,name='other_user_profile'),


]