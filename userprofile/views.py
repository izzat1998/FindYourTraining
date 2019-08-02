from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from post.models import Post
from userprofile.models import UserProfile


class UserPage(View):
    def get(self, request):
        current_user = UserProfile.objects.get(user=request.user)
        posts = Post.objects.filter(author=current_user)
        return render(request, 'userprofile/user_page.html', context={'user': current_user, 'posts': posts})


class Home(TemplateView):
    template_name = 'authorization/home.html'
