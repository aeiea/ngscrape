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
                - parser (str) = 'lxml': Parser used by BS4
    - `scrape_game(url: str, download: str, filename: str) -> None`
        - Scrape a flash game by url. Returns the URL for the swf.
            - Parameters:
                - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
            - Example parameters:
                - `url = 'https://www.newgrounds.com/portal/view/59593'`
            - Example output with debug mode:
                - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
                - NGScrape: Found flash game link `https:\/\/uploads.ungrounded.net\/59000\/59593_alien_booya.swf?f1101313499`
    - `scrape_desc(self, url: str) -> str`
        - Scrape a flash game's description by url. Returns the description of the game.
            - Parameters:
                - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
            - Example parameters:
                - `url = 'https://www.newgrounds.com/portal/view/59593'`
            - Example output with debug mode:
                - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
                - NGScrape: Found game description "Blast FBI agents in this Metal Slug style shooter!"
    - `scrape_card(self, url: str) -> str`
        - Scrape a flash game's card by url. Returns the URL of the card file.
            - Parameters:
                - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
            - Example parameters:
                - `url = 'https://www.newgrounds.com/portal/view/59593'`
            - Example output with debug mode:
                - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
                - NGScrape: Found card link `https://picon.ngfiles.com/59000/flash_59593_card.png?f1607717241`
    - `scrape_title(self, url: str) -> str`
        - Scrape a flash game's title with url. Returns title of the flash game.
            - Parameters:
                - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
            - Example parameters:
                - `url = 'https://www.newgrounds.com/portal/view/59593'`
            - Example output with debug mode:
                - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
                - NGScrape: Found game title "Alien Homonid"
    '''
    def __init__(self, debug: bool = False, cache: bool = False, parser: str = 'html.parser') -> None:
        '''
        Start a new NGScrape Instance.
        - Parameters:
            - debug (bool) = False: Enable/Disable debug mode
            - cache (bool) = False: Enable/Disable caching
            - parser (str) = 'lxml': Parser used by BS4
        '''
        self.debug = debug
        self.cache = cache
        self.parser = parser
        self.cachedsites = {}
        return
    
    def scrape_game(self, url: str) -> str:
        '''
        Scrape a flash game by url. Returns the URL for the swf.
        - Parameters:
            - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - Example parameters:
            - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - Example output with debug mode:
            - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
            - NGScrape: Found flash game link `https:\/\/uploads.ungrounded.net\/59000\/59593_alien_booya.swf?f1101313499`
        '''
        try:
            self.cachedsites[url]
            _gameHTML = self.cachedsites[url]
        except:
            if self.cache:
                self.cachedsites[url] = _gameHTML
            _gameHTML = requests.get(url)
        _soup = bs4.BeautifulSoup(_gameHTML.content, self.parser)
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
        return _gameLink.replace('\\', '')
            
    def scrape_card(self, url: str) -> str:
        '''
        Scrape a flash game's card by url. Returns the URL of the card file.
        - Parameters:
            - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - Example parameters:
            - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - Example output with debug mode:
            - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
            - NGScrape: Found card link `https://picon.ngfiles.com/59000/flash_59593_card.png?f1607717241`
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
        _soup = bs4.BeautifulSoup(_gameHTML.content, self.parser)
        
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
        return _gameLink
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
        _soup = bs4.BeautifulSoup(_gameHTML.content, self.parser)
        
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
    def scrape_title(self, url: str) -> str:
        '''
        Scrape a flash game's title with url. Returns title of the flash game.
        - Parameters:
            - url (str): The URL of the flash game. For example, the URL for Alien Homonid is `https://www.newgrounds.com/portal/view/59593`.
        - Example parameters:
            - `url = 'https://www.newgrounds.com/portal/view/59593'`
        - Example output with debug mode:
            - NGScrape: Made request to `https://www.newgrounds.com/portal/view/59593` and got status code `200`
            - NGScrape: Found game title "Alien Homonid"
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
        _soup = bs4.BeautifulSoup(_gameHTML.content, self.parser)

        try:
            if self.debug:
                print('NGScrape: Found game title "' + _soup.find('title').get_text() + '"')
            return _soup.find('title').get_text()
        except:
            return url
if __name__ == '__main__':
    import sys
    scraper = Scraper(debug = True)
    try:
        scraper.scrape_game(sys.argv[1])
        scraper.scrape_card(sys.argv[1])
        scraper.scrape_desc(sys.argv[1])
    except:
        print('ngscrape https://www.newgrounds.com/portal/view/xxxxx')
        exit(1)
    exit(0)