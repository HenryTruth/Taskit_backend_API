from django.urls import path

from .views import TodosAPIView,TodosAPIDetailView

app_name = 'Todos'
urlpatterns = [
    path('',TodosAPIView.as_view()),
    path('<int:id>/', TodosAPIDetailView.as_view(), name='detail'),
]