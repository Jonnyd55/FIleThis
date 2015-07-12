from django import forms
from cabinet.models import File

class UploadFileForm(forms.ModelForm): 
	provider_url = forms.CharField(help_text="Provider Url", required=False, label='Provider URL')
	provider_name = forms.CharField(help_text="Provider Name", required=False)
	title = forms.CharField(help_text="Title ", required=False)
	bookmark_date = forms.DateField(help_text = 'Bookmark Date', required=False)
	pub_date = forms.DateField(required=False, help_text= 'Published Date')
	text = forms.CharField(widget = forms.Textarea, required=False, help_text = 'text')
	thumbnail = forms.CharField(max_length = 500, required=False, help_text='thumbnail')
	summary = forms.CharField(widget=forms.Textarea, required=False, help_text='summary')
	author = forms.CharField(required=False, help_text='author')
	description = forms.CharField(widget = forms.Textarea, required=False, help_text = 'text')

	def __init__(self, *args, **kwargs):
		super(UploadFileForm, self).__init__(*args, **kwargs)
		self.fields['provider_url'].widget.attrs['class'] = 'form-control'
		self.fields['provider_name'].widget.attrs['class'] = 'form-control'
		self.fields['bookmark_date'].widget.attrs['class'] = 'form-control'
		self.fields['title'].widget.attrs['class'] = 'form-control'
		self.fields['pub_date'].widget.attrs['class'] = 'form-control'
		self.fields['text'].widget.attrs['class'] = 'form-control'
		self.fields['thumbnail'].widget.attrs['class'] = 'form-control'
		self.fields['summary'].widget.attrs['class'] = 'form-control'
		self.fields['author'].widget.attrs['class'] = 'form-control'
		self.fields['description'].widget.attrs['class'] = 'form-control'

	class Meta:
		model = File