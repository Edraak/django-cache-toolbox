# django-cache-toolbox

This project is some sort of a clone of [django-cache-toolbox](https://pypi.python.org/pypi/django-cache-toolbox/0.2.4) but since it no longer maintained we decided to complete its development to keep our instances synced with the latest [edx-platform](https://github.com/edx/edx-platform) version.

## Installation

```bash
pip install -e git+https://github.com/Edraak/django-cache-toolbox.git@1.0.0#egg=cache_toolbox
```

## Usage

in your settings.py do the following:
1. Comment out these authentication middleware:
    - django.contrib.auth.middleware.AuthenticationMiddleware
    - django.contrib.auth.middleware.SessionAuthenticationMiddleware
1. Add the following authentication middleware:
    - cache_toolbox.middleware.CacheBackedAuthenticationMiddleware
1. Add `cache_toolbox` to your `INSTALLED_APPS`.
1. Set `SESSION_ENGINE`'s value to `'django.contrib.sessions.backends.cache'`.
1. Set `SESSION_COOKIE_NAME`'s value to `'sessionid'`

Your final changes in settings should look like:

```PYTHON
INSTALLED_APPS = [
    # ...
    'cache_toolbox',
    # ...
]

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_NAME = 'sessionid'

MIDDLEWARE_CLASSES = [
    # ...
    'cache_toolbox.middleware.CacheBackedAuthenticationMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # ...
]
```

