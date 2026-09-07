package ariketa1;

import java.io.File;

/**
 * Direktorio bateko fitxategi eta direktorioen zerrenda erakusten duen programa.
 * Defektuz c:\windows erabiltzen du; parametro bezala beste direktorio bat pasa daiteke.
 *
 * Erabilera:
 *   java DirektorioZerrenda
 *   java DirektorioZerrenda C:\Users
 *   java DirektorioZerrenda /home/erabiltzailea
 */
public class DirektorioZerrenda {

    private static final String DEFEKTUZKO_DIREKTORIOA = "c:\\windows";

    public static void main(String[] args) {
        String bidea = DEFEKTUZKO_DIREKTORIOA;

        // Hobekuntza: direktorioa parametro bezala pasatu daiteke
        if (args.length > 0 && args[0] != null && !args[0].isBlank()) {
            bidea = args[0];
        }

        File direktorioa = new File(bidea);

        if (!direktorioa.exists()) {
            System.out.println("Errorea: '" + bidea + "' ez da existitzen.");
            return;
        }

        if (!direktorioa.isDirectory()) {
            System.out.println("Errorea: '" + bidea + "' ez da direktorio bat.");
            return;
        }

        File[] elementuak = direktorioa.listFiles();

        if (elementuak == null) {
            System.out.println("Errorea: ezin izan da '" + bidea + "' irakurri.");
            return;
        }

        System.out.println("Direktorioaren edukia: " + direktorioa.getAbsolutePath());
        System.out.println("----------------------------------------");

        int fitxategiKopurua = 0;
        int direktorioKopurua = 0;

        for (File elementua : elementuak) {
            if (elementua.isDirectory()) {
                System.out.println("[DIR]  " + elementua.getName());
                direktorioKopurua++;
            } else {
                System.out.println("[FITX] " + elementua.getName());
                fitxategiKopurua++;
            }
        }

        System.out.println("----------------------------------------");
        System.out.println("Guztira: " + direktorioKopurua + " direktorio, "
                + fitxategiKopurua + " fitxategi.");
    }
}
