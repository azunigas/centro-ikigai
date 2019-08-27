function valida_contacto() {
	$('#valnombre').hide();
	$('#valcorreo').hide();
	$('#valmensaje').hide();
    var nombre, correo, mensaje, regex;
    nombre = document.getElementById('nombre').value;
    correo = document.getElementById('correo').value;
    mensaje = document.getElementById('mensaje').value;
    regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if (nombre === "") {
        $('#valnombre').text('Debe Ingresar su nombre');
        $('#valnombre').show();
        return false;
    } else if (regex.test(correo) === false) {
		$('#valcorreo').text('Correo no valido');
        $('#valcorreo').show();
        return false;
	} else if (mensaje === "") {
        $('#valmensaje').text('Debe Ingresar comentario');
        $('#valmensaje').show();
        return false;
    } else if (regex.test(correo)) {
        return true;
    }
}