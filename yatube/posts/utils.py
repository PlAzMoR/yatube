from django.core.paginator import Paginator

COUNT_POST = 5

def get_page_context(request, post_list):
    paginator = Paginator(post_list, COUNT_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj