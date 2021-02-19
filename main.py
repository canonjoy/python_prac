import justpy as jp
from webapp.home import Home

jp.Route(Home.path, Home.serve)
jp.justpy()


