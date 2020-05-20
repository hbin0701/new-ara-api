import pytest
from django.test import TestCase

from apps.core.models import FAQ
from tests.conftest import RequestSetting


@pytest.mark.usefixtures('set_user_client')
class TestFAQ(TestCase, RequestSetting):
    """
    FAQ는 ReadOnlyModelViewSet
    """
    def test_list(self):
        FAQ.objects.create(ko_question='아라에 단축키가 있나요?',
                           en_question='Are there shortcuts in Ara?',
                           ko_answer='아직 없지만, 추후 업데이트에서 반영할 예정입니다.',
                           en_answer='Not yet, but will be included in next update', )

        faqs = self.http_request('get', 'faqs')
        assert faqs.data.get('num_items') == 1
