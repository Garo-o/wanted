import datetime


class Config:
    JSON_SORT_KEYS = False
    JWT_SECRET_KEY = 'JUSEONG_HONG'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=7)
    DEBUG = True
