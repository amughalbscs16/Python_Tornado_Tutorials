import tornado.web
import json
from controllers import registry


class MainAPIHandler(tornado.web.RequestHandler):

    """

    slug: the controller slug
    method: the controller method

    """

    def get(self, slug, method):
        print(self.request.path)
        self.write("This is the Main API Handler")

        # If correct controller
        controller = None
        if slug in registry:
            controller = registry['slug']
        ctrl_obj = controller()

        # If function in controller
        if method in ctrl_obj.methods:
            ctrl_method = getattr(ctrl_obj, method)
            # call the function with data
            ctrl_method()


