from pages.main_page import MainPage  # импорт класса, описывающий главную страницу который находится в папке pages
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"  # http://selenium1py.pythonanywhere.com/
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" # http://selenium1py.pythonanywhere.com/
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # метод, который будет проверять наличие ссылки. Смотри main_page.py


def test_guest_should_see_login_link_login(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" # http://selenium1py.pythonanywhere.com/
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()  # метод, который будет проверять наличие ссылки. Смотри main_page.py

"""
def test_guest_can_go_to_login_page_2(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page() """
#def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):


#def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):