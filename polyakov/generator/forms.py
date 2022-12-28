from django import forms


class VarForm(forms.Form):
    variant = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False,
                                 label='Введите вариант')


class TaskForm(forms.Form):
    task1 = forms.BooleanField(widget=forms.CheckboxInput(), required=False)


class AnswerForm(forms.Form):
    answer1 = forms.CharField(required=False)
    answer2 = forms.CharField(required=False)
    answer3 = forms.CharField(required=False)
    answer4 = forms.CharField(required=False)
    answer5 = forms.CharField(required=False)
    answer6 = forms.CharField(required=False)
    answer7 = forms.CharField(required=False)
    answer8 = forms.CharField(required=False)
    answer9 = forms.CharField(required=False)
    answer10 = forms.CharField(required=False)
    answer11 = forms.CharField(required=False)
    answer12 = forms.CharField(required=False)
    answer13 = forms.CharField(required=False)
    answer14 = forms.CharField(required=False)
    answer15 = forms.CharField(required=False)
    answer16 = forms.CharField(required=False)
    answer17 = forms.CharField(required=False)
    answer18 = forms.CharField(required=False)
    answer19 = forms.CharField(required=False)
    answer20 = forms.CharField(required=False)
    answer21 = forms.CharField(required=False)
    answer22 = forms.CharField(required=False)
    answer23 = forms.CharField(required=False)
    answer24 = forms.CharField(required=False)
    answer25 = forms.CharField(required=False)
    answer26 = forms.CharField(required=False)
    answer27 = forms.CharField(required=False)

    widgets = {
        'answer1': forms.TextInput(attrs={'class': 'form-control'}),
        'answer2': forms.TextInput(attrs={'class': 'form-control'}),
        'answer3': forms.TextInput(attrs={'class': 'form-control'}),
        'answer4': forms.TextInput(attrs={'class': 'form-control'}),
        'answer5': forms.TextInput(attrs={'class': 'form-control'}),
        'answer6': forms.TextInput(attrs={'class': 'form-control'}),
        'answer7': forms.TextInput(attrs={'class': 'form-control'}),
        'answer8': forms.TextInput(attrs={'class': 'form-control'}),
        'answer9': forms.TextInput(attrs={'class': 'form-control'}),
        'answer10': forms.TextInput(attrs={'class': 'form-control'}),
        'answer11': forms.TextInput(attrs={'class': 'form-control'}),
        'answer12': forms.TextInput(attrs={'class': 'form-control'}),
        'answer13': forms.TextInput(attrs={'class': 'form-control'}),
        'answer14': forms.TextInput(attrs={'class': 'form-control'}),
        'answer15': forms.TextInput(attrs={'class': 'form-control'}),
        'answer16': forms.TextInput(attrs={'class': 'form-control'}),
        'answer17': forms.TextInput(attrs={'class': 'form-control'}),
        'answer18': forms.TextInput(attrs={'class': 'form-control'}),
        'answer19': forms.TextInput(attrs={'class': 'form-control'}),
        'answer20': forms.TextInput(attrs={'class': 'form-control'}),
        'answer21': forms.TextInput(attrs={'class': 'form-control'}),
        'answer22': forms.TextInput(attrs={'class': 'form-control'}),
        'answer23': forms.TextInput(attrs={'class': 'form-control'}),
        'answer24': forms.TextInput(attrs={'class': 'form-control'}),
        'answer25': forms.TextInput(attrs={'class': 'form-control'}),
        'answer26': forms.TextInput(attrs={'class': 'form-control'}),
        'answer27': forms.TextInput(attrs={'class': 'form-control'}),

    }
