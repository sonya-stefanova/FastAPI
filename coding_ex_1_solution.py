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

from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    author: str
    comment: str
    likes: int

class Article(BaseModel):
    author: str
    co_author: Optional[str] = None
    date: str
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[Comment]

comments = [
    Comment(author="sonya",
    comment="The article is great",
    likes=2)]

article = Article(
    author="sonya",
    co_author="plamen",
    date="1/1/2023",
    title="Great post",
    content="This is the content of the article...",
    id=11111,
    likes=["sonya_like","plamen_like"],
    comments=comments
)

print(article)