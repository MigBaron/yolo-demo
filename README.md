# Application de Détection d'Objets YOLO (Raspberry Pi)

Ce projet est une application web de démonstration de vision par ordinateur (Computer Vision). Elle exécute un modèle YOLO pour la détection d'objets en temps réel, accessible via une interface web Flask.

L'application est conçue pour être légère et conteneurisée, facilitant son déploiement sur des systèmes embarqués comme le Raspberry Pi.

![Status](https://img.shields.io/badge/Status-Fonctionnel-green)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Python](https://img.shields.io/badge/Backend-Flask-lightgrey)

## Fonctionnalités

* **Détection d'objets :** Utilisation de l'algorithme YOLO (You Only Look Once) pour identifier des objets dans un flux vidéo ou sur des images.
* **Interface Web :** Visualisation des résultats via un navigateur web (basé sur Flask).
* **Conteneurisation :** Environnement isolé et reproductible grâce à Docker et Docker Compose.
* **Architecture Edge :** Optimisé pour tourner sur des architectures ARM (Raspberry Pi 4/5) ou NVIDIA Jetson.

## Structure du projet

* `src/app/` : Code source de l'application Flask et logique de détection.
* `Dockerfile` : Configuration de l'image Docker (dépendances système et Python).
* `docker-compose.yaml` : Orchestration du service pour un lancement simplifié.
* `requirements.txt` : Liste des librairies Python nécessaires.

## Prérequis

* Raspberry Pi (ou autre environnement Linux) avec Docker et Docker Compose installés.
* Caméra connectée (USB ou module CSI) si l'application utilise un flux vidéo en direct.

## Installation et Démarrage

L'utilisation de Docker Compose automatise l'installation des dépendances et le lancement.

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/votre-username/nom-du-repo.git](https://github.com/votre-username/nom-du-repo.git)
    cd nom-du-repo
    ```

2.  **Construire et lancer le conteneur :**
    Cette commande va télécharger l'image de base, installer les librairies listées dans `requirements.txt` et démarrer le serveur.
    ```bash
    docker-compose up --build -d
    ```

3.  **Accéder à l'application :**
    Ouvrez votre navigateur web et accédez à l'adresse IP du Raspberry Pi sur le port configuré (par défaut 5000) :
    `http://<IP_DU_RASPBERRY>:5000`

## Arrêt de l'application

Pour arrêter le conteneur :
```bash
docker-compose down
