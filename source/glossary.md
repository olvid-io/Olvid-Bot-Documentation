# 📒 Lexique

Dans cette documentation, nous utilisons des termes qui sont spécifiques à Olvid et qui peuvent porter à confusion.
Ce lexique a donc pour but de définir ces termes et de servir de pense-bête tout au long de votre lecture.

:::{glossary}
Daemon
    Une application Olvid indépendante exposant un serveur gRPC afin de le rendre pilotable par un ou plusieurs clients.
    On peut le voir comme une API Olvid mais qui serait hébergée par vos soins.

Bot
    Un programme client qui interagit avec un daemon.
    C'est un terme générique que nous utilisons même lorsque qu'il ne s'agit pas à proprement parler d'un ChatBot.

CLI (Command-Line Interface)
    Une interface en ligne de commande qui permet d'interagir avec un daemon en utilisant des commandes textuelles.
    Elle peut interagir avec la totalité de l'API du daemon à des fins de tests et de débogage.
    Elle est aujourd'hui nécessaire pour l'initialisation d'un daemon.

Identité
    Une identité cryptographique Olvid hébergée sur un daemon. L'équivalent d'un profil sur une application Olvid.
    Elle contient également les données affichées chez vos contacts (nom, prénom, photo, ...).

Clé client
    Une clé utilisée pour s'authentifier auprès d'un daemon.
    Une clé client non-administrateur est toujours associée à une identité hébergée sur ce daemon et ne donne accès qu'aux ressources de cette identité.

Clé d'API
    Une clé fournie par Olvid qui permet de débloquer des fonctionnalités premium.

Plugin Keycloak
    Une fonctionnalité professionnelle d'Olvid qui permet aux membres de votre entreprise d'entrer en contact en un clic, de créer des groupes, ...
    Plus d'informations ici : https://olvid.io/entreprise
:::
