const websocket = new WebSocket("ws://" + window.location.hostname + "/websocket", "protocolOne");

var slider_radial_position_m = 0.5;
var slider_angular_position_rad = 0.0;


websocket.onmessage = (event) => {
  console.log(event.data);

    msg_json_object = JSON.parse(event.data);

    if (msg_json_object.type == "topic") {
        if (msg_json_object.data.topic_name == "slider_radial_position_m") {
            slider_radial_position_m = msg_json_object.data.msg.data;
            console.log("slider_radial_position_m", slider_radial_position_m);
        } else if (msg_json_object.data.topic_name == "slider_angular_position_rad") {
            slider_angular_position_rad = msg_json_object.data.msg.data;
            console.log("slider_angular_position_rad", slider_angular_position_rad);
        }
    }
};

websocket.onopen = (event) => {
    console.log("websocket.onopen");
};
