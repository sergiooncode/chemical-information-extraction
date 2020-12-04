from config.persistence_settings import MONGO_DB_NAME
from config.persistence_settings import MONGO_DB_HOST

PRODUCTION_CONFIG_NAME = "production"
TEST_CONFIG_NAME = "test"
DEFAULT_CONFIG_NAME = "default"


class Config:
    @staticmethod
    def init_app(app):
        """
        If some configuration needs to initialize the app in some way use this function
        :param app: Flask app
        :return:
        """
        pass


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"


class LocalConfig(Config):
    MONGODB_SETTINGS = {"db": MONGO_DB_NAME, "username": "", "password": "", "host": MONGO_DB_HOST, "alias": "default"}
    DEBUG = True
    ENV = "local"


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = "test"


config = {PRODUCTION_CONFIG_NAME: ProductionConfig, TEST_CONFIG_NAME: TestConfig, DEFAULT_CONFIG_NAME: LocalConfig}
