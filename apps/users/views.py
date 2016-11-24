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







# views.py

from django.views.generic import FormView, TemplateView, RedirectView

# Authentication imports
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.core.urlresolvers import reverse_lazy

# from alumno.models import Alumno



class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy('users:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'users:login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('users:login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ControlPanelView(LoginRequiredMixin, TemplateView):
    template_name = 'control_panel/panel.html'

    def get_context_data(self, **kwargs):
        context = super(ControlPanelView, self).get_context_data(**kwargs)
        context['pedidos_pendientes'] = Pedido.objects.pendientes()
        # ....
        # Recopilar resto de la informacion
        # ....

        return context

























class UserCreate(edit.CreateView):
    model = User
    form_class = UserForm
    template_name = 'userCreate.html'
    success_url = reverse_lazy('users:detail')


class UserUpdate(edit.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'userUpdate.html'
    success_url = reverse_lazy('users:detail')


class UserList(ListView):
    model = User
    template_name = 'userList.html'


class UserDelete(edit.DeleteView):
    model = User
    template_name = 'userDelete.html'
    success_url = reverse_lazy('users:list')


class UserDetail(DetailView):
    model = User
    template_name = 'userDetail.html'


# def users_add(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = UserCreationForm()
#     return render(
#         request,
#         'usersAdd.html',
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


@login_required(login_url='users:login')
def private(request):
    user = request.user
    return (request, 'private.html', {'user': user})


# @login_required(login_url='/login')
# def close(request):
#     logout(request)
#     return HttpResponseRedirect('/')
