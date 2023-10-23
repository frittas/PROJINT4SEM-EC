function cambiarBotonChat() {
  var element = document.getElementById("hideshow");
  element.classList.toggle("cerrar-boton-chat");
}

$(document).ready(function () {
  $("#hideshow").on("click", function (event) {
    $(".content-chatbot").toggle("show");
  });
});
$(document).ready(function () {
  $("#hideshow2").on("click", function (event) {
    $(".content2").toggle("show");
  });
});
