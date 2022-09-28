from sys import modules
from os import listdir, path
from pathlib import Path
from typing import Union
from playwright import sync_api

#获取webdriver的路径地址，下面是chromium的，对应的webkit和firefox需要对应的更改路径，webkit在上层路径
def get_executable_path() -> Union[str, None]:
    parent_folder = Path(modules['playwright'].__file__).parent / 'driver' / 'package' / '.local-browsers'

    if not path.exists(parent_folder):
        return None

    child_folders = [name for name in listdir(parent_folder) if path.isdir(parent_folder / name) and name.strip().lower().startswith('chromium')]

    if len(child_folders) != 1:
        return None

    chromium_folder = child_folders[0]

    return parent_folder / chromium_folder / 'chrome-win' / 'chrome.exe'


with sync_api.sync_playwright() as p:
    executable_path = get_executable_path()
    print(executable_path)

    if executable_path:
        browser = p.chromium.launch(
            headless=False,
            executable_path=executable_path
        )
        page = browser.new_page()
        page.goto("http://playwright.dev")
        print(page.title())
        browser.close()