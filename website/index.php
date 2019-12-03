<html>
<body>
Hello and welcome to our database with information about crime! Select the categories you would like to learn more about!<br/><br/><br/><br/>
<?php

// Connecting to mySQL server
$connection = new mysqli("localhost", "csci440", "csci440", "database_project");

// Check connection status
if ($connection->connect_error) {
    die("Failed to connect to mySQL server: " . $connection->connect_error);
}

$startQuery = "SELECT 
    Year, 
    State, 
    City, 
    CONCAT(Offender.Firstname, ' ', Offender.Lastname) AS 'Offender name',
    Offender.Race AS 'Offender race',
    CONCAT(Victim.Firstname, ' ', Victim.Lastname) AS 'Victim name',
    Victim.Race AS 'Victim race',
    Type AS 'Weapon used', 
    Jail_sentence AS 'Sentence length',
    Jail_name AS 'Sentence location' 

FROM CRIME
    JOIN PERSON Offender ON committed_by = Offender.Ssn
    JOIN PERSON Victim ON committed_on = Victim.Ssn
    JOIN WEAPON ON weapon_id = WEAPON.Id 
    JOIN INCARCERATION ON CRIME.Incarceration_id = INCARCERATION.Id

WHERE ";

$endQuery = " TRUE;";

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
$connection_result = $connection->query($startQuery . $endQuery);

if ($connection_result->num_rows > 0){
    echo "<table border=\"1\" cellpadding=\"3\">";
        echo "<tr>
                <th>Year</th>
                <th>State</th>
                <th>City</th>
                <th>Offender name</th>
                <th>Offender race</th>
                <th>Victim name</th>
                <th>Victim race</th>
                <th>Weapon_type</th>
                <th>Sentence length</th>
                <th>Sentence location</th>
              </tr>";
    while($row = $connection_result->fetch_assoc()) {
        //echo $row["Id"] . " - " . $row["Type"] . "<br/>\n";

            
        echo "<tr>";
            echo "<td>" . $row["Year"] . "</td>";
            echo "<td>" . $row["State"] . "</td>";
            echo "<td>" . $row["City"] . "</td>";
            echo "<td>" . $row["Offender name"] . "</td>";
            echo "<td>" . $row["Offender race"] . "</td>";
            echo "<td>" . $row["Victim name"] . "</td>";
            echo "<td>" . $row["Victim race"] . "</td>";
            echo "<td>" . $row["Weapon used"] . "</td>";
            echo "<td>" . $row["Sentence length"] . "</td>";
            echo "<td>" . $row["Sentence location"] . "</td>";
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
