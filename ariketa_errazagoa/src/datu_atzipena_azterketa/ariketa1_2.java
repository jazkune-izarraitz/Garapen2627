package datu_atzipena_azterketa;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Ariketa 1.2 — Lerro kopurua + "Alice" agertzen den lerroak.
 */
public class ariketa1_2 {
    public static void main(String[] args) {
        String fileName = "datuak/alice.txt";
        List<Integer> lerroak = new ArrayList<>();
        int lineCount = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lineCount++;

                if (line.contains("Alice")) {
                    lerroak.add(lineCount);
                }
            }

            System.out.println("Fitxategiaren lerro kopurua: " + lineCount);
            System.out.println("\"Alice\" hitza " + lerroak.size() + " lerrotan agertzen da:");

            if (!lerroak.isEmpty()) {
                System.out.println("Lerro zenbakiak: " + lerroak);
            } else {
                System.out.println("\"Alice\" hitza ez da agertzen fitxategian.");
            }

        } catch (IOException e) {
            System.err.println("Errorea fitxategia irakurtzean: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
