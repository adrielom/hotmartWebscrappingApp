import os
import login
from folder_structure_builder import get_all_modules
from selenium_helper import selenium_setup


def initial_setup():
    if not os.path.exists("videos"):
        os.mkdir("videos")


def web_scrapping():
    initial_setup()
    selenium_setup()
    try:
        login()
        get_all_modules()
    finally:
        # driver.quit()
        pass
    key = input("press any key to quit...")


def main():
    # download_videos()
    web_scrapping()


if __name__ == "__main__":
    main()
