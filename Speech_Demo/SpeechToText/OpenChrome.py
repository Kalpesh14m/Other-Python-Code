"""This Module is for Open chrome and search data what user want"""

import webbrowser as wb

def OpenChrome(text):
    #Chrome path
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    #Open Content into web browser
    f_text = "http://www.google.co.in/search?q=" + text
    wb.get(chrome_path).open(f_text)
