from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse_lazy
from django.views.generic import edit, ListView, DetailView

# para poder usar el modelo user generado por django
from django.contrib.auth.models import User

from .forms import UserForm


class UserCreate(edit.CreateView):
    model = User
    form_class = UserForm
    template_name = 'userCreate.html'
    success_url = reverse_lazy('usr:detail')


class UserUpdate(edit.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'userUpdate.html'
    success_url = reverse_lazy('usr:detail')


class UserList(ListView):
    model = User
    template_name = 'userList.html'


class UserDelete(edit.DeleteView):
    model = User
    template_name = 'userDelete.html'
    success_url = reverse_lazy('usr:list')


class UserDetail(DetailView):
    model = User
    template_name = 'userDetail.html'


# def usr_add(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = UserCreationForm()
#     return render(
#         request,
#         'usrAdd.html',
#         {'form': form},
#     )


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/private')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            user = request.POST['username']
            password = request.POST['password']
            access = authenticate(username=user, password=password)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return HttpResponseRedirect('/restricted')
                else:
                    return render(request, 'noActivo.html')
            else:
                return render(request, 'noAccess.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login')
def private(request):
    user = request.user
    return (request, {'user': user}, 'private.html')


@login_required(login_url='/login')
def close(request):
    logout(request)
    return HttpResponseRedirect('/')
