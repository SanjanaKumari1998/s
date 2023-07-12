from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver instance (replace with the appropriate WebDriver executable path)
driver = webdriver.Chrome('/path/to/chromedriver')

# Navigate to Amazon.ca
driver.get('https://www.amazon.ca')

# Click on the "Today's Deals" link
todays_deals_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'nav-xshop'))).text
if todays_deals_link == "Today's Deals":
    driver.find_element(By.LINK_TEXT, "Today's Deals").click()
else:
    driver.find_element(By.LINK_TEXT, "Prime Day").click()

# Wait for the Prime Day deals page to load
prime_day_deals_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'widgetFilters')))

# Get the list of Prime Day deal items
deals = prime_day_deals_page.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')

# Print the names and prices of the first few deal items
for deal in deals[:5]:
    name = deal.find_element(By.CSS_SELECTOR, 'h2 a').text
    price = deal.find_element(By.CSS_SELECTOR, '.a-price-whole').text
    print(f'Deal Name: {name}')
    print(f'Deal Price: {price}')
    print('---')

# Close the browser
driver.quit()
