# Installation
`python -m venv .venv`

## Activation de l'environnement virtuel
### Windows
-  `.venv\Scripts\Activate.ps1`


windows /MacOs-Linux
-  `.venv/Scripts/activate.ps1`
-  `source .venv/source/activate`

## installation des bibliothèques
- `pip install fastapi uvicorn loguru pydantic requests streamlit`
- `pip freeze > requirements.txt`

ou directement : 
- `pip install -r requierements.txt`


## https://fastapi.tiangolo.com/

## run server uvicorn :
- `(uvicorn main:app --host 127.0.0.1 --port 8000 --reload`

## Afficher la doc : 
- `http://127.0.0.1:8000/docs`


## lancer le client streamlit:
`streamlit run ./pages/0_requests.py`

=> https://github.com/gcortier/fast_api