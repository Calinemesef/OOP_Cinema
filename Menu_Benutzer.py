from Class_Benutzer import Benutzer


class Menu_Benutzer:

    """
    MENU-Klasse
    -enthalt folgende Methoden : Einfugen, Aktualisieren, Loschen
    + zusammenfassung-menu

    """

    @staticmethod
    def einfugen(users):

        """
        Methode fur Einfugen eines neuen Benutzers in der Liste und in der Datei

        """

        print("EINFUGEN EINES NEUEN BENUTZERS")
        vorname = input("Vorname: ")
        nachname = input("Nachname: ")
        new_user = Benutzer(vorname, nachname)  # Erzeugt Objekt vom Typ Benutzer
        i = 0
        Bestellungen = []
        nrBestellungen = int(input("Introduceti numarul de comenzi "))
        while i < nrBestellungen:
            print("Film nr ", i + 1, " ", end='')
            film = input("")
            Bestellungen.append(film)
            i += 1
        users.append(new_user)
        users[len(users)-1].set_bestellungen(Bestellungen)
        print("Neuer Benutzer erfolgreich eingefugt ")

        # EINFUGEN DES NEUEN BENUTZERS IN DER DATEI
        with open("Users", "r") as file:
            data = file.readlines()
        data.append("\n" + vorname + ", " + nachname + ", " + ', '.join(Bestellungen))
        with open("Users", "w") as file:
            file.writelines(data)

    @staticmethod
    def aktualisieren(users):

        """
        Methode fur Aktualisieren der Nachname des Benutzers sowohl in der Liste als auch in der Datei
        """
        try:
            found = 0
            print("Aktualisieren ")
            nachname = input("Aktueller Nachname: ")
            for i in range(0, len(users)):
                if users[i].get_nachname() == nachname or users[i].get_nachname() == nachname + ',\n':
                    found = 1
                    break
            if found == 1:
                users[i].set_nachname(input("Neuer Nachname eingeben: "))
                print("Benutzerdaten erfolgreich aktualisiert ")
            else:
                print("Benutzer nicht gefunden")


            # AKTUALISIEREN DER NAME IN DER DATEI
            with open("Users", "w") as file:
                for user in users:
                    aux = ', '.join(str(v) for v in user.get_bestellungen())
                    file.writelines(
                        user.get_vorname() + ', ' + user.get_nachname() + ', ' + aux)
        except Exception as e:
            print(str(e))

    @staticmethod
    def loschen(users):

        """
        Methode fur Loschen eines gegebenen Benutzers sowohl in der Liste als auch in der Datei
        """
        try:
            found = 0
            nachname = input("Loschen des Benutzers mit der Nachname: ")
            for i in range(0, len(users)):
                if users[i].get_nachname() == nachname:
                    found = 1
                    break
            if found == 1:
                users.pop(i)
                print("Benutzer geloscht")
            else:
                print("Benutzer nicht gefunden")

            #LOSCHEN DES BENUTZERS IN DER DATEI
            with open("Users", "w") as file:
                for user in users:
                    aux = ', '.join(str(v) for v in user.get_bestellungen())
                    file.writelines(
                        user.get_vorname() + ', ' + user.get_nachname() + ', ' + aux)
        except Exception as e:
            print(str(e))

    def menu(self, users):

        """
        Zusammenfassungs-MENU der allen obigen Methoden enthalt
        """

        print("MENU BENUTZER")
        print("Zuruck zum Anfangsmenu: Taste 0")
        print("Fur Einfugen eines Benutzers drucken Sie Taste 1")
        print("Fur Aktualisierung der Nachname drucken Sie Taste 2")
        print("Fur Loschen eines gegebenen Benutzers drucken Sie Taste 3")

        try:
            tasta = int(input("TASTA: "))
            while tasta != 0:
                if tasta == 0:
                    break
                elif tasta == 1:  # Einfugen eines Films
                    self.einfugen(users)
                elif tasta == 2:  # Aktualisierung des Preises eines Films
                    self.aktualisieren(users)
                elif tasta == 3:  # Anzeigen aller Filmen
                    self.loschen(users)
                print("Menu Benutzer")
                print("Zuruck zum Anfangsmenu: Taste 0")
                print("Fur Einfugen eines Benutzers drucken Sie Taste 1")
                print("Fur Aktualisierung der Nachname drucken Sie Taste 2")
                print("Fur Loschen eines gegebenen Benutzers drucken Sie Taste 3")
                tasta = int(input("TASTA: "))
        except Exception as e:
            print(str(e))