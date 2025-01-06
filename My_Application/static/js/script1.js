document.addEventListener("DOMContentLoaded", () => {
    const profileBtn = document.getElementById("profile-btn");
    const dropdownMenu = document.getElementById("dropdown-menu");
    const logoutBtn = document.getElementById("logout-btn");
  
    if (!profileBtn || !dropdownMenu || !logoutBtn) {
      console.error("One or more elements are missing. Check your HTML IDs.");
      return;
    }
  
    // Toggle dropdown visibility
    profileBtn.addEventListener("click", (event) => {
      event.stopPropagation(); // Prevent click event from propagating to the document
      console.log("Profile button clicked.");
      dropdownMenu.classList.toggle("dropdown-visible");
    });
  
    // Handle logout button click
    logoutBtn.addEventListener("click", () => {
      console.log("Logout button clicked.");
      alert("Logging out...");
      window.location.href = "/logout"; // Replace with your logout URL
    });
  
    // Close dropdown if clicked outside
    document.addEventListener("click", (event) => {
      if (!profileBtn.contains(event.target) && !dropdownMenu.contains(event.target)) {
        console.log("Click outside dropdown, hiding menu.");
        dropdownMenu.classList.remove("dropdown-visible");
      }
    });
  });
// Select dropdown and sub-dropdown elements
// Main dropdown toggle
const dropdownToggle = document.querySelector('.dropdown-toggle');
const dropdownContent = document.querySelector('.dropdown-content');

// Sub-dropdowns
const subDropdowns = document.querySelectorAll('.sub-dropdown > a');

// Toggle main dropdown visibility
dropdownToggle.addEventListener('click', (event) => {
    event.preventDefault();
    dropdownContent.classList.toggle('show');
});

// Toggle sub-dropdowns visibility
subDropdowns.forEach((subDropdown) => {
    subDropdown.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation(); // Prevent bubbling up to the document
        const subDropdownContent = subDropdown.nextElementSibling;
        subDropdownContent.classList.toggle('show');
    });
});

// Close dropdowns when clicking outside
document.addEventListener('click', (event) => {
    if (!dropdownToggle.contains(event.target) && !dropdownContent.contains(event.target)) {
        dropdownContent.classList.remove('show');
    }
    document.querySelectorAll('.sub-dropdown-content').forEach((subContent) => {
        if (!subContent.contains(event.target)) {
            subContent.classList.remove('show');
        }
    });
});






function toggleDarkMode() {
    // Toggle dark mode for body
    document.body.classList.toggle('dark-mode');
    
    // Toggle dark mode for navbar
    document.querySelector('.navbar').classList.toggle('dark-mode');
    
    // Toggle dark mode for search bar
    document.querySelector('.search-bar').classList.toggle('dark-mode');
    
    // Toggle dark mode for logout button
    document.querySelector('.logout').classList.toggle('dark-mode');
    
    // Toggle dark mode for sidebar
    document.querySelector('.sidebar').classList.toggle('dark-mode');
    
    // Toggle dark mode for main content
    document.querySelector('.main-content').classList.toggle('dark-mode');
    
    // Toggle dark mode for all cards
    document.querySelectorAll('.card').forEach(card => {
      card.classList.toggle('dark-mode');
    });
  }

  // Toggle the notification sidebar
  function toggleNotificationSidebar() {
    const sidebar = document.getElementById('notificationSidebar');
    sidebar.classList.toggle('open'); // Add or remove the "open" class
  }


  


  
  