from django import template
from Shop_app.models import product
from News_app.models import news

register = template.Library()


@register.inclusion_tag("website/lastest_pruduct.html")
def lastest_pruduct():
    Product = product.objects.all().order_by("stock")[:3]

    return { "Product" : Product }


@register.inclusion_tag("website/lastest_news.html")
def lastest_news():
    new = news.objects.all().order_by("-created_date")[:3]

    return { "news" : new }
