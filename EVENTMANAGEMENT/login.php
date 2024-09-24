<?php
session_start();

include("connection.php");
include("functions.php");

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    // Get the posted data
    $user_name = $_POST['user_name'];
    $password = $_POST['password'];

    // Validate the input fields
    if (!empty($user_name) && !empty($password) && !is_numeric($user_name)) {

        // Query to select the user from the database
        $query = "SELECT * FROM users WHERE user_name = ? LIMIT 1";
        $stmt = $con->prepare($query);
        $stmt->bind_param("s", $user_name);
        $stmt->execute();
        $result = $stmt->get_result();

        // Check if the user exists
        if ($result && mysqli_num_rows($result) > 0) {
            $user_data = mysqli_fetch_assoc($result);

            // Verify the password (assume the password is hashed)
            if (password_verify($password, $user_data['password'])) {
                // Store user information in session
                $_SESSION['user_id'] = $user_data['user_id'];

                // Redirect to index.html after successful login
                header("Location: index.html");
                die;
            } else {
                echo "Incorrect username or password!";
            }
        } else {
            echo "Incorrect username or password!";
        }
    } else {
        echo "Please enter valid information!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>

    <style type="text/css">
        #text {
            height: 25px;
            border-radius: 5px;
            padding: 4px;
            border: solid thin #aaa;
            width: 100%;
        }

        #button {
            padding: 10px;
            width: 100px;
            color: white;
            background-color: lightblue;
            border: none;
        }

        #box {
            background-color: grey;
            margin: auto;
            width: 300px;
            padding: 20px;
        }
    </style>

    <div id="box">
        <form method="post">
            <div style="font-size: 20px; margin: 10px; color: white;">Login</div>

            <input id="text" type="text" name="user_name" placeholder="Username"><br><br>
            <input id="text" type="password" name="password" placeholder="Password"><br><br>

            <input id="button" type="submit" value="Login"><br><br>

            <a href="signup.php">Click to Signup</a><br><br>
        </form>
    </div>

</body>
</html>
