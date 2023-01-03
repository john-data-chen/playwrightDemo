import re
from playwright.sync_api import Page, expect


def test_homepage_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://www.kickscrew.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("KICKSCREW"))

    page.locator(".has-children").first.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*air-jordan"))