const websocket = new WebSocket("ws://" + window.location.hostname + "/websocket", "protocolOne");

var slider_radial_position_m = 0.5;
var slider_angular_position_rad = 0.0;


// --- config: set your expected max radius in meters ---
const MAX_RADIUS_METERS = 1.0; // adjust to your system's max r

// --- canvas setup ---
const canvas = document.getElementById("gui_view");
const ctx = canvas.getContext("2d");

// simple proportional draw
function draw() {
  // assume the canvas already has its CSS size; use its internal size
  const w = canvas.width, h = canvas.height;
  const cx = w / 2, cy = h / 2;

  // scale so MAX_RADIUS_METERS maps to 45% of the shortest canvas half-dimension
  const pxPerM = 0.45 * Math.min(w, h) / MAX_RADIUS_METERS;

  // convert polar to Cartesian
  const r_px = slider_radial_position_m * pxPerM;
  const x = cx + r_px * Math.cos(slider_angular_position_rad);
  const y = cy - r_px * Math.sin(slider_angular_position_rad);

  // clear
  ctx.clearRect(0, 0, w, h);

  ctx.beginPath();
  ctx.arc(cx, cy, Math.max(3, 0.007 * Math.min(w, h)), 0, Math.PI * 2);
  ctx.fillStyle = "rgba(0, 0, 0, 1)";
  ctx.fill();

  // rod (line)
  ctx.beginPath();
  ctx.moveTo(cx - pxPerM * Math.cos(slider_angular_position_rad), cy + pxPerM * Math.sin(slider_angular_position_rad));
  ctx.lineTo(cx + pxPerM * Math.cos(slider_angular_position_rad), cy - pxPerM * Math.sin(slider_angular_position_rad));
  ctx.lineWidth = 2;
  ctx.strokeStyle = "#000";
  ctx.stroke();

  // slider (circle)
  const sliderRadiusPx = Math.max(6, 0.02 * Math.min(w, h));
  ctx.beginPath();
  ctx.arc(x, y, sliderRadiusPx, 0, Math.PI * 2);
  ctx.fillStyle = "#d00";
  ctx.fill();
}


websocket.onmessage = (event) => {
  console.log(event.data);

    msg_json_object = JSON.parse(event.data);

    if (msg_json_object.type == "topic") {
        if (msg_json_object.data.topic_name == "slider_radial_position_m") {
            slider_radial_position_m = msg_json_object.data.msg;
            draw();
            console.log("slider_radial_position_m", slider_radial_position_m);
        } else if (msg_json_object.data.topic_name == "slider_angular_position_rad") {
            slider_angular_position_rad = msg_json_object.data.msg;
            draw();
            console.log("slider_angular_position_rad", slider_angular_position_rad);
        }
    }
};

websocket.onopen = (event) => {
    console.log("websocket.onopen");
};


// optional: keep drawing correct on window resize
window.addEventListener("resize", draw);

// initial draw (run after HTML is loaded; or place script after the canvas)
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", draw, { once: true });
} else {
  draw();
}
