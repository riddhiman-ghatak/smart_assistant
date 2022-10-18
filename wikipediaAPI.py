#import wikipediaapi
#wiki_wiki = wikipediaapi.Wikipedia('en')
#page_py = wiki_wiki.page('what is coronavirus')

#print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

#print("Page - Summary: %s" % page_py.summary[0:60])


from selenium import webdriver


def search_web(input):
    driver = webdriver.Firefox()(executable_path="C:/Users/riddh/Music/geckodriver.exe")
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():
        print("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
search_web("youtube")