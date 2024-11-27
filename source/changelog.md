# {material-regular}`history;1em` CHANGELOG

:::{note}
Versions numbers are synchronised between [bot-daemon](https://hub.docker.com/r/olvid/bot-daemon) docker image, [olvid-bot](https://pypi.org/project/olvid-bot/) pypi module, and  [bot-python-runner](https://hub.docker.com/r/olvid/bot-python-runner) docker image.

Versions follow the MAJOR.MINOR.PATCH semantic.
Every element is supposed to be working with the others if sharing the same major and minor versions, but it's recommended to always use the same patch version.

Minor versions will be incremented at least for every changes in [gRPC API description](https://github.com/olvid-io/Olvid-Bot-Protobuf).
:::

## Latest Release: Version 1.1.0

### Added

- **location**: can now send location messages. Added MessageSendLocation in protobuf, added `message location` command in {term}`CLI` and message_send_location method in OlvidClient.
- **daemon**: can now use TLS to encrypt communications between daemon and bots.
- **olvid-bot**: added olvid.errors to easily catch specific api exceptions.

### Changed

- **olvid-bot**: replaced DAEMON_HOSTNAME and DAEMON_PORT env variable by DAEMON_TARGET.
- **olvid-bot**: .client_key and .admin_client_key are now deprecated, use .env files instead.
- **olvid-bot**: OlvidBot class is now deprecated, use OlvidClient instead (they are equivalent).
- **docker**: simplified and improved [bot-daemon](https://hub.docker.com/r/olvid/bot-daemon) and [bot-python-runner](https://hub.docker.com/r/olvid/bot-python-runner) image build process. They are now faster to build and lighter.

### Fixed

- **olvid-bot**: tools.SelfCleaningBot: clean_inbound_messages and clean_outbound_messages parameters were not properly handled

---

## Version 1.0.0

Initial release of Olvid Bots project.
