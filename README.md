# Proiect la Geometrie Computațională

## Rulare

Atât server-ul cât și front end-ul rulează cu `Docker <https://www.docker.com/>`.
Presupunând că Docker funcționează și că [`docker-compose`](https://docs.docker.com/compose/) este instalat,
puteți porni aplicația prin:

```sh
$ docker-compose up
```

Puteți opri aplicația rulând `Ctrl + C`.

Pentru a elibera resursele utilizate de containere la final puteți rula:

```sh
$ docker-compose down
```

## Testare

Testele automate pentru proiect pot fi rulate cu [pytest](https://docs.pytest.org/en/latest/).

După instalare, este suficient să rulați:

```sh
$ docker run --rm proiect-geomcomp_backend pytest
```

## Documentație

### Back end

Documentația poate fi generată folosind [pdoc](https://pdoc3.github.io/pdoc/).

### Front end

Documentația poate fi generată folosind [jsdoc](https://jsdoc.app/).
