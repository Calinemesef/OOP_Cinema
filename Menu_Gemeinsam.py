class Menu_Gemeinsam:

    """
    MENU-Gemeinsam
    - keine Attribute
    - enthalt folgende Methoden: Bestellung-Option, Anzeigen, Suchen, Schauspieler
    + zusammenfassungs-menu
    """

    @staticmethod
    def bestellung_option(filme):

        """
        Methode fur Bestellen der Filmen
        """
        try:
            print("Bestellung-Option")
            nr = 1
            print("Liste von Filmen und ihren Preis ")
            for i in range(0, len(filme)):
                print(nr)
                nr += 1
                print(filme[i].get_titel() + ' ' + filme[i].get_preis() + " LEI")

            nr = int(input("Wie viele Filmen mochten Sie kaufen?"))

            preis = 0
            print("Wahlen Sie sich die Filme an, indem Sie die entsprechende Zahl angeben:")
            for i in range(0, nr):
                x = int(input())
                preis = preis + int(filme[x - 1].get_preis())
            print("Gesamtpreis: " + str(preis) + " LEI")
        except Exception as e:
            print(str(e))

    @staticmethod
    def anzeigen(benutzer):

        """
        Methode furs Anzeigen aller Benutzern und ihre Bestellungen
        """
        try:
            print("Anzeigen der Benutzern mit aktuellen Bestellungen: ")
            for i in range(0, len(benutzer)):
                print("Benutzer: " + benutzer[i].get_vorname() + ' ' + benutzer[i].get_nachname() + ' ' + " - Bestellungen: " + ' '.join(benutzer[i].get_bestellungen()))
        except Exception as e:
            print(str(e))

    @staticmethod
    def suchen(filme):

        """
        Methode furs Suchen nach Filmen mit der Wertung >= als eingegeben
        """
        try:
            wert = float(input("Suchen nach Filme mit der Wertung uber: "))
            for i in range(0, len(filme)):
                if float(filme[i].get_wertung()) > wert:
                    print(filme[i].get_titel() + ' ' + filme[i].get_wertung())
        except Exception as e:
            print(str(e))

    @staticmethod
    def schauspieler(filme):

        """
        Methode furs Anzeigen aller Filmen in denen ein Schauspieler spielt
        """
        try:
            print("Anzeigen aller Filmen, in denen der gegebene Schauspieler gespielt hat")
            ok = 0
            nume = input("Name: ")
            for i in range(0, len(filme)):
                if filme[i].get_schauspieler() == nume:  # ???????????????????????????????????????????
                    ok = 1
                    print(filme[i].get_titel)

            if ok == 0:
                print("Kein Film mit dem gegebenen Schauspieler gefunden")
        except Exception as e:
            print(str(e))

    def menu_gemeinsam(self, benutzer, filme):

        """
        Zusammenfassungs-Menu der allen obigen Methoden enthalt und sie aufruft
        """
        try:
            print("Gemeinsames Menu")
            print("Zuruck zum Anfangsmenu: Taste 0")
            print("Furs Bestellung-Option drucken Sie Taste 1")
            print("Furs Anzeigen der Liste von Benutzern mit aktuellen Bestellungen drucken Sie Taste 2")
            print("Furs Suchen nach Filme mit einer spezifischen Wertung drucken Sie Taste 3")
            print("Furs Anzeigen aller Filmen mit einem gegebenen Schauspieler drucken Sie Taste 4")
            tasta = int(input("Tasta: "))
            while tasta != 0:
                if tasta == 0:
                    break
                elif tasta == 1:  # Bestellung-Option
                    self.bestellung_option(filme)
                elif tasta == 2:  # Liste von Benutzern mit aktuellen Bestellungen
                    self.anzeigen(benutzer)
                elif tasta == 3:  # Suchen nach Filmen mit einer spezifischen Wertung
                    self.suchen(filme)
                elif tasta == 4:  # Anzeigen aller Filmen mit einem gegebenen Schauspieler
                    self.schauspieler(filme)
                print("Menu Gemeinsam")
                print("Zuruck zum Anfangsmenu: Taste 0")
                print("Furs Bestellung-Option drucken Sie Taste 1")
                print("Furs Anzeigen der Liste von Benutzern mit aktuellen Bestellungen drucken Sie Taste 2")
                print("Furs Suchen nach Filme mit einer spezifischen Wertung drucken Sie Taste 3")
                print("Furs Anzeigen aller Filmen mit einem gegebenen Schauspieler drucken Sie Taste 4")
                tasta = int(input())
        except Exception as e:
            print(str(e))
