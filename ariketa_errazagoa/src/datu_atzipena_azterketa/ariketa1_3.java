package datu_atzipena_azterketa;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Ariketa 1.3 — Aurrekoa + "Alice" duten lerroak alice-lerroak.txt fitxategian gorde.
 */
public class ariketa1_3 {
    public static void main(String[] args) {
        String sarreraFitxategia = "datuak/alice.txt";
        String irteeraFitxategia = "alice-lerroak.txt";

        List<Integer> lerroZenbakiak = new ArrayList<>();
        List<String> lerroEdukiak = new ArrayList<>();
        int lineCount = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(sarreraFitxategia))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lineCount++;

                if (line.contains("Alice")) {
                    lerroZenbakiak.add(lineCount);
                    lerroEdukiak.add(line);
                }
            }

            System.out.println("Fitxategiaren lerro kopurua: " + lineCount);
            System.out.println("\"Alice\" hitza " + lerroZenbakiak.size() + " lerrotan agertzen da");
            System.out.println("Lerro zenbakiak: " + lerroZenbakiak);

            try (BufferedWriter writer = new BufferedWriter(new FileWriter(irteeraFitxategia))) {
                writer.write("ALICE - \"Alice\" hitza duten lerroak\n");
                writer.write("====================================\n");
                writer.write("Fitxategi osoaren lerro kopurua: " + lineCount + "\n");
                writer.write("\"Alice\" hitza " + lerroZenbakiak.size() + " lerrotan agertzen da\n\n");

                for (int i = 0; i < lerroZenbakiak.size(); i++) {
                    writer.write("LERRO " + lerroZenbakiak.get(i) + ":\n");
                    writer.write(lerroEdukiak.get(i) + "\n");
                    writer.write("---\n\n");
                }

                writer.write("=== BUKAERA ===\n");

                System.out.println("Lerroak '" + irteeraFitxategia + "' fitxategian gordeta.");

            } catch (IOException e) {
                System.err.println("Errorea irteera fitxategia idaztean: " + e.getMessage());
            }

        } catch (IOException e) {
            System.err.println("Errorea sarrera fitxategia irakurtzean: " + e.getMessage());
        }
    }
}
