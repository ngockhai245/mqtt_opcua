let mqttClient;

window.addEventListener("load", (event) => {
    connectToBroker();

    const publishButton = document.querySelector(".publish");
    publishButton.addEventListener("click", function () {
        publishMessage();
    });
});

function connectToBroker() {
    const clientId = "client-" + Math.random().toString(36).substring(7);

    // MQTT broker web sockets, port 9001 as listener was declared in file "mosquitto.conf"
    const host = "ws://localhost:9001";

    const options = {
        keepalive: 60,
        clientId: clientId,
        protocolId: "MQTT",
        protocolVersion: 4,
        clean: true,
        reconnectPeriod: 1000,
        connectTimeout: 30 * 1000,
    };

    mqttClient = mqtt.connect(host, options);

    mqttClient.on("error", (err) => {
        console.log("Error: ", err);
        mqttClient.end();
    });

    mqttClient.on("reconnect", () => {
        console.log("Reconnecting...");
    });

    mqttClient.on("connect", () => {
        console.log("Client connected:" + clientId);
    });

    // Received MQTT message
    mqttClient.on("message", (topic, message, packet) => {
        console.log("Received message: " + message.toString() + " from topic: " + topic);
    });
}

function publishMessage() {
    const messageInput = document.querySelector("#message");

    const topic = document.querySelector("#topic").value.trim();
    const message = messageInput.value.trim();

    console.log(`Sending Topic: ${topic}, Message: ${message}`);

    mqttClient.publish(topic, message, {
        qos: 0,
        retain: false,
    });
    messageInput.value = "";
}
