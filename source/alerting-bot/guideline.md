# 📋 Guide d'utilisation

## Créer votre première alerte

Cliquez sur **+ Nouvelle alerte** dans la barre latérale ou en haut de la page des alertes. L'assistant vous guide en quatre
étapes :

1. **Général.** Donnez un titre et une description à l'alerte. Choisissez une **Source** :
   *Data Polling*, *Monitoring* ou *Webhook*.
2. **Déclencheur.** Configurez la source :
    - **Polling** → URL à interroger, format de réponse (JSON / XML / HTML), planification
      cron.
    - **Monitoring** → URL à sonder, planification cron.
    - **Webhook** → Rien à configurer ; l'application génère une URL entrante
      et affiche un bouton pour la copier une fois l'alerte enregistrée.

   L'assistant récupère un exemple de réponse en direct afin que vous puissiez voir la structure
   sur laquelle vous allez écrire vos règles.

3. **Condition.** Décrivez *quand l'alerte doit se déclencher*. Les alertes Webhook
   sautent cette étape : chaque requête POST entrante est considérée comme un déclenchement,
   il n'y a donc aucune condition à définir.

    - **Polling** : Cliquez sur n'importe quelle valeur de l'arbre de la réponse pour insérer
      son chemin (ex. `root.data.item.price`) dans une règle. Une règle est composée d'un
      chemin et d'un opérateur de comparaison (`>`, `<`, `==`, `contains`,
      `changed`, …). Vous pouvez ajouter plusieurs règles et les combiner :
        - **Tous** (ET) : toutes les règles doivent être vérifiées.
        - **Au moins un** (OU) : une seule règle vérifiée suffit.
        - **Somme / Moyenne / Minimum / Maximum** — agrège les valeurs numériques
          de tous les chemins correspondants en un seul nombre, puis le compare
          au seuil (se déclenche par exemple quand la *somme* > 100).

      **Jokers.** Les chemins contenant un **double point (`..`)** correspondent à
      zéro ou plusieurs segments, ce qui permet à une seule règle de couvrir toute une structure :
        - `root.items..price` → chaque `price` n'importe où sous `items`, quels
          que soient la profondeur ou l'index.
        - `..error` → chaque champ `error`, où qu'il apparaisse dans la
          réponse.
        - `sensors..[0].value` → la première `value` de chaque capteur.

      Lors de l'évaluation, une règle avec joker produit un verdict pour chaque
      correspondance concrète.

    - **Monitoring** : règle de correspondance sur le code de statut : codes spécifiques
      (`404, 500`), une plage (`2xx` / `3xx` / `4xx` / `5xx`), ou le raccourci *Tout non-2xx* (tout code hors 2xx). 
      L'option **Pas de réponse HTTP** déclenche l'alerte si le serveur n'a pas répondu.

    - Le **mode de déclenchement** détermine comment l'alerte se redéclenche lorsque la condition
      reste vraie :
        - **À chaque fois** → se déclenche à chaque interrogation tant que la condition est remplie.
        - **Une fois** → se déclenche uniquement lorsque la condition passe de fausse à vraie.
        - **Une fois + à la récupération** → se déclenche une fois quand la condition devient vraie, puis à nouveau lorsqu'elle
          redevient fausse (le message de rétablissement est préfixé par `✓ RECOVERED:`).

4. **Bundles.** Un **bundle** représente un groupe de discussions ainsi que le modèle
   de formatage qui sera appliqué au message de l'alerte. Une alerte peut avoir plusieurs bundles : pratique lorsque différentes
   équipes souhaitent recevoir la même alerte formulée différemment. Pour chaque bundle :
    - Choisissez un **canal** (Olvid ou mail), et ajoutez des destinataires.
        - Olvid → contacts *et groupes* issus de la liste des discussions du démon.
          Les discussions déjà connues du démon apparaissent automatiquement dans le sélecteur ;
          en ajouter une nouvelle se fait en un clic.
        - Email → n'importe quelle adresse saisie.
    - Choisissez un **format** : un résumé simple, la réponse brute, ou un modèle de script
      personnalisé. Les formats personnalisés ouvrent un **éditeur plein écran** avec un script (en haut à gauche),
      l'arbre de la réponse (en bas à gauche, cliquez pour insérer des chemins), et un
      aperçu en direct (à droite).

## Tester une alerte avant sa mise en service

