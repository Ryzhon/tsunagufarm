console.log("Drag.js has been loaded!");
document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.comment-container');
    const dragbar = document.querySelector('.drag-bar');

    let isDragging = false;
    let startY = 0;

    dragbar.addEventListener('mousedown', function(event) {
        isDragging = true;
        startY = event.clientY;
        console.log("Mouse down at:", startY);
    });

    window.addEventListener('mousemove', function(event) {
    if (!isDragging) return;

    let deltaY = event.clientY - startY;
    console.log("Mouse move. Delta:", deltaY);

    if (deltaY >50) {
        container.classList.add('collapsed');
    } else if (deltaY <-50) {
        container.classList.remove('collapsed');
    }


});


    window.addEventListener('mouseup', function() {
        isDragging = false;
    });
});
