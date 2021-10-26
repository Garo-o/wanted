class Config():
    JWT_SECRET_KEY = 'JUSEONG_HONG'
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 30           # 30 min
    JWT_REFRESH_TOKEN_EXPIRES = 60 * 60 * 24 * 7 # 7 days