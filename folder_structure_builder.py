import os
import time
from selenium_helper import (
    wait_for_element,
    wait_for_elements,
    open_networktab,
    copy_m3u8_url,
    play_video,
    clear_devtools,
)
from selenium.webdriver.common.by import By

from video_downloader import has_video_been_downloaded


def get_all_modules():
    # makes the website wait for the ul to load before continuing on searching
    wait_for_element(By.ID, "navigation-modules")
    modules_list = wait_for_elements(By.CSS_SELECTOR, ".card", 30)
    open_networktab()

    module_index = 0
    for element in modules_list:
        module_index += 1
        module = element.find_element(By.CSS_SELECTOR, "h3")
        folder_name = os.path.join("videos", module.text)
        get_all_videos(element, module_index if module_index < 7 else 8)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)


def get_all_videos(module, module_index):
    # makes the website wait for the ul to load before continuing on searching
    module.click()

    print(f"module_index {module_index}")
    videos_wrapper = module.find_element(By.ID, f"module-pages-{module_index}")
    videos_list = videos_wrapper.find_elements(By.CSS_SELECTOR, ".navigation-page")

    module_name = module.find_element(By.CSS_SELECTOR, "h3")
    for video in videos_list:
        video_name = video.find_element(By.CSS_SELECTOR, ".navigation-page-title")
        clear_devtools()
        video.click()
        play_video()
        time.sleep(3)
        args = {"module": module_name.text, "video": video_name.text}
        if not has_video_been_downloaded(
            {"video_name": video_name.text, "module_name": module_name.text}
        ):
            copy_m3u8_url(args)
        else:
            print(f"{module_name.text}/{video_name.text} exists")
