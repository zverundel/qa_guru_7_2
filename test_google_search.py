from selene.support.shared import browser
from selene import be, have


def test_search_result(browser_firefox_open, browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))



def test_empty_search_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('nfkjdsgnfdgkjfbsdjhgbkjfdbjkg').press_enter()
    browser.element('#search').should(be.absent)
    browser.element('.card-section [aria-level="3"]').should(have.text('По запросу nfkjdsgnfdgkjfbsdjhgbkjfdbjkg '
                                                                       'ничего не найдено.'))
