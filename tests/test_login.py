from pages.login_page import LoginPage

def test_uspesan_login(driver):
    login = LoginPage(driver)
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("Lozinka123!")
    login.klikni_login()

    poruka = login.uzmi_tekst_ulogovan()
    assert "Logged in as" in poruka


def test_neuspesan_login(driver):
    login = LoginPage(driver)
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("PogresnaLozinka123")
    login.klikni_login()

    poruka = login.uzmi_poruku_greske()
    assert poruka == "Your email or password is incorrect!"


def test_logout(driver):
    login = LoginPage(driver)
    login.otvori()
    login.unesi_email("milan_test_2026_99@gmail.com")
    login.unesi_lozinku("Lozinka123!")
    login.klikni_login()

    login.klikni_logout()
    assert "/login" in login.driver.current_url