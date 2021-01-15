import time


class UserSettings:
    def __init__(self):
        self.initialize = True

    def clamp(self, n, minn, maxn):
        if n < minn:
            return minn
        elif n > maxn:
            return maxn
        else:
            return n

    def initialize(self):
        if self.initialize == True:
            print("Initializing...")
            time.sleep(2)
            self.initialize = False
            print("Initializing Done")


user_settings = UserSettings()
