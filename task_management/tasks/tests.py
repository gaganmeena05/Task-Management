from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskUrlsTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='Dommy Task', description='Dommy Description')

    def test_gettasks(self):
        url = reverse('gettasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_actiontasks(self):
        url = reverse('actiontasks', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TaskViewsTests(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Dommy Task',
            description='Dommy Description',
            status=False,
            priority=1,
        )

    def test_TaskLists_get(self):
        url = reverse('gettasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_TaskLists_post(self):
        url = reverse('gettasks')
        initial = Task.objects.count()
        response = self.client.post(url, data = {'title': 'Dommy task', 'description': 'Dommy description'},content_type='application/json')
        final = Task.objects.count()
        self.assertEqual(initial+1, final)
        self.assertEqual(response.status_code, 201)

    def test_TaskActions_view(self):
        url = reverse('actiontasks', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_TaskActions_get(self):
        url = reverse('gettasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_TaskActions_put(self):
        url = reverse('actiontasks', args=[self.task.pk])
        response = self.client.put(url, data = {'title': 'Dommy task', 'description': 'Dommy description'},content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_TaskActions_delete(self):
        url = reverse('actiontasks', args=[self.task.pk])
        intial = Task.objects.count()
        response = self.client.delete(url)
        final = Task.objects.count()
        self.assertEqual(response.status_code, 204)
        self.assertEqual(intial-1, final)



class TaskModelTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title='Dommy Task',
            description='Dommy Description',
            status=False,
            priority=1,
        )

    def test_creation(self):
        self.assertEqual(self.task.title, 'Dommy Task')
        self.assertEqual(self.task.description, 'Dommy Description')
        self.assertFalse(self.task.status)
        self.assertEqual(self.task.priority, 1)

    def test_str_representation(self):
        self.assertEqual(str(self.task), 'Dommy Task')

    def test_default_values(self):
        initial = Task.objects.count()
        new_task = Task.objects.create(title='New Dommy Task')
        final = Task.objects.count()
        self.assertFalse(new_task.status, False)
        self.assertEqual(new_task.priority, 0)
        self.assertEqual(initial+1, final)

    def test_update(self):
        self.task.title = 'Dommy title'
        self.task.description = 'Dommy description'
        self.task.status = True
        self.task.priority = 2
        self.task.save()

        updated_task = Task.objects.get(pk=self.task.pk)
        self.assertEqual(updated_task.title, 'Dommy title')
        self.assertEqual(updated_task.description, 'Dommy description')
        self.assertTrue(updated_task.status, True)
        self.assertEqual(updated_task.priority, 2)

    def test_deletion(self):
        inital = Task.objects.count()
        self.task.delete()
        final = Task.objects.count()
        self.assertEqual(inital - 1, final)

    def test_created_timestamp(self):
        self.assertIsNotNone(self.task.created)

    def test_priority_choices(self):
        for value, label in Task.priority_choices:
            task = Task.objects.create(title="Dommy", priority=value)
            self.assertEqual(task.priority, value)

    def test_status_choices(self):
        for value, label in Task.status_choices:
            task = Task.objects.create(title="Dommy", status=value)
            self.assertEqual(task.status, value)