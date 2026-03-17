# 🟥 N8N

```{toctree}
:maxdepth: 2
:hidden:

🛠️ Installation<self>
```

## Installation

### Installation d'un daemon et d'une instance N8N

Dans cette partie vous allez déployer un daemon Olvid et une instance N8N à l'aide de docker et docker-compose.

:::{note}
   Si vous souhaitez utiliser une instance de daemon ou de N8N déjà déployée, vous pouvez ne déployer qu'une partie des services suivants. Il vous faudra seulement remplir correctement les champs `OlvidClient Key` et `Daemon Endoint` au moment de la création des credentials N8N. 
:::

1. Pour commencer, **créer** un nouveau dossier pour votre projet. Ce sera votre répertoire courant pour la suite.
   
   ```shell
   mkdir olvid-n8n
   cd olvid-n8n
   ```

2. Il vous faudra ensuite **générer** une clé client administrateur. Vous pouvez utiliser les commandes `uuidgen` ou `openssl` en fonction de votre configuration. Il faudra stocker le résultat dans un fichier `.env`.

   ```shell
   echo "OLVID_ADMIN_KEY=$(uuidgen)" >> .env
   ```
   **OU**
   ```shell
   echo "OLVID_ADMIN_KEY=$(openssl rand -hex 32)" >> .env
   ```

3. Vous pouvez maintenant créer un fichier `docker-compose.yaml` avec le contenu suivant.

  ```{code-block} yaml
  :substitutions:

   x-logging: &default-logging
     logging:
       driver: "json-file"
       options:
         max-size: "1m"
         max-file: "100"

   services:
     daemon:
       image: olvid/bot-daemon:{{docker_version}}
       environment:
         - OLVID_ADMIN_CLIENT_KEY_CLI=${OLVID_ADMIN_KEY}
       restart: unless-stopped
       volumes:
         - ./data:/daemon/data
         - ./backups:/daemon/backups
       <<: *default-logging

     cli:
       image: olvid/bot-python-runner:{{docker_version}}
       environment:
         - OLVID_ADMIN_CLIENT_KEY=${OLVID_ADMIN_KEY}
         - OLVID_DAEMON_URL=http://daemon:50051
       stdin_open: true
       tty: true
       entrypoint: "olvid-cli"
       volumes:
         - ./photos:/photos
       depends_on:
         - daemon
       # We use a profile cause cli only need to start on user initiative
       profiles:
         - "cli"
       <<: *default-logging

     n8n:
       image: docker.n8n.io/n8nio/n8n
       restart: always
       ports:
         - "5678:5678"
       environment:
         - N8N_DIAGNOSTICS_ENABLED=false
         - N8N_PUBLIC_API_DISABLED=true
         - N8N_PUBLIC_API_SWAGGERUI_DISABLED=true
         - NODES_EXCLUDE=["n8n-nodes-base.executeCommand","n8n-nodes-base.readWriteFile"]
         - N8N_REINSTALL_MISSING_PACKAGES=true
         - WEBHOOK_URL=
       volumes:
         - ./n8n_data:/home/node/.n8n
       entrypoint: sh -c "npm install @olvid/bot-node@0.0.15-alpha && tini -- /docker-entrypoint.sh" #* You can update the version of bot-node here
   ```

4. **Créer** les conteneurs avec la commande suivante.

   ```shell
   docker compose up -d daemon n8n
   ```

### Installer les noeuds Olvid dans N8N

Vous avez lancé un daemon Olvid et une instance N8N qui tournent en fond, il faut maintenant configurer N8N et installer les noeuds Olvid communautaires.  

1. **Ouvrir** la page `http://localhost:5678` dans votre navigateur pour accéder à votre instance N8N.
2. **Créer** un compte N8N (il s'agit d'un compte local).
 
3. **Rendez-vous** sur la page de paramètres
   ```{image} /_static/images/n8n-settings.png
   :alt: Settings button in N8N homepage
   :align: center
   ```

4. **Cliquer** sur `Community Nodes` puis **cliquer** sur `Install a community node`.

   ```{image} /_static/images/n8n-community-nodes-page.png
   :alt: Community Nodes page in N8N
   :align: center
   ```

5. **Entrer** `n8n-nodes-olvid` à la place de _npm Package Name_, prendre le temps de considérer les risques d'installer un noeud communautaire avant de **cocher** la case et **cliquer** sur `Install`.

   ```{image} /_static/images/n8n-install-olvid-node.png
   :alt: Installing Olvid node in N8N
   :align: center
   :width: 50%
   ```

6. **Retourner** sur la page principale pour **créer** votre premier workflow.

Le noeud Olvid devrait maintenant être disponible dans vos workflows.

```{image} /_static/images/n8n-workflow-olvid-page.png
:alt: Olvid node available in a N8N workflow
:align: center
:width: 90%
```

### Configurer le noeud Olvid

Maintenant que vous avez installé le noeud Olvid, avant de l'utiliser, il vous faut créer des **credentials** pour qu'il puisse communiquer avec votre daemon.  

1. Ouvrez ou créez un workflow, et ajoutez-y un un noeud Olvid.

2. Vous pouvez **choisir** indépendamment une action ou un trigger.

   ```{image} /_static/images/n8n-select-trigger.png
   :alt: Trigger selection of Olvid node in N8N
   :align: center
   :width: 50%
   ```

3. **Ouvrez** votre noeud et créez les credentials en **cliquant** sur `Select Credential`.

   ```{image} /_static/images/n8n-olvid-credentials.png
   :alt: Olvid credentials setup in N8N
   :align: center
   :width: 50%
   ```

4. Il vous faut maintenant créer une clé client Olvid pour autoriser votre noeud à communiquer avec le daemon Olvid. Pour cela vous pouvez utiliser les commandes suivantes dans un terminal, dans le dossier contenant votre fichier `docker-compose.yaml`.

   *Prototype: identity new FirstName LastName Position Company*
   ```shell
   docker compose run --rm cli identity new Totoro
   ```

   Cette commande retournera un entier qui est l'identifiant de l'identité que vous venez de créer. Pour les prochaines commandes on considérera que cet identifiant est 1.   

5. Il faut maintenant créer une clé d'API pour cette nouvelle identité à l'aide de la commande suivante.

    *Prototype: key new KeyName IdentityId*
   ```shell
   docker compose run --rm cli key new totoro-n8n-key 1
   ```

   Cette commande renvoi une clé de la forme: `AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE`.

   **Copiez** cette clé et **collez** là dans le champ `OlvidClient Key` de votre modal de création de Credential dans N8N.

6. **Saisissez** ensuite la valeur du champ `Daemon Endpoint` pour mettre `http://daemon:50051` (si n8n a été créé dans le même fichier docker-compose.yaml, sinon saisir l'URL qui permet d'atteindre votre daemon).

7. Vous pouvez maintenant sauvegarder vos credentials avec le bouton **Save**.

**Félicitation 🎉!**

Vous pouvez maintenant utiliser les noeuds Olvid dans vos workflow ! 
