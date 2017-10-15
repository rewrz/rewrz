"""
Django settings for rewrz project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 请在部署之前更改此设定值
SECRET_KEY = '**69ciu_h1%1zy3=5h9#k2_kqu(ex@@ob%rh=elhy3nxrny0ab'

# SECURITY WARNING: don't run with debug turned on in production!
# 根据系统变量决定是否开启调试功能
# 因为我是在Windows10上做的开发，Linux上面部署，所以这样设置。请按照实际情况设置逻辑。
if 'windir' in os.environ:
    DEBUG = True
else:
    DEBUG = False

# 允许访问的主机，请按照实际情况设置
ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', '.rewrz.com']

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp', # Add Two Factor Authentication (2FA)
    'django_otp.plugins.otp_totp', # Add Two Factor Authentication (2FA)
    'axes', # django-axes 限制用户登陆尝试次数
    'ckeditor',# ckeditor富文本编辑器
    'ckeditor_uploader',# ckeditor富文本编辑器
    'haystack',# 全文搜索
    'blog', # 注册 blog 应用
    'comments', # 注册 comments 应用
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware', # 开启gzip压缩
    'htmlmin.middleware.HtmlMinifyMiddleware', # HTML压缩
    'htmlmin.middleware.MarkRequestMiddleware', # HTML压缩
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware', # 2FA
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'rewrz.urls'

# HTML压缩强制开启，默认会在生产环境开启
HTML_MINIFY = True
# Django-Compressor 静态文件压缩暂未使用
# CACHES功能暂未使用

TEMPLATES = [
    #{
    #    'BACKEND': 'django.template.backends.jinja2.Jinja2',
    #    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    #    'APP_DIRS': True,
    #    'OPTIONS': {
    #        'environment': 'rewrz.jinja2_env.environment',
    #    },
    #},
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rewrz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 设置语言为中文
LANGUAGE_CODE = 'zh-Hans'

# 设置时区为上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# ckeditor富文本编辑器设置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',
        # 'skin': 'moono-lisa',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['CodeSnippet', 'Source', '-', 'Save', 'Preview']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Iframe']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize','Preview']},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'clipboard',
            'widget',
            'lineutils',
            'dialog',
            'dialogui',
            'codesnippet',
            'elementspath'
        ]),
    }
}

# 全文搜索 HAYSTACK 配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Django JET 设置
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# ===安全性设置===
# OTP 设置（2FA）
OTP_TOTP_ISSUER = 'RewrZ Inc.'
OTP_ENABLE = False # 自定义的开关

# django-Axes设置
# https://django-axes.readthedocs.io/en/latest/configuration.html
AXES_LOGIN_FAILURE_LIMIT = 3
AXES_LOCK_OUT_AT_FAILURE =True

# 如果启用HTTPS，请将下面两项设置为：True
CSRF_COOKIE_SECURE = False # 将此设置为True可避免意外传输HTTP上的CSRF Coo​​kie
SESSION_COOKIE_SECURE = False # 将此设置为True可避免意外地通过HTTP传输会话Cookie


# 网站设置
# ====后台设置====
ADMIN_SITE_HEADER = "RewrZ" # 后台头部
ADMIN_INDEX_TITLE = 'RewrZ' # 后台标题
ADMIN_SITE_TITLE = '最終のリライト' # 后台管理员副标题
# ====前台设置====
SITE_TITLE = 'RewrZ' # 网站标题
SITE_SUBTITLE = '最終のリライト' # 网站副标题
SITE_DESCRIPTION = '向那遥远的星球发誓，再也不会离开你，将所有一切，全部改写吧！' # 网站描述
BLOG_PAGINATE_NUM = 9 # 文章分页
COMMENT_PAGINATE_NUM = 5 # 评论分页
# ===是否开启固定链接美化===
POST_FIXED_LINK = True