from django.test import TestCase

# for testing the client side
from django.urls import reverse
from .models import Tasks

# Create your tests here.

# client side view tests


def create_task(title):
    return Tasks.objects.create(title=title)


class ClientToDo(TestCase):

    # when no tasks added
    def test_no_tasks(self):
        response = self.client.get(reverse('tasks:list'))

        # the status code wshould be up
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["tasks"], [])

    # when task is added
    def test_with_task(self):

        create_task("Push this one to GitHub")
        response = self.client.get(reverse('tasks:list'))
        self.assertQuerysetEqual(response.context["tasks"], [
                                 '<Tasks: Push this one to GitHub>'])
