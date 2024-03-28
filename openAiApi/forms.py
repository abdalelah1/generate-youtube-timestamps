from django import forms
class YouTubeURLForm(forms.Form):
    youtube_url = forms.URLField(label='YouTube Video URL', max_length=200)