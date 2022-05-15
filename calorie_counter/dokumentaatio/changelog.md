## Viikko 3

- Luotu laskin luokka joka laskee tarvittavat kalorimäärät painon ylläpitämiselle.
- Luotu testi laskin luokkaa varten.
- Luotu alustavat invoke-tehtävät kokeilua varten.

## Viikko 4

- Päivitetty README tiedosto, listätty tarkemmat ohjeet ohjelman suorittamiselle ja ohjelman kuvaus
- Päivitetty tuntikirjanpito sisältämään myös yhteisen ajan käytön
- Päivitetty vaatimusmäärittely, eri toiminnallisuuskohtiin on lisätty "Tehty" merkintä
- Poetry:n start komentoon lisätty "personcreation.py":n suoritus
- Lisätty uusia invoke komentoja
- Luotu uusi tiedosto "calorietracker.py", mikä suorittaa ohjelman perus toiminnallisuuden.
- Päivitetty tiedostoa "personcreation.py"
    - Lisätty metodi joka palauttaa käyttäjän tiedot calorien laskentaa varten

## Viikko 5

- Luotu uusia testejä "personcreation" luokkaa varten
- Luotu uusia metodeja syötyjen ja poltettujen kalorien määrän laskemista varten "personcreation" tiedostossa
    - metodit "give_calories" ja "give_todays_calories"
        - "give_calories" metodi antaa parametrina annetun päivän kalorimäärän
        - "give_todays_calories" metodi antaa kutsupäivänä syödyt kalorit kutsumalla metodia "give_calories"
    - metodit "calories_burned" ja "calories_burned_today"
        - "calories_burned" metodi antaa parametrina annetun päivän poltetut kalorit
        - "calories_burned_today" metodi antaa kutsupäivänä poltetut kalorit 
- Korjattu README tiedosto
- Korjattu eri pylint virheitä
- Muutettu tiedoston avaamis tapaa
- Luotu uusia testejä kattavuutta varten
- Ohjelma nyt laskee poltetut kalorit ja syödytkalorit
    - Näyttää luvut vierekkäin käyttäjälle

## Viikko 6
- Dokumentaatio muutoksia.
    - Arkkitehtuurikuvauksen ja käyttöohjeen luonti
    - READMEn tarkentaminen palautuksen mukaan
- Testiraportti käsittelee ainoastaan ohjelman tärkeitä osia eikä käyttöliittymää
- Docstring dokumentaatio kaikkii tiedostoihin paitsi testeihin.

## Viikko 7
- Dokumentaatio muutoksia.
    - Testausdokumentin luonti
    - Käyttöohjeen päivitys
    - READMEn päivitys
- Testikattavuuden laajennus
    - Testit kattavat nyt kaikki käyttölittymän ulkopuolella olevat metodit ja luokat
- Lisätty uusi tiedosto ohjelman alustamista varten
- Lisätty uusi "poetry invoke" komento ohjelman alustamista varten
