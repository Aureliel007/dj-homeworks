from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrAdminOrReadOnly
from .filters import AdvertisementFilter


class AdvertisementViewSet(viewsets.ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        user = self.request.user
        if not user.is_anonymous:
            queryset = Advertisement.objects.filter(
                Q(status='OPEN') | Q(creator=user, status='CLOSED') | Q(creator=user, status='DRAFT')
            )
        else:
            queryset = Advertisement.objects.filter(status='OPEN')
        return queryset

    @action(detail=True, methods=['post'])
    def add_favorite(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        user = request.user
        ad = self.get_object()
        if ad.creator != user:
            user.favorites.add(ad)
            return Response(
                {'message': 'Объявление добавлено в избранное'}
                )
        else:
            return Response(
                {'message': 'Нельзя добавить собственное объявление в избранное'},
                status=status.HTTP_400_BAD_REQUEST
                )
