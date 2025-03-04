# {fas}`terminal` CLI

```{toctree}
:maxdepth: 2
:hidden:

🛠️ Installation<self>
usage
troubleshooting
references
```

Il existe plusieurs manières d'installer et de lancer la CLI Olvid. La première (recommandée) est celle utilisée dans notre page [](/index).
Mais il existe d'autres possibilités !

:::{note}
Pour exécuter la CLI en dehors de la configuration Docker Compose du daemon, il est nécessaire que celui-ci daemon expose son port 50051.
Pensez à vérifier que le service `daemon` de votre fichier `docker-compose.yaml` contient les lignes suivantes.
```yaml
  ports:
  - 50051:50051
```
:::

Pour permettre à la CLI de se connecter au daemon, il vous faudra récupérer la clé administrateur de votre daemon.
Elle se trouve normalement dans l'environnement de votre daemon. Vous pouvez vérifier sa valeur dans le fichier `docker-compose.yaml` à la section environnement du daemon.
Il s'agit de la valeur d'une variable d'environnement qui commence par **OLVID_ADMIN_CLIENT_KEY**.  
Pour plus de détails sur les clés d'administration du daemon [rendez-vous ici](/daemon/options.md#clés-client-administrateur).

::::{tab-set}
:sync-group: cli

:::{tab-item} Python
:sync: python

**Installation**
```shell
pip3 install olvid-bot
```
:::

:::{tab-item} Docker
:sync: docker

**Installation**
```{code-block}} shell
  :substitution:
docker pull olvid/bot-python-runner:{{docker_version}}
```
:::

::::

::::{tab-set}
:sync-group: cli

:::{tab-item} Python
:sync: python
**Configuration**
```shell
export OLVID_ADMIN_CLIENT_KEY=adminClientKey
export OLVID_DAEMON_TARGET=localhost:50051
```

**ou**

```shell
echo OLVID_ADMIN_CLIENT_KEY=adminClientKey >> .env
echo OLVID_DAEMON_TARGET=localhost:50051 >> .env
```

**Lancement**
```shell
python3 -m olvid-bot
# ou si votre PATH est correctement configuré
olvid-cli
```

:::

:::{tab-item} Docker
:sync: docker

**Lancement**
```{code-block} shell
  :substitution:
docker run --rm -it \
  -e OLVID_ADMIN_CLIENT_KEY=adminClientKey \
  -e OLVID_DAEMON_TARGET=localhost:50051 \
  olvid/bot-python-runner:{{docker_version}}
```
:::
::::

Vous devriez maintenant voir un prompt constitué d'un nombre et du caractère **>**. Si ce n'est pas le cas, rendez-vous sur notre page [](/cli/troubleshooting).
Sinon, vous pouvez continuer avec notre page [](/cli/usage) pour comprendre le fonctionnement de l'outil.
