# Ohjelmistokehityksen teknologioita - Seminaarityö

## Telegram-Bot Pythonilla
## 6 - Python

## Aatu Marttila

## Sisältö
- [Tiivistelmä](##Tiivistelmä)
- [1 Johdanto](##1-Johdanto)
- [2 Käytetyt tekniikat](##2-Käytetyttekniikat)
    - [2.1 Python](##2.1-Python)
    - [2.2 API](##2.2-API)
    - [2.3 Pytest](##2.3-Pytest)
- [3 Arkkitehtuurikaavio](##3-Arkkitehtuurikaavio)
- [4 Pohdinta](##4-Pohdinta)
- [Lähteet](##Lähteet)






## Tiivistelmä
Päädyin valitsemaan seminaarityön aiheeksi Telegram-botin tekemisen Pythonilla. Moti-vaationa minulla oli oppia enemmän botin koodaamisesta sekä Pythonista. Olin ymmärtä-nyt, että Python on yleinen ohjelmointikieli botin kehittämiseen, joten tämä aihe valikoitui loppujen lopuksi melko luontevasti. Tavoitteenani oli saada kehitettyä toimiva botti, joka hakee tietoa APIn kautta sekä välittää APIsta saatavan tiedon edelleen botin käyttäjälle. Apuvälineinä käytin Telegram APIa, kurssin materiaalia, tutoriaalia YouTubesta sekä on-gelmatilanteissa Googlea ja ChatGPT:tä. 
Tärkeimpänä tuloksena pidän sitä, että edellä mainitut tavoitteeni, jotka asetin seminaari-työlleni täyttyivät, ja botti toimii niin kuin sen kuuluu. Koen myös tärkeänä tuloksena oman oppimisen kehittymisen.

## 1 Johdanto
Työni tarkoitus oli koodata toimiva Telegram-botti, jonka toimintaa testaa myös automaatti-set testit. Botin käyttäjänimi on aroundtheworldbot, ja nimensä mukaisesti botin toiminta liittyy maailmaan ja sen eri maihin. Olen aina ollut kiinnostunut maantieteestä sekä matkailu eri puolilla maailmaa on yksi asia vapaa-ajan intohimojani, joten botin aihetta miettiessä ajat-telin, että haluan kehittää botin, joka tuo sen käyttäjälle tietoisuutta maailman eri maista. Botissa on muutamia eri komentoja, jotka tulevat paremmin esille videossa. 
Työskentelyvaiheita oli kokonaisuudessaan kolme. Ensimmäinen vaihe oli ideointia siitä, millainen botin tulisi olla. Ensimmäisessä vaiheessa myös loin botin Telegramiin sekä tutus-tuin YouTube-tutoriaaliin. Toisessa vaiheessa aloin koodaamaan bottia ja sen eri ominai-suuksia, sekä testasin itse bottia samalla kun koodasin, varmistaakseni että botti toimii odotetulla tavalla. Kolmannessa vaiheessa viimeistelin botin koodauksen sekä kirjoitin testit botille.

## 2 Käytetyt tekniikat

###2.1	Python 
Botin koodaamiseen käytetty ohjelmointikieli on Python. Python soveltuu hyvin tämänkal-taiseen projektiin, sillä Pythonin syntaksi on yksinkertainen sekä koodi on helposti luetta-vaa. Python omaa myös hyvän skaalautuvuuden sekä on monipuolinen ohjelmointikieli. Lisäksi Pythonilla on mahdollista käyttää Python-Telegram-Bot nimistä kirjastoa, joka on välttämätön botin toteuttamisessa.
2.2	API
Botti hakee etsimänsä tiedon rajapinnasta nimeltä https://restcountries.com. Kyseinen API osoittautui hyväksi rajapinnaksi botin kehittämiseen, sillä se sisältää monipuolisesti erilaista tietoa, jota voi hyödyntää botissa.
2.3	Pytest
Kaikki botin yksikkötestit on kirjoitettu siten, että niitä pystyy testaamaan Pytestillä. Pytest osoittautui oivaksi työkaluksi yksikkötestien testaamiseen.

## 3 Arkkitehtuurikaavio
![alt](https://www.servicedesk.site/wp-content/uploads/2019/08/діаграма_бота-ru-копия-2-768x297.png)
Kuva 1 Kaavio Telegram-botin arkkitehtuurista (servicedesk.site, 2019).

## 4 Pohdinta
Tärkeimmäksi tulokseksi mainittakoon, että botti sekä botille kirjoitetut testit toimivat odo-tusten mukaisesti. Tietenkin bottia olisi voinut kehittää paljon lisää ja siihen olisi ollut mah-dollista integroida vielä paljon enemmän ominaisuuksia, mutta koen että sain tässä osaa-mispohjaa botin kehittämiseen ja jos päädyn joskus kehittämään tätä bottia tai kokonaan uuden botin, tiedän mistä aloittaa. 
Koin tämän seminaarityön aiheen sekä botin kehittämisen mielekkääksi. Pythonin syntaksi palautui melko helposti mieleen, sillä olen suorittanut vuosi sitten Python-ohjelmoinnin MOOC-kurssin. Kokonaisuudessaan opin alkeet siitä, miten rakennetaan Telegram-botti, sekä miten kirjoittaa sille yksikkötestejä. 
Aiheeseen voisi paneutua enemmän, sillä Telegram päivittää APIaan säännöllisesti. Botin kehittämisessä myös mahdollisuudet ovat rajattomat.

## Lähteet
* Indently. (2023). How To Create A Telegram Bot In Python For Beginners (2023 Tutorial) https://www.youtube.com/watch?v=vZtm1wuA2yc&t=989s

* Svyatoslav. (2019). https://www.servicedesk.site/en/2019/08/09/як-створити-телеграм-бота-правильно/

* API, josta botti hakee tiedot. https://restcountries.com

* Telegram API. https://core.telegram.org/bots/api

