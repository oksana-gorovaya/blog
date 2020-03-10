from math import ceil

from blog.models.Page import Page


class Paginator:
    def __init__(self, records, items_per_page):
        self.records = records
        self.items_per_page = items_per_page
        self.total_pages = self.num_pages()

    def get_page(self, number):
        return Page(self.generate_content(number), number, self.total_pages)

    def num_pages(self):
        return ceil(self.records.count() / self.items_per_page)

    def generate_content(self, number):
        last_record = self.items_per_page * int(number)
        first_record = last_record - self.items_per_page
        return self.records[first_record:last_record]

