const userId = "{{ user.id }}";
console.log("User ID from Django:", userId);

const socket = new WebSocket(`ws://` + window.location.host + `/ws/${userId}`);

socket.onopen = function(event) {
    socket.send("Hello, FastAPI!");
};

socket.onmessage = function(event) {
    console.log("Received: " + event.data);
};

socket.onclose = function(event) {
    console.log("WebSocket closed");
};