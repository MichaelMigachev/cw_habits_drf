from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    RewardAndRelatedValidator,
    FrequencyValidator,
    ExecuteTimeValidator,
    RelatedAndIsGoodValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели привычек"""
    # user = HiddenField(default=CurrentUserDefault())  # Указать поле user как HiddenField для документации
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardAndRelatedValidator(),
            FrequencyValidator(),
            ExecuteTimeValidator(),
            RelatedAndIsGoodValidator(),
        ]
