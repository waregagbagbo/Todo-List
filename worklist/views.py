from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Task 
from .forms import TaskCreationForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


# for login using CBV   
class CustomLoginView(LoginView):
    template_name = 'worklist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
# define a method to achieve the success url    
    def get_success_url(self):
        return reverse_lazy('tasks')

# for registeration

class RegisterUserView(CreateView):
    template_name = 'worklist/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    #let us define a function that will query data for a spefic user
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] =  context["tasks"].filter(user=self.request.user) # queries user related-data
        context["tasks"] = context["tasks"].filter(complete=True)
    # search view section
        search_input = self.request.GET.get('search_input') or '' # the apostrophe is for an empty search
        if  search_input:
           context["tasks"] = context["tasks"].filter(title_startswith=search_input)
        
        context['search_input'] = search_input
        return context
    
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy 
    template_name = 'worklist/task_detail.html'   

#implement the create view to enable edition of tasks
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('tasks') 
    form_class = TaskCreationForm
    #fields = ['title','description','complete']
    template_name ='worklist/task_form.html'
    
    # this is a method that automatically covers the user created form data
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    #fields = ['title','description','complete']
    form_class = TaskCreationForm    
    success_url = reverse_lazy('tasks')
    template_name ='worklist/task_update.html'


#implement the delete view to remove items form
class  TaskDelete(DeleteView, LoginRequiredMixin):
    model = Task
    context_object_name ='worklist/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')
