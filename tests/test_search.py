"""
These tests cover DuckDuckGo searches.
"""
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(PHRASE)

    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # Then the search result title contains "panda"
    # import time
    # time.sleep(5)
    assert PHRASE in result_page.title()


"""
Run the test using 'pipenv run python -m pytest' in command line to test
the fixture. Even though the test should still fail, Chrome should briefly
pop up for a few seconds while the test is running.
Make sure Chrome quits once the test is done.
"""
