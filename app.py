import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time
from webdriver_manager.chrome import ChromeDriverManager

warnings.filterwarnings("ignore", category=DeprecationWarning)

def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/fluidmain/Twitch-Viewer-Bot/main/uptodate")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('uptodate.txt', 'r').read().strip()
        if remote_version != local_version:
            print("An updated version of the bot is available. You can download the update here: https://github.com/fluidmain/Twitch-Viewer-Bot")
            time.sleep(3)
            return False
        return True
    except:
        return True

def print_announcement():
    try:
        r = requests.get("https://pastebin.com/raw/1EwXmhbY", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Bot version check failed. Start manually, but it may not work without the latest version.\n")

def main():
    if not check_for_updates():
        return
    print_announcement()

    os.system(f"title fLUIDscripts. Twitch View Bot 3.1 ")

    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""   ┌─┐┬  ┬ ┬┬┌┬┐┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐
   ├┤ │  │ ││ ││└─┐│  ├┬┘│├─┘ │ └─┐
   └  ┴─┘└─┘┴─┴┘└─┘└─┘┴└─┴┴   ┴ └─┘o
  GITHUB: HTTPS://GITHUB.COM/FLUIDMAIN
""")))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    announcement = print_announcement()
    print("")
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colors.red, Center.XCenter("Thank you for using our bot."))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    print("")

    # Pre-configured proxy server
    proxy_url = "https://www.blockaway.net"  # Change this to your preferred proxy server

    # Pre-configured Twitch username
    twitch_username = "fluidscripts"  # Change this to the target Twitch username

    # Pre-configured number of viewers
    proxy_count = 10  # Change this to the desired number of viewers

    # Next Step
    os.system("cls")
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""   ┌─┐┬  ┬ ┬┬┌┬┐┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐
   ├┤ │  │ ││ ││└─┐│  ├┬┘│├─┘ │ └─┐
   └  ┴─┘└─┘┴─┴┘└─┘└─┘┴└─┴┴   ┴ └─┘o
  GITHUB: HTTPS://GITHUB.COM/FLUIDMAIN
""")))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    print('')
    print('')
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.cyan, Center.XCenter("The bot starts and sends viewers."))
    print(Colors.cyan, Center.XCenter("If not all viewers arrive or it doesn't work,"))
    print(Colors.cyan, Center.XCenter("then restart the bot or change the proxy server."))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    driver.get(proxy_url)

    for i in range(proxy_count):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

    # Ende
    os.system("cls")
    print(Colors.orange, Center.XCenter("╭┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╮"))
    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""   ┌─┐┬  ┬ ┬┬┌┬┐┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐
   ├┤ │  │ ││ ││└─┐│  ├┬┘│├─┘ │ └─┐
   └  ┴─┘└─┘┴─┴┘└─┘└─┘┴└─┴┴   ┴ └─┘o
  GITHUB: HTTPS://GITHUB.COM/FLUIDMAIN
""")))
    print(Colors.orange, Center.XCenter("╰┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╯"))
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.cyan, Center.XCenter("Viewers have arrived."))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.cyan, Center.XCenter("If the viewer count decreases or the bot stops working,"))
    print(Colors.cyan, Center.XCenter("consider restarting the script or trying a different proxy server."))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.cyan, Center.XCenter("Keep the window open for as long as you want to use the bot."))
    print(Colors.cyan, Center.XCenter("When you want to exit the bot, press the ENTER key or close the window."))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))
    input(Colorate.Vertical(Colors.cyan_to_blue, ">>"))
    driver.quit()

if __name__ == '__main__':
    main()
