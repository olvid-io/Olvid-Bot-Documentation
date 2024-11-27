# Daemon

```{contents}
:depth: 2
:local: true
```

## Configuration

You can customize the behavior of the [daemon docker image](https://hub.docker.com/r/olvid/bot-daemon) by passing different environment variables.
These variables are described in the following sections.

Note that when there are CLI parameters and environment variable for the same setting CLI parameters take precedence over environment variables.

### gRPC Server

You can change the gRPC listening port using either a CLI option or an environment variable:

*(default: 50051)*

```sh
-p, --port 8080
```

```sh
DAEMON_PORT=8080
```

### Logs

You can change log levels using environment variables.

*(default: INFO)*

```sh
DAEMON_LOG_LEVEL=DEBUG|INFO|WARNING|ERROR  # daemon logs
ENGINE_LOG_LEVEL=DEBUG|INFO|WARNING|ERROR  # cryptographic engine logs
```

### Admin Client Keys

#### Set

Set temporary admin client keys using either a CLI option or an environment variable.

This is necessary for the first connection and it is used in the [](/quickstart.md#initialize-daemon) process.

```sh
-k, --key 00000000-0000-0000-0000-000000000000
```

```sh
OLVID_ADMIN_CLIENT_KEY=random-uuid
OLVID_ADMIN_CLIENT_KEY_ANY_NAME=any-random-uuid
OLVID_ADMIN_CLIENT_KEY_OTHER=other-random-uuid
```

#### List

List registered client keys and exit the daemon using the following command:

```sh
-l, --list
```

### TLS

For information on deploying TLS properly, see [link](/configuration.md#setup-tls).

#### TLS Server authentication

Both elements are necessary for TLS server authentication:

```sh
--certificate-file server.pem
--key-file server.key
```

```sh
DAEMON_CERTIFICATE_FILE=server.pem
DAEMON_KEY_FILE=server.key
```

#### TLS with Client authentication

The three elements are necessary to enable client authentication:

```sh
--certificate-file server.pem
--key-file server.key
--root-file ca.pem
```

```sh
DAEMON_CERTIFICATE_FILE=server.pem
DAEMON_KEY_FILE=server.key
DAEMON_ROOT_CERTIFICATE_FILE=ca.pem
```

### Backups

#### Restore backup

To restore a backup, see [](/configuration.md#restore-a-backup).

Backup restoration can be started with this option:

```sh
-r, --restore-backup backup-file-path.bytes
```

## Use

### Environment Variables

To configure the daemon environment in docker compose update environment attribute in `docker-compose.yaml` file. For example:

```yaml
services:
  daemon:
    image: olvid/bot-daemon
    environment:
        - OLVID_ADMIN_CLIENT_KEY=cli-key
```

### CLI Options

There are two ways to run the daemon with command-line options:

To set persistent CLI options, update your `docker-compose.yaml` to add the command attribute to your daemon service:

```yaml
services:
  daemon:
    image: olvid/bot-daemon
    command: --key mySuperSecretKey
```

To use temporary options use the `docker compose run` command. For example, run:
.. code-block:: sh

> docker compose run --rm daemon --list

This will list available client keys and exit.
