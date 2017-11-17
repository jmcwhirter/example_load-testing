from locust import HttpLocust
from locust import TaskSet
from locust import task

class HelloTaskSet(TaskSet):

    @task
    def my_task(self):
        self.client.get('/')

class HelloLocust(HttpLocust):
    task_set = HelloTaskSet
