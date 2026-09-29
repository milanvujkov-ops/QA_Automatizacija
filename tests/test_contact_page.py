import os
import pytest
from pages.contact_page import ContactPage

def test_successful_contact_form_submission(driver):
    contact_page = ContactPage(driver)
    contact_page.open("https://automationexercise.com/contact_us")

    # Priprema testnog fajla za upload
    test_file_path = os.path.abspath("test_attachment.txt")
    with open(test_file_path, "w") as f:
        f.write("Ovo je testni fajl za upload u Selenium-u.")

    # Popunjavanje i slanje forme
    contact_page.fill_contact_form(
        name="Petar Petrovic",
        email="petar.qa@example.com",
        subject="Upit za saradnju",
        message="Zdravo, zanimalo bi me vise detalja o ponudi.",
        file_path=test_file_path
    )

    contact_page.submit_form()

    # Verifikacija poruke o uspehu
    success_text = contact_page.get_success_message_text()
    assert "Success! Your details have been submitted successfully." in success_text

    # Ciscenje kreiranog testnog fajla sa diska
    if os.path.exists(test_file_path):
        os.remove(test_file_path)