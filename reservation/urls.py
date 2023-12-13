from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import menuview, bookingview, singleitemview
from .import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'menu',menuview, basename ='menu')
router.register(r'menu/<int:pk>', singleitemview, basename ='singleitem')

router.register(r'tables', bookingview, basename ='booking')





urlpatterns = [
    path('', include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
    

    # path('', views.index, name ='index')
    # path('menu/', views.menuview.as_view()),
    # path('booking/', views.bookingview.as_view())
]