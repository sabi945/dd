package oop;

import org.mindrot.jbcrypt.BCrypt;

public class PasswordUtils {

    // Meng-hash password
    public static String hashPassword(String plainTextPassword) {
        return BCrypt.hashpw(plainTextPassword, BCrypt.gensalt());
    }

    // Memeriksa password
    public static boolean checkPassword(String plainTextPassword, String hashedPassword) {
        return BCrypt.checkpw(plainTextPassword, hashedPassword);
    }

    public static void main(String[] args) {
        // Contoh penggunaan
        String password = "mysecretpassword";
        String hashedPassword = hashPassword(password);
        
        System.out.println("Hashed Password: " + hashedPassword);
        System.out.println("Password match: " + checkPassword(password, hashedPassword));
    }
}
