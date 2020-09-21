from django.urls import path

from vacancy.views import get_job_views, get_jobs_views, post_job

app_name = "api"

urlpatterns = [
    path('get_job', get_job_views.UserView.as_view()),
    path('get_jobs', get_jobs_views.UserView.as_view()),
    path('post_job', post_job.UserView.as_view()),
]
