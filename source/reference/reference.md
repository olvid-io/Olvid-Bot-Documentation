# 📚️ Reference

:::{toctree}
:maxdepth: 1
:hidden:
commands
notifications
admins
datatypes
:::

This section describes the complete API of an Olvid daemon.
The daemon primarily manipulates objects described in the [](datatypes) section, while other sections describe the various entry points exposed by the daemon.

::::{grid} 1

:::{grid-item}
:::{card} 
:width: 100%
:link: commands
:link-type: doc
**Commands**
^^^
Actions that can be performed, such as sending a message, updating your identity or creating a new group.
:::
:::

:::{grid-item}
:::{card} 
:width: 100%
:link: notifications
:link-type: doc
**Notifications**
^^^
Notifications that can be subscribed to, such as "you received a message" or "you joined a new group".     
:::
:::

:::{grid-item}
:::{card}
:width: 100%
:link: admins
:link-type: doc
**Admin Commands**
^^^
Actions that can be performed only with an *admin_client_key*, such as managing identities and client keys.
:::
:::

:::{grid-item}
:::{card}
:width: 100%
:link: datatypes
:link-type: doc
**Datatypes**
^^^
The main objects manipulated by the API, such as messages, attachments or discussions.
:::
:::

::::
