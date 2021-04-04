from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from todos.forms import TodoCreateForm


from todos.models import Todo


class ViewTodoList(ListView):

    model = Todo

    def get_context_data(self, *args, object_list=None, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['form'] = TodoCreateForm()
        return ctx


class CreateTodoView(CreateView):

    model = Todo
    form_class = TodoCreateForm

    def form_valid(self, form):
        self.object = form.save()
        return self.object

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.form_valid(form)
        return self.response_class(
            request=self.request,
            context={
                'object_list': Todo.objects.all(),
            },
            template='todos/todo_items.html',
            using=self.template_engine,
        )



class EditTodoView(UpdateView):
    model = Todo
    form_class = TodoCreateForm


    def form_valid(self, form):
        self.object = form.save()
        return self.object

    def post(self, request, *args, **kwargs):
        existing = self.get_object()
        form = self.get_form()
        form.instance = existing
        self.form_valid(form)
        return self.response_class(
            request=self.request,
            context={'item': self.object},
            template='todos/todo_item.html',
            using=self.template_engine,
        )


class DeleteTodoView(DeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()

        # Version 1 reponse
        # return HttpResponse('', status=200)

        # version 2 response
        return self.response_class(
            request=self.request,
            context={
                'object_list': Todo.objects.all(),
            },
            template='todos/todo_items.html',
            using=self.template_engine,
        )
