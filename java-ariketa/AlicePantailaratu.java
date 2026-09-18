import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * Bertsio sinplea: C:/alice.txt pantailaratzen du lerroz lerro.
 */
public class AlicePantailaratu {

    private static final String FITXATEGI_BIDEA = "C:/alice.txt";

    public static void main(String[] args) {
        String bidea = (args.length > 0) ? args[0] : FITXATEGI_BIDEA;

        try (BufferedReader irakurlea = new BufferedReader(new FileReader(bidea))) {
            String lerroa;
            while ((lerroa = irakurlea.readLine()) != null) {
                System.out.println(lerroa);
            }
        } catch (IOException e) {
            System.err.println("Errorea: " + e.getMessage());
            System.err.println("Fitxategia hemen egon behar da: C:/alice.txt");
        }
    }
}
