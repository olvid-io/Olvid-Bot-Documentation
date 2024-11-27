# 🐍 Client Python

```{toctree}
:maxdepth: 2
:hidden:

🛠️ Installation<self>
tutorials
examples
troubleshooting
```

:::{admonition} Pré-requis
:class: note

Si vous n'avez pas installé de {term}`daemon`, merci de suivre la section [](/index).

Avant de commencer, vérifiez bien que vous avez une instance du daemon Olvid qui tourne, avec
une {term}`identité` créée dessus, et une {term}`clé client` valide pour vous connecter en utilisant cette identité.

Si vous souhaitez vérifier que votre daemon est fonctionnel et/ou récupérer une clé client perdue, utilisez la commande : `docker compose run --rm cli key get`
:::

## Installation
Nous avons développé une librairie Python qui permet d'interagir facilement avec votre daemon.
Elle est disponible à l'installation avec la commande `pip`.

```shell
pip3 install olvid-bot
```

:::{tip}
Le module `olvid-bot` nécessite une version de Python supérieure ou égale à 3.10.
Sur Mac OS, nous vous conseillons d'utiliser HomeBrew pour installer une version plus récente.
```shell
brew install python3
```
:::

## Configuration
Pour vous connecter au daemon, votre programme a besoin d'une clé client. 
Cette clé peut être passée à votre programme en utilisant soit une variable d'environnement, soit un fichier *.env*.

:::{dropdown} {octicon}`command-palette;1em` Fichier *.env*
  :open:

Créez un fichier *.env* en utilisant la commande suivante. 
Rappelez-vous que ce fichier doit être dans le répertoire courant lorsque vous lancez votre programme.

```shell
echo OLVID_CLIENT_KEY=ReplaceWithYourClientKey > .env
```
:::

:::{dropdown} {octicon}`command-palette;1em` Variable d'environnement
Il est également possible d'exporter votre clé en tant que variable d'environnement. 
Dans ce cas, il faut penser à l'exporter à chaque nouvelle session shell.

```shell
export OLVID_CLIENT_KEY=ReplaceWithYourClientKey
```
:::

## Premier programme
Afin de vérifier que tout fonctionne correctement, vous pouvez copier/coller ce programme dans un fichier `main.py`.

```python
import asyncio
from olvid import OlvidClient

async def main():
    client = OlvidClient()
    print((await client.identity_get()).display_name)

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

Vous pouvez ensuite l'exécuter à l'aide de l'interpréteur Python.
```shell
python3 main.py
```

Si tout a bien été configuré, vous devriez voir s'afficher le nom d'usage de l'identité que vous avez créée sur le daemon.

Si c'est le cas, vous pouvez continuer avec notre section [](/python/tutorials) pour apprendre à utiliser notre librairie Python ou dans la section [](/python/examples) pour déployer des projets clés en main.

Sinon, rendez-vous dans notre section [](/python/troubleshooting).