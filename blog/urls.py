from django.urls import path
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('draft/', views.DraftListView.as_view(), name='post_draft_list'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approved/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/approved/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/published/', views.post_publish, name='post_publish'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
