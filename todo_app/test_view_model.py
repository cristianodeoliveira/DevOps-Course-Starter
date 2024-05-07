from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel

# Test Todo items
def test_todo_only_list_todo_items():
    #Arrange
    items =[
        Item(1,"Started Todo","To Do"),
        Item(2,"In Progress Todo","Doing"),
        Item(3,"Finished Todo","Done")
    ]
    view_model = ViewModel(items)

    #ACT
    returned_items = view_model.todo_items

    #Assert
    assert len(returned_items) == 1
    returned_single_item = returned_items[0]
    assert returned_single_item.status == "To Do"

# Test Doing items
def test_doing_only_list_doing_items():
    #Arrange
    items =[
        Item(1,"Started Todo","To Do"),
        Item(2,"In Progress Todo","Doing"),
        Item(3,"Finished Todo","Done")
    ]
    view_model = ViewModel(items)

    #ACT
    returned_items = view_model.doing_items

    #Assert
    assert len(returned_items) == 1
    returned_single_item = returned_items[0]
    assert returned_single_item.status == "Doing"


# Test done items
def test_done_items_property_only_shows_done_items_and_nothing_else():
    #Arrange
    items = [
        Item(1,"Started Todo", "To Do"),
        Item(2,"In Progress Todo", "Doing"),
        Item(3,"Finished Todo", "Done")
    ]
    view_model = ViewModel(items)

    #ACT
    returned_items = view_model.done_items

    #Assert
    assert len(returned_items) == 1
    returned_single_item = returned_items[0]
    assert returned_single_item.status == "Done"
