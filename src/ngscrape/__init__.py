# NGScrape - Newgrounds game scraper made with beautifulsoup4 and requestslib.
# NGScrape is licensed under the GNU Affero General Public License v3.0. If a copy is not included with this file, you can find one at https://www.gnu.org/licenses/agpl-3.0.en.html.
# The source code can be found at https://github.com/aeiea/ngscrape. Please star is this was useful, and make a pull request if you find this useful!

import bs4, requests, os
class Scraper:
    '''
    # NGScrape
    Newgrounds game scraper made with beautifulsoup4 and requestslib.

    NGScrape is licensed under the GNU Affero General Public License v3.0. If a copy is not included with this file, you can find one at https://www.gnu.org/licenses/agpl-3.0.en.html.

    Please star is this was useful!

    Functions:
    - `__init__(debug: bool = False) -> None`
        - Start a new NGScrape Instance.
        - Parameters:
            - debug (bool) = False: Enable/Disable debug mode
            - cache (bool) = False: Enable/Disable caching
    - `scrape_game(url: str, download: str, filename: str) -> None`
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
    - `scrape_desc(self, url: str) -> str`
        - Scrape a flash game's description by url. Returns the description of the game.
        - Parameters:
            - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - Example parameters:
            - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - Example output with debug mode:
            - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
            - NGScrape: Found game description "Blast FBI agents in this Metal Slug style shooter!"
    - `scrape_card(self, url: str, download: str, filename: str) -> str`
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
            - NGScrape: Downloaded `png` file to `testdir/card.png`
    '''
    def __init__(self, debug: bool = False, cache: bool = False) -> None:
        '''
        Start a new NGScrape Instance.
        - Parameters:
            - debug (bool) = False: Enable/Disable debug mode
            - cache (bool) = False: Enable/Disable caching
        '''
        self.debug = debug
        self.cache = cache
        self.cachedsites = {}
        return
    
    def scrape_game(self, url: str, download: str, filename: str) -> None:
        '''
        Scrape a flash game by url.
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
        '''
        try:
            self.cachedsites[url]
            _gameHTML = self.cachedsites[url]
        except:
            if self.cache:
                self.cachedsites[url] = _gameHTML
            _gameHTML = requests.get(url)
        _soup = bs4.BeautifulSoup(_gameHTML.content, 'html.parser')
        if self.debug:
            print('NGScrape: Made request to ' + url + ' and got status code ' + str(_gameHTML.status_code))
        '''
        NOTE: Newgrounds site format has the flash game url inside <script> tags, with the varible 'embed_controller'.
        Example:
        var embed_controller = new embedController([{"url":"https:\/\/uploads.ungrounded.net\/59000\/59593_alien_booya.swf?f1101313499","is_published":true, ... );
                            0                          1  2                                     [3]
        '''
        _scripts = _soup.find_all('script')
        for i in _scripts:
            if 'var embed_controller = new embedController([{"url":"' in i.get_text():
                _gameLink: str = i.get_text().split('"')[3]
                if self.debug:
                    print('NGScrape: Found flash game link ' + _gameLink)
                break
        try:
            os.mkdir(download)
        except:
            pass
        open(download + '/' + filename, 'wb').write(requests.get(_gameLink.replace('\\', ''), allow_redirects = True).content)
        if self.debug:
            print('NGScrape: Downloaded swf file to ' + download + '/' + filename)
            
    def scrape_card(self, url: str, download: str, filename: str) -> str:
        '''
        Scrape a flash game's card by url. The file extention will be automatically determined. Returns the name of the card file.
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
            - NGScrape: Downloaded `png` file to `testdir/card.png`
        '''
        try:
            os.mkdir(download)
        except:
            pass
        try:
            self.cachedsites[url]
            _gameHTML = self.cachedsites[url]
        except:
            if self.cache:
                self.cachedsites[url] = _gameHTML
            _gameHTML = requests.get(url)
        if self.debug:
            print('NGScrape: Made request to ' + url + ' and got status code ' + str(_gameHTML.status_code))
        _soup = bs4.BeautifulSoup(_gameHTML.content, 'html.parser')
        
        _metadata = _soup.find_all('meta')
        for i in _metadata:
            try:
                if i['property'] == 'og:image':
                    _gameLink = i['content']
                    if self.debug:
                        print('NGScrape: Found card link ' + _gameLink)
                    break
            except:
                pass # This is because some tags don't have the property attribute
        _commonImageFileTypes = ['.png', '.jpg', '.jfif', '.webp', '.jpeg', '.jpe', '.jif', '.jfi', '.bmp']
        for i in _commonImageFileTypes:
            if i in _gameLink:
                _imageFiletype = i
        open(download + '/' + filename + _imageFiletype, 'wb').write(requests.get(_gameLink, allow_redirects = True).content)
        if self.debug:
            print('NGScrape: Downloaded swf file to ' + download + '/' + filename + _imageFiletype)
        return filename + _imageFiletype
    def scrape_desc(self, url: str) -> str:
        '''
        Scrape a flash game's description by url. Returns the description of the game.
        - Parameters:
            - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - Example parameters:
            - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - Example output with debug mode:
            - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
            - NGScrape: Found game description "Blast FBI agents in this Metal Slug style shooter!"
        '''

        try:
            self.cachedsites[url]
            _gameHTML = self.cachedsites[url]
        except:
            if self.cache:
                self.cachedsites[url] = _gameHTML
            _gameHTML = requests.get(url)
        if self.debug:
            print('NGScrape: Made request to ' + url + ' and got status code ' + str(_gameHTML.status_code))
        _soup = bs4.BeautifulSoup(_gameHTML.content, 'html.parser')
        
        _metadata = _soup.find_all('meta')
        for i in _metadata:
            try:
                if i['property'] == 'og:description':
                    _desc = i['content']
                    if self.debug:
                        print('Found game description "' + _desc + '"')
                    return _desc
            except:
                pass # This is because some tags don't have the property attribute
        
if __name__ == '__main__':
    import sys
    scraper = Scraper(debug = True)
    try:
        scraper.scrape_game(sys.argv[1], sys.argv[2], sys.argv[3])
        scraper.scrape_card(sys.argv[1], sys.argv[2], sys.argv[3].replace('.swf', ''))
        scraper.scrape_desc(sys.argv[1])
    except:
        print('ngscrape [newgrounds url, should be formatted like this: https://www.newgrounds.com/portal/view/xxxxx] [directory to save to] [file to save to]')
        exit(1)
    exit(0)