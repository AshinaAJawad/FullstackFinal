from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    DOSE_CHOICES = [(i, str(i)) for i in range(1, 11)]
    DAYS_CHOICES = [
        ('mon', 'Monday'),
        ('tues', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thurs', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday')
    ]

    dose = forms.ChoiceField(choices=DOSE_CHOICES)
    days = forms.MultipleChoiceField(
        choices=DAYS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Medicine
        fields = ['name', 'dose', 'days', 'time']
