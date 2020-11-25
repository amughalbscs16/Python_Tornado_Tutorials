import tornado.web


class MainAPIHandler(tornado.web.RequestHandler):

    """

    slug: the controller slug
    method: the controller method

    """

    def __init__(self):
        super().__init__()
        self.stored_var = "stored_val"

    def prepare(self):
        pass

    def get(self, slug, method):
        print(self.request.path)
        self.write("This is the Main API Handler")


    def post(self):
        pass
