from django.forms import ModelForm
from microblog.models import post

class postform(ModelForm):
	class Meta:
		model = post