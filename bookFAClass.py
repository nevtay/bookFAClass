import sys
import pyinputplus as pyip
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def handleBookingSequence(browser):
    sleep(2)
    rightArrow = browser.find_element(
        By.XPATH, "//div[@class='slider-forward icon-arrow-right']")
    if len(sys.argv) == 4:
        if len(sys.argv[3]) != 0:
            for i in range(int(sys.argv[3])):
                rightArrow.click()
                sleep(0.5)
        availableClasses = browser.find_elements(
            By.CLASS_NAME, "list-text-left")
        if len(availableClasses) > 0:
            print("These are the available classes for the day: \n")
            for c, val in enumerate(availableClasses):
                print(f"[{c}]: {val.text}\n")
            targetClass = pyip.inputStr(
                "Please type a class number to book (e.g. '1', '7', '3') and press enter.\nTo cancel, enter 'n' or 'N'.\n")
            if (targetClass == 'n' or targetClass == "N"):
                return
            while (targetClass == ""):
                targetClass = pyip.inputStr(
                    "Please type a class number to book (e.g. '1', '7', '3') and press enter.\nTo cancel, enter 'n' or 'N'.\n")
                if (targetClass == 'n' or targetClass == "N"):
                    print("Booking process cancelled.")
                    return
            for index, val in enumerate(availableClasses):
                if int(targetClass) == index:
                    targetClassText = availableClasses[index].text
                    print(f"You have selected - {targetClassText}")
                    availableClasses[int(targetClass)].click()
                    sleep(1)
                    bookButton = browser.find_element(
                        By.CSS_SELECTOR, "button.full-width.modal-button")
                    decision = pyip.inputStr(
                        "Confirm booking? [y]/[n] ")
                    if (str(decision).strip().lower() == 'y'):
                        bookButton.click()
                        print("Class booked.")
                    else:
                        print("Returning to list of classes of chosen day.")
                        browser.back()
                        handleBookingSequence(browser)


def bookFAClass():
    browser = webdriver.Firefox()
    browser.set_window_size(768, 900)
    browser.get(
        'https://app.glofox.com/portal/#/branch/5ee338c2dc8cfb7a836d9403/classes-week-view')
    sleep(4)
    try:
        browser.find_element(
            By.XPATH, "//*[contains(text(), 'Login')]").click()
        browser.find_element(By.NAME, "loginEmail").send_keys(sys.argv[1])
        browser.find_element(By.NAME, "loginPassword").send_keys(sys.argv[2])
        browser.find_element(By.NAME, "loginPassword").submit()
        browser.get(
            'https://app.glofox.com/portal/#/branch/5ee338c2dc8cfb7a836d9403/classes-day-view')
        sleep(3)
        handleBookingSequence(browser)
    except:
        raise Exception("SOMETHING WENT WRONG")


bookFAClass()
