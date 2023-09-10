from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from apps.writers.models import Writers


class WritersView(ListView):
    template_name = 'Presento/writers.html'
    queryset = Writers.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        data = {
            'writers': self.queryset,
        }
        return render(request, self.template_name, context=data)


class WritersDetailView(DetailView):
    template_name = 'Presento/writers_detail.html'
    queryset = Writers.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        data = {
            'writer': self.queryset.get(slug=self.kwargs['slug']),
        }
        return render(request, self.template_name, context=data)
