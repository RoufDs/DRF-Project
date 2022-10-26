from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class WatchListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 4
    last_page_strings = 'end'
    
    
class WatchListOfPagesPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start'