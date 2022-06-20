from pydoc_data.topics import topics
from django.shortcuts import render, HttpResponse

# Create your views here.
movies = [
    {'id':1, 'title':'IronMan', 'year':2008},
    {'id':2, 'title':'Inception', 'year':2010},
    {'id':3, 'title':'Interstella', 'year':2014}
]

def HTMLTemplate(articleTag):
    global movies
    ol=''
    for movie in movies:
        ol+=f'<li><a href="/read/{movie["id"]}">{movie["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Favorite Movies</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''
def index(request):
    article='''
    <h2>Welcome</h2>
    add your favorite movies!
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global movies
    article =''
    for movie in movies:
        if movie['id'] == int(id):
            article = f'<h2>{movie["title"]}</h2>출시년도: {movie["year"]}'
    return HttpResponse(HTMLTemplate(article))

def create(requset):
    article='''
        <form action="/create/">
        <p><input type ="text" name="title" placeholder="title"></p>    
        <p><input type ="text" name="year" placeholder="year"></p>
        <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))