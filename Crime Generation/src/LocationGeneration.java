import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class LocationGeneration {

    private String location[][] = new String[130][2]; // state, then city in that state
    String row;
    String state;


    public LocationGeneration() {

    }

    public String[][] generateLocation() throws IOException {
        BufferedReader csvReader = new BufferedReader(new FileReader("/Users/myfatduck/Desktop/Databases/Crime Generation/MT-Towns.csv"));

        state = "Montana";
        int i = 0;
        while ((row = csvReader.readLine()) != null) {
            String[] data = row.split(",");

            location[i][0] = state;
            location[i][1] = data[1];
            i++;
        }


        return location; // returns the array of the location

    }
}
