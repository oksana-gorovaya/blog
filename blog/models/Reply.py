
class Reply:
    def __init__(self, parent):
        self.parent = parent

    def save(self, comment_form):
        new_comment = comment_form.save(commit=False)
        new_comment.post = self.parent.post
        new_comment.parent = self.parent
        new_comment.save()

    def reply(self):
        return Reply(self.parent)

