<html>
<body>
<br/>
Welcome to our statistics page on crimes in the state of Montana!
<br/>
<br/>
Want to go back? Click <a href="index.php">here</a>
<br/>
<br/>
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
?>
Statistics on crime committed in Montana by weapon type:
<br/>
<br/>
<?php
printQueryResults($connection, "SELECT Type AS 'Weapon type', COUNT(*) AS 'Number of crimes'  FROM CRIME JOIN WEAPON ON weapon_id = WEAPON.Id GROUP BY Type ;");
?>
<br/>
Statistics on crime committed in Montana by Year:
<br/>
<br/>
<?php
printQueryResults($connection, "SELECT Year, COUNT(*) AS 'Number of crimes' FROM CRIME GROUP BY Year ;");
?>
<br/>
Order of most violent cities in Montana:
<br/>
<br/>
<?php printQueryResults($connection, "SELECT  MAX(City) AS 'Most violent cities in Montana'  FROM CRIME GROUP BY City; ;"); ?>
<br/>
Statistics on crime committed in Montana by city:
<br/>
<br/>
<?php printQueryResults($connection, "SELECT City, COUNT(*) AS 'Number of crimes'  FROM CRIME GROUP BY City ;"); ?>
<br/>
Statistics on crime committed in Montana by victim race:
<br/>
<br/>
<?php printQueryResults($connection, " SELECT Race AS 'Victim race', COUNT(*) AS 'Number of crimes' FROM CRIME JOIN PERSON ON committed_on = PERSON.Ssn GROUP BY Race ;"); ?>
<br/>
Statistics on crime committed in Montana by offender race:
<br/>
<br/>
<?php printQueryResults($connection, " SELECT Race AS 'Offender race, COUNT(*) AS 'Number of crimes' FROM CRIME JOIN PERSON ON committed_by = PERSON.Ssn GROUP BY Race ;
"); ?>
<br/>
Statistics on crime committed in Montana by victim gender:
<br/>
<br/>
<?php printQueryResults($connection, " SELECT Sex AS 'Victim gender', COUNT(*) AS 'Number of crimes' FROM CRIME JOIN PERSON ON committed_on = PERSON.Ssn GROUP BY Sex ;
"); ?>
<br/>
Statistics on crime committed in Montana by offender gender:
<br/>
<br/>
<?php printQueryResults($connection, " SELECT Sex AS 'Offender gender', COUNT(*) AS 'Number of crimes' FROM CRIME JOIN PERSON ON committed_by = PERSON.Ssn GROUP BY Sex ;
"); ?>
<br/>
Statistics on number of crimes per offender:
<br/>
<br/>
<?php printQueryResults($connection, " SELECT Firstname AS 'Offender name', COUNT(*) AS 'Number of crimes' FROM CRIME JOIN PERSON ON committed_by = PERSON.Ssn GROUP BY Firstname;
"); ?>
</body>
</body>
</html>
