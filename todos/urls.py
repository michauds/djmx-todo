from django.urls import path

from todos.views import ViewTodoList, CreateTodoView, EditTodoView, DeleteTodoView

urlpatterns = [
   path('', ViewTodoList.as_view(), name='todo-list'),
   path('create', CreateTodoView.as_view(), name='todos-create'),
   path('<int:pk>', EditTodoView.as_view(), name='edit-todo'),
   path('<int:pk>/delete', DeleteTodoView.as_view(), name='delete-todo')
]
