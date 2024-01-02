from django import forms

TEST_TYPES_CODES = (
    ("1", "Пройдено / Не пройдено"),
    ("3", "Процентный (0-100 %)"),
    ("2", "Балловый (0-n баллов)"),
)


class TestObjectForm(forms.ModelForm):

    test_type = forms.ChoiceField(choices=TEST_TYPES_CODES)
