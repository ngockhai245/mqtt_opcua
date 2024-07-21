function onConnect(){
    clientID = "clientID - " + parseInt(Math.random() * 100);
    host = document.getElementById("host").value;
    port = document.getElementById("port").value;
    userID = document.getElementById("username").value;
    passwordID = document.getElementById("password").value;

    document.getElementById("messages").innerHTML += "<span>Connecting to " + host + "on port " + port + "</span><br>";
    document.getElementById("messages").innerHTML += "<span>Using the client ID " + clientID + "</span><br>";

    client = new paho.MQTT.Client(host, Number(port), clientID);

    //su dung bien client de su dung cac chuc nang khac cua thu vien
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;

    client.connect({
        onSuccess: onConnect,
        userName: userID,
        passwordID: passwordID
    })
}

function onConnect() {
    topic = document.getElementById("topic_sub").value;
    document.getElementById("message").innerHTML += "<span>Subscribing to topic " + topic + "</span><br>"
    
    client.subscribe();
}

function onConnectionLost(responseObject) {
    document.getElementById("messages").innerHTML += "<span>ERROR: Connection is lost.</span><br>";
    if (responseObject != 0) {
        document.getElementById("messages").innerHTML += "<span>ERROR: " + responseObject.errorMessage + "</span><br>";
    }
}

function onMessageArrived(message) {
    console.log("onMessageArrived: " + message.payloadString);
    document.getElementById("messages").innerHTML += "<span>Topic: " + message.destinationName + "| Message : " + message.payloadString + "<span><br>";
}

function onDisconnect(){

}

function publishMessage(){

}