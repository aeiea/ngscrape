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
        - url (str): The URL of the flash game. For example, the URL for Alien Homonid is https://www.newgrounds.com/portal/view/59593.
        - download (str): The directory to download the file to.
        - filename (str): The name of the downloaded file.
    - Example parameters:
        - url = 'https://www.newgrounds.com/portal/view/59593'
        - download = 'testdir'
        - filename = 'game.swf'
    - Example output with debug mode:
        - NGScrape: Made request to https://www.newgrounds.com/portal/view/59593 and got status code 200
        - NGScrape: Found flash game link https:\/\/uploads.ungrounded.net\/59000\/59593_alien_booya.swf?f1101313499
        - NGScrape: Downloaded swf file to testdir/game.swf