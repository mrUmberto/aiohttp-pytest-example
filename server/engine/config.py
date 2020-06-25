import os

class BasicConfig(object):

    @property
    def db_name(self):
        return os.environ.get('POSTGRES_DB')

    @property
    def db_user(self):
        return os.environ.get('POSTGRES_USER')

    @property
    def db_password(self):
        return os.environ.get('POSTGRES_PASSWORD')

    @property
    def db_host(self):
        return os.environ.get('POSTGRES_HOST')

class TestConfig(BasicConfig):

    @property
    def db_name(self):
        return '{}_test'.format(os.environ.get('POSTGRES_DB'))


def get_config(env: str = 'dev') -> BasicConfig:
    config_map = {
        'dev': BasicConfig,
        'test': TestConfig
    }
    return config_map.get(env, BasicConfig)()
