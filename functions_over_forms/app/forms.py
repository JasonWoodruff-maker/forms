from django import forms

class FontTimes(forms.Form):
    string_input = forms.CharField()
    integer_input = forms.IntegerField()

class NoTeenSum(forms.Form):
    integer_1 = forms.IntegerField()
    integer_2 = forms.IntegerField()
    integer_3 = forms.IntegerField()

class XyzThere(forms.Form):
    given_string = forms.CharField()

class CenteredAverage(forms.Form):
    given_amount_1 = forms.IntegerField()
    given_amount_2 = forms.IntegerField()
    given_amount_3 = forms.IntegerField()
    given_amount_4 = forms.IntegerField()
    given_amount_5 = forms.IntegerField()
    given_amount_6 = forms.IntegerField(required=False)
    given_amount_7 = forms.IntegerField(required=False)


