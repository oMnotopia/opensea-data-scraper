import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

# driver.get("https://opensea.io/activity?search[collections][0]=fvckrender&search[collections][1]=artifex-fvckrender&search[collections][2]=fvck-limited&search[collections][3]=unidentified-contract-kg9mf80eue&search[eventTypes][0]=AUCTION_SUCCESSFUL")
driver.get(
    "https://opensea.io/activity/artifex-fvckrender?search[collections][0]=artifex-fvckrender&search[eventTypes][0]=AUCTION_SUCCESSFUL")
driver.implicitly_wait(5)

# Getting fiat prices
price_of_pieces_fiat = driver.find_elements(
    "xpath", "//div[@class='sc-fe5f9c83-0 mGAUR Price--fiat-amount']")
for piece in price_of_pieces_fiat:
    fiat_prices = piece.get_attribute("innerHTML")
list_of_prices_fiat = [fiat_prices]

# Getting time stamps
time_stamp = driver.find_elements(
    "xpath", "//a[@class='sc-1f719d57-0 fKAlPV EventTimestamp--link']")
for single_time in time_stamp:
    ActionChains(driver).move_to_element(single_time).click()


# Code for scrolling down the page
# pre_scroll_height = driver.execute_script('return document.body.scrollHeight;')
# run_time, max_run_time = 0, 1
# while True:
#     iteration_start = time.time()
#     # Scroll webpage, the 100 allows for a more 'aggressive' scroll
#     driver.execute_script(
#         'window.scrollTo(0, 100*document.body.scrollHeight);')

#     time.sleep(1)

#     # Adding the fiat prices after scrolling
#     price_of_pieces_fiat = driver.find_elements(
#         "xpath", "//div[@class='sc-fe5f9c83-0 mGAUR Price--fiat-amount']")
#     for item in price_of_pieces_fiat:
#         fiat_prices = item.get_attribute("innerHTML")
#         list_of_prices_fiat.append(fiat_prices)

#     post_scroll_height = driver.execute_script(
#         'return document.body.scrollHeight;')

#     scrolled = post_scroll_height != pre_scroll_height
#     timed_out = run_time >= max_run_time

#     if scrolled:
#         run_time = 0
#         pre_scroll_height = post_scroll_height
#     elif not scrolled and not timed_out:
#         run_time += time.time() - iteration_start
#     elif not scrolled and timed_out:
#         break

# print(list_of_prices_fiat)
