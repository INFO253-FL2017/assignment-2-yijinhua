var contactForm = document.getElementById("contactForm");
contactForm.addEventListener("submit",function(event) {
	var name = contactForm.elements[0].value;
	var subject = contactForm.elements[1].value;
	var message = contactForm.elements[2].value;
	if (name.length == 0 || subject.length == 0 || message.length == 0) {
		if (name.length == 0) {
			document.getElementById("nameEmpty").innerHTML = "please complete name field";
		} else {
			document.getElementById("nameEmpty").innerHTML = null;
		}
		if(subject.length == 0) {
			document.getElementById("subjectEmpty").innerHTML = "please complete subject field";
		} else {
			document.getElementById("subjectEmpty").innerHTML = null;
		}
		if(message.length == 0) {
			document.getElementById("messageEmpty").innerHTML = "please complete message field";
		} else {
			document.getElementById("messageEmpty").innerHTML = null;
		}
	} else {
		document.getElementById("subjectEmpty").innerHTML = null;
		document.getElementById("messageEmpty").innerHTML = null;
		document.getElementById("nameEmpty").innerHTML = "Hi "+ name + ", your message has been sent";
		document.getElementById("contactForm").submit();
	}

	
})