from django.urls import path
from . import views 

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('subjects/', views.subjects_view, name='subjects'),
    path('subjects/<str:subject_name>/', views.lessons_view, name='lessons'),
    path('subjects/<str:subject_name>/lesson/<int:lesson_no>/', views.lesson_detail, name='lesson_detail'),
 path("quizzes/", views.quizzes_subjects, name="quizzes_subjects"),
    path("quizzes/<str:subject_name>/", views.quiz_list, name="quiz_list"),
    path("quizzes/<str:subject_name>/<int:quiz_no>/", views.quiz_detail, name="quiz_detail"),
    path('progress/', views.progress_view, name='progress'),
    path('notebook/', views.notebook_view, name='notebook'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
      path("chatbot/", views.chatbot_view, name="chatbot"),
    path("chatbot/api/", views.chatbot_api, name="chatbot_api"),
    
]