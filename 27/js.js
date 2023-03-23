const myDiv = document.createElement('div');
const myDiv2 = document.createElement('div');
myDiv.className = 'buttons';
myDiv.style.background = 'white';
myDiv.style.textAlign = 'center'
myDiv2.className = 'paragraph';
myDiv2.style.background = 'white';
myDiv2.style.textAlign = 'left'


var numPool = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ],
rand = numPool[Math.floor(Math.random() * numPool.length)];

['Додати в друзі', 'Написати повідомлення', 'Запропонувати роботу'].map(buttonName => {
    let button = document.createElement('button');
    button.className = 'btn btn-info';
    button.id = 1;
    button.innerText = `${buttonName}` ;
    button.style.margin = '5px'
    myDiv.appendChild(button);
})

document.getElementsByTagName('body')[0].appendChild(myDiv);

['Кількість друзів '].map(paragraphName => {
    let paragraph = document.createElement('p');
    paragraph.className = 'alert alert-success';
    paragraph.innerText = `${paragraphName} ${rand}`;
    paragraph.style.margin = '5px'
    myDiv2.appendChild(paragraph);
})

document.getElementsByTagName('body')[0].appendChild(myDiv2);

const btn = document.getElementById('1')[0];
btn.addEventListener('click', (myVarEv) => {
  paragraph.innerText = `${paragraphName} ${rand+1}`;
  myVarEv.target.style.background = 'black';
  myVarEv.target.disabled = true;
});

