const myButton = document.querySelector('#changeTextBtn');
const myParagraph = document.querySelector('#message');

myButton.addEventListener('click',function(){
    myParagraph.textContent = '哇！文字被改變了！'
})