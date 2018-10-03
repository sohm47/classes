package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains PayParkingLot class which keeps track of the total amount of money
 * made by a parking lot.
 */

import java.text.DecimalFormat;

/**
 * PayParkingLot
 *
 * This class extends from the ParkingLot class and keeps a track of how much
 * money is gathered.
 */
public class PayParkingLot extends ParkingLot{

    public double hourlyRate, profit;

    /**
     * PayParkingLot
     *
     * Class constructor which calls the other constructor, and gives a default
     * hourly rate of $1.00.
     *
     * @param name Name of lot.
     * @param space Number of available spaces in the lot.
     */
    PayParkingLot(String name, int space) {
        this(name, space, 1.00);
    }

    /**
     * PayParkingLot
     *
     * Class Constructor which calls the parent class, and the proceeds to set the
     * hourly rate, and initial profit to 0.
     *
     * @param name Name of lot.
     * @param space Number of available spaces in the lot.
     * @param hourlyRate Hourly fee for the car which uses the lot.
     */
    PayParkingLot(String name, int space, double hourlyRate) {
        super(name, space);
        this.hourlyRate = hourlyRate;
        profit = 0.0;
    }

    /**
     * getProfit
     *
     * Returns profit made by parking lot.
     *
     * @return The funds collected at any time.
     */
    public double getProfit() { return profit; }

    /**
     * marVehicleExit
     *
     * This function overrides the parent function and calculates the profit
     * made when a vehicle exits a lot.
     *
     * @param time Number of minutes since the lot opened.
     * @param vehicleID ID of the vehicle which left the lot (0 if unknown).
     *
     * @return 0 for success.
     */
    @Override
    public int markVehicleExit(int time, int vehicleID) {
        // Calculating the profit.
        if (vehicle.containsKey(vehicleID))
            profit += (time - vehicle.get(vehicleID)) * hourlyRate / 60.0;

        // Marks the exit of a vehicle
        super.markVehicleExit(time, vehicleID);

        return 0;
    }

    /**
     * toString
     *
     * Overrides the toString function to include the current money collected.
     * It appends " Money Collected: $[totalProfit]" to the string produced
     * by the parent class. The profit is rounded to the nearest cent. It does
     * not rewrite the prent class's toString contents.
     *
     * @return A string which is described above.
     */
    public String toString () {
        DecimalFormat formatter = new DecimalFormat("0.##");
        return super.toString() + " Money collected: $" + formatter.format(profit);
    }
}
