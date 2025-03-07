document.addEventListener('DOMContentLoaded', function() {
    // Get elements
    const envelope = document.querySelector('.envelope');
    const seal = document.querySelector('.seal');
    
    // Debug check
    console.log("Envelope script loaded");
    console.log("Envelope element found:", !!envelope);
    console.log("Seal element found:", !!seal);
    
    // Add click event to the seal
    seal.addEventListener('click', function() {
        console.log("Seal clicked - opening envelope");
        envelope.classList.add('opened');
    });
});