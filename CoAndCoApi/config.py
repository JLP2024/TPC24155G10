class Config:
    DEBUG = True
    TESTING = True

    #Configuración de base dedatos 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Kimao@localhost:3306/coandco"
   

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'jlp'
    DEBUG = True
    TESTING = True
    from os.path import abspath, dirname, join
# Define the application directory
    BASE_DIR = dirname(dirname(abspath(__file__)))
# Media dir
    MEDIA_DIR = join(BASE_DIR, 'CoAndCoApi')
    POSTS_STATIC_DIR = join(MEDIA_DIR, 'static')
    POSTS_IMAGES_DIR = join(POSTS_STATIC_DIR, 'imagenes')