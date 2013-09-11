import tornado.ioloop
import tornado.web
import os
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
	    techs = ['Koding', 'Python', 'Tornado', 'AngularJS']
        self.render('index.html', techs=techs)
 
settings = {"template_path": os.path.join(os.path.dirname(__file__), "templates")}

application = tornado.web.Application([(r"/", MainHandler)], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
