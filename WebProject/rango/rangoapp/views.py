from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': 'I am bold font from the context.'}
    return render_to_response('rangoapp/index.html', context_dict, context)


def page(request):
    context = RequestContext(request)
    return render_to_response('rangoapp/about.html', None, context)

    # return HttpResponse(
    #     'Rango Says: Here is the about page. <a href="/rangoapp/">back to main</a>'
    # )
