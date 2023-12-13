from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import menuview, bookingview


router = DefaultRouter()
router.register(r'menu',menuview, basename ='menu')
router.register(r'menu/<int:pk>', bookingview, basename ='menu')

router.register(r'tables', bookingview, basename ='booking')





urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name ='index')
    # path('menu/', views.menuview.as_view()),
    # path('booking/', views.bookingview.as_view())
]