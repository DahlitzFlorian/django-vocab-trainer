from django.shortcuts import render
from django.views import generic


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
        return []
