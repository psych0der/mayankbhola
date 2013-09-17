import time
from blogengine.models import Post,Category,Tag
from calendar import month_name

def monthList():
    """Make a list of months to show archive links."""

    if not Post.objects.count(): return []

    # set up vars
    year, month = time.localtime()[:2]
    first = Post.objects.order_by("pub_date")[0]
    fyear = first.pub_date.year
    fmonth = first.pub_date.month
    months = []

    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, month_name[m],'/blog/archive/'+str(y)+'/'+str(m)+'/'))
    return months



def categoryList():
    if not Category.objects.count() : return []
    categories = Category.objects.all()[0:10]
    return categories


def TagList():
    if not Tag.objects.count() : return []
    tags = Tag.objects.all()
    return tags