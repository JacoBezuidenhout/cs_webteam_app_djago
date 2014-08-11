from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from microblog.models import category,post
from microblog.form import postform

# Create your views here.
def main(request):
	f = postform()
	return render(request, 'home.html',locals())
	return HttpResponse('Hello world')

def editPost(request, _id=None):
	print _id
	if _id:
		p = get_object_or_404(post,id=_id)
		f = postform(instance=p)
	else:
		f = postform()
	if request.POST:
		if _id:
			f = postform(request.POST,instance=p)
		else:
			f = postform(request.POST)
		if f.is_valid():
			f.save()
			return redirect('microblog')
	return render(request, 'edit.html',locals())