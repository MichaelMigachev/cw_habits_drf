from django.urls import path

from habits.views import HabitViewSet, HabitsPublicListAPIView
from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"", HabitViewSet, basename="habits")

urlpatterns = [path("public/",
                    HabitsPublicListAPIView.as_view(),
                    name="public-habits")]
urlpatterns += router.urls
