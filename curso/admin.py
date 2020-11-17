# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Curso, Rating


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'creation', 'update', 'active')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('curso', 'name', 'email', 'rating', 'creation', 'update', 'active' )
