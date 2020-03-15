from math import ceil
from mptt.utils import get_cached_trees
from blog.models.Page import Page


class Pagination:
    def __init__(self, records, items_per_page):
        self.records = records
        self.items_per_page = items_per_page
        self.total_pages = self.num_pages()

    def get_page(self, number):
        return Page(number, self.total_pages)

    def num_pages(self):
        return ceil(self.records.count() / self.items_per_page)

    def generate_content(self, number):
        last_record = (self.items_per_page * int(number)) - 1
        first_record = (last_record - self.items_per_page) + 1
        root_comments = get_cached_trees(self.records)[first_record:last_record + 1]
        return [tree.get_descendants(include_self=True) for tree in root_comments]
