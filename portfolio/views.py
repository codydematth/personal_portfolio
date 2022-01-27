from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def homeView(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]

    context = {'posts': posts}
    return render(request, 'index.html', context)

def postsView(request):
    posts = Post.objects.filter(active=True)

    page = request.GET.get('page')

    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'posts.html', context)


def postView(request,slug):
    post = Post.objects.get(slug=slug)
    
    context = {'post':post}
    return render(request, 'post.html', context)


def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['coding.cody01@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'email_sent.html')