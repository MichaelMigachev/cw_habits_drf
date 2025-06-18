from habits.views import HabitViewSet
from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r"", HabitViewSet, basename="habits")

urlpatterns = []
urlpatterns += router.urls
