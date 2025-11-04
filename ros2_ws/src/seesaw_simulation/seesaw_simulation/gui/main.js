const websocket = new WebSocket("ws://" + window.location.hostname + "/websocket", "protocolOne");

websocket.onmessage = (event) => {
  console.log(event.data);

    msg_json_object = JSON.parse(event.data);

    if (msg_json_object.type == "topic") {
        if (msg_json_object.data.topic_name == "slider_radial_position_m") {
            var slider_radial_position_msg = msg_json_object.data.msg;
        } else if (msg_json_object.data.topic_name == "slider_angular_position_rad") {
            var slider_angular_position_msg = msg_json_object.data.msg;
        }
    }
};

websocket.onopen = (event) => {
    console.log("websocket.onopen");
};
