# pushover
[Pushover](https://pushover.net/api) client application implemented in various languages.

# Pushover Details

API details can be found [here](https://pushover.net/api)
## Priority

|Priority|Code|Description|
|---|---|---|
|Low|`-1`|Trigger alert notification only.  No sound, vibration|
|Normal (default)|`0`|Trigger sound, vibration and display alert on user's device|
|High|`1`|Same as `normal` but ignores quiet hours|
|Emergency|`2`|Same as `high` but alerts are repeated until acknowledged|

See [priority](https://pushover.net/api#priority) documentation for more details.

# Bash

**Usage**
```bash
pushover [-t title] [-p priority] [-v] -m message
```

**Arguments:**
```
-t      notification title
-p      notification priority
-v      verbose logging
-m      notification text
```

*example*
```bash
pushover -t "Sample Title" -m "Sample message" -v
```

# Python

## Installation
1. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install requirements
```bash
pip install -r requirements.txt
```
## Usage
```
usage: pushover.py [-h] [-v] -m MESSAGE [-t TITLE] [-p PRIORITY]

DESCRIPTION

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose logging
  -m MESSAGE, --message MESSAGE
                        notification
  -t TITLE, --title TITLE
                        notification title
  -p PRIORITY, --priority PRIORITY
                        notification priority
```
