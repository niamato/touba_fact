#-*-coding:utf-8-*
# Create your views here.
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response, redirect
from blog.models import Article
from blog.forms import ContactForm, ArticleForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context import RequestContext


def homepage(request):
    return render(request, 'blog/homepage.html')


def list_facts(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        show_lines = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        show_lines = paginator.page(paginator.num_pages)
    #return render(request, 'blog/facts.html', {'articles': articles})
    return render_to_response('blog/facts.html', RequestContext(request, {
        'articles': show_lines
    }))


def view_fact(request, id_fact):
    article = get_object_or_404(Article, id=id_fact)
    return render(request, 'blog/fact.html', {'article': article})


def mouridisme(request):
    return render(request, 'blog/mouridisme.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']
            return HttpResponseRedirect('/blog/')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'title': 'Contacter nous!', 'form': form})


def add(request):
    if not request.user.is_authenticated:
        return render('/blog/login')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            auteur = form.cleaned_data['auteur']
            contenu = form.cleaned_data['contenu']
            categorie = form.cleaned_data['categorie']
            form.save()
            return HttpResponseRedirect('/blog/facts')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_fact.html', {'title': 'Ajouter !', 'form': form})


def about(request):
    pass


def connexion(request):
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(homepage()))