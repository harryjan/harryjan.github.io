// Add an event listener for the scroll event
window.addEventListener('scroll', function () {
    const header = document.querySelector('header'); // Select the header element
    if (window.scrollY > 80) {
        header.classList.add('scrolled'); // Add the 'scrolled' class
    } else {
        header.classList.remove('scrolled'); // Remove the 'scrolled' class
    }
});