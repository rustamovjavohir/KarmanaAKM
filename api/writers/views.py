class EventsListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.filter(is_active=True).order_by('-created_at')
    permission_classes = (AllowAny,)
    pagination_class = EventsPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', "description"]
    filterset_class = EventFilter
