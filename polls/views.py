from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Blog, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Blog.objects.filter(
            blog_date__lte=timezone.now()
        ).order_by('-blog_date')[:5]


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Blog.objects.filter(blog_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Blog
    template_name = 'polls/results.html'


def vote(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        selected_choice = blog.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'blog': blog,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:detail', args=(blog.id,)))
