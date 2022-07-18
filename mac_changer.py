# Adding CLI Args soon
import random
from time import sleep
import subprocess
from rich.console import Console

console = Console()
loop = True

class Spoof:
    def __init__(self) -> None:
        pass

    @staticmethod
    def logo() -> None:
        color = [
            "red1", "blue", "cyan", "grey0", "green3", "yellow1"
            ]
        _color2 = [
            "red1", "blue", "cyan", "grey0", "green3", "yellow1"
            ]
        random_color = random.choice(color)
        _random_color2 = random.choice(_color2)

        console.print(f"""[{random_color}]

    [{_random_color2}] __  __               _____                    __[/{_random_color2}]
    [{random_color}]|  \/  |             / ____|                  / _|         [/{random_color}]
    [{_random_color2}]| \  / | __ _  ___  | (___  _ __   ___   ___ | |_ ___ _ __[/{_random_color2}]
    [{random_color}]| |\/| |/ _` |/ __|  \___ \| '_ \ / _ \ / _ \|  _/ _ \ '__|[/{random_color}]
    [{_random_color2}]| |  | | (_| | (__   ____) | |_) | (_) | (_) | ||  __/ |   [/{_random_color2}]
    [{random_color}]|_|  |_|\__,_|\___| |_____/| .__/ \___/ \___/|_| \___|_|   [/{random_color}]
    [{_random_color2}]                           | |                             [/{_random_color2}]
                               |_|
           [/{random_color}]""", style="blink")

        
    # Could make it a "spoofer" if you gen random macs and put it inside the while loop.
    @staticmethod
    def mac_change() -> None:
        while loop:
            try:
                new_mac = input("Enter new Mac Address >@ \n")
                subprocess.call("ifconfig " + " eth0" + " down", shell=True)
                subprocess.call("ifconfig " + " eth0 " + " hw ether " + new_mac, shell=True)
                subprocess.call("ifconfig " + " eth0 " + " up", shell=True)
                console.print(f"[+] Changing new MAC to {new_mac}\n")
            except:
                console.print(f"[-] Something Went Wrong")
                raise SystemExit
            


def main():
    start = Spoof()
    start.logo()
    start.mac_change()


if __name__ == "__main__":
    main()
    
