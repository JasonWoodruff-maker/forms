from django import forms

class heyyou (forms.Form):
    x = forms.CharField(required = True)



class ages(forms.Form):
    birthyear = forms.IntegerField( required=True)
    cur_year = forms.IntegerField( required=True)


class foods(forms.Form):
    fries = forms.IntegerField( required=True)
    drinks = forms.IntegerField( required=True)
    burgers = forms.IntegerField( required=True)
