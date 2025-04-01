from datetime import datetime


class Post:
    def __init__(
        self,
        id: int,
        title: str,
        subtitle: str,
        body: str,
        image_url: str,
        author: str,
        date: datetime,
    ) -> None:
        self.id: int = id
        self.title: str = title
        self.subtitle: str = subtitle
        self.body: str = body
        self.image_url: str = image_url
        self.author: str = author
        self.date: datetime = date
