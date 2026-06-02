const chatWidget = document.getElementById("chat-widget");
const postId = chatWidget.dataset.postId;
let chatHistory = [];

const chatInput = document.getElementById("chat-input");
const chatSend = document.getElementById("chat-send");
const chatMessages = document.getElementById("chat-messages");

function appendMessage(role, text) {
  const div = document.createElement("div");
  div.classList.add("chat-message", role === "user" ? "chat-message-user" : "chat-message-model");

  if (role === "model") {
    const label = document.createElement("span");
    label.classList.add("chat-ai-label");
    label.textContent = "✦ Atlas";
    div.appendChild(label);
  }

  div.appendChild(document.createTextNode(text));
  chatMessages.appendChild(div);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function sendMessage() {
  //User input
  const message = chatInput.value.trim();
  if (!message) return;

  chatInput.value = "";
  appendMessage("user", message);

  //Typing indicator
  const typingIndicator = document.getElementById("chat-typing");
  typingIndicator.classList.remove("d-none");
  chatMessages.scrollTop = chatMessages.scrollHeight;

  //Using custom API
  const response = await fetch(`/chat/${postId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, history: chatHistory })
  });

  typingIndicator.classList.add("d-none");

  const data = await response.json();
  appendMessage("model", data.reply);
  chatHistory = data.history;
}

chatSend.addEventListener("click", sendMessage);
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});