package oop;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FileWriterExample {
    public static void main(String[] args) {
        // Menggunakan try-with-resources untuk memastikan BufferedWriter ditutup dengan benar
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("baso.txt"))) {
            bw.write("halo semuanya");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
