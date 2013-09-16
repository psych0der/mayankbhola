from django.shortcuts import render_to_response ,render
from django.core.paginator import Paginator, EmptyPage
from blogengine.models import Post, Category
from django.contrib.syndication.views import Feed
from mayankbhola.common.sidebar import monthList , categoryList
from django.views.generic.dates import YearArchiveView ,MonthArchiveView






def aboutMe(request):
      return render_to_response('about.html', { 'type':'about'})


def projects(request):
      return render_to_response('projects.html', { 'type':'project'})




def getPostsList(request, selected_page=1):
    # Get all blog posts
    posts = Post.objects.all().order_by('-pub_date')

    # Add pagination
    pages = Paginator(posts, 4)

    # Get the specified page
    try:
        returned_page = pages.page(int(selected_page))
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the posts
    return render_to_response('posts.html', { 'posts':returned_page.object_list, 'page':returned_page,'months': monthList() , 'categories':categoryList(),'type':'blog'})

def getPost(request, postSlug):
    # Get specified post
    post = Post.objects.filter(slug=postSlug)

    # Display specified post
    return render_to_response('single.html', { 'posts':post,'months': monthList() , 'categories':categoryList(),'type':'blog'})

def getCategory(request, categorySlug, selected_page=1):
    # Get specified category
    posts = Post.objects.all().order_by('-pub_date')
    category_posts = []
    for post in posts:
        if post.categories.filter(slug=categorySlug):
            category_posts.append(post)

    # Add pagination
    pages = Paginator(category_posts, 5)

    # Get the category
    try :
        category = Category.objects.filter(slug=categorySlug)[0]
    
    except IndexError:
        category = categorySlug.replace('-', ' ')

    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the posts
    return render_to_response('category.html', { 'posts': returned_page.object_list, 'page': returned_page, 'category': category,'months': monthList() , 'categories':categoryList(),'type':'blog'})



def getTag(request, tagSlug, selected_page=1):
    # Get specified category
    posts = Post.objects.all().order_by('-pub_date')
    tag_posts = []
    for post in posts:
        if post.tags.filter(slug=tagSlug):
            tag_posts.append(post)

    # Add pagination
    pages = Paginator(tag_posts, 5)

    # Get the category
    try :
        tag = Tag.objects.filter(slug=tagSlug)[0]
    
    except IndexError:
        tag = tagSlug.replace('-', ' ')

    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    # Display all the posts
    return render_to_response('category.html', { 'posts': returned_page.object_list, 'page': returned_page, 'category': tag,'months': monthList() , 'categories':categoryList()})

class PostsFeed(Feed):
    title = "Psych0der's Blog posts"
    link = "feeds/posts/"
    description = "Posts from Psych0der's blog"

    def items(self):
        return Post.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text


class PostYearArchiveView(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    template_name ="year_archive.html"
    months = monthList()
    categories = categoryList()

class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    template_name = "month_archive.html"
    def get_context_data(self, *args, **kwargs):
        context = super(PostMonthArchiveView, self).get_context_data(*args, **kwargs)
        context['months'] = monthList()
        context['categories'] = categoryList()
        context['type']='blog'

        return context
    




def handler404(request):
    return render(request,'404.html')


