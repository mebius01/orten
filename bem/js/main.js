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