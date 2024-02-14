from pydantic import BaseModel
from typing import List, Optional
"""
Your goal is to create a social media post model using pydantic. The model should have:
An author, which is a string
An optional co-author, which is a string
A date, which is a string
A title, which is a string
The content, which is a string
An ID, which is an integer
Likes, which is a list of strings

The post should also have a field for comments, which is a list of comment models. The model should have:
An author, which is a string
The comment, which is a string
Likes, which is an integer

Practice creating a social media post with whatever data you like, so long as it compiles.
"""

class Comment(BaseModel):
    author: str
    comment: str
    likes: int

class Article(BaseModel):
    author:str
    co-author:Optional[str] = None
    date:str
    title:str
    content:str
    _id: int
    likes: List[str]
    comments: List[Comment]

comments_list = [
    Comment(author="sonya", comment="this is a nice post", likes=2),
    Comment(author="plamen", comment="this is a great post", likes=1),
]

article = Article(
    author="sonya",
    date="14/12/2019",
    title="New Article",
    content="Great news",
    _id=21432,
    likes=["sonya","plamen"],
    comments=comments_list
)


print(article)