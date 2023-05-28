# NGScrape - Newgrounds game scraper made with beautifulsoup4 and requestslib.
# NGScrape is licensed under the GNU Affero General Public License v3.0. If a copy is not included with this file, you can find one at https://www.gnu.org/licenses/agpl-3.0.en.html.
# The source code can be found at https://github.com/aeiea/ngscrape. Please star is this was useful, and make a pull request if you find this useful!

import bs4
import requests
class Scraper:
    '''
    # NGScrape
    Newgrounds game scraper made with beautifulsoup4 and requestslib.
    
    NGScrape is licensed under the GNU Affero General Public License v3.0. If a copy is not included with this file, you can find one at https://www.gnu.org/licenses/agpl-3.0.en.html.
    
    The source code can be found at https://github.com/aeiea/ngscrape. Please star is this was useful!
    
    Functions:
        __init__(debug: bool = False) -> None:
            Start a new NGScrape Instance.
        scrape_game_by_url(url: str, download: str, filename: str) -> None
            Scrape a flash game by url.
    '''
    def __init__(self, debug: bool = False) -> None:
        '''
        Start a new NGScrape Instance.
        '''
        if debug:
            self.debug = True
            return
        self.debug = False 
        return
    
    def scrape_game_by_url(self, url: str, download: str, filename: str) -> None:
        '''
        Scrape a flash game by url.
        
        Parameters:
            url (str): The URL of the flash game. For example, the URL for Alien Homonid is https://www.newgrounds.com/portal/view/59593.
            download (str): The directory to download the file to.
            filename (str): The name of the downloaded file.
        Example parameters:
            url = 'https://www.newgrounds.com/portal/view/59593'
            download = 'testdir'
            filename = 'game.swf'
        Example output with debug mode:
            NGScrape: Made request to https://www.newgrounds.com/portal/view/59593 and got status code 200
            NGScrape: Found flash game link https:\/\/uploads.ungrounded.net\/59000\/59593_alien_booya.swf?f1101313499
            NGScrape: Downloaded swf file to testdir/game.swf
        '''
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
                _gameLink = i.get_text().split('"')[3]
                if self.debug:
                    print('NGScrape: Found flash game link ' + _gameLink)
        open(download + '/' + filename, 'wb').write(requests.get(_gameLink, allow_redirects = True).content)
        if self.debug:
            print('NGScrape: Downloaded swf file to ' + download + '/' + filename)
                
if __name__ == '__main__':
    scraper = Scraper(debug = True)
    scraper.scrape_game_by_url('https://www.newgrounds.com/portal/view/59593', 'testdir', 'game.swf')