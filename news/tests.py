from django.test import TestCase
from .models import Editor,Article,tag
import datetime as dt


class EditorTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.kevin = Editor(first_name='Kevin',last_name='Nyota',email='kevin@gmail.com')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kevin,Editor))

    #Testing the save method
    def test_save_method(self):
        self.kevin.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    #Testing the delete method
    def test_delete_method(self):
        self.jescah = Editor(first_name='jescah',last_name='M',email='jesca@gmail.com')
        self.jescah.save_editor()
        self.kevin.save_editor()
        self.kevin.delete_editor()
        editors = Editor.objects.all()
        self.assertEqual(len(editors),1)


class ArticleTestClass(TestCase):
    def setUp(self):
        #Create an editor
        self.kevin = Editor(first_name='Kevin',last_name='Nyota',email='kevin@gmail.com')
        self.kevin.save_editor()

        #Creating a new tag and saving it
        self.new_tag = tag(name = 'testing')
        self.new_tag.save()

        #New article
        self.new_article =Article(title = 'Test Article',post = 'This is a random test post',editor = self.kevin)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tag.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)== 0)

