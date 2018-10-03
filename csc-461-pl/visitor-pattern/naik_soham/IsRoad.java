package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains IsRoad class which just checks if a particular tile is a road.
 */

/**
 * IsRoad
 *
 * This class implements Visitor and just check if a tile is a road.
 */
public class IsRoad implements Visitor {

    // True if a tile is a road, false otherwise.
    private boolean check;

    /**
     * IsRoad
     *
     * Class constructor.
     */
    IsRoad(){
        check = false;
    }

    /**
     * visit
     *
     * Changes boolean value to false.
     *
     * @param e Object of class Empty.
     */
    public void visit(Empty e) {
        check = false;
    }

    /**
     * visit
     *
     * Changes boolean value to false.
     *
     * @param b Object of class Building.
     */
    public void visit(Building b) {
        check = false;
    }

    /**
     * visit
     *
     * Changes boolean value to false.
     *
     * @param g Object of class Greenspace.
     */
    public void visit(Greenspace g) {
        check = false;
    }

    /**
     * visit
     *
     * Changes boolean value to false.
     *
     * @param r Object of class Road.
     */
    public void visit(Road r) {
        check = true;
    }

    /**
     * getIsRoad
     *
     * Getter function which tells if the current tile is a road.
     *
     * @return True if the current tile is a road, and false otherwise.
     */
    public boolean getIsRoad() { return check; }
}
