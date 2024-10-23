# YOLOv8 Car Counter

## Introduction

This project implements an advanced **computer vision** solution for automatic vehicle counting from video streams. It uses the **YOLOv8** (You Only Look Once) object detection model to identify vehicles and the **SORT** (Simple Online and Realtime Tracking) algorithm to track detected objects across frames. The goal is to count vehicles crossing a predefined line in the image while maintaining high accuracy, even in dense and complex environments.

## Features

- **Real-time detection** of vehicles using **YOLOv8**.
- **Object tracking** with the **SORT** algorithm, enabling detection-to-detection association across frames.
- **Automatic counting** of vehicles crossing a virtual line in the video.
- **Enhanced accuracy** through advanced image processing techniques using **OpenCV** and **cvzone**.
- **Support for both live and pre-recorded videos**, offering flexibility for real-world applications like traffic monitoring.

## Prerequisites

- **Python 3.8+**
- **YOLOv8** and **SORT** for detection and tracking.
- **OpenCV** for image processing.
- **cvzone** to simplify working with OpenCV.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Car-Counter.git

2.Navigate to the project directory:
    ```bash
      cd Car-Counter
    ```

3.Install the required dependencies from requirements.txt:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Place the video you want to process in the project directory.

2. Run the main script to start the vehicle detection and counting process:
```bash
python Car_Counter.py --input <video_name.mp4>
```

3.The program will display real-time detections, vehicle tracking, and the total number of vehicles that have crossed the line.

## Project Structure
- Car_Counter.py: Main script handling vehicle detection, tracking, and counting.
- video_save_car_counter.py: Script for processing and saving annotated videos.
- sort.py: The SORT tracking algorithm for associating detections across frames.
- mask.png and graphics.png: Image files used for processing or display purposes.
- requirements.txt: List of required dependencies for the project.
  
## How It Works
- Detection: Each video frame is passed through the YOLOv8 model, which identifies vehicles and outputs bounding boxes.
- Tracking: Detected objects are tracked using SORT, assigning unique IDs to vehicles and linking detections across frames.
- Counting: When a vehicle crosses a predefined line in the image, it is counted. The position of this line can be adjusted based on the scene.

## Results and Performance
- Detection Accuracy: The project achieves high detection accuracy, optimized by using the YOLOv8 model.
- Robust Tracking: With SORT, the system tracks vehicles effectively even in dense scenes.
- Real-time Processing: The project can handle real-time video processing with minimal latency.


## Screenshot

The following images demonstrate the vehicle detection and counting process at various stages:

