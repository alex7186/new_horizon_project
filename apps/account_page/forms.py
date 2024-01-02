from django import forms

CURRENT_STATUS_CODES = (
    ("0", "Не начато"),
    ("1", "Начато"),
    ("2", "Пройдено"),
    ("3", "Успешно пройдено"),
)


class AccountTestProgressForm(forms.ModelForm):

    current_status = forms.ChoiceField(choices=CURRENT_STATUS_CODES)
