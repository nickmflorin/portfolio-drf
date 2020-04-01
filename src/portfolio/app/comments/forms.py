from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "cols": 128}),
        required=True,
    )

    class Meta:
        model = Comment
        fields = '__all__'
