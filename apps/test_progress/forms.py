from django import forms


class TestObjectForm(forms.ModelForm):
    TEST_TYPES = (
        ("1", "Пройдено / Не пройдено"),
        ("3", "Процентный (0-100 %)"),
        ("2", "Балловый (0-n баллов)"),
    )
    test_type = forms.ChoiceField(choices=TEST_TYPES)
