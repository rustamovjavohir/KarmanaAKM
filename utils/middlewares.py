from django.utils import timezone
from apps.monitoring.models import Visitors


class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log visitor activity here
        # Example: Create a Visit record in your database
        Visitors.objects.update_or_create(ip_address=self.get_client_ip(request),
                                          defaults={
                                              'user_agent': request.META.get('HTTP_USER_AGENT'),
                                              'path': request.path,
                                              'method': request.method,
                                              'status_code': request.META.get('STATUS_CODE'),
                                              'query_string': request.META.get('QUERY_STRING'),
                                              'updated_at': timezone.now(),
                                          })
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
