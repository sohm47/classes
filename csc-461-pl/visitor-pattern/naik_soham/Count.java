package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains the Count class which helps in counting each type of tile.
 */

/**
 * Count
 *
 * Implements the visitor class that helps in counting each type of tile.
 */
public class Count implements Visitor {

    // Keeps count of each tile.
    private int empty, building, greenspace, road;

    /**
     * Count
     *
     * Class constructor which initializes counts to 0.
     */
    Count(){
        empty = 0;
        building = 0;
        greenspace = 0;
        road = 0;
    }

    /**
     * visit
     *
     * Increments count of Empty tiles.
     *
     * @param e
     */
    public void visit(Empty e) { empty += 1; }

    /**
     * visit
     *
     * Increments count of Building tiles.
     *
     * @param b
     */
    public void visit(Building b) { building += 1; }

    /**
     * visit
     *
     * Increments count of Greenspace tiles.
     *
     * @param g
     */
    public void visit(Greenspace g) { greenspace += 1; }

    /**
     * visit
     *
     * Increments count of Road tiles.
     *
     * @param r
     */
    public void visit(Road r) { road += 1; }

    /**
     * toString
     *
     * Makes a string which formats the output.
     *
     * @return String with count on each tile.
     */
    @Override
    public String toString(){
        return "Empty: " + Integer.toString(empty) + "\nGreenspaces: " + Integer.toString(greenspace) +
                "\nRoads: " + Integer.toString(road) + "\nBuildings: " + Integer.toString(building);
    }
}
