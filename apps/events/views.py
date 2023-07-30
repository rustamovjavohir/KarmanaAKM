from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from apps.events.models import Events, Category


# Create your views here.
class EventsView(ListView):
    template_name = 'Presento/events.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class EventDetailView(DetailView):
    template_name = 'Presento/event_detail.html'
    queryset = Events.objects.filter(is_active=True)
    model = Events
    category_model = Category.objects.filter(is_active=True, is_event=True)

    def get_object(self, queryset=None):
        return self.queryset.get(id=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        main_image = self.get_object().image.filter(is_main=True).first()
        categories = self.category_model.all()
        context = {
            'event': self.get_object(),
            'main_image': main_image,
            'categories': categories
        }
        return render(request, self.template_name, context=context)
