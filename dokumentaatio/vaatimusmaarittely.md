# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on pitää kirjaa käyttäjän kalorimääristä. Sovellukseen kirjataan mitä päivän aikana käyttäjä syö ja mitä urheilua on tehty.
Tietojen perusteella sovellus laskee käyttäjän päivittäisen kalorien polton. Käyttäjä voi asettaa itselleen päivittäisen kaloritavoitteen.

## Käyttäjät

Sovellukseen on tarkoitus luoda vain yksi käyttäjä ensimmäisella aukaisukerralla. Myöhemmin sovellukseen saatetaan lisätä mahdollisuus luoda uusia käyttäjiä ja/tai 
_valmentaja_ käyttäjä, joka voi tarkastella muiden käyttäjien kaloreita.

## Käyttöliittymäluonnos
 ![](./kuvat/Luonnos1.jpg?raw=true]

## Perusversion tarjoama toiminnallisuus
### Ensimmäinen sovelluksen aukaisu
- Sovellus kysyy käyttäjän tiedot joilla lasketaan kalorien poltto
  - Tietoihin kuuluu esim. käyttäjän paino, pituus ja sukupuoli
 
### Tietojen tallentamisen jälkeen
- Sovellus näyttää päivän kaloritavoitteen ja päivämäärän
  - Tavoitteen lisäksi näkyy myös kuinka monta kaloria on syöty päivän aikana
- Käyttäjä voi lisätä syödyn ruuan
  - Uudessa ikkunassa voidaan kirjoittaa mitä on syöty ja käyttäjä täyttää kaloriarvion
- Käyttäjä voi lisätä treenin
  - Uudessa ikkunassa voidaan kirjoittaa miten on urheiltu ja käyttäjä täyttää kaloriarvion
- Käyttäjä voi myös nähdä aikaisempien päivien kalori määrät, ruuat ja treenit
  - Tiedot näkyvät taulukossa

## Jaktokehitysideoita
Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:
- Sovelluksessa on valmiiksi tallennettuja treenejä jotka voi valita ilman että käyttäjän tarvitsisi miettiä kaloreiden polttoa
- Sovellus muistaa aikaisempia harjoituksia ja ehdottaa niitä, kun käyttäjä lisää uuden treenin
- Sovelluksessa on valmiiksi tallennettuja ruokia jotka voi valita ilman että käyttäjän tarvitsis miettiä kuinka monta kaloria ruuassa oli
- Sovellus muistaa aikaisempia syötyjä ruokia ja ehdottaa niitä, kun käyttäjä lisää uuden ruokailun
- Sovellus laskee myös mitä vitamiineja syödystä ruoasta on saatu
- Sovellus laskee kuinka paljon proteiinia ruuasta on saatu joka päivä
- Sovellus voi antaa viikottaisen arvion/kokoelman viikon tavoitteiden täytöstä
- Sovellukseen voi myös asettaa harjoittelu tavoitteita kalori tavoitteen lisäksi
- Käyttäjä voi valita tarkemmin erilaisia kaloritavoitteita
