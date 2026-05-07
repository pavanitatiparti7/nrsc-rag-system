async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const userMessage = input.value;

    if (userMessage.trim() === "") {
        return;
    }

    chatBox.innerHTML += `
        <div class="message">
            <div class="user">You:</div>
            <div>${userMessage}</div>
        </div>
    `;

    input.value = "";

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userMessage
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <div class="message">
            <div class="bot">AI:</div>
            <div>${data.response}</div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}