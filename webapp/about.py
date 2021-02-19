import justpy as jp

class About:
#each instance has same path
#composition has-a inhernce is-a
    path = "/about"
    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is a about page!", classe="text-4xl m-2"
              )
        jp.Div(a=div, text="""
               What ever content this is
               """, classes = "text-lg"
              )
        return wp
#get output right away  input_box.on('input', cls.get_fun)!!!!!!!!!!!!!!!!!!!!!

#staticmethod-> avoid expectation of instance or class
jp.Route(About.path, About.serve)
jp.justpy(port=8001)

