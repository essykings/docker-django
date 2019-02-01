from django.conf.urls import include, url
from tasks.views import (TaskListView, TaskDetailView)



urlpatterns=[
    url(r'^tasks/$', TaskListView.as_view(), name="task_list"),
   url(r'^tasks_details/(?P<pk>[^/]+)/$',
        TaskDetailView.as_view(), name="tasks_details")
   

]