document.addEventListener('DOMContentLoaded', function() {
    // Get carousel elements
    const carouselContainer = document.querySelector('.carousel-container');
    const slides = document.querySelectorAll('.carousel-slide');
    const prevButton = document.querySelector('.carousel-prev');
    const nextButton = document.querySelector('.carousel-next');
    
    // If carousel doesn't exist on the page, exit the function
    if (!carouselContainer) return;
    
    let currentIndex = 0;
    const slideCount = slides.length;
    
    // Exit if there are no slides
    if (slideCount === 0) return;
    
    // Set up initial state
    updateCarousel();
    
    // Add event listeners for buttons
    prevButton.addEventListener('click', function() {
        currentIndex = (currentIndex - 1 + slideCount) % slideCount;
        updateCarousel();
    });
    
    nextButton.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateCarousel();
    });
    
    // Set up automatic sliding
    let interval = setInterval(autoSlide, 10000); // Change slide every 10 seconds
    
    // Pause automatic sliding when mouse hovers over carousel
    carouselContainer.addEventListener('mouseenter', function() {
        clearInterval(interval);
    });
    
    // Resume automatic sliding when mouse leaves carousel
    carouselContainer.addEventListener('mouseleave', function() {
        interval = setInterval(autoSlide, 10000);
    });
    
    // Function to handle automatic sliding
    function autoSlide() {
        currentIndex = (currentIndex + 1) % slideCount;
        updateCarousel();
    }
    
    // Function to update carousel display
    function updateCarousel() {
        const offset = -currentIndex * 100; // Each slide is 100% width
        carouselContainer.style.transform = `translateX(${offset}%)`;
    }
});