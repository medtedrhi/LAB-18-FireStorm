# LAB-18-FireStorm

Étape 1 : Préparation de l'environnement

Installer l'application cible (APK) sur l'émulateur ou l'appareil physique via la commande adb install.

Vérifier que le serveur d'instrumentation Frida est bien actif en utilisant :
frida-ps -U

<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/21055c98-87aa-4097-9e09-2baa09755580" />

Étape 2 : Analyse statique avec Jadx

Ouvrir et décompiler l'APK dans Jadx-GUI pour inspecter le code source

<img width="1488" height="835" alt="image" src="https://github.com/user-attachments/assets/4ce47e38-c5f4-4e1f-bb4a-6608ec26ffad" />

Étape 3 : Instrumentation dynamique avec Frida

Créer et exécuter un script JavaScript avec Frida pour interagir avec l'application en cours d'exécution.

<img width="1108" height="760" alt="image" src="https://github.com/user-attachments/assets/90126004-472b-47ed-a4f4-b9eef5d51437" />

Hooker l'application pour forcer l'exécution manuelle de la méthode cachée Password() et récupérer le mot de passe généré dans la console.

command utilisé :
frida -U -f com.pwnsec.firestorm -l frida_firestorm.js

<img width="1231" height="448" alt="image" src="https://github.com/user-attachments/assets/849f8269-82b4-4662-b250-358a87a15ee7" />

Étape 4 : Extraction de la configuration Firebase

Inspecter le fichier res/values/strings.xml depuis Jadx.

<img width="1369" height="391" alt="image" src="https://github.com/user-attachments/assets/593e7558-10bd-4fdf-aff1-30e09dc339be" />

Étape 5 : Exploitation et récupération du flag (Python)

Créer un script Python en utilisant la bibliothèque pyrebase.

<img width="1126" height="1040" alt="image" src="https://github.com/user-attachments/assets/e322cb6b-662d-4276-ace7-3e25c1cd6129" />

Utiliser les informations de configuration extraites et le mot de passe dynamique obtenu avec Frida pour s'authentifier sur Firebase et extraire le flag final.

<img width="1472" height="756" alt="image" src="https://github.com/user-attachments/assets/23091c06-9797-4fee-a454-c1798465510b" />


