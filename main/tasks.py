from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
import requests

logger = get_task_logger(__name__)
@task(name='my_first_task')
def my_first_task(page):
    r = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=949bff8e08031ca57f596f86e7440dde&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=' + page)
    print(r.json())
    return('first_task_done')
