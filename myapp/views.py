from pydoc_data.topics import topics
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
movies = [
    {'id':1, 'title':'IronMan', 'year':2008},
    {'id':2, 'title':'Inception', 'year':2010},
    {'id':3, 'title':'Interstella', 'year':2014}
]
nextId=4

def HTMLTemplate(articleTag, id=None):
    global movies
    contextUI=''
    if id !=None:
        contextUI= f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input  type="submit" value="delete">
                </form>
            </li>
        '''
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
            {contextUI}
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
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    if request.method =='GET':
        article='''
            <form action="/create/" method="post">
            <p><input type ="text" name="title" placeholder="title"></p>    
            <p><input type ="text" name="year" placeholder="year"></p>
            <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method =="POST":
        title = request.POST['title']
        year = request.POST['year']
        newMovie={"id":nextId, "title":title, "year":year}
        movies.append(newMovie)
        url='/read/'+str(nextId) 
        nextId =nextId + 1
        return redirect(url)

@csrf_exempt
def delete(request):
    global movies
    if request.method=='POST':
        id=request.POST['id']
        newMovies=[]
        for movie in movies:
            if movie['id'] != int(id):
                newMovies.append(movie)
        movies=newMovies
        return redirect('/')