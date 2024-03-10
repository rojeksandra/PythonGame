# PythonGame

# Projekt Gra w Pythonie

## Cel projektu
Projekt zakłada stworzenie gry w języku Python opartej na modelu klasowym oraz wykorzystującej bibliotekę Turtle. Głównym celem jest zapewnienie szerokiego spektrum rozgrywki, umożliwiając graczom wybór planszy, koloru postaci oraz zapewniając wzrost trudności wraz z kolejnymi poziomami.

## Narzędzia
- PyCharm
- Python

## Opis
Gra składa się z trzech różnych plansz, z których każda została opatrzona wcześniejszą instrukcją. Gracz może wybrać planszę poprzez wpisanie odpowiedniego słowa kluczowego, takiego jak "forest", "ocean" lub "desert", w wyznaczone pole. Dodatkowo, każda plansza jest opatrzona odpowiednim dźwiękiem, który pasuje do jej tematyki.

<img src="images_readme/instrukacja.png" alt="Zdjęcie 1">
Instrukcja plansza las
<img src="images_readme/instrukcja1.png" alt="Zdjęcie 2">
Instrukcja plansza ocean
<img src="images_readme/instrukcja2.png" alt="Zdjęcie 3">
Instrukcja plansza pustynia
<img src="images_readme/instrukcja33.png" alt="Zdjęcie 4">
Wybór planszy 
<img src="images_readme/select_game_board.png" alt="Zdjęcie 5">

Gracz ma również możliwość wyboru koloru swojego awatara

<img src="images_readme/select_color.png" alt="Zdjęcie 6">

Pierwsza plansza, "Forest", która jest również domyślną planszą, generuje kryjówki, w których gracz może ukryć się przed poruszającymi się zagrożeniami. Celem gracza jest dotarcie do mety, reprezentowanej przez żółty obiekt. Gracz może poruszać się w dowolnym kierunku za pomocą strzałek na klawiaturze.
<img src="images_readme/level1.png" alt="Zdjęcie 7">

Ukrycie gracza 

<img src="images_readme/hide_player.png" alt="Zdjęcie 8">

W przypadku zderzenia z zagrożeniem gra automatycznie się kończy, a jednocześnie generowany jest dźwięk zderzenia, informujący gracza o niepowodzeniu.

<img src="images_readme/collision.png" alt="Zdjęcie 9">

Wraz z każdym kolejnym poziomem generowane są nowe ustawienia kryjówek dla gracza, a ich liczba stopniowo maleje. Po osiągnięciu piątego poziomu, liczba kryjówek spada do zera, co oznacza, że zdobycie tego poziomu gwarantuje zwycięstwo. Dodatkowo, wraz z postępem w grze, liczba oraz szybkość zagrożeń zwiększa się, stając się coraz większym wyzwaniem dla gracza.

<img src="images_readme/victory.png" alt="Zdjęcie 10">

Wygląd innych plansz

Ocean 

<img src="images_readme/ocean.png" alt="Zdjęcie 11">

Pustynia 

<img src="images_readme/desert.png" alt="Zdjęcie 12">

