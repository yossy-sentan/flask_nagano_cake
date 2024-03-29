import os
# SQLALchemyの設定
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{user}:{password}@{host}/nagano_cake'.format(**{
        'user': os.getenv('DB_USER', 'postgres'),
        'password': os.getenv('DB_PASSWORD', 'himitu'),
        'host': os.getenv('DB_HOST', 'localhost:5432'),
})
SQLALCHEMY_TRACK_MODIFICATIONS = False

# ログイン情報を設定
SECRET_KEY = 'secret_key'