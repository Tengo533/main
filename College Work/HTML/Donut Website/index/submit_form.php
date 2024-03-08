<?php
// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    // You can perform additional validation and sanitization here

    // Send email (example)
    $to = '546003@escg.ac.uk'; // Your email address
    $subject = 'New message from Imperial Donuts contact form';
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";

    // Send email
    if (mail($to, $subject, $body)) {
        // Email sent successfully
        echo 'Thank you for contacting us! We will get back to you soon.';
    } else {
        // Error sending email
        echo 'Oops! Something went wrong. Please try again later.';
    }
} else {
    // Form was not submitted properly
    echo 'Oops! Form submission error. Please try again.';
}
?>