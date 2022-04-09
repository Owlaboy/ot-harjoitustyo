
# CalorieCounterApp

Sovelluksen avulla käyttäjä voi pitää kirjaa päivittäisestä kalorikulutuksestaan. Ohjelmaan kirjataan aluksi omat tiedot joilla voidaan laskea päivittäinen kalorikulutus. Alustamisen jälkeen käyttäjä kirjaa ohjelmaan 

## Ohjhelman Python-versio

Sovelluksen toiminta on testattu Python-versiolla `3.8`.

# Ohjelmistotekniikka, harjoitustyö
## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/Owlaboy/ot-harjoitustyo/blob/cb63175993b1c7a3a6ffea62b9294800f659ca5b/calorie-counter/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/Owlaboy/ot-harjoitustyo/blob/cb63175993b1c7a3a6ffea62b9294800f659ca5b/calorie-counter/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/Owlaboy/ot-harjoitustyo/blob/bb8e1b9ff35ef3fec95e620e7e65f5045a82d34b/calorie-counter/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Sovellus käynnistetään komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy aloittamaan komennolla:

```bash
poetry run invoke start
```

### Testaaminen

Ohjelman testaaminen suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testien kattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage_report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
