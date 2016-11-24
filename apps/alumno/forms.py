#!/usr/local/lib/python3.4
# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput, Select, DateInput

from .models import *


class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = (
            'legajo',
            'apellido',
            'nombre',
            'dni',
            'fecha_nacimiento',
            'sexo'
        )
        widgets = {
            'legajo': TextInput(attrs={'class': 'form-control', 'placeholder': '99999'}),
            'apellido': TextInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'dni': TextInput(attrs={'class': 'form-control', 'placeholder': '99999999'}),
            'fecha_nacimiento': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': Select(attrs={'class': 'form-control'}),
        }
        # error_messages = {
        #     'legajo': {
        #         'required': "Este campo es obligatorio.",
        #     },
        #     'apellido': {
        #         'required': "Este campo es obligatorio.",
        #     },
        #     'nombre':{
        #         'required': "Este campo es obligatorio.",
        #     },
        #     'dni': {
        #         'required': "Este campo es obligatorio.",
        #     },
        # }
