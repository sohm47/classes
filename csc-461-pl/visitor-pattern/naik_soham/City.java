package naik_soham;

/**
 * @author Soham Naik
 *
 * This file contains all of the functions the city will be using to modify
 * its tiles.
 */

import java.util.Scanner;

/**
 * City
 *
 * City class which initializes a 5x5 grid with empty cells, and functions which
 * help modify them.
 */
public class City {
    public Tile grid[][];

    /**
     * City
     *
     * Class constructor which initializes the city.
     */
    City() {
        grid = new Tile[5][5];
        for(int i=0;i<5;i++) {
            for(int j=0; j<5;j++) {
                grid[i][j] = new Empty();
            }
        }
    }

    /**
     * printCity
     *
     * Prints the 5x5 city, one row at a time.
     */
    public void printCity(){
        for(int i=0;i<5;i++) {
            for(int j=0;j<5;j++) {
                System.out.print(grid[i][j].getSymbol());
            }
            System.out.println();
        }
        System.out.println();
    }

    /**
     * defaultCity
     *
     * Changes the city's layout to the default type as specified in the
     * paper.
     */
    public void defaultCity() {
        grid = new Tile[][] {
                { new Road(), new Road(), new Road(), new Greenspace(), new Greenspace() },
                { new Road(), new Road(), new Road(), new Greenspace(), new Empty() },
                { new Road(), new Road(), new Road(), new Building(), new Empty() },
                { new Empty(), new Empty(), new Empty(), new Building(), new Empty() },
                { new Empty(), new Empty(), new Empty(), new Empty(), new Greenspace()}
        };
    }

    /**
     * setTile
     *
     * This function asks the user for tile type and the input location, and
     * sets the tile based on users choice. If the numbers are invalid, then
     * it output 'Invalid Option' and shows the menu.
     *
     * @param in Scanner object.
     */
    public void setTile(Scanner in){

        // Getting tile type
        System.out.print("Input tile type 1) greenspace 2) building 3) road #) empty: ");
        int choice = Integer.parseInt(in.next());

        // Getting location
        System.out.print("Input location (x y): ");
        int locX = Integer.parseInt(in.next());
        int locY = Integer.parseInt(in.next());

        // Setting tile
        switch (choice) {
            case 1:
                grid[locX][locY] = new Greenspace();
                break;
            case 2:
                grid[locX][locY] = new Building();
                break;
            case 3:
                grid[locX][locY] = new Road();
                break;
            default:
                grid[locX][locY] = new Empty();
                break;
        }
    }

    /**
     * removeTile
     *
     * This function asks the user for the x y coordinates of a cell on the grid
     * and resets the tile to empty. If the numbers are invalid, then it outputs
     * 'Invalid Option' and shows the menu.
     *
     * @param in Scanner object.
     */
    public void removeTile(Scanner in) {

        // Getting location
        System.out.print("Input location (x y): ");
        int locX = Integer.parseInt(in.next());
        int locY = Integer.parseInt(in.next());

        grid[locX][locY] = new Empty();
    }

    /**
     * countTile
     *
     * Counts how many of each tile the City has and then outputs the result.
     * This is done using the visitor pattern.
     */
    public void countTile() {
        Count visitor = new Count();

        for(int i=0; i<5; i++) {
            for(int j=0;j<5;j++) {
                grid[i][j].accept(visitor);
            }
        }

        System.out.println(visitor);
    }

    /**
     * setColor
     *
     * This function asks for a tile type, and then the color, and sets the
     * tile to that color. The effect is permanent on all tiles of that type
     * present in that grid. However, a new tile of that type is not affected,
     * and will be of the default color. If the user chooses an invalid color, it
     * is defaulted to black. This is done using visitor pattern.
     * If the user chooses an invalid tile type, it outputs 'Invalid option'.
     * It then reprints the city and menu.
     *
     * @param in Scanner object.
     */
    public void setColor(Scanner in) {

        // Getting tile type
        System.out.print("Input tile type 1) greenspace 2) building 3) road #) empty: ");
        int tileType = Integer.parseInt(in.next());

        // Getting color
        System.out.print("Input color 1) red 2) yellow 3) blue 4) green #) black: : ");
        int color = Integer.parseInt(in.next());

        // Defaulting color to black
        if(color < 0 || color > 4)
            color = 7;

        // Changing color
        Color colorVisitor = new Color(tileType, color);
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                grid[i][j].accept(colorVisitor);
            }
        }
    }

    /**
     * fixRoads
     *
     * This replaces all road type tiles with specific symbols. This is done
     * using visitor patter.
     */
    public void fixRoads() {
        Fix visitor = new Fix(grid);

        for(int i=0;i<5;i++) {
            for(int j=0;j<5;j++) {
                visitor.setPosition(i, j);
                grid[i][j].accept(visitor);
            }
        }
    }
}