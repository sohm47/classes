package naik_soham;

/**
 * @author Soham Naik
 *
 * This file contains the Tile Class which will be extended by its types.
 */

/**
 * Tile
 *
 * This is an abstract class which is extended by the tile
 * types (greenspaces, buildings, roads and empty).
 */
public abstract class Tile {
    // Symbol of each tile type.
    protected char symbol;

    // Color of the tile.
    protected ColorText.Color color;

    /**
     * accept
     *
     * This function accepts a visitor.
     *
     * @param visitor Visitor object.
     */
    abstract void accept(Visitor visitor);

    /**
     * getSymbol
     *
     * Gets the symbol of the tile.
     *
     * @return String containing the symbol of the tile.
     */
    public String getSymbol() {
        return ColorText.colorString(symbol, color);
    }
}
