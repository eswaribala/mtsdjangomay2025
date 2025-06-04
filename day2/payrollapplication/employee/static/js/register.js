$(document).ready(function() {

    alert("Register page loaded successfully!");
    $('#first_name_check').hide();
    let first_name_error = false;
    let phone_number_error = false;
    $('#first_name').keyup(function() {
        validate_first_name();
    });
    $("#phone_number").keyup(function() {
        validate_phone_number();
    }) 

    function validate_first_name() {
        var first_name_length = $('#first_name').val().length;
        if (first_name_length < 3) {
            first_name_error = true;
            $('#first_name_check').show();
            $('#first_name_check').html("**First name must be at least 3 characters long");
            $('#first_name_check').focus();
            return false;
        } else {
            $('#first_name_check').hide();
            first_name_error = false;
        }
         if (first_name_length > 10) {
            first_name_error = true;
            $('#first_name_check').show();
            $('#first_name_check').html("**First name must be up to 10 characters long");
            $('#first_name_check').focus();
            return false;
        } else {
            $('#first_name_check').hide();
            first_name_error = false;
        }

        const firstName = $('#first_name').val();
        const regex = /^[a-zA-Z]+$/;
        if(!regex.test(firstName)) {
            first_name_error = true;
            $('#first_name_check').show();
            $('#first_name_check').html("**First name must contain only letters");
            $('#first_name_check').focus();
            return false;
        }else{
            $('#first_name_check').hide();
            first_name_error = false;
        }
    }

    function validate_phone_number() {
        const phoneNumber = $('#phone_number').val();
        const regex = /^\d{10}$/; // Regular expression for 10-digit phone number   
        if (!regex.test(phoneNumber)) {
            phone_number_error = true;
            $('#phone_number_check').show();
            $('#phone_number_check').html("**Phone number must be 10 digits long");
            $('#phone_number_check').focus();
            return false;
        } else {
            $('#phone_number_check').hide();
            phone_number_error = false;
        }   
        
    }
   
    $('#submit_btn').click(function() {
        
        validate_first_name();
        validate_phone_number();
        alert("Form submitted successfully!");
        alert("First Name Error: " + first_name_error);
        alert("Phone Number Error: " + phone_number_error);
        if (first_name_error === false && phone_number_error === false) {
            return true; // Form is valid, allow submission
        } else {
            return false; // Prevent form submission
        }
    });


})