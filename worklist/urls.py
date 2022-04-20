from django.urls import path
from .import views  # this occurs to the views within the same app
from .views import TaskList,TaskDetail,TaskCreate,TaskDelete,TaskUpdate,CustomLoginView,RegisterUserView
from django.contrib.auth.views import LogoutView
urlpatterns =[
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task-add',TaskCreate.as_view(), name='task-add'),
    path('task_delete/<int:pk>/',TaskDelete.as_view(), name="task_delete"),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page="login"), name='logout'),
    path('register/',RegisterUserView.as_view(), name='register'),
]