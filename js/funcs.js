// For notification popup
function notif(_id) {
  var x = document.getElementById(_id);
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

