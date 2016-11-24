
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from braces.Views import FormMessagesMixin

from .models import *
from .forms import *


class AlumnoMixins(FormMessagesMixin):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'base/genericForm.html'
    # success_url = reverse_lazy('libro:ventana_nuevo')

    def get_success_url(self):
        return reverse_lazy('alumno:update', kwargs={'pk': self.object.pk})
        # return reverse('app_upload', kwargs={'pk': self._id, 'slug': slug})


class AlumnoCreate(CreateView):
    title_form = 'Nuevo Alumno'

    def get_form_valid_message(self):
        return 'Alumno "{0}" creado'.format(self.object)


class AlumnoUpdate(UpdateView):
    title_form = 'Editar Alumno'

    def get_form_valid_message(self):
        return 'Alumno "{0}" editado'.format(self.object)


class AlumnoList(ListView):
    model = Alumno
    template_name = 'alumnoList.html'


class AlumnoDetail(DetailView):
    model = Alumno
    template_name = 'alumnoDetail.html'
