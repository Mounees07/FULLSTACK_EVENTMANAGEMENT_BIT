<?php

session_start();
include("connection.php"); // Make sure your DB connection is established here
include("functions.php");  // Include the file where functions are defined

// Check if the user is logged in
$user_data = check_login($con);

// If login is successful, redirect to index.html
if ($user_data) {
    header("Location: index.html");
    die;
}

// check_login function definition
function check_login($con) {

    // Check if user_id exists in the session
    if (isset($_SESSION['user_id'])) {
        $id = $_SESSION['user_id'];
        
        // Select user details from the database
        $query = "SELECT * FROM users WHERE user_id = '$id' LIMIT 1";
        $result = mysqli_query($con, $query);
        
        if ($result && mysqli_num_rows($result) > 0) {
            $user_data = mysqli_fetch_assoc($result);
            return $user_data;
        }
    }

    // If not logged in, redirect to login page
    header("Location: login.php");
    die;
}

// random_num function definition
function random_num($length) {
    $text = "";
    if ($length < 5) {
        $length = 5;  // Ensure a minimum length of 5 digits
    }

    $len = rand(4, $length);

    for ($i = 0; $i < $len; $i++) {
        $text .= rand(0, 9);  // Append random digits
    }

    return $text;
}
?>
