from locust import TaskSet, task
from locust.contrib.fasthttp import FastHttpUser
from locust.main import main
import re, sys


class DashboardTask(TaskSet):
    @task
    def get_dashboard(self):
        response = self.client.get(f'/dashboard/{ self.get_test_id() }')

    def get_test_id(self):
        return '10001000'


class MobileAppUser(FastHttpUser):
    tasks = [DashboardTask]

    def __init__(self, *args, **kwargs):
        super(MobileAppUser, self).__init__(*args, **kwargs)

    def wait_time(self):
        return 0

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
