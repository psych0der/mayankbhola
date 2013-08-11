from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from blogengine.models import Post


def getPostsList(request, selected_page=1):
    print 'hey'
    posts = Post.objects.all().order_by('-pub_date')

    pages = Paginator(posts, 5)

    try:
        returned_page = pages.page(int(selected_page))
    except EmptyPage:
        returned_page = pages.page(1)

    # Display all the posts
    return render_to_response('posts.html', {'posts': returned_page.object_list, 'page': returned_page})


def getPost(request, postSlug):

    post = Post.objects.filter(slug=postSlug)
    return render_to_response('posts.html', {'posts': post})
