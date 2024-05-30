import pytest
from lib.task_manager import *

def test_includes_todo_tag():
    result = task_manager("This is a #TODO")
    assert result == True
    
def test_includes_todo_tag_lower():
    result = task_manager("This is a #Todo")
    assert result == False
    
    
def test_does_not_include_todo():
    result = task_manager("Hello")
    assert result == False
    
def test_empty_string():
    result = task_manager("")
    assert result == False
    
def test_none():
    with pytest.raises(Exception) as e:
        task_manager()
    error_message = str(e.value)
    assert error_message == "You haven't entered anything"
        