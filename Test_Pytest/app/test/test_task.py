import pytest

from datetime import datetime
from datetime import timedelta
from app.task import Task, DueDateError

class TestTask():

    def test_task(self):
        assert True

    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)

        task = Task('title','description','usuario',due_date)

        assert task.title == 'title'
        assert task.description == 'description'
        assert task.assigned_to == 'usuario'
        assert task.due_date == due_date

    def test_due_date_error(self):
        #Contesto para el error
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('title','description','usuario',due_date)

