import threading, ngscrape

# ⚙️ CONFIG
threads = 4
range_of_search = (10050, 100500)

# 🐍 CODE



def search_range(range_min, range_max):
    s = ngscrape.Scraper()
    for i in range(range_min, range_max + 1):
        temp = s.scrape_desc('https://www.newgrounds.com/portal/view/' + str(i))
        if temp != None:
            try:
                print(s.scrape_title('https://www.newgrounds.com/portal/view/' + str(i)) + ' | Description: ' + temp + ' | URL: ' + 'https://www.newgrounds.com/portal/view/' + str(i))
            except:
                continue
    return
if __name__ == '__main__':
    list_of_ranges = []
    range_of_range_of_search = range_of_search[1] - range_of_search[0]
    increment_value = range_of_range_of_search // threads
    for i in range(1, threads):
        list_of_ranges.append((range_of_search[0] + (i - 1) * increment_value, range_of_search[0] + i * increment_value))
    list_of_ranges.append((range_of_search[0] + (threads - 1) * increment_value, range_of_search[1]))
    
    processes = []
    for i in range(threads):
        processes.append(threading.Thread(target=search_range, args=list_of_ranges[i]))
        processes[i].start()