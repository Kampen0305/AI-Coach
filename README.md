# AI Coach voor Docenten

Dit eenvoudige Streamlit-project biedt docenten een AI coach die helpt bij het ontwerpen van lessen. De coach gebruikt **digitale didactiek** en houdt rekening met de **taxonomie van Bloom**.

## Installatie

1. Zorg dat Python 3.8 of hoger geïnstalleerd is.
2. Installeer de vereiste pakketten:
   ```bash
   pip install -r requirements.txt
   ```
3. Stel de omgevingvariabele `OPENROUTER_API_KEY` in met je API-sleutel voor OpenRouter.

## Starten van de applicatie

Voer het volgende commando uit:
```bash
streamlit run main.py
```

## Gebruik

- Vul het vakgebied, onderwijsniveau en je lesdoel in.
- De AI coach geeft advies dat is gekoppeld aan de niveaus van Bloom en suggereert digitale werkvormen.
- Je kunt het advies downloaden als PDF.

