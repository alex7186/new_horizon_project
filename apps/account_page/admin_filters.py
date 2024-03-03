from django.contrib import admin


class IsAdminFilter(admin.SimpleListFilter):
    title = "Админ?"
    parameter_name = "is_admin"

    def lookups(self, request, model_admin):
        return (
            ("False", "Нет"),
            ("True", "Да"),
        )

    def queryset(self, request, queryset):
        value = self.value()

        if value == "True":
            return queryset.filter(is_admin=True)

        elif value == "False":
            return queryset.filter(is_admin=False)
