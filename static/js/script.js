// Loading animation
document.addEventListener("DOMContentLoaded", function() {
  const loaderWrapper = document.querySelector(".loader-wrapper");
  const loader = document.querySelector(".loader");

  gsap.fromTo(loader, { rotation: 0 }, { rotation: 360, duration: 2, repeat: -1, ease: "linear" });

  window.addEventListener("load", function() {
    gsap.to(loaderWrapper, { duration: 0.5, opacity: 0, pointerEvents: "none", onComplete: () => loaderWrapper.classList.add("loaded") });
  });
});


// Add event listener for form submission
const newPostForm = document.getElementById("newPostForm");

if (newPostForm) {
  newPostForm.addEventListener("submit", function (e) {
    const titleInput = document.getElementById("title");
    const contentInput = document.getElementById("content");

    if (titleInput.value.trim() === "" || contentInput.value.trim() === "") {
      alert("Please fill in both title and content!");
      e.preventDefault(); // Prevent form submission if fields are empty
      return;
    }


  });
}

const toggleButton = document.getElementById('theme-toggle');
const bodyElement = document.body;
const themeIconMoon = document.querySelector('#theme-toggle i.fas.fa-moon');
const themeIconSun = document.querySelector('#theme-toggle i.fas.fa-sun');

// Check initial theme preference
const isDarkThemePreferred = localStorage.getItem('theme') === 'dark';
if (isDarkThemePreferred) {
  bodyElement.classList.add('dark-mode');
  themeIconMoon.style.display = 'none';
} else {
  themeIconSun.style.display = 'none';
}

// Toggle functionality
toggleButton.addEventListener('click', function () {
  bodyElement.classList.toggle('dark-mode');

  // Update local storage for persistence
  localStorage.setItem('theme', bodyElement.classList.contains('dark-mode') ? 'dark' : 'light');

  // Toggle theme icon
  themeIconMoon.style.display = bodyElement.classList.contains('dark-mode') ? 'none' : 'block';
  themeIconSun.style.display = bodyElement.classList.contains('dark-mode') ? 'block' : 'none';

  // Update individual element styles based on theme change
  const headers = document.querySelectorAll('.header');
  headers.forEach(header => {
    header.style.backgroundColor = bodyElement.classList.contains('dark-mode') ? 'var(--dark-bg)' : 'var(--light-bg)';
    header.style.color = bodyElement.classList.contains('dark-mode') ? 'var(--dark-text)' : 'var(--light-text)';
  });

  const footers = document.querySelectorAll('.footer');
  footers.forEach(footer => {
    footer.style.backgroundColor = bodyElement.classList.contains('dark-mode') ? 'var(--dark-bg)' : 'var(--light-bg)';
    footer.style.color = bodyElement.classList.contains('dark-mode') ? 'var(--dark-text)' : 'var(--light-text)';
  });
});






