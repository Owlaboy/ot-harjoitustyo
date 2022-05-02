# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne muodostuu kolmesta osasta.
- Sovelluksen käyttöliittymä, luokka [Calorietracker](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/calorietracker.py)
- Laskin, luokka [Calculator](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/calculator.py)
- Tietokanta, luokka [Userdata](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/personcreation.py) 

Sovelluksen käyttöliittymä kutsuu laskin ja tietokanta luokkia.

Tietokannan rakenne muodostuu kolmesta taulukosta.
- User
- Meals
- Exercises

User taulukkoon tallennetaan käyttäjän tiedot:
- Nimi
- Ikä
- Sukupuoli
- Pituus
- Paino

Meals taulukkoon tallennetaan käyttäjän syödyt ruuat ja ruokien päivämäärät:
- Päiväys
- Kuvaus ruuasta
- Ruuan kalorimäärä

Exercises taulukkoon tallennetaan käyttäjän suorittamat treenit ja niiden päivämäärät:
- Päiväys
- Kuvaus treenistä
- Treenin polttamat kalorit

## Käyttöliittymä
Käyttölittymä sisältää neljä tilaa.
- Kirjautuminen
- Perus näkymä
- Ruoan lisäys
- Treenin lisäys

Kirjautuessa käyttäjältä pyydetään tietoja kalorikulutuksen laskemiseen
Perusnäkymässä näkyy käyttäjän kalorikulutus ja käyttäjälle annetaan vaihtoehdoksi ruuan tai treenin lisäys.
Ruuan lisäämisessä käyttäjältä pyydetään mitä on syöty ja kuinka paljon kaloreita on syöty.
Treenin lisäämiseltä käyttjälätä pyydetään miten on liikuttu ja kuinka paljon kaloreita on poltettu.

Kaikki näkymät ovat tällähetkellä eri metodeija saman luokan [Calorietracker](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/calorietracker.py) sisällä. Käyttöliittymä yhdistää ohjelman eri luokkien metodit, jotta käyttäjälle voitaisiin näyttää päivittäinen kalorikäyttö.

## Sovelluslogiikka
Sovelluksen looginen toiminta muodostuu kolmesta osasta.
- Sovelluksen käyttöliittymä, luokka [Calorietracker](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/calorietracker.py)
- Laskin, luokka [Calculator](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/calculator.py)
- Tietokanta, luokka [Userdata](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/personcreation.py) 

Sovelluksen käyttöliittymä yhdistää laskimen ja tietokannan toiminnot. 
Käyttöliittymä kutsuu laskinta ja tietokantaa saadakseen selville miten paljon kaloreita on kulutettava päivän aikana ja
kuinka paljon kaloreita on kulutettu/kuluu päivän aikana. 
Käyttöliittymän kautta tietokantaan lisätään eri ruokailuja ja treenejä mitä käyttäjä on tehnyt päivien aikana.
Käyttölittymä saa dataa tietokannasta ainoastaan [Userdata](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/personcreation.py) luokan kautta.

Tietokannan toiminnallisuudesta vastaa luokka [Userdata](https://github.com/Owlaboy/ot-harjoitustyo/blob/b6256bcf24776b51d364a82c1db44ffed56c07eb/calorie_counter/src/personcreation.py).
Luokka sisältää eri metodeja tietokannan käyttämistä varten. Näitä ovat esimerkiksi:
- `new_person`
- `new_meal`
- `give_user_data`

## Datan tallennus

Ohjelman ensinmäisellä suoritus kerralla luodaan tiedosto `user.db` johon alustetaan tietokantaan tallennettavat taulukot.
Ohjelma käyttää Sqlite3 tietokannan hallintaan.
Kun ohjelma käynnistetään uudelleen, se jatkaa `user.db` käyttöä.


## Päätoiminnallisuudet

### Käyttäjän tietojen tallennus
Kun ohjelmaa kutsutaan ensinmäistä kertaa, ohjelma pyytää käyttäjän tietoja. Ohjelman luokat toimivat seuraavasti:
![](https://github.com/Owlaboy/ot-harjoitustyo/blob/666e596a7bb4451f5a909ca2719cce72875b490f/calorie_counter/dokumentaatio/kuvat/Screenshot_20220502_171457.png)

### Uusi ruokailu ja treeni
Ruokailun ja treenin lisääminen toimii samalla tavalla.
Luokat kutsuvat toisiaan seuraavasti:
![](https://github.com/Owlaboy/ot-harjoitustyo/blob/666e596a7bb4451f5a909ca2719cce72875b490f/calorie_counter/dokumentaatio/kuvat/Screenshot_20220502_171813.png)

### Kalorikulutuksen laskenta
Kalorikulutksen laskenta suoritetaan seuraavasti:
![](https://github.com/Owlaboy/ot-harjoitustyo/blob/666e596a7bb4451f5a909ca2719cce72875b490f/calorie_counter/dokumentaatio/kuvat/Screenshot_20220502_172638.png)




