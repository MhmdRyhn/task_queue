from task_queue import celery_app


@celery_app.task()
def long_add(number):
    result = 0
    for i in range(number):
        result += 1
    return result
