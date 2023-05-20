$(document).ready(function() {
    $.ajax({
      url: '/mi-vista/',
      type: 'GET',
      success: function(data) {
        // Hacer algo con los datos devueltos
        console.log(data);
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error en la solicitud AJAX');
      }
    });
  });
  