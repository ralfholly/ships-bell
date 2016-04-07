# Ship's Bell
A little Python 3 app that plays the well-known [ship's bell](https://en.wikipedia.org/wiki/Ship%27s_bell) sounds every half an hour.

## Requirements
1. Standard Python installation, version >= 3.3
2. A command-like MP3 player like `mpg321`, eg.:
   ```
   sudo apt-get install mpg321
   ```
   If you use a different MP3 player, adapt `MP3_PLAYER_CALL` in `ships_bell.py` accordingly.

## Basic usage
```
# Show help:
python3 ./ships_bell --help
# Bell sounds from 00:00 to 24:00:
python3 ./ships_bell
# No bell sounds before 9:00 and after 20:00
python3 ./ships_bell  --from 9 --to 20
```
## License
See file LICENSE.

