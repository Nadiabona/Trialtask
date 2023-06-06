from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets, mixins
from network.models import Unit, Products
from network.serializers import UnitSerializer, ProductsSerializer


class UnitViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet ):
    queryset = Unit.objects.filter(is_deleted=False)
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]


class UnitCreateView(generics.CreateAPIView):
    model=Unit
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UnitSerializer

    def perform_create(self, serializer: UnitSerializer):
        serializer.save()

class UnitListView(ListAPIView):
    model = Unit
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UnitSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,]
    ordering_fields = ["level", "created"]
    ordering = ["title"]
    search_fields = ["city"]

class UnitManageView(RetrieveUpdateDestroyAPIView):
    model = Unit
    serializer_class = Unit
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Unit.objects.filter(is_deleted=False)

    def perform_destroy(self, instance: Unit) -> None:
        with transaction.atomic():
            instance.is_deleted = True
            instance.save(update_fields=('is_deleted', ))
            #если удалили юнит, надо удалить продкуты
            #транасакционно - это чтобы если вторая операция прошла, а первая нет, чтобы она тоже откатилась
            #о есть либо выполнялись обе либо никакая
            instance.unit.update(status=Unit.Status.archived)

# class ProductsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet ):
#     queryset = Products.objects.filter(is_deleted=False)
#     serializer_class = ProductsSerializer
#     permission_classes = [permissions.IsAuthenticated]