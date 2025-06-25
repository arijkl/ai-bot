const messageInput = document.getElementById('message');
const responseArea = document.getElementById('response');
const loadingDots = document.getElementById('loading');

function send() {
  const message = messageInput.value.trim();
  if (!message) return;

  // Show loading
  loadingDots.classList.remove('hidden');

  // Simulate AI response delay
  setTimeout(() => {
    loadingDots.classList.add('hidden');

    // Add user message
    const userBubble = document.createElement('div');
    userBubble.className = 'bubble user-bubble';
    userBubble.textContent = message;
    responseArea.appendChild(userBubble);

    // Simulate AI response (based on user input)
    const aiBubble = document.createElement('div');
    aiBubble.className = 'bubble ai-bubble';
    aiBubble.textContent = getAIResponse(message);
    responseArea.appendChild(aiBubble);

    // Scroll chat down
    responseArea.scrollTop = responseArea.scrollHeight;

    // Clear message input
    messageInput.value = '';
  }, 1000);
}

function getAIResponse(message) {
  const lower = message.toLowerCase();

  if (lower.includes("hello") || lower.includes("hi")) {
    return "Hello there! How can I help you today?";
  }
  if (lower.includes("your name")) {
    return "I’m your AI Helper Bot 🤖, here to answer questions.";
  }
  if (lower.includes("help")) {
    return "Sure! Ask me anything — I'm here for you.";
  }
  if (lower.includes("time")) {
    return "It's currently " + new Date().toLocaleTimeString();
  }
  if (lower.includes("date")) {
    return "Today's date is " + new Date().toLocaleDateString();
  }

  // Default
  return "I'm not sure I understand, but I'm learning!";
}

function toggleTheme() {
  document.body.classList.toggle("dark-theme");
}

function clearChat() {
  if (confirm("Are you sure you want to clear the chat?")) {
    responseArea.innerHTML = '';
  }
}

function saveChat() {
  alert("Save chat feature coming soon!");
}

function startListening() {
  alert("Voice assistant coming soon!");
}
document.getElementById('sidebarToggle').addEventListener('click', () => {
  const sidebar = document.getElementById('chat-history');
  const container = document.querySelector('.container');

  sidebar.classList.toggle('active');
  container.classList.toggle('sidebar-open');
});



