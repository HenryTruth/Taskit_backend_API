from django.contrib import admin
from .models import Todos
from .forms import TodosForm
# Register your models here.

class TodosAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['user', '__str__', 'completed']
        form = TodosForm

admin.site.register(Todos, TodosAdmin) 