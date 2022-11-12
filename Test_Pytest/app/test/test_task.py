import pytest

from datetime import datetime
from datetime import timedelta
from app.task import Task, DueDateError


def is_available_to_skip():
    """En esta funcion se ejecutara para verificiar si se puede realizar la prueba unitaria o si esta tiene que ser saltada"""
    return False

class TestTask():

    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)

        task = Task('title','description','usuario',due_date)

        assert task.title == 'title'
        assert task.description == 'description'
        assert task.assigned_to == 'usuario'
        assert task.due_date == due_date

    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        #Contesto para el error
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('title','description','usuario',due_date)

    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title','Description', 'usuario', due_date)

        assert task.due_date > datetime.now()

    @pytest.mark.skip(reason='La prueba no cumple con los requerimientos')
    def test_skip_one(self):
        pass

    @pytest.mark.skipif(is_available_to_skip(), reason='La prueba no cumple con los requerimientos')
    def test_skip_two(self):
        assert True