Une fois enregistrées, les alertes Monitoring et Polling disposent d'un bouton **Tester l'alerte** dans le panneau de visualisation. Il exécute
l'ensemble du traitement (récupération → analyse → évaluation → rendu des bundles) *sans
envoyer de messages*, et ouvre une fenêtre de résultat indiquant ce qui s'est déclenché, pourquoi, et à quoi
aurait ressemblé chaque bundle. Idéal pour ajuster votre condition ou votre
modèle Handlebars sans inonder vos contacts Olvid.

## Lire le journal d'envoi

Une fois l'alerte active, un panneau de journal se met à jour à chaque exécution planifiée ou déclenchement entrant.
Les lignes sont colorées :

| Libellé     | Signification                                                                                                |
| ----------- | ------------------------------------------------------------------------------------------------------------ |
| **Envoyé**  | Tous les canaux de tous les bundles ont été délivrés.                                                        |
| **Partiel** | Certains canaux ont été délivrés, d'autres ont échoué. Dépliez pour voir le détail par canal.                |
| **Échec**   | Tous les canaux ont échoué, ou l'exécution s'est interrompue avant l'envoi (erreur de récupération/analyse). |

## Gestion des utilisateurs et de l'authentification

### Rôles

Toute personne disposant d'un compte peut effectuer les tâches courantes : consulter, créer, modifier,
tester et supprimer des alertes ainsi que leurs bundles. Le rôle ne conditionne que l'accès à
la **gestion des utilisateurs** :

- **User** — accès complet aux alertes : parcourir la liste, en créer de nouvelles, modifier
  les déclencheurs / conditions / bundles, lancer des tests, consulter les journaux d'envoi, et supprimer
  les alertes devenues inutiles. N'a pas accès à `/users`.
- **Admin** — tout ce que peut faire un utilisateur, plus la page `/users` : inviter de nouvelles
  personnes par n'importe quel canal, lister les utilisateurs existants, et supprimer des comptes.

Un administrateur ne peut pas supprimer son propre compte, ni celui du dernier administrateur restant :
ces boutons sont désactivés et affichent une infobulle explicative.

### Inviter des utilisateurs

Depuis `/users`, cliquez sur **Inviter un utilisateur**. Choisissez un canal d'envoi :

- **Mail** : envoie un mail d'invitation contenant un lien en un clic. Nécessite
  que le serveur SMTP soit configuré et une adresse mail pour la personne invitée.
- **Olvid** : envoie le même lien en message privé sur Olvid. Nécessite que le bot ait déjà
  une discussion de contact avec la personne invitée (celle-ci a ajouté le
  bot depuis son téléphone). Les discussions de groupe sont exclues ici : les invitations
  d'utilisateurs sont toujours envoyées **uniquement à des contacts** (l'envoi des bundles n'a pas
  cette restriction).
- **Lien partageable** : aucun envoi. La fenêtre affiche l'URL pour que vous puissiez
  la transmettre par un autre moyen.

Saisissez ensuite son identifiant, son nom d'affichage (facultatif) et son contact Olvid (si l'envoi se fait par Olvid).

Vous pouvez inviter un *utilisateur* ou un *administrateur* en basculant le
sélecteur de rôle dans la fenêtre d'invitation.

### Accepter une invitation
En cliquant sur un lien d'invitation, le nouvel utilisateur doit choisir au moins une des
méthodes d'authentification suivantes :
- **Authentification Olvid** : Cette méthode nécessite uniquement un identifiant et une discussion
  Olvid associée. Lors d'une demande de connexion, un message est envoyé dans votre discussion Olvid.
  Vous pouvez autoriser la connexion en ajoutant une réaction au message, sans avoir besoin
  de mot de passe. Cette méthode n'est disponible que si le lien d'invitation a été envoyé via Olvid.
- **Mot de passe** : Choisissez un mot de passe (au moins 8 caractères) pour vous connecter.

Les deux méthodes peuvent être activées simultanément. Vous pourrez alors choisir l'une ou l'autre à chaque
connexion.

### Réinitialiser le mot de passe
Un utilisateur peut demander une réinitialisation de son mot de passe, soit par mail, soit par Olvid.
Ce dernier recevra un lien afin de choisir un nouveau mot de passe.


### Supprimer un utilisateur

Depuis la ligne de l'utilisateur, cliquez sur **Supprimer** et confirmez. Si l'utilisateur était encore
*en attente* (n'a jamais accepté son invitation) et que l'invitation a été envoyée via Olvid,
le bot supprime le message d'invitation de la discussion de la personne invitée avant de supprimer
la ligne. Cela évite de laisser traîner des liens actifs ou des invitations envoyées par erreur.
