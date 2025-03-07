document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const envelope = document.querySelector('.envelope');
    const seal = document.querySelector('.seal');
    const openButton = document.getElementById('open-invitation');
    
    // Add click event to the seal
    seal.addEventListener('click', function() {
        // Add the 'opened' class to start the animation
        envelope.classList.add('opened');
    });
    
    // Add click event to the open invitation button
    openButton.addEventListener('click', function() {
        // Redirect to the home page after a slight delay
        setTimeout(function() {
            window.location.href = '/';
        }, 500);
    });
});