# {octicon}`code-square;1em` CLI

```{eval-rst}
.. todo:: improve Setup section
```

## Setup

To use the Olvid CLI you need a running {term}`daemon`. If you don't know what we are talking about you might start with our [](/quickstart.md).

### Install

To install **olvid-cli** use pip3.

```sh
pip3 install olvid-bot
```

### Common Actions

```{eval-rst}
.. todo:: Set a profile photo
```

```{eval-rst}
.. todo:: add a contact (specify how to find your bot invitation link)
```

```{eval-rst}
.. todo:: create another identity
```

### Admin Client Key

To connect to daemon CLI will need a client key with admin rights registered on daemon.

On first start this key can be passed to daemon ([](/references/daemon.md#admin-client-keys)).

This client key can be passed to CLI using environment:

```sh
export OLVID_ADMIN_CLIENT_KEY=YourAdminClientKey
```

If you always launch CLI from the same working directory you can write your key in a file.
CLI will automatically read it on start if OLVID_ADMIN_CLIENT_KEY variable was not set.

```sh
echo OLVID_ADMIN_CLIENT_KEY=YourAdminClientKey > .env
```

## References

Here is a list of every commands available in {program}`olvid-cli`.

```{eval-rst}
.. include:: cli_commands.rstinc
```
