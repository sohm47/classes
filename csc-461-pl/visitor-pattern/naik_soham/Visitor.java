package naik_soham;

/**
 * @author Soham Naik
 *
 * Contains the Visitor Interface.
 */

/**
 * Visitor
 *
 * Functions are called for every element in the grid.
 */
public interface Visitor {
    /**
     * visit
     *
     * Does operations on the Empty tile.
     *
     * @param visitor
     */
    void visit(Empty visitor);

    /**
     * visit
     *
     * Does operations on the Building tile.
     *
     * @param visitor
     */
    void visit(Building visitor);

    /**
     * visit
     *
     * Does operations on the Greenspace tile.
     *
     * @param visitor
     */
    void visit(Greenspace visitor);

    /**
     * visit
     *
     * Does operations on the Road tile.
     *
     * @param visitor
     */
    void visit(Road visitor);
}
