from rest_framework.serializers import ValidationError


class RewardAndRelatedValidator:
    """Исключение одновременного выбора связанной привычки и вознаграждения"""

    def __call__(self, habit):
        print(habit)
        if habit.get("related_habit") and habit.get("reward"):
            raise ValidationError(
                "Вознаграждение и связанная привычка"
                " не могут быть одновременно указаны"
            )


class ExecuteTimeValidator:
    """Проверка времени выполнения привычки"""

    def __call__(self, habit):
        duration = habit.get("duration")
        if duration is not None and duration > 2:
            raise ValidationError(
                "Время на выполнение привычки не может превышать 2 минуты"
            )


class RelatedAndIsGoodValidator:
    """Проверка связанной привычки и признания ее приятной"""

    def __call__(self, habit):
        if habit.get("related_habit"):
            if not habit.get("is_good_habit"):
                raise ValidationError(
                    "Связанная привычка должна быть приятной"
                )


class FrequencyValidator:
    """Проверка частоты выполнения привычки"""

    def __call__(self, habit):
        frequency = habit.get("frequency")
        print(frequency)
        if frequency is not None:
            if not (1 <= frequency <= 7):
                raise ValidationError(
                    "Частота выполнения привычки "
                    "должна быть не реже 1 раза в 7 дней"
                )
