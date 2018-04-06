from bottle_neck import BaseHandler


class AppView(BaseHandler):
    """App view.
    """
    def get(self):
        return self.render('templates/index')
