from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name ='sign_up'),
    path('create-post', views.create_post, name ='create_post'),
    path('update-post/<int:pk>', views.update_post, name ='update_post'),
    path('post/<int:pk>', views.view_post, name ='view_post'),
    path('view_profile', views.view_profile, name ='view_profile'),
    path('update_profile/<int:pk>/', views.update_user, name='update_user'),
    path('post/<int:pk>/comment', views.add_comment, name='add_comment'),
    path('post/<int:pk>/update-comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('upload_profile_pic/', views.upload_profile_pic, name='upload_profile_pic'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)