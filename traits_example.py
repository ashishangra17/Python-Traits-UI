'''
Example to demonstrate usage of traitsui in python
Prerequisites - install traits and traitsUI libraries
'''
from traitsui.api import View, Item, UItem, CheckListEditor, HGroup
from traits.api import HasTraits, Str, List, Button

my_to_do_list = ['li1', 'li2' , 'li3']

class ToDo(HasTraits) :
    todo_list = List(Str())
    completed_todos = List(Str())
    add_todo_field = Str()
    add_todo = Button()
    remove_todo = Button()
    '''
      my_view = View(
            Item('todo_list', #style = 'readonly'
                  )
    '''

    def _add_todo_changed(self):
        self.todo_list.append(self.add_todo_field)

    def _remove_todo_changed(self):
        self.todo_list = self.todo_list[:-1]

    my_view = View(
        Item('add_todo_field'),
        HGroup(
            UItem('add_todo'),
        UItem('remove_todo'),
        ),
        UItem('completed_todos',  style = 'custom' ,
             editor = CheckListEditor(name = 'todo_list')
        ),
        resizable=True
        #,UItem('add_todo')
        #,Item('completed_todos')
    )

my_to_do = ToDo(todo_list = my_to_do_list)

my_to_do.configure_traits()
