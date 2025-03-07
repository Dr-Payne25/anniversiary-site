document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const envelope = document.querySelector('.envelope');
    const seal = document.querySelector('.seal');
    
    console.log("Envelope script loaded successfully");
    
    // Add click event to the seal
    seal.addEventListener('click', function() {
        console.log("Seal clicked - opening envelope");
        
        // Add the 'opened' class to animate the envelope
        envelope.classList.add('opened');
        
        // Optional: Add automatic redirect after animation completes
        // setTimeout(function() {
        //     window.location.href = '/home/';
        // }, 2500);
    });
});