from django import forms

class FontTimes(forms.Form):
    string_input = forms.CharField()
    integer_input = forms.IntegerField()

class NoTeenSum(forms.Form):
    int_1 = forms.IntegerField()
    int_2 = forms.IntegerField()
    int_3 = forms.IntegerField()

class XyzThere(forms.Form):
    given_string = forms.CharField()

class CenteredAverage(forms.Form):
    amount_1 = forms.IntegerField()
    amount_2 = forms.IntegerField()
    amount_3 = forms.IntegerField()
    amount_4 = forms.IntegerField()
    amount_5 = forms.IntegerField()
    amount_6 = forms.IntegerField(required=False)
    amount_7 = forms.IntegerField(required=False)

