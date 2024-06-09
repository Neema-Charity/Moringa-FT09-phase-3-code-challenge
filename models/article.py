from author import Author 
from magazine import Magazine

class Article:
    def __init__(self, id, title: str, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        @property
        def title(self):
            """Return the title of the article."""
            sql = """
                SELECT title
                FROM articles
                WHERE id =?
            """
            return self.title

        @title.setter
        def title(self, new_title):
            """Set the title of the article."""
            if hasattr(self, 'title'):
                raise AttributeError('Title cannot be changed')
            else:
                if isinstance(new_title, str):
                    if 5<=len(new_title)<= 50:
                        self.title = new_title
                    else:
                        raise ValueError('Name must be longer than 0 characters')
                else:
                    raise ValueError('Name must be of type str')

    def __repr__(self):
        return f'<Article {self.title}>'
