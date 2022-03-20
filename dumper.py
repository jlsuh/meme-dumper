from instaloader import instaloader


class Dumper:
    def __init__(self, target_usernames, loader):
        self.target_usernames = target_usernames
        self.loader = loader

    def __filter_public_usernames(self):
        public_usernames = []
        for username in self.target_usernames:
            profile_type = "public"
            profile = instaloader.Profile.from_username(
                self.loader.context, username)
            if not profile.is_private:
                public_usernames.append(username)
            else:
                profile_type = "private"
            print(f"{username} is {profile_type}")
        return public_usernames

    def init_dump(self):
        print("Dump initiated")
        public_target_usernames = self.__filter_public_usernames()
        print(f"Public target usernames: {public_target_usernames}")
