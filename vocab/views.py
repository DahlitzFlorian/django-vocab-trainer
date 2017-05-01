from django.shortcuts import render
from django.views import generic

from .models import Learnset


class IndexView(generic.ListView):
    """
    Index-view for vocab-app
    """
    template_name = 'vocab/index.html'

    context_object_name = 'sets'

    def get_queryset(self):
        """
        Getting queryset for index-page of vocab-app
        """
        return Learnset.objects.all().order_by('-creation_date')


class TrainingView(generic.DetailView):
    """
    Shows trainings-session
    """
    template_name = 'vocab/training.html'

    context_object_name = 'learnset'

    def get_queryset(self):
        return Learnset.objects.all()
