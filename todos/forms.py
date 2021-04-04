
from django.forms import ModelForm

from todos.models import Todo


class TodoCreateForm(ModelForm):

    class Meta:
        fields = ['name', 'done']
        model = Todo

