# Mini projet MLOps - Exercice 1

Ce projet implemente un pipeline MLOps simple avec :
- entrainement d'un modele scikit-learn
- exposition via une API FastAPI
- conteneurisation Docker
- pipeline CI GitHub Actions

## Dataset choisi

Le dataset utilise est **Iris** (inclus dans scikit-learn).

## 1) Entrainement du modele

Script : `train.py`

Il :
- charge le dataset Iris
- applique un pretraitement (`StandardScaler`)
- entraine un classifieur (`LogisticRegression`)
- calcule l'accuracy
- sauvegarde :
  - `model.pkl`
  - `metrics.json`

Commande :

```bash
python train.py
```

## 2) API de prediction

Fichier : `app.py`

Endpoints :
- `GET /health`
- `POST /predict`

Lancer l'API :

```bash
uvicorn app:app --reload
```

Exemple de requete prediction :

```bash
curl -X POST "http://127.0.0.1:8000/predict" ^
  -H "Content-Type: application/json" ^
  -d "{\"sepal_length\":5.1,\"sepal_width\":3.5,\"petal_length\":1.4,\"petal_width\":0.2}"
```

## 3) Docker

Build :

```bash
docker build -t mini-projet-mlops .
```

Run :

```bash
docker run -p 8000:8000 mini-projet-mlops
```

Docker Compose :

```bash
docker compose up --build
```

Le service lance d'abord `python train.py`, puis demarre l'API sur `http://localhost:8000`.

## 4) CI GitHub Actions

Workflow : `.github/workflows/ci.yml`

Regles :
- push sur `feature/*` : install dependencies + train model
- push sur `develop` : install dependencies + train + docker build + push image GHCR

Image poussee vers :
- `ghcr.io/<owner-lowercase>/mini-projet-mlops:latest`
- `ghcr.io/<owner-lowercase>/mini-projet-mlops:<sha>`

## Elements pour le rapport PDF

Inclure :
- nom et prenom
- dataset choisi : Iris
- URL du depot Git
- capture d'ecran pipeline sur `feature/*`
- capture d'ecran pipeline sur `develop` avec train + build + publication
