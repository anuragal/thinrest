# thinrest

#### Very thin layer over Django to implement REST API using [Tastypie library](https://github.com/django-tastypie/django-tastypie).

## Technology
* Python 2.7
* Django 1.5.12
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

3. Include the thinrest URLs

    ```python
    patterns = ('',
        ...
        url(r'^thinrest/', include('thinrest.urls')),
    )
    ```

## Usage

####Employee Table

Sample Data:

```{
    "fields": {
        "first_name": "Anurag",
        "last_name": "Agarwal",
        "address": "Wakad",
        "city": "Pune",
        "state": "Maharashtra",
        "zip_code": "411057"
    },
    "model": "thinrest.employee",
    "pk":1
}```

Employee LIST: GET http://www.example.com/thinrest/api/v1/employee?format=json

Employee DETAIL: GET http://www.example.com/thinrest/api/v1/employee/1?format=json

Employee CREATE / UPDATE: POST http://www.example.com/thinrest/api/v1/employee/

Employee DETELE: DELETE http://www.example.com/thinrest/api/v1/employee/1/

####Settings Table

Settings table is a key-value pair type table. Passing `id` to REST will not work for this type of table. So little tweaking is done in api of this table to handle column `name` as input param.

Sample Data:

```{
    "fields": {
        "name": "email",
        "value": 1
    },
    "model": "thinrest.systemsetting",
    "pk": 1
}```

Setting LIST: GET http://www.example.com/thinrest/api/v1/setting?format=json

Setting DETAIL: GET http://www.example.com/thinrest/api/v1/setting/email?format=json

Setting CREATE / UPDATE: POST http://www.example.com/thinrest/api/v1/setting/

Setting DETELE: DELETE http://www.example.com/thinrest/api/v1/employee/setting/email/

## Running Test

```python manage.py test```

## Bugs & Contributions

Please report bugs by opening an issue
