class Dumper:
    def __init__(self, target_profiles, loader):
        self.target_profiles = target_profiles
        self.loader = loader

    def __filter_public_profiles(self):
        public_profiles = []
        for profile in self.target_profiles:
            profile_type = "private"
            if not profile.is_private:
                public_profiles.append(profile)
                profile_type = "public"
            print(f"{profile.username} is {profile_type}")
        return public_profiles

    def init_dump(self):
        print("Dump initiated")
        public_target_profiles = self.__filter_public_profiles()
        print(f"Public target profiles: {public_target_profiles}")
