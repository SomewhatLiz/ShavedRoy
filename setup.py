import subprocess
import sys
import json

user = {
        "client_id" : "",
        "client_secret" : "",
        "user_agent" : "",
        "username" : "",
        "password" : ""
}




def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("praw")
install("pyttsx3")

user["client_id"] = input("client_id: ")
user["client_secret"] = input("client_secret: ")
user["password"] = input("password: ")
username = input("username (no u/): ")
user["user_agent"] = username
user["username"] = username

with open('info.txt', 'w') as outfile:
    json.dump(user, outfile)

print("all ready!")