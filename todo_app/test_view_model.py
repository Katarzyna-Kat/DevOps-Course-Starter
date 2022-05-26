import pytest
from todo_app.class_items import Item
from todo_app.view_model_class import ViewModel

@pytest.fixture
def items():
    _items = []
    to_do_item = Item("1", "ToDoItemName", "To Do")
    _items.append(to_do_item)
    doing_item = Item("2", "DoingItemName", "Doing")
    _items.append(doing_item)
    done_item = Item("3", "DoneItemName", "Done")
    _items.append(done_item)
    return _items


def test_to_do_items_only_shows_items_in_the_to_do_list(items):
    view_model = ViewModel(items)
    result: list[Item] = view_model.to_do_items
    assert len(result) == 1
    item = result[0]
    assert item.status == "To Do"
    assert item.name == "ToDoItemName"


def test_to_do_items_only_shows_items_in_the_doing_list(items):
    view_model = ViewModel(items)
    result: list[Item] = view_model.doing_items
    assert len(result) == 1
    item = result[0]
    assert item.status == "Doing"
    assert item.name == "DoingItemName"


def test_to_do_items_only_shows_items_in_the_done_list(items):
    view_model = ViewModel(items)
    result: list[Item] = view_model.done_items
    assert len(result) == 1
    item = result[0]
    assert item.status == "Done"
    assert item.name == "DoneItemName"
