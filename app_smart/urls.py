from django.urls import path,include
from . import views
from app_smart.api.viewsets import CreateUserAPIViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app_smart.api.viewsets import CreateUserAPIViewSet, SensorViewSet
from rest_framework.routers import DefaultRouter
from app_smart.api.filters import (
    SensorFilterView
)

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUserAPIViewSet.as_view(), name='create_user'),
    path('usuarios', views.autenticacao, name='cad_user'),
    path('cad_user', views.cad_user, name='cad_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/sensor_filter/', SensorFilterView.as_view(), name='sensor_filter'),

]