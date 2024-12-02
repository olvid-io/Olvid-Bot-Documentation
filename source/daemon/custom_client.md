# 🎨 Client personnalisé

:::{warning}
Cette page n'est pas un tutoriel.
Écrire son propre client est une procédure complexe et nous vous recommandons, dans la mesure du possible, d'utiliser l'une de nos librairies clientes :
- [](/python/python)
- [](/js/js)
:::

:::{note}
Nous essayons, dans cette page, de lister les éléments qu'il est bon de connaître avant de se lancer dans l'écriture de votre propre client.
Cette liste est non-exhaustive.

Si vous souhaitez compléter cette page, vous pouvez ouvrir une issue ou une pull request en cliquant sur le bouton GitHub de la barre supérieure ou nous contacter par mail : [bot@olvid.io](mailto:bot@olvid.io).
:::

## Buf
Pour compiler nos fichiers protobuf, nous utilisons l'outil buf.
Il est possible de faire autrement (avec protoc), mais cela facilite grandement la tâche.

Pour commencer, nous vous conseillons donc d'aller voir [Buf](https://buf.build/).

Nos fichiers protobuf sont disponibles ici : [Olvid-Bot-Protobuf](https://github.com/olvid-io/Olvid-Bot-Protobuf)

Voici un exemple de fichier buf utilisé dans notre client Python : [buf.gen.yaml](https://github.com/olvid-io/Olvid-Bot-Python-Client/blob/main/buf.gen.yaml).

## Authentification
Pour se connecter au daemon, votre client devra communiquer sa clé client.
Nous utilisons les headers HTTP de gRPC pour communiquer cette information dans chaque requête.

Nous utilisons deux headers. Le premier, obligatoire, pour passer la clé client.
Le deuxième, optionnel, pour passer l'identifiant de l'identité à utiliser dans le cas d'une clé client administrateur.

```shell
# passer la clé client
daemon-client-key: 00000000-0000-0000-0000-000000000000
# passer l'identifiant d'identité à utiliser
daemon-identity-id: 1
```
