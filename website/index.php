<html>
<body>
<br/>
Welcome to our database with information about crime committed in the state of Montana!
<br/>
<br/>
Select the categories you would like to learn more about in the fields below and click Go!<br/><br/><br/><br/>
<?php

// Connecting to mySQL server
$connection = new mysqli("localhost", "csci440", "csci440", "database_project");

// Check connection status
if ($connection->connect_error) {
    die("Failed to connect to mySQL server: " . $connection->connect_error);
}


echo "<form>\n";

// query all years and make drop down
$connection_result = $connection->query("SELECT DISTINCT Year FROM CRIME ORDER BY Year;");

if ($connection_result->num_rows > 0){
    echo "<select name=Year>\n";
    echo "<option value=\"*\">All Years</option>\n";
    while($row = $connection_result->fetch_assoc()) {
        $selected = "";
        if($_GET["Year"] == $row["Year"]){
            $selected = "selected";
        }
        echo "<option " . $selected . " value=\"" . $row["Year"] . "\">" . $row["Year"] . "</option>\n";
    }  
    echo "</select>\n";

}

// query all cities and make drop down
$connection_result = $connection->query("SELECT DISTINCT City FROM CRIME ORDER BY City;");

if ($connection_result->num_rows > 0){
    echo "<select name=City>\n";
    echo "<option value=\"*\">All Cities</option>\n";
    while($row = $connection_result->fetch_assoc()) {
        $selected = "";
        if($_GET["City"] == $row["City"]){
            $selected = "selected";
        }
        echo "<option " . $selected . " value=\"" . $row["City"] . "\">" . $row["City"] . "</option>\n";
    }  
    echo "</select>\n";

}

// query all weapons and make drop down
$connection_result = $connection->query("SELECT * FROM WEAPON ORDER BY Type;");

if ($connection_result->num_rows > 0){
    echo "<select name=weapon_id>\n";
    echo "<option value=\"*\">All Weapon types</option>\n";
    while($row = $connection_result->fetch_assoc()) {
        $selected = "";
        if($_GET["weapon_id"] == $row["Id"]){
            $selected = "selected";
        }
        echo "<option " . $selected . " value=\"" . $row["Id"] . "\">" . $row["Type"] . "</option>\n";
    }  
    echo "</select>\n";

}
// query all jail sentences and make drop down
$connection_result = $connection->query("SELECT DISTINCT Jail_sentence FROM INCARCERATION ORDER BY Jail_sentence;");

if ($connection_result->num_rows > 0){
    echo "<select name=Jail_sentence>\n";
    echo "<option value=\"*\">All Jail sentences</option>\n";
    while($row = $connection_result->fetch_assoc()) {
        $selected = "";
        if($_GET["Jail_sentence"] == $row["Jail_sentence"]){
            $selected = "selected";
        }
        echo "<option " . $selected . " value=\"" . $row["Jail_sentence"] . "\">" . $row["Jail_sentence"] . "</option>\n";
    }  
    echo "</select>\n";

}
// query all jail names and make drop down
$connection_result = $connection->query("SELECT DISTINCT Jail_name FROM INCARCERATION ORDER BY Jail_name;");

if ($connection_result->num_rows > 0){
    echo "<select name=Jail_name>\n";
    echo "<option value=\"*\">All Jail locations</option>\n";
    while($row = $connection_result->fetch_assoc()) {
        $selected = "";
        if($_GET["Jail_name"] == $row["Jail_name"]){
            $selected = "selected";
        }
        echo "<option " . $selected . " value=\"" . $row["Jail_name"] . "\">" . $row["Jail_name"] . "</option>\n";
    }  
    echo "</select>\n";

}

echo '<input type="submit" value="Go!">';
echo "</form>\n";

// main table

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

foreach($_GET as $key => $value){
    if ($value != "*"){
        $conditions .= $key . " = '" . $value . "' AND \n";
    }
}

$endQuery = " TRUE;";

$completeQuery = $startQuery . $conditions . $endQuery;
//echo $completeQuery;

$connection_result = $connection->query($completeQuery);

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
