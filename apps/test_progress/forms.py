from django import forms

TEST_TYPES_CODES = (
    ("1", "Пройдено / Не пройдено"),
    ("3", "Процентный (0-100 %)"),
    ("2", "Балловый (0-n баллов)"),
)


CURRENT_STATUS_CODES = (
    ("0", "Не начато"),
    ("1", "Начато"),
    ("2", "Завершено"),
    ("3", "Засчитано"),
)

FINAL_STATUS_CODES = (
    ("2", "Не пройдено"),
    ("3", "Пройдено"),
)


class AccountTestProgressFormAdmin(forms.ModelForm):

    current_status = forms.ChoiceField(choices=CURRENT_STATUS_CODES)


class AccountTestProgressForm(forms.ModelForm):
    answers = forms.JSONField()


class TestObjectForm(forms.ModelForm):

    test_type = forms.ChoiceField(choices=TEST_TYPES_CODES)