1. **Before Crossing the Line**:
   ![Before Crossing the Line](https://github.com/Gastunechi/YOLOV8_Car_Counter/blob/5bb3a47d6acd17dae398f36b6f83bd523427c206/frames/8eme%20voiture%20avant.jpg)
   This image shows the vehicle detection before crossing the predefined line.

2. **During Crossing the Line**:
   ![During Crossing the Line](https://github.com/Gastunechi/YOLOV8_Car_Counter/blob/5bb3a47d6acd17dae398f36b6f83bd523427c206/frames/8eme%20voiture%20pendant.jpg)
   Here, the vehicle is in the process of crossing the line, illustrating real-time tracking and detection.

3. **After Crossing the Line**:
   ![After Crossing the Line](https://github.com/Gastunechi/YOLOV8_Car_Counter/blob/5bb3a47d6acd17dae398f36b6f83bd523427c206/frames/8eme%20voiture%20apres.jpg)
   This image captures the moment after the vehicle has crossed the line, highlighting the successful count increment.

These screenshots provide a clear view of how the system tracks and counts each vehicle accurately, demonstrating the effectiveness of the YOLOv8 and SORT integration in a real-world traffic scenario.


## Contributions
Contributions are welcome. For any suggestions or improvements, please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


_____________________________________________________________________________________________________________________________________________________________________________________________________________


# Compteur de voitures YOLOv8

## Introduction

Ce projet met en oeuvre une solution avancée de **vision artificielle** pour le comptage automatique de véhicules à partir de flux vidéo. Il utilise le modèle de détection d'objets **YOLOv8** (You Only Look Once) pour identifier les véhicules et l'algorithme **SORT** (Simple Online and Realtime Tracking) pour suivre les objets détectés à travers les images. L'objectif est de compter les véhicules qui franchissent une ligne prédéfinie dans l'image tout en conservant une grande précision, même dans des environnements denses et complexes.

## Caractéristiques

- **Détection en temps réel** de véhicules à l'aide de **YOLOv8**.
- Suivi des objets** avec l'algorithme **SORT**, permettant l'association de détection à détection entre les images.
- Comptage automatique** des véhicules qui franchissent une ligne virtuelle dans la vidéo.
- Précision accrue** grâce à des techniques avancées de traitement d'images utilisant **OpenCV** et **cvzone**.
- Prise en charge des vidéos en direct et préenregistrées**, offrant une flexibilité pour les applications réelles telles que la surveillance du trafic.

## Prérequis

- **Python 3.8+**
- **YOLOv8** et **SORT** pour la détection et le suivi.
- **OpenCV** pour le traitement d'images.
- **cvzone** pour simplifier le travail avec OpenCV.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/your-username/Car-Counter.git

2. naviguez vers le répertoire du projet :
    ```bash
      cd Car-Counter
    ```

3. installez les dépendances requises à partir du fichier requirements.txt :
  ```bash
  pip install -r requirements.txt
  ```
   

## Utilisation
1. Placez la vidéo que vous souhaitez traiter dans le répertoire du projet.

2. Exécutez le script principal pour lancer le processus de détection et de comptage des véhicules :
```bash
python Car_Counter.py --input <nom_de_la_vidéo.mp4>
```

3. le programme affichera les détections en temps réel, le suivi des véhicules et le nombre total de véhicules qui ont franchi la ligne.

## Structure du projet
- Car_Counter.py : Script principal gérant la détection, le suivi et le comptage des véhicules.
- video_save_car_counter.py : Script de traitement et de sauvegarde des vidéos annotées.
- sort.py : L'algorithme de suivi SORT pour associer les détections entre les images.
- mask.png et graphics.png : Fichiers images utilisés à des fins de traitement ou d'affichage.
- requirements.txt : Liste des dépendances requises pour le projet.
  
## Fonctionnement
- Détection : Chaque image vidéo passe par le modèle YOLOv8, qui identifie les véhicules et produit des boîtes de délimitation.
- Suivi : Les objets détectés sont suivis à l'aide de SORT, qui attribue des identifiants uniques aux véhicules et relie les détections d'une image à l'autre.
- Comptage : Lorsqu'un véhicule traverse une ligne prédéfinie dans l'image, il est compté. La position de cette ligne peut être ajustée en fonction de la scène.

## Résultats et performances
- Précision de la détection : Le projet atteint une grande précision de détection, optimisée par l'utilisation du modèle YOLOv8.
- Suivi robuste : Avec SORT, le système suit efficacement les véhicules, même dans les scènes denses.
- Traitement en temps réel : Le projet peut traiter des vidéos en temps réel avec une latence minimale.


## Capture d'écran

Les images suivantes illustrent le processus de détection et de comptage des véhicules à différentes étapes :

1. **Avant de franchir la ligne** :
   ![Avant de franchir la ligne](https://github.com/Gastunechi/YOLOV8_Car_Counter/blob/5bb3a47d6acd17dae398f36b6f83bd523427c206/frames/8eme%20voiture%20avant.jpg)
   Cette image montre la détection du véhicule avant le franchissement de la ligne prédéfinie.

2. **Pendant le franchissement de la ligne** :
   ![Pendant le franchissement de la ligne](https://github.com/Gastunechi/YOLOV8_Car_Counter/blob/5bb3a47d6acd17dae398f36b6f83bd523427c206/frames/8eme%20voiture%20pendant.jpg)
   Ici, le véhicule est en train de franchir la ligne, ce qui illustre le suivi et la détection en temps réel.

3. **Après avoir franchi la ligne** :
   ![Après avoir franchi la ligne](https://github.com/Gastunechi/YOLOV8_Car_Counter/blob/5bb3a47d6acd17dae398f36b6f83bd523427c206/frames/8eme%20voiture%20apres.jpg)
   Cette image capture le moment où le véhicule a franchi la ligne, mettant en évidence l'incrémentation réussie du compte.

Ces captures d'écran montrent clairement comment le système suit et compte chaque véhicule avec précision, démontrant ainsi l'efficacité de l'intégration de YOLOv8 et de SORT dans un scénario de trafic réel.


## Contributions
Les contributions sont les bienvenues. Pour toute suggestion ou amélioration, veuillez ouvrir un problème ou soumettre une demande de téléchargement sur GitHub.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.



