def test_vyhldani_zbozi(page):
    #otevři webovou stránku autodílů "https://www.autodily-pema.cz/"
    page.goto('https://www.autodily-pema.cz', timeout=10000)

    #potvrď tlačítko cookies "Povolit vše"
    cookies_button = page.locator("input[name='grantAllButton']")
    cookies_button.click()

    #klikni do vyhledávacího pole
    search_input = page.locator("input[data-dropdown-id='layoutHeaderDropdownSearch']")
    search_input.click()

    #zadej do vyhledávacího pole zboží "Olej"
    search_input.fill("Olej")

    #klikni na tlačítko lupy (hledat) a použij první (hlavní) lupu
    search_button = page.locator("button[aria-label='Vyhledávaní…']").first
    search_button.click()

    #počkej dokud se nenačtou všechny produkty
    page.wait_for_load_state("networkidle")

def test_muj_ucet_registrace(page):
    #otevři webovou stránku autodílů "https://www.autodily-pema.cz/"
    page.goto('https://www.autodily-pema.cz', timeout=10000)

    #potvrď tlačítko cookies "Povolit vše"
    cookies_button = page.locator("input[name='grantAllButton']")
    cookies_button.click()

    #klikni na horním panelu na button "Můj účet"
    account_button = page.locator('span.layoutHeaderMainBar__button__icon').first
    account_button.click()

    #klikni na v rozbalené nabídce na "Registrace"
    registration_link = page.locator('a.dropdownMenu__item.--link[href="/registrace"]')
    registration_link.click()

    #počkej dokud se nenačte stránka pro zadání registrace
    page.wait_for_load_state("networkidle")

def test_prihlaseni_uzivatele(page):
    #otevři webovou stránku autodílů "https://www.autodily-pema.cz/"
    page.goto('https://www.autodily-pema.cz', timeout=10000)

    #potvrď tlačítko cookies "Povolit vše"
    cookies_button = page.locator("input[name='grantAllButton']")
    cookies_button.click()

    #klikni na horním panelu na button "Můj účet"
    account_button = page.locator('span.layoutHeaderMainBar__button__icon').first
    account_button.click()

    #klikni na v rozbalené nabídce na "Přihlášení"
    login_link = page.locator('a.dropdownMenu__item.--link.ajax[href="/prihlaseni"]').first
    login_link.click()

    #zadej přihlašovací údaje email
    email_input = page.locator('input[name="email"]')
    email_input.fill('test@example.com')  # Příklad vyplnění hodnoty

    #zadej přihlašovací údaje heslo
    password_input = page.locator('input[name="password"]')
    password_input.fill('your_password')  # Příklad vyplnění hesla

    #kliknutí na tlačítko "Přihlásit se"
    submit_button = page.locator('input[type="submit"][name="login"]')
    submit_button.click()

    #počkej dokud se nenačte stránka po zadání údajů
    page.wait_for_load_state("networkidle")

    #nyní test skončí hláškou "Zadali jste nesprávný email nebo heslo."

def zakladni_test_funkce_search_field(page):
    #otevři webovou stránku autodílů "https://www.autodily-pema.cz/"
    page.goto('https://www.autodily-pema.cz', timeout=10000)

    #potvrď tlačítko cookies "Povolit vše"
    cookies_button = page.locator("input[name='grantAllButton']")
    cookies_button.click()

    #klikni na button "Autodíly"
    autodily_link = page.locator('a[href="https://www.autodily-pema.cz/autodily"]')
    autodily_link.click()

    #počkej dokud se nenačte stránka po zadání údajů
    page.wait_for_load_state("networkidle")

def test_zakladni_tlacitka_autodily_na_hlavni_strance(page):
    #otevři webovou stránku autodílů "https://www.autodily-pema.cz/"
    page.goto('https://www.autodily-pema.cz', timeout=10000)

    #potvrď tlačítko cookies "Povolit vše"
    cookies_button = page.locator("input[name='grantAllButton']")
    cookies_button.click()

    #klikni na button "Autodíly"
    autodily_text = page.locator('span.categoryGridPagePart__name__name.balance-text:text("Autodíly")')
    autodily_text.click()

    #počkej dokud se nenačte stránka po zadání údajů
    page.wait_for_load_state("networkidle")