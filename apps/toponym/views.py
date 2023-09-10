from django.shortcuts import render
from django.views.generic import ListView, DetailView
from apps.toponym.models import Toponym


class ToponymListView(ListView):
    model = Toponym
    queryset = Toponym.objects.filter(is_active=True)
    template_name = 'Presento/toponyms.html'
    context_object_name = 'toponyms'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = {
            'toponyms': self.queryset,
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())


class ToponymDetailView(DetailView):
    model = Toponym
    queryset = Toponym.objects.filter(is_active=True)
    template_name = 'Presento/toponyms_detail.html'
    context_object_name = 'toponym'

    def get_context_data(self, **kwargs):
        context = {
            'toponym': self.queryset.get(slug=self.kwargs['slug']),
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())
