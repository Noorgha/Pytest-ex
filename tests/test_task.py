import pytest
from TaskManager import Task as t

@pytest.fixture
def setup():
    return t.Task("tosomething")


@pytest.mark.parametrize("des", ["tocode", "tosleep", "toeat"])
def test_taskCreationWithParams(des):
    assert t.Task(des).description == des


def test_taskCreation(setup):
    # assert t.Task(des).description == des
    assert setup.description == "tosomething"


def test_taskStatus(setup):
    assert setup.status == False


def test_MarkAsCompleted(setup):
    setup.markTaskAsCompleted()
    assert setup.taskStatus() == "completed"


@pytest.mark.xfail
def test_xFail(setup):
    assert setup.status == True