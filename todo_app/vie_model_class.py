import pytest
from todo_app.class_items import Item


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def to_do_items(self):
        to_do_output = []
        for item in self._items:
            if item.status == "To Do":
                to_do_output.append(item)
        return to_do_output
        

    @property
    def doing_items(self):
        doing_output = []
        for item in self._items:
            if item.status == "Doing":
                doing_output.append(item)
        return doing_output

    @property
    def done_items(self):
        done_output = []
        for item in self._items:
            if item.status == "Done":
                done_output.append(item)
        return done_output