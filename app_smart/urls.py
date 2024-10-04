from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app_smart.api.viewsets import CreateUser, SensorViewSet, TemperaturaDataViewSet
from rest_framework.routers import DefaultRouter
from app_smart.api.filters import SensorFilterView
from app_smart.views import abre_index, upload_csv_view

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUser.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/upload/', upload_csv_view, name='upload_csv'),  # Nova URL para upload de CSV
]
