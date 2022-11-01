import pytest

from datetime import datetime
from app.task import Task 

class TestTask():

    def test_task(self):
        assert True

    def test_new_task(self):
        due_date = datetime.now()

        task = Task('title','description','usuario',due_date)

        assert task.title == 'title'
        assert task.description == 'description'
        assert task.assigned_to == 'usuario'
        assert task.due_date == due_date
