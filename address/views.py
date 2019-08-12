from . import models, serializers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_name']

    def get_serializer_class(self):
        if self.request.query_params.get('companies_more_than'):
            return serializers.PostCodeSerializer
        if self.request.query_params.get('city'):
            return serializers.CompanyNameSerializer
        return serializers.AddressSerializer

    def get_queryset(self):
        queryset = models.Address.objects.all()
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(locality__city__name=city)
            return queryset.values('company_name')
        companies_more_than = self.request.query_params.get('companies_more_than')
        if companies_more_than:
            company_aggregate = models.Address.objects.values('postal_code').annotate(company_count=Count('company_name')).\
                filter(company_count__gte=companies_more_than).order_by('company_count').values_list('postal_code', flat=True)
            queryset = models.Address.objects.filter(postal_code__in=company_aggregate)
            return queryset.values('postal_code').distinct()
        return queryset


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
