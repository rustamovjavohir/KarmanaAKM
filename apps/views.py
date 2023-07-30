from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'Presento/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class BaseView(TemplateView):
    template_name = 'Presento/blog-single.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def error_404(request, exception):
    return render(request, '404.html', {})
