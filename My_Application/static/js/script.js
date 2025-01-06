document.addEventListener("DOMContentLoaded", () => {
  // Dropdown Button and Menu
  const profileBtn = document.getElementById("profile-btn");
  const dropdownMenu = document.getElementById("dropdown-menu");
  const logoutBtn = document.getElementById("logout-btn");

  if (!profileBtn || !dropdownMenu || !logoutBtn) {
    console.error("One or more elements are missing. Check your HTML IDs.");
    return;
  }

  // Toggle dropdown visibility when profile button is clicked
  profileBtn.addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent click event from propagating to the document
    console.log("Profile button clicked.");
    dropdownMenu.classList.toggle("show"); // Ensure you're using the correct class here
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
      dropdownMenu.classList.remove("show");
    }
  });

  // Dropdown and Sub-dropdown Elements
  const dropdownToggle = document.querySelector('.dropdown-toggle');
  const dropdownContent = document.querySelector('.dropdown-content');
  const subDropdowns = document.querySelectorAll('.sub-dropdown > a');
  
  // Toggle the visibility of the main dropdown
  if (dropdownToggle) {
    dropdownToggle.addEventListener('click', (event) => {
      event.preventDefault();  // Prevent default behavior (if any)
      dropdownContent.classList.toggle('show');
    });
  }

  // Toggle sub-dropdown visibility
  subDropdowns.forEach((subDropdown) => {
    subDropdown.addEventListener('click', (event) => {
      event.preventDefault();  // Prevent default anchor behavior
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
});

// Toggle Dark Mode
function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  document.querySelector('.navbar').classList.toggle('dark-mode');
  document.querySelector('.search-bar').classList.toggle('dark-mode');
  document.querySelector('.logout').classList.toggle('dark-mode');
  document.querySelector('.sidebar').classList.toggle('dark-mode');
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

document.getElementById('venuesAvailable').onclick = function (event) {
  event.preventDefault(); // Prevent default link behavior

  fetch('{% url "admin_event_list" %}')
      .then(response => response.text())
      .then(html => {
          document.getElementById('home-content').innerHTML = html; // Load the content into the home-content div
      })
      .catch(error => console.error('Error loading events:', error));
};