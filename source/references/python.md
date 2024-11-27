# Python Client

% currentmodule: olvid.datatypes

```{eval-rst}
.. automodule:: olvid.datatypes
   :members:
   :undoc-members:
```

% .. autoclass:: olvid.datatypes.Message
%     :members:
%     :exclude-members: OnMessageEventListener,WaitForMessageEventListener
%     :member-order: bysource

## Exceptions

% todo: add link to source code

Here is a list of the main exceptions you might encounter in when using this library.
The exhaustive list can be found in `olvid/core/exceptions.py`.

This is a code example catching a specific exception (NotFound) or any other OlvidException.

```python3
import asyncio
from olvid import OlvidClient, exceptions

async def main():
    client: OlvidClient = OlvidClient()
    try:
        print(await client.discussion_get(discussion_id=1))
    # handle if the requested discussion does not exists
    except exceptions.NotFound:
        print("This discussion does not exist.")
    # catch any other exception
    except exceptions.OlvidException as e:
        print(f"Something went wrong: {e.name}: {e.details}")

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

______________________________________________________________________

### Daemon methods exceptions

These exceptions might be raised during a daemon method call.

```{eval-rst}
.. automodule:: olvid.errors
    :members: NotFound, InvalidArgument, Unauthenticated, PermissionDenied, InternalError
    :undoc-members:
    :member-order: bysource
```

______________________________________________________________________

### gRPC exceptions

These exceptions might be raised by gRPC at any time.

```{eval-rst}
.. automodule:: olvid.errors
    :members: Unavailable, Cancelled, Unimplemented
    :undoc-members:
    :member-order: bysource
```
