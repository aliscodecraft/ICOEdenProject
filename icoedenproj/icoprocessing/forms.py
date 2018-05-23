import re
import time
from datetime import date

from django import forms

from .models import ICOModel


class ICOForm(forms.ModelForm):
    class Meta:

        fields = '__all__'

        model = ICOModel

        widgets = {'ico_start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'mm/jj/aaaa'},
                                                     format='DD/MM/YYYY'),

                   'ico_end_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'mm/jj/aaaa'},
                                                   format='DD/MM/YYYY'),

                   'min_cap_in_eth': forms.TextInput(
                       attrs={'class': 'form-control', 'placeholder': 'Min CAP in ETH ( like 1000000 )'}),

                   'max_cap_in_eth': forms.TextInput(
                       attrs={'class': 'form-control', 'placeholder': 'Max CAP in ETH ( like 1000000 )'}),

                   'tokens_per_eth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tokens per ETH'}),

                   'discount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount'}),

                   'max_token_supply': forms.TextInput(
                       attrs={'class': 'form-control', 'placeholder': 'Max Token Supply ( like 1000000 )'}),

                   'for_sale': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'For Sale ( like 1000000 )'}),

                   'white_label_address': forms.TextInput(
                       attrs={'class': 'form-control', 'placeholder': 'White label address'}),

                   'admin_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admin Email'})

                   }

    def clean_ico_end_date(self):

        raw_ico_start_date = self.cleaned_data.get('ico_start_date')
        raw_ico_end_date = self.cleaned_data.get('ico_end_date')

        converted_start_date = time.strptime(str(raw_ico_start_date) ,'%Y-%m-%d' )
        converted_end_date = time.strptime( str(raw_ico_end_date) , '%Y-%m-%d')

        if converted_end_date <= converted_start_date :
            raise forms.ValidationError('La date de fin doit être superieur à celle du début.')
        else:

            return raw_ico_end_date


    def convert_to_num(self, data):

        if 'm' in data or 'M' in data:
            return int(data) * 1000000
        if 'k' in data or 'K' in data:
            return int(data) * 1000

        if 'b' in data or 'B' in data:
            return int(data) * 1000000000

        return int(data)






    def clean_min_cap_in_eth(self):
        data = self.cleaned_data.get('min_cap_in_eth')

        data = str(data)

        if not re.match(r'^\d+', data) and re.match(r'^\d+[kmbKMB]', data):

            raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')
        else:

            return self.convert_to_num(data)

    def clean_max_cap_in_eth(self):
        data = self.cleaned_data.get('max_cap_in_eth')
        data = str(data)

        min = self.cleaned_data.get('min_cap_in_eth')

        if not re.match(r'^\d+[kmbKMB]', data) and not re.match(r'^\d+', data):
            raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')

        if int(data) <= min:
            raise forms.ValidationError('Le cap max doit être supérieur au cap min.')

        return self.convert_to_num(data)

    def clean_max_token_supply(self):
        data = self.cleaned_data.get('max_token_supply')
        data = str(data)

        if not re.match(r'^\d+[kmbKMB]', data) and not re.match(r'^\d+', data):
            raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')

        else:
            return self.convert_to_num(data)

    def clean_for_sale(self):

        data = self.cleaned_data.get('for_sale')
        data = str(data)

        if not re.match(r'^\d+[kmbKMB]', data) and not re.match(r'^\d+', data):
            raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')

        else:
            return self.convert_to_num(data)

