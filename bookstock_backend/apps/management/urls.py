from apps.management import api
from apps.management.api import StockViewSet, BookViewSet, BookTransactionViewSet  # Importe os ViewSets
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", api.UserViewSet)
router.register(r"register-user", api.UserRegister, basename="register-user")
router.register(r"stocks", StockViewSet)  # Registre o StockViewSet
router.register(r"books", BookViewSet)  # Registre o BookViewSet
router.register(r"books-transactions", BookTransactionViewSet)  # Registre o BookViewSet

urlpatterns = [
    path("logout/", api.LogoutView.as_view()),
    path(
        "change_password/<uuid:pk>/",
        api.UserChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path("", include(router.urls)),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]