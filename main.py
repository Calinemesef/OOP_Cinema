"""
Die Anwendung von Lab 3 soll als objektorientierte Anwendung gestaltet sein.
Anforderungen:
- Keine globale Variablen (0.5p)
- Keine Funktionen außerhalb von Klassen (0.5p)
- Persistenz der Objekte (d.h. als Dateien speichern und aus Dateien lesen) (2p)
- Docstrings für alle Methoden und Klassen (1p)
- Unit Tests für alle Methoden (außer Zugriffsmethoden und reine Outputmethoden) (1p)
- Benutzen von Ausnahmenbehandlungsmechanismen (try except) (1p)
- Diagramm mit den Klassen und Methoden (1p)

"""
from Class_Benutzer import Benutzer
from Class_Film import Film
from Menu_Benutzer import Menu_Benutzer
from Menu_Filme import Menu_Filme
from Menu_Gemeinsam import Menu_Gemeinsam

class Main:

    """
    Die Main-Klasse, hat folgende Methoden:
        - Methode fur Erzeugen der Anfangsliste des Benutzers/Films von deren entsprechenden Datei
        - Methode furs Anzeigen des Anfangsmenu mit allen entsprechenden Methoden drin
    """

    @staticmethod
    def anfangsliste_benutzer(users):

        """
        Methode furs Erzuegen der Anfangsliste der Benutzer
        - Liest die entsprechende Datei ein und fugt sich alle Benutzern als Objekte in einer Liste ein
        """

        index_utilizator = 0
        file = open("Users", "r")
        lines = file.readlines()
        for line in lines:
            thisline = line.split(", ")
            users.append(Benutzer(thisline[0], thisline[1]))
            for i in range(2, len(thisline)):
                users[index_utilizator].set_bestellungen(thisline[i])
            index_utilizator += 1
        file.close()

    @staticmethod
    def anfangsliste_filmen(filme):

        """
        Methode furs Erzeugen der Anfangsliste der Filmen
        - liest die entsprechende Datei ein und fugt sich alle Filmen als Objekte in einer Liste ein

        """

        index_film = 0
        file = open("Movies", "r")
        lines = file.readlines()
        for line in lines:
            thisline = line.split(", ")
            filme.append(Film(thisline[0], thisline[1], thisline[2], thisline[3]))
            for i in range(4, len(thisline)):
                filme[index_film].set_schauspieler(thisline[i])
            index_film += 1

    @staticmethod
    def principal(users, filme):

        """
        Methode furs Anzeigen des Anfangsmenu
        - enthalt die anderen 2 Methoden die die Anfangstlisten erzeugen
        - enthalt die 3 entsprechenden Menus: Menu-Benutzer, Menu-Film und Menu-Gemeinsam
        - wird erstens aufgerufen

        """

        users = []
        filme = []
        Main.anfangsliste_benutzer(users)
        Main.anfangsliste_filmen(filme)
        print("MENIU STANDARD")
        print("PENTRU EXIT: TASTA 0")
        print("PENTRU MENIU UTILIZATOR: TASTA 1")
        print("PENTRU MENIU FILME: TASTA 2")
        print("PENTRU MENIU COMUN: TASTA 3")

        comanda = int(input("TASTA: "))

        while comanda != 0:
            if comanda == 0:
                break
            elif comanda == 1:
                m = Menu_Benutzer()
                m.menu(users)
            elif comanda == 2:
                f = Menu_Filme()
                f.menu_filme(filme)
            elif comanda == 3:
                g = Menu_Gemeinsam()
                g.menu_gemeinsam(users, filme)
            print("MENIU STANDARD")
            print("PENTRU EXIT: TASTA 0")
            print("PENTRU MENIU UTILIZATOR: TASTA 1")
            print("PENTRU MENIU FILME: TASTA 2")
            print("PENTRU MENIU COMUN: TASTA 3")
            comanda = int(input("TASTA: "))


users = []
filme = []
Main.principal(users, filme)