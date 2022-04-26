
# CalorieCounterApp

Sovelluksen avulla käyttäjä voi pitää kirjaa päivittäisestä kalorikulutuksestaan. Ohjelmaan kirjataan aluksi omat tiedot joilla voidaan laskea päivittäinen kalorikulutus. Alustamisen jälkeen käyttäjä voi kirjata ohjelmaan syödyt ruuat ja poltetut kalorit treeneistä. Näiden tietojen avulla ohjelma sitten laskee käyttäjän päivittäisen kalorikulutuksen ja kuinka paljon kaloreita on syöty.

## Ohjhelman Python-versio

- [Ohjelman release](https://github.com/Owlaboy/ot-harjoitustyo/releases/tag/viikko5)

Sovelluksen toiminta on testattu Python-versiolla `3.8`.

# Ohjelmistotekniikka, harjoitustyö
## Dokumentaatio
- [Vaatimusmäärittely](calorie-counter/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](calorie-counter/dokumentaatio/tuntikirjanpito.md)
- [Changelog](calorie-counter/dokumentaatio/changelog.md)

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

## !!Ohjelman testaaminen tällä hetkellä poistaa käyttäjän tallennetut tiedot!!

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
