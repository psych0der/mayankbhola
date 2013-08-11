from django.shortcuts import render_to_response
from blogengine.models import Post

def getRecentPosts(request):
    # Get all blog posts
    posts = Post.objects.all().order_by('-pub_date')

    # Sort posts into chronological order
    #sorted_posts = posts.

    # Display all the posts
    return render_to_response('posts.html', { 'posts':posts})