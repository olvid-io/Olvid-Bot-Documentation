# 🔑 Keycloak

:::{warning}
Ce noeud est encore en phase de test et pourrait évoluer dans de futures mises à jour.

Nous sommes toujours preneurs de vos retours ou vos idées, vous pouvez nous contacter par mail: [bot@olvid.io](mailto:bot@olvid.io) ou ouvrir une issue sur [GitHub](https://github.com/olvid-io/n8n-nodes-olvid-keycloak/issues/new). 
:::

## Installation

Contrairement au noeud [](/n8n/olvid), ce noeud ne nécessite pas l'installation d'un daemon, facilitant grandement sa mise en place.

Cependant il requiert l'utilisation d'un annuaire Olvid dont la mise en place dépasse largement le cadre de ce document.
Rendez-vous 👉️ [ici](https://www.olvid.io/faq/olvid-management-console) 👈️ pour en apprendre plus sur cette fonctionnalité, ou contactez-nous pour en savoir plus: [contact@olvid.io](mailto:contact@olvid.io).

### Installation de N8N

Si vous souhaitez que vos flows envoient des messages Olvid nous vous conseillons de suivre [cette procédure](/n8n/olvid) d'installation et de revenir ensuite pour configurer le noeud Keycloak.
Sinon, vous pouvez suivre la [documentation officielle](https://docs.n8n.io/hosting/)

### Installation du noeud N8N

Une fois votre instance n8n installée et configurée, installez notre noeud communautaire [n8n-nodes-olvid-keycloak](https://www.npmjs.com/package/n8n-nodes-olvid-keycloak). 
La procédure est disponible dans la documentation n8n: [installer un noeud communautaire](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/) 

### Configuration des identifiants

1. Pour se connecter à votre annuaire votre noeud aura besoin d'un compte gestionnaire. Pour le créer rendez-vous dans votre console de gestion, dans l'onglet *Gestion du contrôle d'accès*.

```{figure} /_static/images/keycloak-access-control-menu.png
:alt: Access Control menu tab
:align: center
```

:::{hint}
Si l'option *Gestion du contrôle d'accès* n'est pas visible, vous n'avez pas configuré de royaume administrateur, la procédure de configuration est disponible [ici](https://olvid.io/keycloak/olvid-admin-realm/). 
:::

2.  **Cliquer** sur créer un nouveau gestionnaire.

```{figure} /_static/images/keycloak-create-new-manager-button.png
:alt: Create new manager button
:align: center
:width: 90%
```

3. **Remplir** le formulaire selon vos préférences. Les champs importants sont les champs `username` et `role`. Le role détermine les permissions accordées votre bot. 
```{figure} /_static/images/keycloak-create-new-manager-form.png
:alt: Create new manager form
:align: center
```

4. **Noter** le nom d'utilisateur utilisé et le mot de passe affiché.

5. Dans l'interface n8n, **créer** un nouveau workflow, et **ajoutez** n'importe un noeud *OlvidKeycloak*.
```{figure} /_static/images/n8n-keycloak-node.png
:alt: Olvid Keycloak node in n8n workflow
:align: center
```

6. **Choisir** l'action qui vous intéresse.
```{figure} /_static/images/n8n-keycloak-node-select-action.png
:alt: select action for Olvid Keycloak node
:align: center
```

7. **Configurer** de nouveaux credentials pour ce noeud.
```{figure} /_static/images/n8n-keycloak-node-credential.png
:alt: create new credentials for Olvid Keycloak node
:align: center
```

8. **Remplir** le formulaire. 

- *Keycloak URL*: l'URL d'accès à votre instance keycloak.  
⚠️ Pensez au suffixe `/auth/` si votre instance keycloak l'utilise
- *Admin Realm name*: le nom de votre royaume administrateur (le royaume rouge dans l'onglet *Configuration des domaines* de la console).
- *Client ID*: vous pouvez utiliser le client *admin-cli* présent par défaut, ou créer un nouveau client qui gère les *offline tokens* dans keycloak.qui gère les *offline tokens*.
- *Client Secret*: (optionnel) laissez vide par défaut, à remplir si vous avez créé votre propre client et que celui-ci le nécessite.
- *Username* et *Password*: les identifiants du compte créé un peu plus tôt.

```{figure} /_static/images/n8n-keycloak-node-credential-form.png
:alt: new credential form for Olvid Keycloak node
:align: center
```

9. Vous pouvez maintenant exécuter votre noeud *Keycloak Olvid* et l'intégrer dans vos workflows !

## Utilisation

### Exemples
Des idées de workflows sont disponibles dans notre section [](/n8n/examples).

### Actions personnalisées

Le noeud *OlvidKeycloak* n'implémente pas toutes les possibilités de la console Olvid, mais techniquement il peut faire n'importe quelle action réalisable dans la console *(si le rôle du compte associé le permet)*.

Pour étendre les capacités actuelles du noeud vous pouvez utiliser l'action **Custom Request** du noeud *Olvid Keyclak*.

Lorsque vous êtes dans votre console d'administration Olvid, ouvrez la console développeur de votre navigateur, à l'onglet Réseau. Réalisez l'action que vous souhaitez reproduire, et copier le contenu de la requête json au point d'entrée `configuration`.

Il vous suffit ensuite de coller cette requête dans le champ *payload* de l'action **Custom Request**. Vous pouvez ensuite l'exécuter, l'éditer et l'intégrer dans vos workflow à volonté.

```{figure} /_static/images/n8n-keycloak-node-custom-action.png
:alt: custom request for Olvid Keycloak node
:align: center
```

:::{info}
Si vous jugez qu'il manque des possibilités à ce noeud et qu'elles devraient être officiellement intégrées, vous pouvez nous contacter par mail: [bot@olvid.io](mailto:bot@olvid.io).
:::
