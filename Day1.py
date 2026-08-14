class InvalidPasswordError(Exception):
    pass

class SystemLockdownError(Exception):
    pass

class ShadowTerminal:
    def __init__(self, master_key : str = "kiddy999", max_attempts : int = 3):
        self.master_key = master_key
        self.max_attempts = max_attempts
        self.is_locked = False

    def authenticate(self, entered_key : str):
        if self.is_locked:
            raise SystemLockdownError("CRITICAL : System is permanently locked due to multiple failed attempts.")

        if entered_key == self.master_key:
            return "Access Granted" 

        self.max_attempts -= 1

        if self.max_attempts > 0:
            raise InvalidPasswordError(
                f"[SECURITY BREACH] : Invalid password. You have {self.max_attempts} attempts left."
            )
        else:
            self.is_locked = True
            raise SystemLockdownError("CRITICAL : System is permanently locked due to multiple failed attempts.")

if __name__ == "__main__":
    print("=== Welcome to the Shadow Terminal ===")
    terminal = ShadowTerminal(master_key="kiddy999", max_attempts=3)

    test_keys = ["wrongpass", "anotherwrong", "kiddy999"]
    for key in test_keys:
        print(f"\nAttempting to authenticate with key: '{key}'")
        try:
            result = terminal.authenticate(key)
            print(result)
            break  # Exit loop on successful authentication
        except InvalidPasswordError as e:
            print(e)
        except SystemLockdownError as e:
            print(e)
            break  # Exit loop on system lockdown

        