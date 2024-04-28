LUO:
-.venv (tehdessä käytetty Python ver. 3.12.3, vanhemmat versiot aiheuttivat virheitä)


ASENNETTAVAT:
-Asenna fastapi, uvicorn, sqlmodel

---------

RESULTS:
POST /results/ - Create Result:
-Luodaan uusi mittaustulos, tiedoiksi annetaan luku ja anturin ID

DELETE /results/{id} - Delete Result:
-Poistetaan luotu mittaustulos tuloksen ID perusteella


SENSORS:
POST /sensors/ - Create Sensor:
-Luodaan uusi anturi, annetaan lohkon ID, anturin ID tulee automaattisesti, anturin default tila = normal

GET /sensors/ - Get Sensors:
-Haetaan kaikki anturit, voidaan myös hakea antureita tilan mukaan

GET /sensors/{blockID} - Get Sensors Block:
-Haetaan antureita lohkon ID:n mukaan, palauttaa lohkon anturit

GET /sesnsors/{id} - Get Sensor:
-Haetaan antureita anturin ID:n perusteella

PUT /sensors/{id}/state - Change State:
-Vaihdetaan anturin tila, vaatii anturin ID:n ja tilan johon muutetaan
-Luo automaattisesti uuden objektin Changes-tauluun

PUT /sensors/{id}/block - Change Block:
-Muutetaan anturin lohkoa, vaatii anturin ID:n ja lohkon johon siirretään ID:n


CHANGES:
GET /changes/{id} - Get Changes:
-Haetaan anturin tilamuutokset anturin ID:n perusteella