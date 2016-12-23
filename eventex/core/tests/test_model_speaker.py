from django.test import TestCase

from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    def test_create(self):
        speaker = Speaker.objects.create(
            name='Grace Hopper',
            website = 'http://hbn.link/hopper-site',
            photo = 'http://hbn.link/hopper-pic',
            description = 'Programadora e Almirante'
        )

        self.assertTrue(Speaker.objects.exists())
