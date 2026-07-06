import React, { useState } from 'react';
import './TodoList.css';

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [headingInput, setHeadingInput] = useState('');
  const [listInputs, setListInputs] = useState({});

  const handleAddTodo = () => {
    if (headingInput.trim() !== '') {
      setTodos([...todos, { heading: headingInput, lists: [] }])
      setHeadingInput('');
    }
  };

  const handleDeleteTodo = (index) => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  const handleAddList = (index) => {
    if (listInputs[index] && listInputs[index].trim() !== '') {
      setTodos(prevTodos => {
        const newTodos = [...prevTodos];
        newTodos[index] = {
          ...newTodos[index],
          lists: [...newTodos[index].lists, listInputs[index]]
        };
        return newTodos;
      });
      setListInputs('');
    }
  }

  const handleListInputChange = (index, value) => {
    setListInputs({ ...listInputs, [index]: value });
  };

  const handleHeadingSubmit = (e) => {
    e.preventDefault();
    handleAddTodo();
  }

  const handleListSubmit = (e, index) => {
    e.preventDefault();
    handleAddList(index);
  }

  return (
    <>
      <div className="todo-container">
        <h1 className="title">My Todo List</h1>
        <form className='input-container' onSubmit={handleHeadingSubmit}>
          <input
            type="text"
            className="heading-input"
            placeholder="Enter heading"
            value={headingInput}
            onChange = {(e) => {setHeadingInput(e.target.value)}}
          />
          <button className="add-list-button">Add Heading</button>
        </form>
      </div>
      <div className="todo_main">
        {todos.map((todo, index) => (
          <div key={index} className='todo-card'>
            <div className='heading_todo'>
              <h3>{todo.heading}</h3>
              <button className='delete-button-heading' onClick={() => handleDeleteTodo(index)}>Delete Heading</button>
            </div>
            <ul>
                {todo.lists.map((list, listIndex) => (
                  <li key={listIndex} className='todo_inside_list'>
                    <p>{list}</p>
                  </li>
                ))}
            </ul>
            <form className='add_list' onSubmit={(e) => handleListSubmit(e, index)}>
              
              <input
                type='text'
                className='list-input'
                placeholder='Add List'
                value={listInputs[index] || ''}
                onChange={(e) => handleListInputChange(index, e.target.value)}/> 
              <button className='add-list-button'>Add List</button>
            </form>
          </div>
        ))}
      </div>
    </>
  );
};

export default TodoList;
