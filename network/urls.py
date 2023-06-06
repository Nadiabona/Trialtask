from django.urls import path
from network import views
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register("units", views.UnitViewSet)
# router.register("products", views.ProductsViewSet)
#Unit
urlpatterns = [
    #units
    path('unit/create', views.UnitCreateView.as_view()),
    path('unit/list', views.UnitListView.as_view()),
    path('unit/<int:pk>', views.UnitManageView.as_view()),
    #path('unit/unit_amounts_due', views.UnitDebtView.as_view),
    #products
]
# urlpatterns+=router.urls