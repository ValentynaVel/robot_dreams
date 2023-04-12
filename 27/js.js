const myDiv = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'white';
myDiv.style.textAlign = 'center'

// Пошук рандомного числа друзів
let friendCount = Math.floor(Math.random() * 100) + 1;
document.getElementById("friends").innerText = `Кількість друзів: ${friendCount}`;

// Створення 3 кнопок
['Додати в друзі', 'Написати повідомлення', 'Запропонувати роботу'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-info';
    button.id = 1;
    button.innerText = `${buttonName}` ;
    button.style.margin = '5px'
    myDiv.appendChild(button);
})
document.getElementsByTagName('body')[0].appendChild(myDiv);

// Додавання ивенту після кліку на button 'Додати в друзі'.
let buttonFriends =  document.getElementsByClassName('btn btn-info')[0];
let eventHandler = (event) => {
    event.target.disabled = true;
    buttonFriends.innerText = "Очікується підтвердження";
    friendCount++;
    document.getElementById("friends").innerText = `Кількість друзів: ${friendCount}`;
}
buttonFriends.addEventListener('click', eventHandler);




