from rest_framework.pagination import PageNumberPagination

class PropertyPagination(PageNumberPagination):
    """
    Pagination class for properties.

    This pagination class sets the page size to 8 properties per page.
    """

    page_size = 8
