dict_ = {
    "school code": "dev",
    "class": "python",
    "roll": "sovereign",
    "sec": "unknow"
}

name = input("Enter your secret name: ").strip().title()

if name == "Samir":
    print("\n[ACCESS GRANTED] User Credentials Loaded:")
    for key, value in dict_.items():
        print(f"  • {key.title()}: {value}")
else:
    print("\n[ACCESS DENIED] Unauthorized user name.")
