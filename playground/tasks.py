from celery.task import task


@task(name='long_add')
def long_add(number):
    result = 0
    for i in range(1, number):
        result += 1
    return result
