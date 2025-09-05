// Add an event listener for the scroll event
window.addEventListener('scroll', function () {
    const header = document.querySelector('header'); // Select the header element
    if (window.scrollY > 80) {
        header.classList.add('scrolled'); // Add the 'scrolled' class
    } else {
        header.classList.remove('scrolled'); // Remove the 'scrolled' class
    }
});

// CSS styles
header {
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

header.scrolled {
    background-color: #333; /* Dark background */
    color: #fff; /* Light text */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Add a shadow */
}