public class WeaponGeneration {



    private final int weaponArraySize; // placeholder value
    private String weaponType;
    private int[] weaponID;

    public WeaponGeneration(int size) {
        weaponArraySize = size;
        weaponID = new int[weaponArraySize];
        generateID();


    }


    private void generateID() {
        for(int i = 0; i < weaponArraySize; i++) {
            weaponID[i] = i;
        }

    }

    public int[] getWeaponID() {return weaponID;}

}
