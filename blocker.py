import datetime
import time

from host_manager import block_websites, unblock_websites


def start_blocking(host_path, websites, redirect, end_time):
    print("Website blocker started.")

    while datetime.datetime.now() < end_time:
        block_websites(host_path, websites, redirect)

        print("Websites are currently blocked.")
        time.sleep(5)

    print("Blocking time has ended.")

    unblock_websites(host_path, websites)

    print("Websites have been unblocked.")
