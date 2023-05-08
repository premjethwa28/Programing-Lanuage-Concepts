// Name: Prem Atul Jethwa
// Stud ID: 1001861810
// Language: Java version 11.0.16.1
// OS : Mac OS (Omega compatible)

import java.io.File; // import file module to calculate the size of a file
import java.lang.String;

public class paj1810_lab01 {
    public static long get_size(File foldertoreplace) {
        long size = 0; // initialize size variable to 0
        for (File f : foldertoreplace.listFiles()) { // recursion to list all the files in the folder
            if (f.isFile())
                size += f.length(); // check whether the current file is file or a directory
            else
                size += get_size(f); // add the file size to the bytes variable
        }
        return size; // return the final size of the directory
    }

    public static void main(String[] args) // main method
    {
        File fol = new File("."); // Getting the path of folder
        long s = get_size(fol); // call the get_size function to get the size

        System.out.println("Size " + s + "  Bytes"); // print the size in integer

    }
}