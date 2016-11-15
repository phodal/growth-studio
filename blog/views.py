from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render_to_response('blog/list.html', {
        'blogs': blogs
    })


def blog_detail(request, slug):
    return render_to_response('blog/detail.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })
