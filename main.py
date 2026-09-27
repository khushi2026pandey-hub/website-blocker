from config import SITE_BLOCK, HOST_PATH, REDIRECT, END_TIME
from validator import validate_websites
from blocker import start_blocking


def main():

    if not validate_websites(SITE_BLOCK):
        print("Invalid website configuration.")
        return

    print("Starting Website Blocker...")

    start_blocking(
        HOST_PATH,
        SITE_BLOCK,
        REDIRECT,
        END_TIME
    )


if __name__ == "__main__":
    main()
