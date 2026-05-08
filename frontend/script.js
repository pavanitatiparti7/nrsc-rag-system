// Connect to your FastAPI backend (assuming it runs on port 8000)
const API_BASE = "http://localhost:8000";

async function sendMessage() {
    const input = document.getElementById('userInput');
    const chatWindow = document.getElementById('chat-window');
    
    if (!input.value) return;

    // Add user message to UI
    chatWindow.innerHTML += `<div class="message user">${input.value}</div>`;
    
    const query = input.value;
    input.value = '';

    try {
        const response = await fetch(`${API_BASE}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: query })
        });
        
        const data = await response.json();
        chatWindow.innerHTML += `<div class="message bot">${data.response}</div>`;
    } catch (error) {
        console.error("Error connecting to backend:", error);
    }
}

document.getElementById('sendBtn').addEventListener('click', sendMessage);