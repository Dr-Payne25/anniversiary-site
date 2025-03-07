document.addEventListener('DOMContentLoaded', function() {
    console.log("Envelope script loaded"); // Debug message
    
    // Get elements
    const envelope = document.querySelector('.envelope');
    const seal = document.querySelector('.seal');
    const openButton = document.getElementById('open-invitation');
    
    // Add click event to the seal
    seal.addEventListener('click', function() {
        console.log("Seal clicked"); // Debug message
        envelope.classList.add('opened');
    });
    
    // Add click event to the open invitation button
    openButton.addEventListener('click', function() {
        console.log("Button clicked, redirecting soon..."); // Debug message
        
        // Use the correct path based on your URL configuration
        const homePath = '/home/'; // If you changed to use '/home/' as per earlier suggestion
        
        console.log("Will redirect to: " + homePath);
        
        // Redirect to the home page after a delay
        setTimeout(function() {
            window.location.href = homePath;
        }, 1000); // Longer delay to ensure animation completes
    });
});