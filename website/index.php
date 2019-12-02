<html>
<body>
Hello and welcome to our database with information about crime! Select the categories you would like to learn more about!<br/>
<?php

// Connecting to mySQL server
$connection = new mysqli("localhost", "csci440", "csci440", "database_project");

// Check connection status
if ($connection->connect_error) {
    die("Failed to connect to mySQL server: " . $connection->connect_error);
}

// query all weapons and make drop down
$connection_result = $connection->query("SELECT * FROM WEAPON ORDER BY Type;");

if ($connection_result->num_rows > 0){
    echo "<form>\n";
    echo "<select name=weapon_type>\n";
    while($row = $connection_result->fetch_assoc()) {
        echo "<option value=\"" . $row["Id"] . "\">" . $row["Type"] . "</option>\n";
    }  
    echo "</select>\n";
  echo '<input type="submit" value="Go!">';

    echo "</form>\n";
}
else{
    echo "No results";
}

// query all weapons and print table
$connection_result = $connection->query("SELECT * FROM WEAPON;");

if ($connection_result->num_rows > 0){
    echo "<table border=\"1\" cellpadding=\"10\">";
        echo "<tr><th>Id</th><th>Weapon_type</th></tr>";
    while($row = $connection_result->fetch_assoc()) {
        //echo $row["Id"] . " - " . $row["Type"] . "<br/>\n";

            
        echo "<tr>";
            echo "<td>" . $row["Id"] . "</td>";
            echo "<td>" . $row["Type"] . "</td>";
        echo "</tr>";

    }  
     echo "</table>";
}
else{
    echo "No results";
}
?>
</body>
</html>
