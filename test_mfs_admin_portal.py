from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="function")
def login(page: Page):
    page.goto("http://103.191.178.87:8080/crimson-admin-portal-staging/login")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("tanim.test")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Test@12345")
    page.get_by_role("button", name="SIGN IN").click()
    yield page


################################################
##################### Bank Cashin###############
################################################


def test_cashin_to_distributor(login: Page):
    page = login  # Use the page object from the login fixture
    page.goto("http://103.191.178.87:8080/crimson-admin-portal-staging/bank/cashIn")
    page.get_by_title("Select Distributor Wallet").click()
    page.locator("input[type=\"search\"]").fill("tan")
    page.get_by_role("treeitem", name="(Tanum)").click()
    page.locator("#txtAmount").click()
    page.locator("#txtAmount").fill("1100")
    page.locator("#txtDescription").click()
    page.locator("#txtDescription").fill("Test Money Cash in")
    page.get_by_role("button", name="Cash In").click()
    page.get_by_role("button", name="Cash In").click()

#############################################################
################## Approve Bank Cashin ######################
#############################################################

def test_approve_cashin(login: Page):
    page = login  # Use the page object from the login fixture
    page.goto("http://103.191.178.87:8080/crimson-admin-portal-staging/bank/cashIn/list")
    
    # Assert the first occurrence of the phone number
    phone_number = page.locator("td", has_text="018331837111").nth(0)
    expect(phone_number).to_have_text("018331837111")
    
    # Assert the first occurrence of the amount
    amount = page.locator("td", has_text="11000").nth(0)
    expect(amount).to_have_text("11000")
    
    # Click the first "Approve" button
    approve_button = page.get_by_role("button", name="Approve").nth(0)
    approve_button.click()


##################################################
############### Bank Cashout ######################
##################################################


def test_bank_cashout(login: Page):
    page = login  # Use the page object from the login fixture

    page.goto("http://103.191.178.87:8080/crimson-admin-portal-staging/bank/cashOut")
    page.get_by_title("Select Distributor Wallet").click()
    page.locator("input[type=\"search\"]").fill("tan")
    page.get_by_role("treeitem", name="(Tanum)").click()
    page.locator("#txtAmount").click()
    page.locator("#txtAmount").fill("200")
    page.locator("#txtDescription").click()
    page.locator("#txtDescription").fill("Bank CashOut")
    page.get_by_role("button", name="Submit").click()


#############################################################
#################Bank Cashout Approve######################
#############################################################

def test_bank_cashout_approve(login: Page):
    page = login  # Use the page object from the login fixture

    page.goto("http://103.191.178.87:8080/crimson-admin-portal-staging/bank/cashIn/list")
    # Assert the first occurrence of the phone number
    phone_number = page.locator("td", has_text="018331837111").nth(0)
    expect(phone_number).to_have_text("018331837111")
    # Assert the first occurrence of the amount
    amount = page.locator("td", has_text="200").nth(0)
    expect(amount).to_have_text("200")
    # Click the first "Approve" button you find
    approve_button = page.get_by_role("button", name="Approve").nth(0)
    approve_button.click()
