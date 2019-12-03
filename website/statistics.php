<html>
<body>
<br/>
Welcome to our statistics page on crimes in the state of Montana!
<br/>
<br/>
Select the categories you would like to learn more about in the field below and click Go!<br/><br/><br/><br/>
<?php

function printQueryResults($connection, $query){
$connection_result = $connection->query($query);

if ($connection_result->num_rows > 0){
    echo "<table border=\"1\" cellpadding=\"3\">";

    $row = $connection_result->fetch_assoc();
    echo "<tr>";
    foreach($row as $key => $value){
        echo "<th>" . $key . "</th>";
    }
    echo "</tr>";

    echo "<tr>";
    foreach($row as $key => $value){
        echo "<td>" . $value . "</td>";
    }
    echo "</tr>";

    while($row = $connection_result->fetch_assoc()) {
        echo "<tr>";
        foreach($row as $key => $value){
            echo "<td>" . $value . "</td>";
        }
        echo "</tr>";
    }

    echo "</table>";
}
else{ 
    echo "No results";
};
}

// Connecting to mySQL server
$connection = new mysqli("localhost", "csci440", "csci440", "database_project");

// Check connection status
if ($connection->connect_error) {
    die("Failed to connect to mySQL server: " . $connection->connect_error);
}

printQueryResults($connection, "SELECT * FROM WEAPON;");
?>

vanlig html :)

<?php printQueryResults($connection, "SELECT * FROM CRIME WHERE weapon_id > 3;"); ?>
</body>
</html>
