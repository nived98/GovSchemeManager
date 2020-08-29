from django import forms

from schemes.models import StateSchemeList, CentreSchemeList


class CreateStateSchemeListForm(forms.ModelForm):

    class Meta:
        model = StateSchemeList
        fields = ['title', 'overview', 'monetory_benefits', 'eligibility_criterion',
                  'minority', 'gender', 'family_members', 'BPL', 'caste', 'religion', 'age', 'max_yearly_income']


class CreateCentreSchemeListForm(forms.ModelForm):

    class Meta:
        model = CentreSchemeList
        fields = ['title', 'overview', 'monetory_benefits', 'eligibility_criterion',
                  'minority', 'gender', 'family_members', 'BPL', 'caste', 'religion', 'age', 'max_yearly_income']


class UpdateStateSchemeListForm(forms.ModelForm):

    class Meta:
        model = StateSchemeList
        fields = ['title', 'overview', 'monetory_benefits', 'eligibility_criterion',
                  'minority', 'gender', 'family_members', 'BPL', 'caste', 'religion', 'age', 'max_yearly_income']

    def save(self, commit=True):
        state_scheme_listings = self.instance
        state_scheme_listings.title = self.cleaned_data['title']
        state_scheme_listings.overview = self.cleaned_data['overview']
        state_scheme_listings.monetory_benefits = self.cleaned_data['monetory_benefits']
        state_scheme_listings.eligibility_criterion = self.cleaned_data['eligibility_criterion']
        state_scheme_listings.minority = self.cleaned_data['minority']
        state_scheme_listings.gender = self.cleaned_data['gender']
        state_scheme_listings.family_members = self.cleaned_data['family_members']
        state_scheme_listings.BPL = self.cleaned_data['BPL']
        state_scheme_listings.caste = self.cleaned_data['caste']
        state_scheme_listings.religion = self.cleaned_data['religion']
        state_scheme_listings.age = self.cleaned_data['age']
        state_scheme_listings.max_yearly_income = self.cleaned_data['max_yearly_income']
        # if self.cleaned_data['image']:
        #     property_listings.image = self.cleaned_data['image']

        if commit:
            state_scheme_listings.save()
        return state_scheme_listings


class UpdateCentreSchemeListForm(forms.ModelForm):

    class Meta:
        model = CentreSchemeList
        fields = ['title', 'overview', 'monetory_benefits', 'eligibility_criterion',
                  'minority', 'gender', 'family_members', 'BPL', 'caste', 'religion', 'age', 'max_yearly_income']

    def save(self, commit=True):
        centre_scheme_listings = self.instance
        centre_scheme_listings.title = self.cleaned_data['title']
        centre_scheme_listings.overview = self.cleaned_data['overview']
        centre_scheme_listings.monetory_benefits = self.cleaned_data['monetory_benefits']
        centre_scheme_listings.eligibility_criterion = self.cleaned_data['eligibility_criterion']
        centre_scheme_listings.minority = self.cleaned_data['minority']
        centre_scheme_listings.gender = self.cleaned_data['gender']
        centre_scheme_listings.family_members = self.cleaned_data['family_members']
        centre_scheme_listings.BPL = self.cleaned_data['BPL']
        centre_scheme_listings.caste = self.cleaned_data['caste']
        centre_scheme_listings.religion = self.cleaned_data['religion']
        centre_scheme_listings.age = self.cleaned_data['age']
        centre_scheme_listings.max_yearly_income = self.cleaned_data['max_yearly_income']
        # if self.cleaned_data['image']:
        #     property_listings.image = self.cleaned_data['image']

        if commit:
            state_scheme_listings.save()
        return state_scheme_listings
