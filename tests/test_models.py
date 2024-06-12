import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):

    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertIsNone(author.id)

    def test_article_creation(self):
        article = Article("Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_name_setter(self):
        author = Author("John Doe")
        with self.assertRaises(TypeError):
            author.name = 123
        with self.assertRaises(ValueError):
            author.name = ""
        author.name = "Jane Doe"
        self.assertEqual(author.name, "Jane Doe")

    def test_author_id_setter(self):
        author = Author("John Doe")
        with self.assertRaises(TypeError):
            author.id = "abc"
        author.id = 1
        self.assertEqual(author.id, 1)

    def test_magazine_name_setter(self):
        magazine = Magazine("Tech Weekly")
        with self.assertRaises(TypeError):
            magazine.name = 123
        with self.assertRaises(ValueError):
            magazine.name = "A"
        with self.assertRaises(ValueError):
            magazine.name = "A" * 17
        magazine.name = "New Name"
        self.assertEqual(magazine.name, "New Name")

    def test_magazine_category_setter(self):
        magazine = Magazine("Tech Weekly", "Technology")
        with self.assertRaises(TypeError):
            magazine.category = 123
        with self.assertRaises(ValueError):
            magazine.category = ""
        magazine.category = "Science"
        self.assertEqual(magazine.category, "Science")

    def test_article_title_setter(self):
        article = Article("Test Title", "Test Content", 1, 1)
        with self.assertRaises(TypeError):
            article.title = 123
        with self.assertRaises(ValueError):
            article.title = "A" * 4
        with self.assertRaises(ValueError):
            article.title = "A" * 51
        article.title = "Valid Title"
        self.assertEqual(article.title, "Valid Title")

    def test_article_save(self):
        Article.create_table()  # Ensure the table exists
        article = Article("Test Title", "Test Content", 1, 1)
        article.save()
        self.assertIsNotNone(article.id)
        Article.drop_table()  # Clean up by dropping the table

if __name__ == "__main__":
    unittest.main()
