from django.urls import include, path
from . import views
from .views import feedback
from .views import feedback_status
from .views import thank_you_view
from .views import search_results




urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('feedback/', feedback, name='feedback'),
    path('feedback/status/', feedback_status, name='feedback_status'),
    path('thank-you/', thank_you_view, name='thank_you'),
    path('search_results/', search_results, name='search_results'),
    
]