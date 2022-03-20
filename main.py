import sys
from instaloader import ConnectionException, instaloader

from defines.creds import get_creds
from dumper import Dumper


def map_profiles(target_usernames, loader):
    return map(lambda username: instaloader.Profile.from_username(loader.context, username), target_usernames)


def main():
    CREDS = get_creds()
    IL = instaloader.Instaloader()
    try:
        IL.load_session_from_file(
            CREDS.get("instagram_username"), CREDS.get("session_file_path"))
    except ConnectionException as e:
        sys.exit(f"Session import failed: {str(e)}")

    target_profiles = map_profiles(CREDS.get("target_usernames"), IL)
    dumper = Dumper(target_profiles, IL)
    dumper.init_dump()
    IL.save_session_to_file(CREDS.get("session_file_path"))


if __name__ == "__main__":
    main()
