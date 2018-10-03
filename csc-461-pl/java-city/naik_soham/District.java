package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains the District class.
 */

import java.math.RoundingMode;
import java.util.ArrayList;
import java.math.BigDecimal;

/**
 * This class keeps a track of all the lots in a parking district.
 * @author Soham Naik
 */
public class District {
    // List of all parking lots
    public ArrayList<ParkingLot> lots;

    // Checks if parking lot is closed or not
    private boolean closed;

    // Amount of time the parking lot was closed, and the last closing time
    private int closedMinutes, last;

    /**
     * District
     *
     * Class Constructor.
     */
    District(){
        lots = new ArrayList<>(0);
        closed = false;
        closedMinutes = 0;

        // Last time at which the vehicle had entered or exited the lot
        last = 0;
    }

    /**
     * add
     *
     * Adds a parking lot to the District.
     *
     * @param l Parking lot which is added to the District.
     *
     * @return Index of the parking lot.
     */
    public int add(ParkingLot l) {
        lots.add(l);
        return lots.size()-1;
    }

    /**
     * markVehicleEntry
     *
     * This method is called when a vehicle enters a lot in a district. It saves
     * the entry time and checks if parking lot is filled up or not.
     *
     * @param index Parking Lot index which the vehicle is entering.
     * @param time Number of minutes since the opening of the district.
     *
     * @return ID of the vehicle which entered or -1 of no entry was made.
     */
    public int markVehicleEntry(int index, int time) {

        // Calling ParkingLot method
        int madeEntry = lots.get(index).markVehicleEntry(time);
        if(madeEntry == -1)
            return -1;

        // Adds the time during which all parking lots were closed.
        if (closed) {
            closedMinutes += time - last;
        }
        else {
            // Checks to see if all parking lots in a district are closed.
            closed = true;
            for(ParkingLot l: lots) {
                if(!l.isClosed()) {
                    closed = false;
                    break;
                }
            }
        }

        // The last time when a vehicle had entered a parking lot
        last = time;

        return madeEntry;
    }

    /**
     * markVehicleExit
     *
     * This method is called when a vehicle exits the lot.
     *
     * @param index Index of the parking lot the vehicle enters.
     * @param time Number of minutes since the district had opened.
     * @param vehicleID ID of the vehicle which left the lot.
     */
    public void markVehicleExit(int index, int time, int vehicleID) {
        lots.get(index).markVehicleExit(time, vehicleID);

        // Checks to see if all the lots are closed.
        if(closed) {
            for(ParkingLot l: lots) {
                if(!l.isClosed()) {
                    // Adds time during which all parking lots were closed
                    closedMinutes += time - last;
                    closed = false;
                    break;
                }
            }
        }
    }

    /**
     * getClosedMinutes
     *
     * Gets the amount of minutes during which a parking lot was closed.
     *
     * @return The number of minutes that all of the parking lots are closed
     * at the same time.
     */
    public int getClosedMinutes() {
        return closedMinutes;
    }

    /**
     * getLot
     *
     * Gets a parking lot.
     *
     * @param index Index of the parking lot.
     *
     * @return A valid Parking Lot
     */
    public ParkingLot getLot(int index) {
        return lots.get(index);
    }

    /**
     * getVehiclesParkedInDistrict
     *
     * Counts the total number of vehilces in a parking lot.
     *
     * @return Total number of parked cars in the district.
     */
    public int getVehiclesParkedInDistrict(){
        int total = 0;
        for(int i=0; i<lots.size();i++)
            total += lots.get(i).getVehiclesInLot();

        return total;
    }

    /**
     * getTotalMoneyCollected
     *
     * Counts the total profit made by a pay parking lot.
     *
     * @return Total money collected in the district.
     */
    public double getTotalMoneyCollected() {
        double profit = 0.0;

        // Calculates total profit in all the parking lots in the district.
        for(int i=0; i<lots.size(); i++) {
            if(lots.get(i) instanceof PayParkingLot)
                profit += ((PayParkingLot) lots.get(i)).getProfit();
        }

        // Rounding to 2 decimal places
        BigDecimal bd = new BigDecimal(profit);
        bd = bd.setScale(2, RoundingMode.HALF_UP);

        return bd.doubleValue();
    }

    /**
     * isClosed
     *
     * Checks if a parking lot is closed.
     *
     * @return True if all parking lots in the district are closed. False otherwise.
     */
    public boolean isClosed(){
        return closed;
    }

    /**
     * toString
     *
     * Overrides the toString method to print the status of a parking lot.
     *
     * @return Information about parking lots in a district.
     */
    public String toString(){
        String s = "District status:\n";
        for (ParkingLot l: lots) {
            s += l.toString()+"\n";
        }
        return s;
    }
}
