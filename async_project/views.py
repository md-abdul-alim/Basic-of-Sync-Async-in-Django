from django.http import HttpResponse
import time, asyncio
from movies.models import Movie
from stories.models import Story

#https://docs.djangoproject.com/en/3.1/topics/async/
from asgiref.sync import sync_to_async
#helper function
def get_movies():
    print('Prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all the movies!')

def get_stories():
    print('Prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all the stories!')

@sync_to_async
def get_movies_async():
    print('Prepare to get the movies...')
    asyncio.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all the movies!')

@sync_to_async
def get_stories_async():
    print('Prepare to get the stories...')
    asyncio.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all the stories!')



#views
def home_view(request):
    start_time = time.time()
    total = (time.time()- start_time)
    print('total howe view:',total)
    return HttpResponse('Hello World')

def main_view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time()- start_time)
    print('total Sync Time:',total)
    return HttpResponse('sync')
    #total: 7.0250163078308105 s

#Note: When creating async await functions (without the sync_to_async decorator) instead of 'time.sleep(x)' we should use await 'asyncio.sleep(x)'
async def main_view_async(request):
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_movies_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])
    ##or
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total Async Time: ',total)
    return HttpResponse('async')
    #total:  0.007979154586791992 s
