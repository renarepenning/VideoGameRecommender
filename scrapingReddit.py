import pandas as pd
import praw
#!pip install praw

reddit = praw.Reddit(client_id='GsD6yO1LgjoIQOYfyPq7Kg',
                     client_secret='UDdjKE1yalj0pE7dEZndqhNgCW1pTQ', user_agent='CapstoneVG')

hot_posts = reddit.subreddit('gamingsuggestions').hot(limit=10)
for post in hot_posts:
    print(post.title)

posts = []
gaming_subreddit = reddit.subreddit('gamingsuggestions')
for post in gaming_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit,
                 post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts, columns=[
                     'title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# posts

submission = reddit.submission(id="qttjxb")
for top_level_comment in submission.comments:
    print(top_level_comment.body)
