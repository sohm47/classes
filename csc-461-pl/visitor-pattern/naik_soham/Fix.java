package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains the Fix class which helps in 'fixing' road.
 */

/**
 * Fix
 *
 * Implements Visitor class which visits every type of tile and does specific
 * operations.
 */
public class Fix implements Visitor {
    // The 5x5 City
    private Tile[][] grid;

    // Variables which keep track of adjacent tiles.
    boolean left, top, bot, right;

    // Location of tile on the grid.
    private int x, y;

    /**
     * Fix
     *
     * Class constructor which initializes the grid.
     *
     * @param grid
     */
    Fix(Tile[][] grid) {
        this.grid = grid;
    }

    /**
     * setPosition
     *
     * Stores position of the tile.
     *
     * @param x x coordinate
     * @param y y coordinate
     */
    public void setPosition(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * SetAdjacencies
     *
     * Indicate the road tiles adjacent to this one. The road time image
     * chosen is dependent on the tiles around it. This is where the
     * adjacency of road tiles is indicated.
     *
     * @param left True if road tile to upper left
     * @param top True if road tile to upper right
     * @param bot True if road tile to lower left
     * @param right True if road tile to lower right
     */
    void SetAdjacencies(boolean left, boolean top, boolean bot, boolean right)
    {
        // Create the adjacency code
        int code = (left ? 1 : 0) | (top ? 2 : 0) | (bot ? 4 : 0) | (right ? 8 : 0);

        // Unicode list
        char symbols[] = {
                '━',      // 0 right
                '━',      // 1 right
                '┃',      // 2 ud
                '┛',      // 3 lu
                '┃',      // 4 ud
                '┓',      // 5 ld
                '┃',      // 6 ud
                '┫',     // 7 lud
                '━',      // 8 right
                '━',      // 9 right
                '┗',      // 10 top
                '┻',     // 11 lur
                '┏',      // 12 dr
                '┳',    // 13 ldr
                '┣',     // 14 udr
                '╋'    // 15 ludr
        };

        // Changing symbol in the grid
        grid[x][y].symbol = symbols[code];
    }

    /**
     * visit
     *
     * Does nothing as this class only operates on roads.
     *
     * @param e Empty object
     */
    public void visit(Empty e) {
        return;
    }

    /**
     * visit
     *
     * Does nothing as this class only operates on roads.
     *
     * @param b Building object
     */
    public void visit(Building b) {
        return;
    }

    /**
     * visit
     *
     * Does nothing as this class only operates on roads.
     *
     * @param g Greenspace object
     */
    public void visit(Greenspace g) {
        return;
    }

    /**
     * visit
     *
     * Checks adjacent tiles of each tile is a road so that it can 'fix' them.
     *
     * @param r Road object
     */
    public void visit(Road r) {
        IsRoad ir = new IsRoad();
        left = false;
        top = false;
        bot = false;
        right = false;

        // Left
        if (y-1 >= 0) {
            grid[x][y-1].accept(ir);
            left = ir.getIsRoad();
        }

        // top
        if(x-1 >=0 ) {
            grid[x-1][y].accept(ir);
            top = ir.getIsRoad();
        }

        // bot
        if(x+1 < 5 ) {
            grid[x+1][y].accept(ir);
            bot = ir.getIsRoad();
        }

        // Right
        if(y+1 < 5) {
            grid[x][y+1].accept(ir);
            right = ir.getIsRoad();
        }

        SetAdjacencies(left, top, bot, right);
    }
}
