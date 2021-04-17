import redis
from django.shortcuts import render
from django.http import HttpResponse
from celery.result import AsyncResult
from .tasks import my_first_task
redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0)


# Create your views here.
def homepage(request):
	return HttpResponse("<h4>Hello World</h4>")


def tasks(request, page):
	response = my_first_task.delay(1)
	redis_cache.set('task1', response.id)
	ready = response.get()
	return HttpResponse(ready)

def check_task_status(request):
    task_id = redis_cache.get('task1')
    return AsyncResult(task_id).status
