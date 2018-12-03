from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from rangoapp.models import Category, Page
from rangoapp.form import CategoryForm, PageForm


def index(request):
    context = RequestContext(request)

    category_list = Category.objects.order_by('-likes')[:5]  # 加-符号: 倒序
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {
        'categories': category_list,
        'pages': page_list
    }

    for category in category_list:
        category.url = category.name.replace(' ', '_')
    return render_to_response('rangoapp/index.html', context_dict, context)


def page(request):
    context = RequestContext(request)
    return render_to_response('rangoapp/about.html', None, context)
    # return HttpResponse(
    #     'Rango Says: Here is the about page. <a href="/rangoapp/">back to main</a>'
    # )


def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
        context_dict['category_name_url'] = encode_url(category_name)
    except Category.DoesNotExist:
        pass

    return render_to_response('rangoapp/category.html', context_dict, context)


def add_category(request):
    context = RequestContext(request)

    if request.method == 'POST':
        # request.POST: A dictionary-like object containing all given HTTP POST parameters,
        #               providing that the request contains form data
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, 'rangoapp/add_category.html', {'form': form}, context)


def encode_url(urlstr):
    return '/rangoapp/category/{0}'.format(urlstr)


def deocde_url(url):
    try:
        result = url.split('/')[3]
    except:
        result = ''
    return result


def add_page(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)

            cat = Category.objects.get(name=category_name)
            page.category = cat
            page.views = 0
            page.save()
        
            return category(request, category_name_url)
    
        else:
            print(form.errors)
    else:
        form = PageForm()

    return render(request,  'rangoapp/add_page.html',
            {'category_name_url': category_name_url,
             'category_name': category_name,
             'form': form},
             context)
