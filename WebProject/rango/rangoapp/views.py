from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from rangoapp.models import Category, Page
from rangoapp.form import CategoryForm, PageForm
import urllib.parse


#region 主页相关
# 主页
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
#endregion


#region page页 相关

# 处理page请求
def page(request):
    context = RequestContext(request)
    return render_to_response('rangoapp/about.html', None, context)
    # return HttpResponse(
    #     'Rango Says: Here is the about page. <a href="/rangoapp/">back to main</a>'
    # )

# 新增 page
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

    return render(
        request, 'rangoapp/add_page.html', {
            'category_name_url': category_name_url,
            'category_name': category_name,
            'form': form
        }, context)


#endregion


#region category页 相关
# 种类category页
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

# 新增种类
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


#endregion


#region 非请求处理方法
def encode_url(urlstr):
    return urllib.parse.quote(urlstr)


def decode_url(url):
    try:
        result = urllib.parse.unquote(url)
    except:
        result = ''
    return result

#endregion
