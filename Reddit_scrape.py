import praw
import pandas as pd
import emoji_scrape as es

"""Scrape Reddit"""
# Reddit Credentials
user_agent = 'Scrapper'
reddit = praw.Reddit(
    client_id = 'c75j7UVTqRdXTXWmSVJvuQ',
    client_secret = 'kVAB0LPVPNK-gwjGlzyVg-PtUoyCBg',
    user_agent = user_agent
)

# URL link
submission_url = 'https://www.reddit.com/r/soccer/comments/1h1g1bf/post_match_thread_liverpool_20_real_madrid_uefa/'
submission = reddit.submission(url = submission_url)
submission.comments.replace_more(limit = 500)


"""Check comments"""
# for comment in submission.comments.list()[:10]:
#     print(f"Comment by {comment.author}: {comment.body}\n")

# Create lists for Reddit comments 
reddit_text = []
reddit_time = []
reddit_upvote = []
reddit_flair = []

# Iterate comments 
count = 0
for comment in submission.comments.list():

    # Remove emojis
    clean_comment = es.emoji_scrape(comment.body)

    # Append output to respective list
    reddit_text.append(clean_comment)
    reddit_time.append(comment.created_utc)
    reddit_upvote.append(comment.score)
    reddit_flair.append(comment.author_flair_text)

    # If exceeding count break
    count = count + 1
    if count >= 2000:
        break


"""Creating csv"""
print("Scrapping completed")

# Create dataframe to store results
df = pd.DataFrame({
    "text" : reddit_text,
    "time" : reddit_time,
    "upvote" : reddit_upvote,
    "flair" : reddit_flair
})

# Save to new csv
df.to_csv("CL_final.csv", index=False)
print("CSV created")

