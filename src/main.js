// vim: backupcopy=yes
import styles from './style.css';

(function() {
	"use strict";
	var url = window.location.href;
	var main = document.querySelector("#main");

	if (url.indexOf('daniel') >= 0) {
		main.innerHTML = "No";
	} else {
		main.innerHTML = "Yes!";
	}
})();
