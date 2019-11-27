import praw
import os

reddit = praw.Reddit('bot1', user_agent='hi')

subreddit = reddit.subreddit("BotTestingPlace")

msg = "Hello!"

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("Comment_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

while True:
    for c in subreddit.comments(limit=5):
        if "hi bot" in c.body.lower() and c not in comments_replied_to:
            print("Found a friendly comment")
            c.reply(msg)
            comments_replied_to.append(c.id)

    with open("comments_replied_to.txt", "w+") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")
