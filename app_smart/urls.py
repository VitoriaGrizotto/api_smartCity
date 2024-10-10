from django.urls import path, include
from. import views
from app_smart.api.viewsets import CreateUser, SensorViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from app_smart.views import CSVUploadView, process_csv_upload
from app_smart.api.viewsets import(
    CreateUser,
    SensorViewSet,
    TemperaturaDataViewSet,
)

router = DefaultRouter()
router.register(r'sensores', SensorViewSet)
router.register(r'temperatura', TemperaturaDataViewSet)

urlpatterns = [
    path('', views.abre_index, name='abre_index'),
    path('api/create_user/', CreateUser.as_view(), name='create_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('process-upload/', process_csv_upload, name='process-upload'),
    # path('api/upload/temperatura/', TemperaturaDataViewSet.as_view({'post': 'upload'}), name='upload_temperatura'),
]
