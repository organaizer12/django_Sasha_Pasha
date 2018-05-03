window.onload = function() {
	document.getElementById('btn_know').onclick = function() {
		open_text('text_1');
		return false;
	};
};

function open_text(id) {
	document.getElementById(id).style.display = "block"
};
