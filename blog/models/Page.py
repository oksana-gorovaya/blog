class Page:
    def __init__(self, records, number, total_pages):
        self.records = records
        self.number = int(number)
        self.total_pages = total_pages

    def has_previous(self):
        return self.number > 1

    def has_next(self):
        return self.number < self.total_pages

    def previous_page_number(self):
        return self.number - 1

    def next_page_number(self):
        return self.number + 1

