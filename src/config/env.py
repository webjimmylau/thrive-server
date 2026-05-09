from src.config import BaseConfig


# 开发环境
class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root123:123456@127.0.0.1:3306/thrivex'


# 生产环境
class ProduceConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root123:123456@127.0.0.1:3306/thrivex'


# 选择环境
switch = {
    "dev": DevelopConfig,
    "pro": ProduceConfig
}
