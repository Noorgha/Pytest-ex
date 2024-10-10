import pytest
from TaskManager import TaskManager as t
from TaskManager import Task as T

@pytest.fixture
def setup():
    return t.TaskManager(" ")


@pytest.fixture
def taskSetup():
    return T.Task("any")


#@pytest.mark.parametrize("des", ["tocode", "tosleep", "toeat"])
def test_addTasks(setup, taskSetup):
    setup.addTasks(taskSetup)
    assert taskSetup in setup.listTasks()


def test_addTasksToFile(setup):
    with pytest.raises(FileNotFoundError) as e:
        setup.addTasksToFile()
        assert setup.loadTasks() == setup.listTasks()


def test_loadTasks(setup):
    with pytest.raises(FileNotFoundError):
        assert setup.loadTasks() == setup.listTasks()
