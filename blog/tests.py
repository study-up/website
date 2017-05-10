from django.test import TestCase
from blog.models import Note


class NoteTestCase(TestCase):
    def setUp(self):
        Note.objects.create(title='test django', body='the is test case')

    def test_note_can_url(self):
        title = Note.objects.get(title='test django')
        time = title.publish
        self.assertEqual(title.get_absolute_url(), u'/blog/detail/%s/%s/%s/%s/' %
                         (time.year, time.strftime('%m'), time.strftime('%d'), title.id))
