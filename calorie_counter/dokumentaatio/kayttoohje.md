# Käyttöohje
Tässä miten aloittaa ohjelma.

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Ensinmäisellä suoritus kerralla käytä komentoa:

```
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```
Komennot pitää suorittaa calorie_counter hakemistossa.

## Ensinmäinen käynnistys
Kun käynnistätä ohjelman ensinmäistä kertaa sinulta kysytään tietoja kalorikuluksesi laskemiseen.
Kirjoita vastauksesi terminaaliin ja paina enter avainta kun olet valmis.
Ohjelma pyytää sinun, nimesi, ikäsi, sukupuolesi, pituutesi ja painosi.
Tietojen antamisen jälkeen ohjelman voi avata komennolla :
```
poetry run invoke start
```

## Perusnäkymä
Perusnäkymässä sinulle näytetäään kuinka paljon kaloreita olet syönyt tänään, kuinka paljon kaloreita olet polttanut.
Näkymästä pääset lisäämän ruokailun antamalla numeron 1 tai lisäämän treenin antamalla numeron 2.
Ohjelman voi sulkea antamalla 0.

## Ruuan tai treenin lisäys
Ruuan ja treenin lisäys toimii tasan samalla tavalla.
Ensin pyydetään kuvailemaan syötyä ruokaa/tehtyä treeniä jonka jälkeen pyydetään ruuan/treenin kaloriarvoa.
Tietojen antamisen jälkeen ne tallennetaan tietokantaan ja palataan perusnäkymään.
