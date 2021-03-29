from Class_Film import Film


class Menu_Filme:

    """
    MENU-Klasse fur Filmen
    - keine Attribute
    - Methoden fur Einfugen, Aktualisieren, Anzeigen
    + zusammenfassung-menu

    """

    @staticmethod
    def einfugen(filme):

        """
        Methode fur Einfugen eines Films in der Liste und in der Datei
        """
        print("Einfugen von Filme ")
        titel = input("Name: ")
        jahr = input("Erscheinungsjahr: ")
        wertung = input("Wertung: ")
        preis = input("Preis: ")
        new_film = Film(titel, jahr, wertung, preis)
        i = 0
        schauspieler = []
        nr = int(input("Introduceti numarul de actori "))
        while i < nr:
            print("Actor nr ", i + 1, " ", end='')
            film = input("")
            schauspieler.append(film)
            i += 1
        filme.append(new_film)
        filme[len(filme) - 1].set_schauspieler(schauspieler)
        print("Neues Film erfolgreich eingefugt ")

        # Einfugen in der Datei
        with open("Movies", "r") as file:
            data = file.readlines()
        data.append("\n" + titel + ", " + jahr + ", " + wertung + ', ' + preis + ', ' + ', '.join(schauspieler))
        with open("Movies", "w") as file:
            file.writelines(data)


    @staticmethod
    def aktualisieren(filme):

        """
        Methode fur Aktualisieren eines Filmpreises sowohl in der Liste als auch in der Datei
        """
        try:
            found = 0
            print("Preis-Aktualisierung ")
            titel = input("Filmname: ")
            for i in range(0, len(filme)):
                if filme[i].get_titel() == titel or filme[i].get_titel() == titel + ',\n' :
                    found = 1
                    break
            if found == 1:
                filme[i].set_preis(input("Neuer Preis: "))
                print("Preis erfolgreich aktualisiert: ")
            else:
                 print("Film nicht gefunden")

            # Aktualisieren in der Datei
            with open("Movies", "w") as file:
                for film in filme:
                    aux = ', '.join(str(v) for v in film.get_schauspieler())
                    file.writelines(film.get_titel() + ', ' + film.get_jahr() + ', ' + film.get_wertung() + ', ' + film.get_preis() + ', ' + aux)
        except Exception as e:
            print(str(e))


    @staticmethod
    def anzeigen(filme):

        """
        Methode furs Anzeigen der Filmliste
        """
        try:
            print("Liste von Filmen: ")
            for i in range(0, len(filme)):
                print(filme[i].get_titel())
        except Exception as e:
            print(str(e))

    def menu_filme(self, filme):

        """
        Zusammenfassungsmenu der allen obigen Methoden enthalt und sie aufruft
        """

        try:
            print("Menu Filme")
            print("Zuruck zum Anfangsmenu: Taste 0")
            print("Fur Einfugen eines Films drucken Sie Taste 1")
            print("Fur Aktualisierung eines Filmspreises drucken Sie Taste 2")
            print("Fur Anzeigen der Liste von Filmen drucken Sie Taste 3")

            tasta = int(input("TASTA: "))
            while tasta != 0:
                if tasta == 0:
                    break
                elif tasta == 1:  # Einfugen eines Films
                    self.einfugen(filme)
                elif tasta == 2:  # Aktualisierung des Preises eines Films
                    self.aktualisieren(filme)
                elif tasta == 3:  # Anzeigen aller Filmen
                    self.anzeigen(filme)
                print("Menu Filme")
                print("Zuruck zum Anfangsmenu: Taste 0")
                print("Fur Einfugen eines Films drucken Sie Taste 1")
                print("Fur Aktualisierung eines Filmspreises drucken Sie Taste 2")
                print("Fur Anzeigen der Liste von Filmen drucken Sie Taste 3")
                tasta = int(input("TASTA: "))
        except Exception as e:
            print(str(e))
