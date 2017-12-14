from invoke import MockContext, Result

from tasks import main


class TestMain():
    def test_it_is_callable(self, monkeypatch):
        ctx = MockContext(run=Result())

        required_env_vars = [
            'AWS_DEFAULT_REGION', 'BUCKET', 'BASEURL',
            'CACHE_CONTROL', 'BRANCH', 'CONFIG', 'REPOSITORY', 'OWNER',
            'SITE_PREFIX', 'GENERATOR', 'AWS_ACCESS_KEY_ID',
            'AWS_SECRET_ACCESS_KEY']

        for env_var in required_env_vars:
            monkeypatch.setenv(env_var, f'{env_var}-value')

        main(ctx)
