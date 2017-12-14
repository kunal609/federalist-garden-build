import pytest

from unittest.mock import MagicMock

from publishing.SiteObject import (SiteObject, SiteFile, SiteRedirect)


class TestSiteObject():

    test_kwargs = {
        'filename': 'dirprefix/boop.txt',
        'md5': 'hashyhash',
        'site_prefix': 'site_prefix',
        'dir_prefix': 'dirprefix',
    }

    def test_it_is_constructable(self):
        obj = SiteObject(**self.test_kwargs)
        assert obj is not None
        assert obj.filename == 'dirprefix/boop.txt'
        assert obj.md5 == 'hashyhash'
        assert obj.site_prefix == 'site_prefix'
        assert obj.dir_prefix == 'dirprefix'

    def test_properties_work(self):
        obj = SiteObject(**self.test_kwargs)
        assert obj.s3_key == 'site_prefix/boop.txt'

        obj.dir_prefix = None
        assert obj.s3_key == 'site_prefix/dirprefix/boop.txt'

    def test_upload_to_s3(self):
        obj = SiteObject(**self.test_kwargs)
        with pytest.raises(NotImplementedError):
            obj.upload_to_s3(bucket='bucket', s3_client={})

    def test_delete_from_s3(self):
        s3_client = MagicMock()
        s3_client.delete_object = MagicMock()
        obj = SiteObject(**self.test_kwargs)
        obj.delete_from_s3(bucket='bucket', s3_client=s3_client)
        s3_client.delete_object.assert_called_once_with(
            Bucket='bucket', Key='site_prefix/boop.txt')


class TestSiteFile():
    pass

class TestSiteRedirect():
    pass
