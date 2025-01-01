document.addEventListener("DOMContentLoaded", function () {
    // Select the slider container and buttons
    const sliderContainer = document.querySelector("[data-slider-container]");
    const prevButton = document.querySelector("[data-slider-prev]");
    const nextButton = document.querySelector("[data-slider-next]");
  
    // Ensure the container exists
    if (!sliderContainer) return;
  
    // Get all slider items
    const sliderItems = Array.from(sliderContainer.children);
    const totalItems = 6; // Fixed to the exact number of items in the slider
  
    let currentIndex = 0; // Track the current index
    let itemWidth = calculateItemWidth(); // Dynamically calculate item width
  
    // Function to calculate item width based on viewport size
    function calculateItemWidth() {
      return sliderItems[0].getBoundingClientRect().width + 16; // Account for the gap
    }
  
    // Function to update the slider position
    function updateSliderPosition() {
      const offset = -(currentIndex * itemWidth);
      sliderContainer.style.transform = `translateX(${offset}px)`;
      sliderContainer.style.transition = "transform 0.3s ease-in-out";
    }
  
    // Recalculate item width on window resize
    window.addEventListener("resize", function () {
      itemWidth = calculateItemWidth();
      updateSliderPosition(); // Adjust the slider position after recalculating
    });
  
    // Click event for the previous button
    prevButton.addEventListener("click", function () {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = totalItems - 1; // Loop back to the last item
      }
      updateSliderPosition();
    });
  
    // Click event for the next button
    nextButton.addEventListener("click", function () {
      if (currentIndex < totalItems - 1) {
        currentIndex++;
      } else {
        currentIndex = 0; // Loop back to the first item
      }
      updateSliderPosition();
    });
  });
  