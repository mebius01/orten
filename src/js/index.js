import '../img/logo.png'
import '../img/map.png'
import '../img/favicon-32x32.png'
import '../css/main.scss'


// top down and bottom up
const scrollA = document.getElementById('scrollA');
const scrollB = document.getElementById('scrollB');
window.addEventListener('scroll', function() {
    const heightDoc = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (document.documentElement.scrollTop > 100) {
        scrollA.style.display = "block";
        scrollB.style.display = "block";
    } else {
        scrollA.style.display = "none";
        scrollB.style.display = "none";
    }
    if (document.documentElement.scrollTop > heightDoc - 100) {
        scrollB.style.display = "none";
    }
});
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
function downFunction() {
    document.body.scrollTop = heightDoc;
    document.documentElement.scrollTop = heightDoc;
}
scrollA.addEventListener('click', topFunction)
scrollB.addEventListener('click', downFunction)

// Canegories
const categories = document.getElementById("categories")
console.log(categories);


const card = document.querySelector(".card")

card.addEventListener("click", cardHendler)
console.log(card);
function cardHendler(e) {
    e.preventDefault()
    console.log(e.form-footer);
}