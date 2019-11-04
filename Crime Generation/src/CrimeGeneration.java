import java.io.IOException;

public class CrimeGeneration {

    // constants for looping correctly
    public final int maxCrimeID = 5; // number of crimes in database (5 for now)
    private final int attributeNumberCrime = 8;
    private final int numberWeaponID = 5;




    public String crimeArray[][] = new String[maxCrimeID][attributeNumberCrime];
    public int[] crimeID = new int[maxCrimeID]; // array of crime
    public String[][] location; // location array (city and state)
    public int[] year = new int[2]; // year array
    public int[] weaponID = new int[numberWeaponID];


    public CrimeGeneration() throws IOException {
        LocationGeneration lg = new LocationGeneration(); // generate location
        location = lg.generateLocation();
        generateID();
        WeaponGeneration wg = new WeaponGeneration(numberWeaponID);
        weaponID = wg.getWeaponID();





        reassemble();
        printCrimeArray();



    }

    public int getYear() { // for now returns 2016
        year[0] = 2017;
        return year[0];
    }

    private void generateID() {
        for(int i = 0; i < maxCrimeID; i++) {
            crimeID[i] = i;
        }
    }

    public int getID(int index) {
        return crimeID[index];

    }

    private void reassemble() {

        for(int i = 0; i < maxCrimeID; i++) {

                crimeArray[i][0] = Integer.toString(crimeID[i]);
                crimeArray[i][1] = Integer.toString(getYear());
                crimeArray[i][2] = location[i][0];
                crimeArray[i][3] = location[i][1];
                crimeArray[i][4] = Integer.toString(weaponID[i]);
        }

    }

    public void printCrimeArray() {
        for(int i = 0; i < maxCrimeID; i++) {
            System.out.print("Crime iD: " + crimeArray[i][0]);
            System.out.print("\tYear: " + crimeArray[i][1]);
            System.out.print("\tState: " + crimeArray[i][2]);
            System.out.print("\tCity: " + crimeArray[i][3]);
            System.out.print("\t\tWeapon ID: " + crimeArray[i][4]);

            System.out.println();
        }
    }





}
