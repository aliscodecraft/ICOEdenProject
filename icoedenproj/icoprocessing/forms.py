import re
from django import forms
from .models import ICOModel


class ICOForm(forms.ModelForm):




    class Meta:

        fields = '__all__'


        model = ICOModel


        widgets = {'ico_start_date' : forms.DateInput(attrs={'class' :'form-control', 'placeholder':'jj/mm/aaaa'}, format='%dd/%mm/%YYYY'),

                   'ico_end_date': forms.DateInput(attrs={'class':'form-control' , 'placeholder':'jj/mm/aaaa'}, format='%dd/%mm/%YYYY' ),

                   'min_cap_in_eth' : forms.TextInput(attrs= {'class':'form-control' , 'placeholder': 'Min CAP in ETH ( like 1m )'}) ,

                    'max_cap_in_eth' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Max CAP in ETH ( like 10m )'}) ,

                    'tokens_per_eth' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tokens per ETH'}) ,

                    'discount' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Discount'}) ,

                    'max_token_supply': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max Token Supply ( like 1b )'}),

                    'for_sale' : forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'For Sale ( like 1m )'}),

                    'white_label_address' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'White label address'}),

                    'admin_email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Admin Email'})

                   }

    def clean_min_cap_in_eth(self):
        data = self.cleaned_data.get('min_cap_in_eth')

        if not re.match(r'^\d+[kmbKMB]', data ) :
             raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')
             #  return ''
        else:
            return data

    def clean_max_cap_in_eth(self):
        data = self.cleaned_data.get('max_cap_in_eth')

        if not re.match(r'^\d+[kmbKMB]', data ) :
             raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')
             return ''
        else:
            return data


    def clean_max_token_supply(self):
        data = self.cleaned_data.get('max_token_supply')

        if not re.match(r'^\d+[kmbKMB]', data ) :
             raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')
             return ''
        else:
            return data


    def clean_for_sale(self):

        data = self.cleaned_data.get('for_sale')

        if not re.match(r'^\d+[kmbKMB]', data ) :
             raise forms.ValidationError('Veuillez respecter le format de saisie pour ce champ.')
             return ''
        else:
            return data