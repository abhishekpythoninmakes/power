from django import forms

from person.models import Person, City

roles = (('male',"Male"),('female',"Female"),('trans',"Trans"))
mater = (('debit',"DebitCard"),('credit',"CreditCard"),('check',"Checkbook"))
class PersonCreationForm(forms.ModelForm):

    gender =forms.ChoiceField(choices=roles, widget=forms.RadioSelect())
    materials =forms.ChoiceField(choices=mater,widget=forms.RadioSelect())
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = City.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')