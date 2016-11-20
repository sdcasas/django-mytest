
from django.views.generic import edit, ListView, DetailView

from .models import *
from .forms import *


class AlumnoCreate(edit.CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'base/genericForm.html'


class AlumnoUpdate(edit.UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'base/genericForm.html'


class AlumnoList(ListView):
    model = Alumno
    template_name = 'alumnoList.html'


class AlumnoDetail(DetailView):
    model = Alumno
    template_name = 'alumnoDetail.html'
