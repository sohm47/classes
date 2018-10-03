package naik_soham;

/**
 * @author Soham Naik
 *
 * This file contains the Road class which is a type of Tile.
 */

/**
 * Road
 *
 * This class extends from Tile. It initializes the symbol and color, and
 * accepts the visitor object, and also converts character to string for that
 * specific tile.
 */
public class Road extends Tile{
    /**
     * Road
     *
     * Constructor which initializes the color and symbol.
     */
    Road() {
        symbol = '━';
        color = ColorText.Color.BLACK;
    }

    /**
     * accept
     *
     * Overrides the accept function from the parent class, and accepts
     * the visitor object.
     *
     * @param visitor Visitor object.
     */
    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }

    /**
     * toString
     *
     * Overrides the toString method and returns a symbol.
     *
     * @return A character symbol.
     */
    public String toString(){
        return Character.toString(symbol);
    }
}
