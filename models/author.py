# from __init__ import CURSOR, CONN

class Author:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        """Insert a new row to the Author's table."""
        sql = """
        INSERT INTO authors (name)
        VALUES (?)
        """
        self.CURSOR.execute(sql, (self._name,))
        self.CONN.commit()
        self._id = self.cursor.lastrowid 

    @property
    def id(self):
        """Return the id of the author."""
        return self._id

    @property
    def name(self):
        """Return the name of the author."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Set the name of the author."""
        if hasattr(self, '_name'):
            raise AttributeError('Name cannot be changed')
        else:
            if isinstance(new_name, str):
                if len(new_name) > 0:
                    self._name = new_name
                else:
                    raise ValueError('Name must be longer than 0 characters')
            else:
                raise ValueError('Name must be of type str')

    def __repr__(self):
        return f'<Author {self.name}>'
