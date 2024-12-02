# 📒 Lexique

::::{admonition} Lexique
:class: note
:name: Name

This documentation covers several concepts that are specific to Olvid and this framework.
We'll attempt to define them now as clearly as possible.

:::{glossary}
Daemon
    A standalone and fully manageable Olvid application exposing [gRPC](https://grpc.io) services to control it.

Bot
    Any program interacting as a client with a daemon instance.

CLI
    A text-based interface to set up and manually interact with a daemon instance.

Identity
    An Olvid profile hosted in a daemon.

Client Key
    A unique identifier used to authenticate with the Olvid API. A client key is associated with an identity and only gives a client the permission to manage this identity.

API Key
    A key given by the Olvid team to let you use this framework without limitations. This key is set up once.
:::
::::

% todo add identity details to the big global glossary
