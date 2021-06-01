from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.index, name='home'),
    path('create', cache_page(60)(views.create), name='create'),
    path('<int:id>', views.TaskDetailView.as_view(), name='task-detail'),
    path('<int:id>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('<int:id>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
]


