from django.contrib import admin
from apps.test_progress.forms import CURRENT_STATUS_CODES

import sys


class TestResultStatusListFilter(admin.SimpleListFilter):
    title = "Результат прохождения"
    parameter_name = "current_status"

    def lookups(self, request, model_admin):
        return (
            ("0", "Не начато"),
            ("1", "Начато"),
            ("2", "Завершено"),
            ("3", "Засчитано"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if not value:
            return queryset

        print(f"{value=}", file=sys.stdout)
        return queryset.filter(current_status=value)
