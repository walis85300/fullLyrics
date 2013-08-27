var $artistInput = $('#artista');
var $button = $('#boton');

$artistInput.on('keyup',onKeyUp)
$button.on('click',onSubmit);

function onKeyUp(evt)
{
	if(evt.keyCode == 13)
		onSubmit();
}

function onSubmit()
{
	$(location).attr('href','artista?artist='+$artistInput.val());
	$artistInput.val() = '';

}