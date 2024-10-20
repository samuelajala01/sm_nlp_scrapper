# import praw
# import dotenv

# hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")
# client_id = dotenv.get_key(dotenv.find_dotenv(), "REDDIT_CLIENT_ID")
# client_secret = dotenv.get_key(dotenv.find_dotenv(), "REDDIT_CLIENT_SECRET")

# # Reddit API credentials
# reddit = praw.Reddit(
#     client_id=client_id,
#     client_secret=client_secret,
#     user_agent='my_reddit_scraper/0.1 by u/cx'
# )

# comments_list = []

# urls = [
#     "https://www.reddit.com/r/CarsIndia/comments/1eokb94/whats_this_crazy_trend_or_getting_after_market/",
#     "https://www.reddit.com/r/CarsIndia/comments/18z9gnh/cng_vs_petroldiesel/"

# ]

# for url in urls:
#     # Specify the URL of the Reddit page with comments
#     submission = reddit.submission(url=url)

#     # Fetch the top 20 comments
#     submission.comments.replace_more(limit=0)
#     comments = submission.comments.list()

#     # Print the first 20 comments
#     for comment in comments[:5]:
#         comments_list.append(comment.body)


# print(comments_list)

# # Specify the URL of the Reddit page with comments
# submission = reddit.submission(url='https://www.reddit.com/r/CarsIndia/comments/1eokb94/whats_this_crazy_trend_or_getting_after_market/')

# # Fetch the top 20 comments
# submission.comments.replace_more(limit=0)
# comments = submission.comments.list()

# comments_list = []

# # Print the first 20 comments
# for comment in comments[:5]:
#     comments_list.append(comment.body)

import praw
import dotenv

hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")
client_id = dotenv.get_key(dotenv.find_dotenv(), "REDDIT_CLIENT_ID")
client_secret = dotenv.get_key(dotenv.find_dotenv(), "REDDIT_CLIENT_SECRET")

# Reddit API credentials
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent='my_reddit_scraper/0.1 by u/cx'
)

comments_list = []

urls = [
    "https://www.reddit.com/r/CarsIndia/comments/1eokb94/whats_this_crazy_trend_or_getting_after_market/",
    "https://www.reddit.com/r/CarsIndia/comments/18z9gnh/cng_vs_petroldiesel/"
]

for url in urls:
    # Specify the URL of the Reddit page with comments
    submission = reddit.submission(url=url)

    # Fetch the top comments
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()

    # Store each comment in a dictionary with the comment ID
    for comment in comments[:3]:
        comments_list.append({
            'comment_body': comment.body,
        })

# print(comments_list)

for comment_dict in comments_list:
    print(f"Comment: {comment_dict['comment_body']}")
    print('-' * 50)
