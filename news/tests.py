from django.test import TestCase
from .models import Editor,Article,tags


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