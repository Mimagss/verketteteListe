from typing import Any

#stand 27.09.2023

class Knoten:
    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.naechster = None

    def __str__(self) -> str:
        return f"Knoten({str(self.inhalt)}, Nächster({self.naechster}))"
    
class VerketteteListe:
    def __init__(self):
        self.erster = None  

    def swap(self, i : int, j : int) -> None:
        buffer : Any = self.inhalt(index= i)
        self.ersetzen(index = i, inhalt= self.inhalt(j))
        self.ersetzen(index = j, inhalt= buffer)

    def einfuegen_vorne(self, pInhalt) -> None:
        """doc pls"""
        neu = Knoten(pInhalt)
        neu.naechster = self.erster
        self.erster = neu  

    def entfernen_vorne(self) -> Any:
        """doc pls"""
        if self.erster is None:
            raise RuntimeError
        
        letzterInhalt = self.erster.inhalt
        self.erster = self.erster.naechster
        return letzterInhalt


    def __str__(self) -> str:
        inhalte = []
        knoten = self.erster
        while knoten is not None:
            inhalte.append(knoten.inhalt)
            knoten = knoten.naechster
        return " -> ".join(inhalte)

    def ist_leer(self) -> bool:
        """
        prüft den Listen kopf auf einen None Verweis
        """
        if self.anzahl_elemente() == 0:
            return True
        return False
    
    def anzahl_elemente(self) -> int:
        """Zählt die iterierungen der Liste und gibt de letztendliche Anzahl zurück"""
        erster = self.erster
        if erster is None:
            return 0
        
        i = 0
        
        while erster is not None:
            i += 1
            erster = erster.naechster
        
        return i
    
    def inhalt(self, index) -> Any:
        """doc pls"""
        if index < 0:
            raise IndexError("Index out of range")
        knoten = self.erster
        for i in range(index):
            if knoten is None:
                raise IndexError("Index out of range")
            knoten = knoten.naechster
        if knoten is None:
            raise IndexError("Index out of range") 
        return knoten.inhalt
    
    def ersetzen(self, index, inhalt) -> None:
        """doc pls"""
        if index < 0:
            raise IndexError("Index out of range")
        knoten = self.erster
        for i in range(index):
            if knoten is None:
                raise IndexError("Index out of range")
            knoten = knoten.naechster
        if knoten is None:
            raise IndexError("Index out of range")  
        knoten.inhalt = inhalt

    def einfuegen(self, index, inhalt)  -> None:
        """doc pls"""
        if index < 0:
            raise IndexError("Method doesn`t support negative Indexes")
        
        neu = Knoten(inhalt)
        if index == 0 and self.erster.naechster is None:
            neu.naechster = self.erster
            self.erster = neu
        
        else:
            knoten = self.erster
            i = 0 
            while knoten.naechster is not None:
                if i > self.anzahl_elemente():
                    raise IndexError("Index out of Range")
                elif index == i:
                    neu.naechster = knoten.naechster
                    knoten.naechster = neu
                    return
                
                i += 1

            knoten.naechster = neu

    def enthaelt(self, inhalt) -> bool:
        """doc pls"""
        knoten = self.erster
    
        while knoten is not None:
            if knoten.inhalt == inhalt:
                return True
            
            if knoten.naechster is not None:
                knoten = knoten.naechster
            else:
                raise ValueError(f"{inhalt} is not in List")
            
        return False

    def anhaengen(self, inhalt) -> None:
        """doc pls"""
        neu = Knoten(inhalt)
        if self.erster is None:
            self.erster = neu
        else:
            knoten = self.erster
            while knoten.naechster is not None:
                knoten = knoten.naechster
            knoten.naechster = neu
                 
    def entfernen(self, index) -> Any:
        """doc pls"""
        knoten = self.erster
        letzterKnoten = self.erster
        i = 0 
        
        if index < 0:
            raise IndexError("Index out of range")
        
        if index == 0:
            if self.erster.naechster is not None:
                self.erster = self.erster.naechster

            else:
                self.erster.inhalt = ""
                self.erster.naechster = None

        if index > self.anzahl_elemente() -1:
            raise IndexError("Index out of Range")
        
        while knoten is not None:
            if i > self.anzahl_elemente():
                raise IndexError("Index out of Range")
            elif index == i:
                letzterKnoten.naechster = knoten.naechster
                return
            
            letzterKnoten = knoten
            knoten = knoten.naechster
            i += 1
            

    def entfernen_element(self, inhalt : str) -> None:
        """doc pls"""
        knoten = self.erster
        letzterKnoten = self.erster

        while knoten is not None:
            if knoten.inhalt == inhalt:
                if knoten.naechster is not None:
                    letzterKnoten.naechster = knoten.naechster

                else:
                    knoten.inhalt = ""
                    letzterKnoten.naechster = None

            if knoten.naechster is not None:
                letzterKnoten = knoten
                knoten = knoten.naechster

            else:
                break

