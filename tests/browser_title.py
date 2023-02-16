from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000/')

try:
    assert 'The install worked successfully! Congratulations!' in browser.title
    print('Assertion test passed.')

except Exception as e:
    print(f'Assertion test failed. {browser.title} exception was', format(e))