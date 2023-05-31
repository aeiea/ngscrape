# NGScrape
Newgrounds game scraper made with beautifulsoup4 and requestslib.

NGScrape is licensed under the GNU Affero General Public License v3.0. If a copy is not included with this file, you can find one at https://www.gnu.org/licenses/agpl-3.0.en.html.

Please star is this was useful!

Functions:
- `__init__(debug: bool = False) -> None`
    - Start a new NGScrape Instance.
- `scrape_game_by_url(url: str, download: str, filename: str) -> None`
    - Scrape a flash game by url.
    - Parameters:
        - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - download (str): The directory to download the file to.
        - filename (str): The name of the downloaded file.
    - Example parameters:
        - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - `download = 'testdir'`
        - `filename = 'game.swf'`
    - Example output with debug mode:
        - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
        - NGScrape: Found flash game link `https:\/\/uploads.ungrounded.net\/59000\/59593_alien_booya.swf?f1101313499`
        - NGScrape: Downloaded swf file to testdir/game.swf
- `scrape_desc_by_url(self, url: str) -> str`
    - Scrape a flash game's description by url. Returns the description of the game.
    - Parameters:
        - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
    - Example parameters:
        - `url = 'https://www.newgrounds.com/portal/view/59593'`
    - Example output with debug mode:`
        - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
        - NGScrape: Found game description "Blast FBI agents in this Metal Slug style shooter!"
- `scrape_card_by_url(self, url: str, download: str, filename: str) -> str`
    - Scrape a flash game's card by url. The file extention will be automatically determined. Returns the name of the card file.
    - Parameters:
        - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - download (str): The directory to download the file to.
        - filename (str): The name of the downloaded file. The file extention will be automatically determined.
    - Example parameters:
        - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - `download = 'testdir'`
        - `filename = 'card'`
    - Example output with debug mode:
        - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
        - NGScrape: Found card link `https://picon.ngfiles.com/59000/flash_59593_card.png?f1607717241`
        - NGScrape: Downloaded `swf` file to `testdir/card.png`