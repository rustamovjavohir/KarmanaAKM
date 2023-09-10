from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from config import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL, key_prefix='index')
def index(request):
    return render(request, 'Presento/index.html', {})


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


def error_500(request, *args, **argv):
    return render(request, '500.html', status=500)
