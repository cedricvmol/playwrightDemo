import time

from playwright.sync_api import Playwright, sync_playwright, expect
from pom.contact_us_page import ContactUsPage

def test_submit_form(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Cedric Van Mol","Kramwegel 24", "vanmolcedric@hotmail.com" , "0471466464", "testen" , "dit is een test bericht")






with sync_playwright() as playwright:
    test_submit_form(playwright)
    time.sleep(5)