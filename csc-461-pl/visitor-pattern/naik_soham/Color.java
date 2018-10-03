package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains class Color which helps in coloring the tiles.
 */

/**
 * Color
 *
 * This class implements the Visitor interface, and helps in coloring the
 * tiles.
 */
public class Color implements Visitor {

    // Object of enum which contains colors
    private ColorText.Color color;

    private int tileType;

    /**
     * Color
     *
     * Constructor which initializes color based on users input.
     *
     * @param tileType Stores the type of tile. 1 for Greenspace, 2 for Building,
     *                 3 for Road, and any other number for Empty.
     * @param color Stores color
     */
    Color(int tileType, int color){
        this.tileType = tileType;

        if (color == 1)
            this.color = ColorText.Color.RED;
        else if (color == 2)
            this.color = ColorText.Color.YELLOW;
        else if (color == 3)
            this.color = ColorText.Color.BLUE;
        else if (color == 4)
            this.color = ColorText.Color.GREEN;
        else
            this.color = ColorText.Color.BLACK;
    }

    /**
     * visit
     *
     * Changes empty tile's color.
     *
     * @param e object of class empty.
     */
    public void visit(Empty e) {
        if (tileType >3 || tileType <1 )
            e.color = this.color;
    }

    /**
     * visit
     *
     * Changes building tile's color.
     *
     * @param b object of class building.
     */
    public void visit(Building b) {
        if (tileType == 2 )
            b.color = this.color;
    }

    /**
     * visit
     *
     * Changes greenspace tile's color.
     *
     * @param g object of class empty.
     */
    public void visit(Greenspace g) {
        if (tileType == 1 )
            g.color = this.color;
    }

    /**
     * visit
     *
     * Changes road tile's color.
     *
     * @param r object of class empty.
     */
    public void visit(Road r) {
        if (tileType == 3 )
            r.color = this.color;
    }
}
