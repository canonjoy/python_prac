#will use Quasar.dev for this
import justpy as jp
class Home:
    path = "/"
    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        layout = jp.QLayout(a=wp, view="hHh lpR fFf") 
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=layout, show_if_above=True,
                            v_model="left",
                            bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_class = "p-2 m-2 text-lg text-blue-400 hover:text-blue-300"
        jp.A(a=qlist, text="Home", href="/home", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictonary", href="/dictionary", classes=a_class)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_class)
        jp.Br(a=qlist)


        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text = "Instant Dictionary") 
        container = jp.QPageContainer(a=layout)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is a home page!", classes = "text=lg")
        jp.Div(a=div, text="""
               This is content
               """)
        return wp


    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True




