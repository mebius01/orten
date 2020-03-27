  //Get the button
  var mybutton = document.getElementById("myBtn");
  // When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
  // When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

var acc = document.getElementsByClassName("link");
var i;
for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight){
        panel.style.maxHeight = null;
        } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

$(document).ready(function(){
    $('.menu').click(function(){
        $('ul').toggleClass('active');
    })
})

// Modal windows for product_detail
let more = document.querySelector('.more'),
        overlay = document.querySelector('.overlay'),
        close = document.querySelector('.close');
    more.addEventListener('click', function() {
        overlay.style.display = 'block';
    });
    close.addEventListener('click', function() {
        overlay.style.display = 'none';
    });
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' || event.keyCode === 27) {
            overlay.style.display = 'none';
        }
    });

    let more_2 = document.querySelector('.more_2'),
        overlay_2 = document.querySelector('.overlay_2'),
        close_2 = document.querySelector('.close_2');
    more_2.addEventListener('click', function() {
        overlay_2.style.display = 'block';
    });
    close_2.addEventListener('click', function() {
        overlay_2.style.display = 'none';
    });
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' || event.keyCode === 27) {
            overlay_2.style.display = 'none';
        }
    });
    
    let more_3 = document.querySelector('.more_3'),
        overlay_3 = document.querySelector('.overlay_3'),
        close_3 = document.querySelector('.close_3');
    more_3.addEventListener('click', function() {
        overlay_3.style.display = 'block';
    });
    close_3.addEventListener('click', function() {
        overlay_3.style.display = 'none';
    });
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' || event.keyCode === 27) {
            overlay_3.style.display = 'none';
        }
    });