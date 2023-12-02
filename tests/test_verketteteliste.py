from verkettete_liste.verkettete_liste import VerketteteListe
import pytest

def test_einfuegen_vorne_leer() -> None:
    liste = VerketteteListe()
    liste.einfuegen_vorne("test1")
    erwarteter_string = "test1"
    assert erwarteter_string == str(liste)

def test_einfuegen_vorne_nicht_leer() -> None:
    liste = VerketteteListe()
    liste.einfuegen_vorne("test3")
    liste.einfuegen_vorne("test2") 
    liste.einfuegen_vorne("test1")
    erwarteter_string = "test1 -> test2 -> test3"
    assert erwarteter_string == str(liste) 

def test_entfernen_vorne_leer() -> None:
    liste = VerketteteListe()
    with pytest.raises(RuntimeError):
        liste.entfernen_vorne()

def test_entfernen_vorne()  -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")  
    liste.anhaengen("test2")  
    liste.anhaengen("test3") 
    erg = liste.entfernen_vorne()
    erwarteter_string = "test2 -> test3"
    assert erwarteter_string == str(liste) and erg == "test1" 

def test_ist_leer() -> None:
    liste = VerketteteListe()
    assert liste.ist_leer()

def test_ist_nicht_leer() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test")
    assert not liste.ist_leer()

def test_anzahl_elemente_leer() -> None:
    liste = VerketteteListe()
    assert 0 == liste.anzahl_elemente()

def test_anzahl_elemente_not_leer() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")  
    liste.anhaengen("test2")  
    liste.anhaengen("test3")
    liste.anhaengen("test4")  
    assert 4 == liste.anzahl_elemente()
    
def test_inhalt_negativer_index() -> None:
    liste = VerketteteListe()
    with pytest.raises(IndexError):
        inhalt = liste.inhalt(-1)

def test_inhalt_index_zu_gross() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")    
    with pytest.raises(IndexError):
        inhalt = liste.inhalt(2)

def test_inhalt() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2") 
    liste.anhaengen("test3") 
    liste.anhaengen("test4")
    istest1 =  "test1" == liste.inhalt(0)
    istest2 =  "test2" == liste.inhalt(1)
    istest3 =  "test3" == liste.inhalt(2)
    istest4 =  "test4" == liste.inhalt(3)
    assert istest1 and istest2 and istest3 and istest4

def test_ersetzen_negativer_index() -> None:
    liste = VerketteteListe()
    with pytest.raises(IndexError):
        liste.ersetzen(-1, "test1")

def test_ersetzen_negativ_index_zu_gross() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    with pytest.raises(IndexError):
        liste.ersetzen(1, "test2")

def test_ersetzen() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")  
    liste.anhaengen("test2")  
    liste.anhaengen("test3") 
    liste.ersetzen(0,"test4")
    liste.ersetzen(1,"test5")
    liste.ersetzen(2,"test6")
    erwarteter_string = "test4 -> test5 -> test6"
    assert erwarteter_string == str(liste)

def test_einfuegen_negativer_index() -> None:
    liste = VerketteteListe()
    with pytest.raises(IndexError):
        liste.einfuegen(-1,"test1")

def test_einfuegen_index_zu_groß() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")  
    liste.anhaengen("test2")  
    liste.anhaengen("test3") 
    with pytest.raises(IndexError):
        liste.einfuegen(3, "test4")

def test_einfuegen_index_zu_groß() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.einfuegen(0,"test2")
    erwarteter_string = "test2 -> test1"
    assert erwarteter_string == str(liste) 

def test_einfuegen() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2")
    liste.anhaengen("test3")
    liste.einfuegen(1,"test4")
    erwarteter_string = "test1 -> test4 -> test2 -> test3"
    assert erwarteter_string == str(liste)

def test_enthaelt() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")  
    liste.anhaengen("test2")  
    liste.anhaengen("test3")
    istest1 = liste.enthaelt("test1")
    istest2 = liste.enthaelt("test2")
    istest3 = liste.enthaelt("test3")
    assert istest1 and istest2 and istest3

def test_anhaengen_1() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test")
    str(liste) == "test"

def test_anhaengen_2() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2") 
    liste.anhaengen("test3") 
    liste.anhaengen("test4")
    erwarteter_string = "test1 -> test2 -> test3 -> test4"
    assert erwarteter_string == str(liste) 
   
    
def test_entfernen_negativer_index() -> None:
    liste = VerketteteListe()
    with pytest.raises(IndexError):
        liste.entfernen(-1)

def test_entfernen_index_zu_gross() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    with pytest.raises(IndexError):
        liste.entfernen(1)

def test_entfernen_vorne_ersters_element() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.entfernen(0)
    erwarteter_string = ""
    assert erwarteter_string == str(liste)

def test_entfernen_vorne_letztes_element1() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2")
    liste.entfernen(1)
    erwarteter_string = "test1"
    assert erwarteter_string == str(liste)

def test_entfernen_vorne_letztes_element2() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2")
    liste.anhaengen("test3")
    liste.entfernen(2)
    erwarteter_string = "test1 -> test2"
    assert erwarteter_string == str(liste)

def test_entfernen_vorne_mittleres_element() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2")
    liste.anhaengen("test3")
    liste.entfernen(1)
    erwarteter_string = "test1 -> test3"
    assert erwarteter_string == str(liste)

def test_entfernen_element_empty() -> None:
    liste = VerketteteListe()
    liste.entfernen_element("test1")
    erwarteter_string = ""
    assert erwarteter_string == str(liste)

def test_entfernen_element1() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.entfernen_element("test1")
    erwarteter_string = ""
    assert erwarteter_string == str(liste)

def test_entfernen1() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test2")
    liste.anhaengen("test3")
    liste.anhaengen("test4")
    liste.entfernen_element("test4")
    liste.entfernen_element("test2")
    erwarteter_string = "test1 -> test3"
    assert erwarteter_string == str(liste)

def test_entfernen2() -> None:
    liste = VerketteteListe()
    liste.anhaengen("test1")
    liste.anhaengen("test1")
    liste.entfernen_element("test1")
    erwarteter_string = "test1"
    assert erwarteter_string == str(liste)