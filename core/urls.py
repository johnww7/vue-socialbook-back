from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path
from . import views
from core.apiViews import api_upload, api_like_post, api_profile, api_follow, api_settings, api_createprofile,api_user_suggestion

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upLoad, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('api/register/', RegisterView.as_view(), name="api_register"),
    path('api/login/', LoginView.as_view(), name="api_login"),
    path('api/logout/', LogoutView.as_view(), name="api_logout"),
    path('api/user/', UserDetailsView.as_view(), name="api_user"),
    path('api/upload', api_upload.as_view() , name='api_upload'),
    path('api/like-post', api_like_post.as_view()  , name='api_like_post'),
    path('api/profile/', api_profile.as_view() , name='api_profile'),
    path('api/follow', api_follow.as_view() , name='api_follow'),
    path('api/settings', api_settings.as_view() , name='api_settings'),
    path('api/create-profile/<str:pk>', api_createprofile.as_view() , name='api_createprofile'),
    path('api/user-suggestion', api_user_suggestion.as_view(), name="api_suggestion")
] 