# Animals Project

## Übersicht
Dieses Projekt ermöglicht es, Informationen über verschiedene Tiere von der API Ninja Animals API abzurufen und in einer übersichtlichen HTML-Seite darzustellen. Benutzer können den Namen eines Tieres eingeben, und das Projekt generiert eine Webseite mit Details wie Ernährung, Lebensraum und Tierart.

## Features
- Fetch von Tierdaten über die API Ninja Animals API
- Benutzerdefinierte Eingabe für Tiernamen
- Dynamische HTML-Generierung mit ansprechendem Layout
- Fehlerbehandlung für nicht vorhandene Tiere
- Umgebungsvariablen zur sicheren Speicherung des API-Keys

## Installation

1. Repository klonen
   git clone https://github.com/AnasSardarzai/animals_project.git
   cd animals_project

markdown
Code kopieren

2. Python-Abhängigkeiten installieren
   pip install requests python-dotenv

markdown
Code kopieren

3. API-Key konfigurieren
- Erstelle eine `.env` Datei im Projektordner:
  API_KEY='DEIN_API_KEY_HIER'

markdown
Code kopieren

## Nutzung

1. Script ausführen:
   python animals_web_generator.py

markdown
Code kopieren

2. Eingabeaufforderung:
   Please enter an animal:

markdown
Code kopieren
- Gib den Namen des gewünschten Tieres ein, z. B. `Lion` oder `Fox`.

3. Ergebnis:
- Eine HTML-Datei `animals.html` wird im Projektordner erstellt.
- Öffne die Datei in einem Browser, um die Tierinformationen anzuzeigen.

## Projektstruktur

animals_project/
│
├─ animals_web_generator.py
├─ data_fetcher.py
├─ animals_template.html
├─ .env
├─ .gitignore

markdown
Code kopieren

## Hinweise
- Die `.env` Datei **darf nicht ins Git-Repository** hochgeladen werden.
- Wenn ein Tiername nicht existiert, zeigt die Webseite eine freundliche Fehlermeldung an.
- Das Projekt kann lokal weiterentwickelt oder in Codio genutzt werden.

## Lizenz
Dieses Projekt ist frei verfügbar und kann für Lern- und Übungszwecke genutzt werden.






Du:
gib mir die datei bitte


ChatGPT:
Hier ist die vollständige README.md-Datei als reiner Text, die du direkt speichern kannst:

markdown
Code kopieren
# Animals Project

## Übersicht
Dieses Projekt ermöglicht es, Informationen über verschiedene Tiere von der API Ninja Animals API abzurufen und in einer übersichtlichen HTML-Seite darzustellen. Benutzer können den Namen eines Tieres eingeben, und das Projekt generiert eine Webseite mit Details wie Ernährung, Lebensraum und Tierart.

## Features
- Fetch von Tierdaten über die API Ninja Animals API
- Benutzerdefinierte Eingabe für Tiernamen
- Dynamische HTML-Generierung mit ansprechendem Layout
- Fehlerbehandlung für nicht vorhandene Tiere
- Umgebungsvariablen zur sicheren Speicherung des API-Keys

## Installation

1. Repository klonen
```bash
git clone https://github.com/AnasSardarzai/animals_project.git
cd animals_project
Python-Abhängigkeiten installieren

bash
Code kopieren
pip install requests python-dotenv
API-Key konfigurieren

Erstelle eine .env Datei im Projektordner:

text
Code kopieren
API_KEY='DEIN_API_KEY_HIER'
Nutzung
Script ausführen:

bash
Code kopieren
python animals_web_generator.py
Eingabeaufforderung:

text
Code kopieren
Please enter an animal:
Gib den Namen des gewünschten Tieres ein, z. B. Lion oder Fox.

Ergebnis:

Eine HTML-Datei animals.html wird im Projektordner erstellt.

Öffne die Datei in einem Browser, um die Tierinformationen anzuzeigen.

Projektstruktur
bash
Code kopieren
animals_project/
│
├─ animals_web_generator.py
├─ data_fetcher.py
├─ animals_template.html
├─ .env
├─ .gitignore
Hinweise
Die .env Datei darf nicht ins Git-Repository hochgeladen werden.

Wenn ein Tiername nicht existiert, zeigt die Webseite eine freundliche Fehlermeldung an.

Das Projekt kann lokal weiterentwickelt oder in Codio genutzt werden.

Lizenz
Dieses Projekt ist frei verfügbar und kann für Lern- und Übungszwecke genutzt werden.

bash
Code kopieren

Du kannst den Text einfach in eine Datei **`README.md`** im Projektordner kopieren.  

Wenn du willst, kann ich dir auch noch eine **kompakte Version für Codio-Kurse** schreiben, die nur das Nötigste enthält. Willst du, dass ich das mache?