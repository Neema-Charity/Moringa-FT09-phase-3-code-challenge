# from __init__ import CURSOR, CONN

class Magazine:
    def __init__(self, id: int, name: str, category):
        self.id = id
        self.name = name
        self.category = category
        """Insert a new row into the Magazines table"""
        sql = """
        INSERT INTO magazines (name, category)
        VALUES (?,?)
        """
        self.CURSOR.execute(sql, (self.name, self.category))
        self.CONN.commit()
        self.id = self.CURSOR.lastrowid

    @property
    def id(self):
        """Return the id of the magazine."""
        return self.id

    @property
    def name(self):
        """Return the name of the magazine."""
        sql = """
        SELECT name
        FROM magazines
        WHERE id =?
        """
        return self.name

    @property
    def category(self):
        """Return the category of the magazine."""
        sql = """
        SELECT category
        FROM magazines
        WHERE id =?
        """
        return self.category

    @name.setter
    def name(self, new_name):
        """Set the name of the author."""

        if isinstance(new_name, str):
            if 2<=len(new_name)<=16:
                self._name = new_name
            else:
                raise ValueError('Name must be between 2 and 16 characters')
        else:
            raise ValueError('Name must be of type str')

    @category.setter
    def category(self, new_category):
        """Set the category of the magazine."""

        if isinstance(new_category, str):
            if len(new_category)>0:
                self._category = new_category
            else:
                raise ValueError('Category must be longer than 0 characters')
        else:
            raise ValueError('Category must be of type str')

    def __repr__(self):
        return f'<Magazine {self.name}>'
