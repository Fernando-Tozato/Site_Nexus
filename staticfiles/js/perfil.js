document.getElementById("profileForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const name = document.getElementById("name");
    const email = document.getElementById("email");
    const phone = document.getElementById("phone");
    const password = document.getElementById("password");
    const nameError = document.getElementById("nameError");
    const emailError = document.getElementById("emailError");
    const phoneError = document.getElementById("phoneError");
    const passwordError = document.getElementById("passwordError");
    let isFormValid = true;
    if (name.value.length < 3) {
        nameError.innerText = "Name must be at least 3 characters long.";
        isFormValid = false;
    } else {
        nameError.innerText = "";
    }
    if (!email.checkValidity()) {
        emailError.innerText = "Please enter a valid email address.";
        isFormValid = false;
    } else {
        emailError.innerText = "";
    }
    if (phone.value.length < 10) {
        phoneError.innerText = "Please enter a valid phone number.";
        isFormValid = false;
    } else {
        phoneError.innerText = "";
    }
    if (password.value.length < 8) {
        passwordError.innerText = "Password must be at least 8 characters long.";
        isFormValid = false;
    } else {
        
    }
    if (isFormValid) {
        // Handle form submission here
        console.log("Form submitted:", {
            name: name.value,
            email: email.value,
            phone: phone.value,
            password: password.value,
        });
    }
});