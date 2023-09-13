from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class MonitoringView(TemplateView):
    template_name = 'monitoring/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_data = {
            'title': 'Monitoring',
            'page_title': 'Monitoring',
            'page_description': 'Monitoring',
            'page_header': 'Monitoring',
            'page_breadcrumb': 'Monitoring',
        }
        context.update(extra_data)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
