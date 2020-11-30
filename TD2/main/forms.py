from django import forms

class HomeForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
