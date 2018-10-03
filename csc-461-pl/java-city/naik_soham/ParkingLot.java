package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains the ParkingLot class.
 */

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.HashMap;

/**
 * ParkingLot
 *
 * The ParkingLot class has functions which keeps track of individual vehicles
 * in a lot.
 */
public class ParkingLot {
    // Class constant
    public static final int CLOSED_THRESHOLD = 80;
    // Name of Parking Lot
    private String name;
    private int numVehicles, ids, space, timeClosed, lastTime, exitTime;
    private boolean open, reachedThreshold;
    private ArrayList<Integer> exitedCars;
    public HashMap<Integer, Integer> vehicle;

    /**
     * ParkingLot
     *
     * Class constructor which calls the other constructor, and gives a default name
     * of 'test' to the lot.
     *
     * @param space Number of empty spaces in the lot.
     */
    ParkingLot(int space){
        // Default name of the lot is going to be 'test'
        this("test", space);
    }

    /**
     * ParkingLot
     *
     * This is the main constructor and it initializes class variables.
     *
     * @param name Name of the parking lot as given by the user.
     * @param space Number of spaces in the empty parking lot.
     */
    ParkingLot(String name, int space) {
        this.name = name;
        this.space = space;

        // ID's of the vehicles
        ids = 1;

        numVehicles = 0;

        // The last time at which a vehicle had entered and exited the lot
        lastTime = 0;
        exitTime = 0;

        // Stores vehicles ID's
        vehicle = new HashMap<>(0);

        // Stores cars in the lot
        exitedCars = new ArrayList<>(0);

        // Time at which a parking lot closes
        timeClosed = 0;

        // parking lot is initially open
        open = true;
        reachedThreshold = false;
    }

    /**
     * markVehicleEntry
     *
     * This method is called when a vehicle enters a lot. It is assumed that
     * time never goes backwards. It keeps a count of the vehicles, checks
     * if the parking lot is filled up, and gives each vehicle an unique ID.
     *
     * @param time Number of minutes since the lot opened.
     *
     * @return The ID of the vehicle which entered or -1 if the time is
     * illegal or lot is closed.
     */
    public int markVehicleEntry(int time) {
        // Exits if time is illegal or parking lot is closed
        if(time < lastTime || !open)
            return -1;

        // Increasing count of vehicles
        numVehicles += 1;
        vehicle.put(ids, time);
        ids += 1;

        if (reachedThreshold && isClosed())
            timeClosed += time-lastTime;

        // Closing parking lot
        if (space == numVehicles)
            open = false;

        lastTime = time;

        // Checks if lot reached its threshold
        if (!reachedThreshold && isClosed())
            reachedThreshold = true;

        // Unique ID
        return ids-1;
    }

    /**
     * markVehicleExit
     *
     * This method is called when a vehicle exits the lot. It is assumed that
     * time never goes backwards. It decreases count of vechiles and opens the
     * parking lot if a vehilce leaves.
     *
     * @param time Number of minutes since the lot opened.
     * @param vehicleID ID of the vehicle which left the lot (0 if unknown).
     *
     * @return -1 if time is illegal or vehicle already exited the lot.
     * 0 otherwise
     */
    public int markVehicleExit(int time, int vehicleID) {
        // Checks if time is illegal or if vehicle already exited the lot.
        if(time < lastTime || exitedCars.contains(vehicleID) || time < exitTime)
            return -1;

        // Checks if vehicleID is legal
        if (vehicle.containsKey(vehicleID)) {
            vehicle.remove((vehicleID));
            exitedCars.add(vehicleID);
        }

        // Decreasing count
        numVehicles -= 1;

        // Checks if lot threshold is reached
        if (reachedThreshold && !isClosed()) {
            reachedThreshold = false;
            timeClosed += time - lastTime;
        }

        // Opening lot
        if(!open)
            open = true;
        exitTime = time;

        return 0;
    }

    /**
     * getName
     *
     * Gets name of parking lot.
     *
     * @return Name of the parking lot.
     */
    public String getName() {
        return name;
    }

    /**
     * getVehiclesInLot
     *
     * Gets count of vehicles in a parking lot.
     *
     * @return Number of vehicles in the lot at any one time.
     */
    public int getVehiclesInLot() {
        return numVehicles;
    }

    /**
     * isClosed
     *
     * Checks if a parking lot is closed.
     *
     * @return True if number of vehicles over 80% of the number of spaces, and
     * False otherwise.
     */
    public boolean isClosed() {
        if (numVehicles*100.0/space >= CLOSED_THRESHOLD)
            return true;
        else
            return false;
    }

    /**
     * getClosedMinutes
     *
     * Gets amount of time during which a parking lot is closed.
     *
     * @return Number of minutes during which the lot is closed.
     */
    public int getClosedMinutes() {
        return timeClosed;
    }

    /**
     * toString
     *
     * Makes a string of the form "Status for [name] parking lot: [x]
     * vehicles([p])", where [name] is filled in by the name, [x] by the
     * number of vehicles currently in lot, [p] by the percentage of the
     * lot that is occupied. If the percentage is at or above the threshold,
     * display "CLOSED" for the percentage inside.
     *
     *  @return A string like the one described above.
     */
    public String toString() {
        String status = "Status for " + this.name + " parking lot: " + numVehicles + " vehicles (";

        if (numVehicles*100.0/space >= CLOSED_THRESHOLD)
            status += "CLOSED)";
        else {
            DecimalFormat format = new DecimalFormat("0.##");
            status += format.format(numVehicles*100.0/space) + "%)";
        }

        return status;
    }
}