import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip as pc
from video_downloader import download_video
from video_model import VideoModel

TARGET_URL = "https://aescoladasplantas.club.hotmart.com/login"

driver = webdriver.Chrome()


def selenium_setup():
    driver.get(TARGET_URL)
    driver.fullscreen_window()


def wait_for(number):
    driver.implicitly_wait(number)


def wait_for_element(type, selector, wait=10):
    element = WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((type, selector))
    )
    return element


def wait_for_elements(type, selector, wait=10):
    element = WebDriverWait(driver, wait).until(
        EC.presence_of_all_elements_located((type, selector))
    )
    return element


def open_networktab():
    pyautogui.hotkey("ctrl", "shift", "i")
    pyautogui.moveTo(1657, 120)
    time.sleep(3)
    pyautogui.leftClick()
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.write("m3u8")
    clear_devtools()
    time.sleep(2)


def toggle_networktab():
    pyautogui.hotkey("ctrl", "shift", "i")


def get_mouse_position():
    print(pyautogui.position())


def copy_m3u8_url(args):
    get_mouse_position()
    # click the first network record
    pyautogui.moveTo(1442, 383)
    pyautogui.click()
    # copy the network record log
    pyautogui.moveTo(1679, 404)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")

    time.sleep(2)
    raw_url = f"{args['module']}**{args['video']}-{pc.paste()}"

    video = VideoModel(raw_url)
    download_video(video)

    time.sleep(80)
    clear_devtools()
    time.sleep(2)


def clear_devtools():
    pyautogui.moveTo(1409, 143)
    pyautogui.click()


def play_video():
    pyautogui.moveTo(961, 457)
    pyautogui.click()
    time.sleep(3)
