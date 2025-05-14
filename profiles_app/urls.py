from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_app import views

router = DefaultRouter()
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.PostFeedViewSet)

urlpatterns = [
    path("login/", views.ProfileLoginApiView.as_view()),
    path("", include(router.urls)),
]
