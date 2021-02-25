from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from entities.bet.views import BetViewSet
from entities.game.views import GameViewSet
from entities.users.views import ObtainTokenPairView, UserViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet, basename='games')
router.register(r'bets', BetViewSet, basename='bets')
router.register(r'users', UserViewSet, basename='users')


api_urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]
