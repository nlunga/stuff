getUserInput('btn-todo').addEventListener('click', addToView);
var newItem = getUserInput('new-item');

function addToView(e) {
    if (newItem.value !== '') {
        e.preventDefault();
        var globalView = [];
        // console.log(newItem.value);
        document.getElementById('todo-view').innerHTML = 'Hi';
        // getUserInput('todo-view').innerHTML += `<li> ${newItem.value}</li>`;
        // updateView(newItem.value);
    }
}

function getUserInput(id) {
    return document.getElementById(id);
}

function updateView(data) {
    return getUserInput('todo-view').innerHTML += `<li> ${data}</li>`;
}