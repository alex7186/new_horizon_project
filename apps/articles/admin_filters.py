from django.contrib import admin
from datetime import datetime, timedelta


class DateFieldListFilter(admin.SimpleListFilter):
    title = "Дата изменения"
    parameter_name = "last_modified"

    def lookups(self, request, model_admin):
        return (
            ("last_week", "Эта неделя"),
            ("last_month", "Этот месяц"),
            ("last_6month", "Этот полугодие"),
            ("last_year", "Этот год"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        today = datetime.today().date()

        if value == "last_week":
            return queryset.filter(last_modified__gte=today - timedelta(days=7))

        elif value == "last_month":
            end_of_last_month = today.replace(day=1) - timedelta(days=1)
            return queryset.filter(
                last_modified__gte=end_of_last_month.replace(day=today.day)
            )

        elif value == "last_6month":
            start_of_month = today.replace(day=1)
            return queryset.filter(
                last_modified__gte=start_of_month.replace(
                    month=start_of_month.month - 6
                )
            )

        elif value == "last_year":
            start_of_month = today.replace(day=1)
            return queryset.filter(
                last_modified__gte=start_of_month.replace(year=start_of_month.year - 1)
            )

        return queryset


class ShowingFieldListFilter(admin.SimpleListFilter):
    title = "Показывается?"
    parameter_name = "flag_article_enabled"

    def lookups(self, request, model_admin):
        return (
            ("True", "Да"),
            ("False", "Нет"),
        )

    def queryset(self, request, queryset):
        value = self.value()

        if value == "True":
            return queryset.filter(flag_article_enabled=True)

        elif value == "False":
            return queryset.filter(flag_article_enabled=False)

        return queryset
