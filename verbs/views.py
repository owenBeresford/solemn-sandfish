from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 
from django.urls.exceptions import Resolver404
import re

def error_404(reqt:HttpRequest, exception: Resolver404)->HttpResponse:
    """ Emit a more user friendly error message
        IMPURE across Django stack
	
		I would like to know where doesn't seem be be an official means to access the path in that exception.
    """
    annoying:str=str(exception.args)
    annoying2=re.search( '\'path\': \'([^\']*)', annoying)
    return render(reqt, '404.html', {'reqt_url':'/'+annoying2.group(1), 'code':404 }, status=404)

def error_500(reqt:HttpRequest)->HttpResponse:
    """ Emit a more user friendly error message
        IMPURE across Django stack
    """
    print("[500] IS this code run?")
    return render(reqt, '500.html', {'reqt_url':"help!", 'code':500 }, status=500)

