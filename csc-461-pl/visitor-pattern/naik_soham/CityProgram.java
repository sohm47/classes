package naik_soham;

/**
 * @author Soham Naik
 *
 * Visitor Pattern
 *
 * CSC 461 - Programming Languages
 *
 * September 26, 2018
 *
 * Java 9, IntelliJ
 *
 * This program demonstrates the use of the Visitor Pattern in
 * Object Oriented Programming (OOP). Here, we code a 5x5 'city' which has
 * empty spaces, streets, greenspaces, and buildings. Each object occupies
 * one square (or tile) of the city. The user starts with a blank city, or
 * update to a default setup. Afterward, users can change individual tiles,
 * count how many of each type of tile there are, 'fix' the streets, and
 * change the color of a type of object. The count, fix, and color operations
 * are done with visitor pattern.
 *
 * Bugs - None
 */

import java.util.Scanner;

/**
 * CityProgram
 *
 * Class that simulates the city.
 */
public class CityProgram {

    /**
     * menu
     *
     * Displays the menu to the user and calls specific functions based on the
     * choice.
     *
     * @param goa Object of class City.
     * @param in Scanner object for data input.
     *
     * @return true if user wants to exit the menu, and false otherwise.
     */
    public boolean menu(City goa, Scanner in) {

        System.out.println("0) Make default City");
        System.out.println("1) Set Tile");
        System.out.println("2) Remove tile");
        System.out.println("3) Count Zones");
        System.out.println("4) Set tile color");
        System.out.println("5) Fix roads");
        System.out.println("6) Quit\n");
        System.out.print("Choice: ");

        try {
            int choice = Integer.parseInt(in.next());
            switch(choice) {
                case 0:
                    goa.defaultCity();
                    break;
                case 1:
                    goa.setTile(in);
                    break;
                case 2:
                    goa.removeTile(in);
                    break;
                case 3:
                    goa.countTile();
                    break;
                case 4:
                    goa.setColor(in);
                    break;
                case 5:
                    goa.fixRoads();
                    break;
                case 6:
                    return false;
                default:
                    System.out.println("Invalid option");
                    break;
            }
        }
        catch(Exception e){
            System.out.println("Invalid option");
        }

        return true;
    }

    /**
     * main
     *
     * Gets the program started.
     *
     * @param args Arguments given by user.
     */
    public static void main(String[] args) {

        CityProgram user = new CityProgram();
        Scanner in = new Scanner(System.in);
        City goa = new City();

        do {
            goa.printCity();
        } while(user.menu(goa, in));
    }
}