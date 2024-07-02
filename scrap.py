from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the website
    driver.get('https://bidplus.gem.gov.in/advance-search')

    # Wait for the well element to be present
    well_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="well"]'))
    )

    # Click the "Search by Ministry / Organization" tab
    ministry_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="ministry-tab"]'))
    )
    ministry_tab.click()

    # Wait for the select element to be present
    select_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ministry"))
    )

    # Click on the Select2 container to open the dropdown
    select2_container = driver.find_element(By.XPATH, "//span[@id='select2-ministry-container']")
    select2_container.click()

    # Wait for the dropdown to open and search for "MINISTRY OF DEFENCE"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='select2-search__field']"))
    )
    search_box.send_keys("MINISTRY OF DEFENCE")
    search_box.send_keys(Keys.RETURN)

    # Wait for a moment to ensure the selection is made
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "select2-ministry-container"), "MINISTRY OF DEFENCE")
    )

    print("Successfully selected MINISTRY OF DEFENCE")

    # Find the search button (anchor tag) and click it
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="searchByBid" and @onclick="searchBid(\'ministry-search\')"]'))
    )
    driver.execute_script("arguments[0].click();", search_button)

    print("Search button clicked")

    # Wait for the search results to load (you might need to adjust this based on the page behavior)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "search-results")]'))
    )

    print("Search results loaded")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Keep the browser open
# If you want to close the browser, uncomment the following line
# driver.quit()