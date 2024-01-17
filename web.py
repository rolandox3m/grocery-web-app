import streamlit
from functions import get_todos, write_todos
grocery_list = get_todos()


def add_grocery():
    new_grocery = streamlit.session_state['grocery_input'] + '\n'
    grocery_list.append(new_grocery)
    write_todos(grocery_list)


streamlit.title('My Web App')
streamlit.subheader('This is my grocery list')
streamlit.write('This app is to increase your productivity')


for index, item in enumerate(grocery_list):
    checkbox = streamlit.checkbox(item, key=item)
    if checkbox:
        grocery_list.pop(index)
        write_todos(grocery_list)
        del streamlit.session_state[item]
        streamlit.rerun()


streamlit.session_state['grocery_input'] = ""
streamlit.text_input(label='New grocery',
                     placeholder='Enter grocery',
                     on_change=add_grocery,
                     key='grocery_input'
                     )

