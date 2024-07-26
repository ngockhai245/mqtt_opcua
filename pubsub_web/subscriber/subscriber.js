let mqttClient;

window.addEventListener("load", (event) => {
    connectToBroker();

    const subscribeButton = document.querySelector("#subscribe");
    subscribeButton.addEventListener("click", function () {
        subscribeToTopic();
    });

    const unsubscribeButton = document.querySelector("#unsubscribe");
    unsubscribeButton.addEventListener("click", function () {
        unsubscribeToTopic();
    });
});

function connectToBroker() {
    const clientId = "client" + Math.random().toString(36).substring(7);

    // MQTT broker web sockets, port 9001 as listener was declared in file "mosquitto.conf"
    const host = "ws://localhost:9001";

    // streamBuilder, options: https://github.com/mqttjs/MQTT.js#mqttclientstreambuilder-options
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
    // listener to the "message event", this event gets called when received MQTT message from broker 
    mqttClient.on("message", (topic, message, packet) => {
        console.log(
            "Received Message: " + message.toString() + "\nOn topic: " + topic
        );
        const messageTextArea = document.querySelector("#message");
        // messageTextArea.value += message + "\r\n"; //create a scroll list of data published
        messageTextArea.value = message; //print newest data only in message box
    });
}

function subscribeToTopic() {
    const status = document.querySelector("#status");
    const topic = document.querySelector("#topic").value.trim();
    console.log(`Subscribing to Topic: ${topic}`);

    mqttClient.subscribe(topic, { qos: 0 });
    
    status.value = "SUBSCRIBED";
}

function unsubscribeToTopic() {
    const status = document.querySelector("#status");
    const topic = document.querySelector("#topic").value.trim();
    console.log(`Unsubscribing to Topic: ${topic}`);

    mqttClient.unsubscribe(topic, { qos: 0 });
    
    status.value = "UNSUBSCRIBED";
}