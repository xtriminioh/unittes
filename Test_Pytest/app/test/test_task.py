import pytest

from datetime import datetime
from datetime import timedelta
from app.task import Task, DueDateError

def is_available_to_skip():
    """En esta funcion se ejecutara para verificiar si se puede realizar la prueba unitaria o si esta tiene que ser saltada"""
    return False

@pytest.fixture
def username():
    print('\n >>> Ejecutar el codigo antes de la prueba.')
    yield 'Cody'
    print('\n >>> Ejecutar el codigo despues de la prueba.')

def test_username(username):
    print(username)
    assert username == 'Cody'

class TestTask():

    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    @pytest.mark.parametrize(
        'title, descripcion, assigned_to, due_date',
        [
            ('title 1', 'description 1', 'assigned_to 1', datetime.now() + timedelta(days=1)),
            ('title 2', 'description 2', 'assigned_to 2', datetime.now() + timedelta(days=1)),
            ('title 3', 'description 3', 'assigned_to 3', datetime.now() + timedelta(days=1)),
            ('title 4', 'description 4', 'assigned_to 4', datetime.now() + timedelta(days=1)),
        ]
    )
    def test_new_task(self, title, descripcion, assigned_to, due_date ):
        due_date = datetime.now() + timedelta(days=1)

        task = Task(title, descripcion, assigned_to,due_date)

        assert task.title == title 
        assert task.description == descripcion
        assert task.assigned_to == assigned_to 
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

