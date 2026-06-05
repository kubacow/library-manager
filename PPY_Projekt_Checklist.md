# Checklist projektu zaliczeniowego z Pythona: Mini Biblioteka

Poniższa lista kontrolna ułatwia weryfikację kompletności projektu pod kątem oficjalnych wytycznych i kryteriów oceniania (maks. 40 punktów).

## 1. Struktura programu i architektura (Maks. 8 pkt)
- [x] **Podział na moduły i pliki (3 pkt):** Kod jest podzielony na logiczne pliki (np. `main.py` dla menu, `models.py` dla klas, `utils.py` dla walidacji/funkcji pomocniczych). Brak jednego ogromnego pliku tekstowego.
- [x] **Poprawne użycie klas (3 pkt):** Zaimplementowano programowanie obiektowe (np. klasa `Book` reprezentująca pojedynczą książkę oraz klasa `Library` zarządzająca kolekcją). Klasy mają logiczne atrybuty i metody.
- [ ] **Czytelność i organizacja kodu (2 pkt):** Kod posiada logiczne wcięcia, przejrzyste nazwy zmiennych/metod w języku angielskim lub polskim oraz brak zbędnego, zakomentowanego kodu.

## 2. Elementy języka Python (Maks. 20 pkt)
*Każdy element musi być użyty w sposób naturalny, uzasadniony i zintegrowany z logiką aplikacji.*

- [ ] **Instrukcje sterujące (1 pkt):** Użyto `if-elif-else` (np. wybór w menu), pętli `for` (np. iteracja po książkach) oraz `while` (np. główna pętla programu).
- [x] **Operatory (1 pkt):** Użyto operatorów arytmetycznych, logicznych (`and`, `or`, `not`) oraz porównania (`==`, `!=`, `<`, `>`) w warunkach.
- [x] **Funkcje i lambda (3 pkt):** Zdefiniowano czytelne funkcje z argumentami i zwracanymi wartościami, oraz użyto **co najmniej jednej funkcji lambda** (np. jako klucz sortowania w `sorted(self.books, key=lambda x: x.title)`).
- [x] **Własny dekorator (3 pkt):** Napisano i poprawnie zastosowano własny dekorator (np. `@log_action`, który zapisuje do konsoli lub pliku informację o wywołaniu metody bibliotecznej).
- [x] **Kolekcje (2 pkt):** Wykorzystano wbudowane struktury danych – np. lista (`list`) do przechowywania spisu książek, słownik (`dict`) do szybkiego wyszukiwania po ISBN, lub zbiór (`set`) do unikalnych autorów.
- [x] **Kolekcje składane / Comprehensions (2 pkt):** Użyto przynajmniej jednego wyrażenia typu *list/dict/set comprehension* (np. filtrowanie dostępnych książek: `[b for b in self.books if not b.is_borrowed]`).
- [ ] **Generator (2 pkt):** Zaimplementowano funkcję generatorową z instrukcją `yield` lub wyrażenie generatorowe (np. generator zwracający po kolei przeterminowane wypożyczenia).
- [x] **Praca z plikami + Context Manager (3 pkt):** Użyto konstrukcji `with open(...)` do bezpiecznego otwierania i zamykania plików podczas operacji I/O.
- [x] **Serializacja danych (2 pkt):** Stan biblioteki jest trwale zapisywany i odczytywany przy starcie za pomocą formatu JSON (preferowany), CSV lub pickle (`json.dump` / `json.load`).
- [x] **Wyrażenia regularne / RegEx (1 pkt):** Użyto modułu `re` do sensownej walidacji danych wejściowych (np. sprawdzenie czy wprowadzony numer ISBN pasuje do wzorca `^\d{3}-\d-\d{3}-\d{5}-\d$` lub czy format e-mail użytkownika jest poprawny).

## 3. Obsługa błędów i wyjątków (Maks. 4 pkt)
- [x] **Sensowne komunikaty błędów (2 pkt):** Program przechwytuje niepoprawne dane wprowadzane przez użytkownika (np. litery zamiast cyfr w menu) za pomocą bloków `try-except` i wyświetla zrozumiałe komunikaty zamiast surowego tracebacku.
- [x] **Co najmniej jeden własny wyjątek (2 pkt):** Zdefiniowano własną klasę wyjątku dziedziczącą po `Exception` (np. `class BookNotAvailableError(Exception): pass`) i jest ona jawnie rzucana (`raise`) i obsługiwana w logice biznesowej.

## 4. Interfejs użytkownika (Maks. 4 pkt)
- [x] **Czytelne menu / komendy (2 pkt):** Interfejs tekstowy (CLI) wyświetla jasną listę opcji (np. 1. Dodaj książkę, 2. Wypożycz, 3. Wyświetl, 4. Wyjdź).
- [x] **Przewidywalne zachowanie programu (2 pkt):** Aplikacja reaguje stabilnie na akcje użytkownika, nie wyłącza się samoczynnie przy błędnym wpisie i pozwala na płynną nawigację.

## 5. Dokumentacja (Maks. 2 pkt)
- [ ] **Plik README (1 pkt):** W głównym katalogu znajduje się plik `README.md` zawierający krótki opis działania systemu Mini Biblioteki.
- [ ] **Instrukcja uruchomienia (1 pkt):** W pliku `README.md` podano dokładne polecenie potrzebne do uruchomienia programu (np. `python main.py`).

## 6. Jakość i pomysłowość (Maks. 2 pkt)
- [ ] **Estetyka kodu i przemyślana logika (2 pkt):** Kod jest elegancki, funkcje nie są przesadnie długie, a struktura aplikacji wykazuje dbałość o detale programistyczne.

---

## 🚨 Krytyczne Punkty Obrony (Przed wysłaniem!)
- [ ] **Nazwa archiwum:** Plik został spakowany jako `.zip` o dokładnej nazwie według schematu: `sXXXXX_projekt.zip` (gdzie sXXXXX to Twój numer indeksu). **[Błąd kosztuje -5 pkt]**
- [ ] **Zawartość .zip:** Wewnątrz archiwum znajdują się *wyłącznie* pliki tekstowe (`.py`, `.md`, `.json`). Usunięto foldery wirtualnego środowiska (`venv`), konfiguracje IDE (`.idea`, `.vscode`) oraz foldery repozytorium (`.git`). **[Błąd kosztuje -5 pkt]**
- [ ] **Test czystego uruchomienia:** Program uruchamia się bez błędów w terminalu bezpośrednio po rozpakowaniu. **[Brak uruchomienia kosztuje -10 pkt przy obronie!]**
- [ ] **Stabilność prezentacji:** Przetestowano wszystkie ścieżki w menu pod kątem braku nieobsłużonych crashów. **[Crash podczas prezentacji kosztuje -5 pkt!]**
- [ ] **Zrozumienie kodu:** Potrafisz samodzielnie odpowiedzieć na pytania prowadzącego dotyczące działania zaimplementowanych mechanizmów (np. jak działa Twój dekorator lub generator). **[Musisz odpowiedzieć na min. 3 z 5 pytań, inaczej otrzymujesz 0 pkt za projekt!]**
