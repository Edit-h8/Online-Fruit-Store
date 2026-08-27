from django import template
from News_app.models import news

register = template.Library()


@register.inclusion_tag("news/Lastest_News.html")
def Lastest_News():
    News = news.objects.all().order_by("-created_date")[:4]

    return { "news" : News }



@register.inclusion_tag("news/Archived_post.html")
def Archived_Post():
    News = news.objects.all().order_by("created_date")[:4]

    return { "news" : News }
