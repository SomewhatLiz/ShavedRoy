import praw 
import json
import pyttsx3

user = {}
banned = []

with open('info.txt') as json_file:
    user = json.load(json_file)
   

with open("banned.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    banned.append(stripped_line)

engine = pyttsx3.init()

reddit = praw.Reddit(client_id = user["client_id"],
                    client_secret = user["client_secret"],
                    user_agent = user["username"],
                    username = user["username"],
                    password = user["password"])

print("-" * 20)
print("For the next part copy the end of your stream link. Example:")
print("Full link: https://www.reddit.com/rpan/r/RedditSessions/l55k3n")
print("Stream ID: l55k3n")
print("-" * 20)
input("Press any key to continue")

url = input("Stream id: ")

def printInfo(comment):
    print(20*'-')
    print(comment.author)
    print(comment.body)
    print(20*'-')

lastCommentAuthor = ""
lastCommentText = ""

while True:
    sub = reddit.submission(url)
    sub.comments.replace_more(limit=10)
    comment = sub.comments.list()[len(sub.comments.list()) - 1]
    if lastCommentAuthor != comment.author or lastCommentText != comment.body:
        if not comment.body in banned:
            engine.say(comment.body)
            engine.runAndWait()
            printInfo(comment)
        else:
            print("Banned word used!")
    else:
        print("Repeat")
    lastCommentAuthor = comment.author
    lastCommentText = comment.body