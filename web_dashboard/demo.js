function startConnect(){
    clientID = "clientID - " + parseInt(Math.random() * 1000);//random client id 
    
    host = document.getElementById("host").value;
    port = document.getElementById("port").value;
    userID = document.getElementById("username").value;
    passwordID = document.getElementById("password").value;

    //Thong bao trong box
    document.getElementById("messages").innerHTML += "<span>Connecting to " + host + " on port " + port + "</span><br>";
    document.getElementById("messages").innerHTML += "<span>Using the client ID " + clientID + "</span><br>";

    client = new Paho.Client(host, Number(port), clientID);

    //callback, su dung bien client de su dung cac chuc nang khac cua thu vien
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;

    client.connect({ onSuccess: onConnect });
}

function onConnect() {
    topic = document.getElementById("topic_sub").value;
    document.getElementById("messages").innerHTML += "<span>Subscribing to topic " + topic + "</span><br>";
    
    client.subscribe(topic);
}

function onConnectionLost(responseObject) {
    document.getElementById("messages").innerHTML += "<span>ERROR: Connection is lost.</span><br>";
    if (responseObject != 0) {
        document.getElementById("messages").innerHTML += "<span>ERROR: " + responseObject.errorMessage + "</span><br>";
    }
}

function onMessageArrived(message) {
    console.log("onMessageArrived: " + message.payloadString);
    document.getElementById("messages").innerHTML += "<span>Topic: " + message.destinationName + " | Message : " + message.payloadString + "<span><br>";
}

function startDisconnect(){
    client.disconnect();
    document.getElementById("messages").innerHTML += "<span>Disconnected. </span><br>";
}

function publishMessage(){
    msg = document.getElementById("message").value;
    topic = document.getElementById("topic_pub").value;

    Message = new Paho.Message(msg);
    Message.destinationName = topic;

    client.send(Message);
    
    document.getElementById("messages").innerHTML += "<span> Message to topic " + topic + " is sent </span><br>";
}