package datu_atzipena_azterketa;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * Ariketa 1.1 — Fitxategiaren lerro kopurua kontatu.
 */
public class ariketa1_1 {
    public static void main(String[] args) {
        // Proiektuaren erroan exekutatuz gero bide erlatibo hau erabili
        String fileName = "datuak/alice.txt";
        int lineCount = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lineCount++;
            }

            System.out.println("Fitxategiaren lerro kopurua: " + lineCount);

        } catch (IOException e) {
            System.err.println("Errorea fitxategia irakurtzean: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
