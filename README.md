# thinrest

#### Very thin layer over Django to implement REST API using [Tastypie library](https://github.com/django-tastypie/django-tastypie).

## Technology
* Python 2.7
* Django 1.5
* Tastypie 0.12.2

## Aim

To build a simple interface that can provide for CRUD operations for two types of Database tables:
1. Column based e.g. EMPLOYEE(FIRST_NAME, LAST_NAME, ADDRESS, CITY, STATE, ZIP)

2. Key Value pairs e.g. SYSTEM_SETTINGS(SETTING_NAME, SETTING_VALUE)

## Quick start

1. ```pip install thinrest```

2. Add `thinrest` to your `INSTALLED_APPS` setting:

    ```python
        INSTALLED_APPS = (
            ...
            'thinrest',
        )
    ```

3. Include the thinrest URLs to a path of your choice

    ```python
    patterns = ('',
        ...
        url(r'^thinrest/', include('thinrest.urls')),
    )
    ```

## Bugs & Contributions

Please report bugs by opening an issue
