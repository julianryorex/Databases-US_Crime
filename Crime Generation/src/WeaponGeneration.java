import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class WeaponGeneration {

    private final int weaponArraySize; // placeholder value


    private String[] weaponType; // list of different weapons extracted from a file
    private int[] weaponID;
    private String[][] weapon;
    String row;
    String[] yearIndex;

    public WeaponGeneration(int size) throws IOException {
        weaponArraySize = size;
        weaponID = new int[weaponArraySize];
        weaponType = new String[15];
        generateID();
        generateWeaponType();



    }

    public void generateWeaponType() throws IOException {
        BufferedReader csvReader = new BufferedReader(new FileReader("/Users/myfatduck/OneDrive/School/University/Year 4/CSCI 440/Project/Databases-US_Crime/Crime Generation/weaponTypes.csv"));

        int weaponIndex = 0;
        while ((row = csvReader.readLine()) != null) {

            String[] data = row.split(",");
            weaponType[weaponIndex] = data[0];
            weaponType[weaponIndex] = weaponType[weaponIndex].trim();
            weaponIndex++;



        }


    }


    private void generateID() {
        for(int i = 0; i < weaponArraySize; i++) {
            weaponID[i] = i;
        }

    }

    public String[] getWeaponType() {return weaponType;}

}
