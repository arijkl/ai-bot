// Save settings to localStorage
document.getElementById('darkModeToggle').addEventListener('change', function () {
  localStorage.setItem('darkMode', this.checked);
});

document.getElementById('voiceToggle').addEventListener('change', function () {
  localStorage.setItem('voiceEnabled', this.checked);
});

document.getElementById('chatStyle').addEventListener('change', function () {
  localStorage.setItem('chatStyle', this.value);
});

document.getElementById('fontSize').addEventListener('change', function () {
  localStorage.setItem('fontSize', this.value);
});

document.getElementById('countrySelect').addEventListener('change', function () {
  localStorage.setItem('userCountry', this.value);
});

document.getElementById('languageSelect').addEventListener('change', function () {
  localStorage.setItem('userLanguage', this.value);
});

// Clear chat history
function clearHistory() {
  localStorage.removeItem('chatHistory');
  alert('Chat history cleared!');
}
// dark mode toggle
function toggleDarkMode() {
  const body = document.body;
  const isDarkMode = localStorage.getItem('darkMode') === 'true';
  
  if (isDarkMode) {
    body.classList.remove('dark-mode');
    localStorage.setItem('darkMode', 'false');
  } else {
    body.classList.add('dark-mode');
    localStorage.setItem('darkMode', 'true');
  }
}

// Load settings from localStorage
window.onload = function () {
  document.getElementById('darkModeToggle').checked = localStorage.getItem('darkMode') === 'true';
  document.getElementById('voiceToggle').checked = localStorage.getItem('voiceEnabled') === 'true';
  document.getElementById('chatStyle').value = localStorage.getItem('chatStyle') || 'bubble';
  document.getElementById('fontSize').value = localStorage.getItem('fontSize') || 'medium';
  document.getElementById('countrySelect').value = localStorage.getItem('userCountry') || 'us';
  document.getElementById('languageSelect').value = localStorage.getItem('userLanguage') || 'en';
}
document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const href = this.getAttribute('href');
    const overlay = document.getElementById('page-transition');
    overlay.classList.add('active');
    setTimeout(() => window.location.href = href, 500);
  });
});
const title = document.querySelector('h1');

document.addEventListener('mousemove', (e) => {
  const { innerWidth, innerHeight } = window;
  const x = e.clientX / innerWidth;
  const y = e.clientY / innerHeight;

  const posX = x * 100;
  const posY = y * 100;

  title.style.backgroundPosition = `${posX}% ${posY}%`;
});

// Optional: clear history function
function clearHistory() {
  alert("History cleared! (This is just a placeholder.)");
}

