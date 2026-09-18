import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * Alice.txt fitxategia irakurtzen duen programa.
 * Suposatzen da fitxategia C:/alice.txt bidean dagoela.
 *
 * Egiten duena:
 *  - Fitxategia lerroz lerro irakurri
 *  - Lerro, hitz eta karaktere kopurua kalkulatu
 *  - "Alice" hitza zenbat aldiz agertzen den kontatu (maiuskulak/minuskulak kontuan hartu gabe)
 */
public class AliceIrakurri {

    // Erabiltzaileak eskatu bezala: alice.txt C:/ -n
    private static final String FITXATEGI_BIDEA = "C:/alice.txt";

    public static void main(String[] args) {
        // Aukeraz: argumentu bat emanez bidea alda daiteke (probetarako)
        String bidea = (args.length > 0) ? args[0] : FITXATEGI_BIDEA;

        int lerroKopurua = 0;
        int hitzKopurua = 0;
        int karaktereKopurua = 0;
        int aliceKopurua = 0;

        System.out.println("Fitxategia irakurtzen: " + bidea);
        System.out.println("----------------------------------------");

        try (BufferedReader irakurlea = new BufferedReader(new FileReader(bidea))) {
            String lerroa;
            while ((lerroa = irakurlea.readLine()) != null) {
                lerroKopurua++;
                karaktereKopurua += lerroa.length();

                // Hitzak: zuriune eta puntuazioaren arabera banatu
                String[] hitzak = lerroa.trim().split("\\s+");
                if (!lerroa.trim().isEmpty()) {
                    hitzKopurua += hitzak.length;
                }

                // "Alice" agerpenak (puntuazioa kenduta)
                for (String hitza : hitzak) {
                    String garbia = hitza.replaceAll("[^a-zA-Z]", "");
                    if (garbia.equalsIgnoreCase("Alice")) {
                        aliceKopurua++;
                    }
                }
            }

            System.out.println("Lerroak:          " + lerroKopurua);
            System.out.println("Hitzak:           " + hitzKopurua);
            System.out.println("Karaktereak:      " + karaktereKopurua);
            System.out.println("\"Alice\" agerpenak: " + aliceKopurua);

        } catch (IOException e) {
            System.err.println("Errorea fitxategia irakurtzean: " + e.getMessage());
            System.err.println("Egiaztatu alice.txt fitxategia C:/alice.txt bidean dagoela.");
        }
    }
}
