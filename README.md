
# Currency exchange website

## Description

In the project allows to check exchange rate of selected currency in specific day.
User can also check the lowest and the highest exchange rate of currency within number of last quotation(limited to 255).
Rates are based on official NBP data.
Exchange rate for weekends and holidays is not available





## Installation

Install packages from requirements.txt -> pip install -r requirements.txt

In envs directory change name of .env-example file to .env and add your secret key
```
DEBUG=1
SECRET_KEY='YOUR SERCET KEY'
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1'
```

Run app:

```
python manage.py runserver
```


## Usage/Examples

### Exchange rate endpoint

```
http://localhost:8000/exchange/gbp/2023-04-21/

```

Returns

```
{
    "data": {
        "currency": "GBP",
        "date": "2023-04-21",
        "exchange_rate": "5.2086"
    }
}
```

Selected date is weekend, holiday, currency doesn't exist, date format is incorrect or date isn't from past:


```
http://localhost:8000/exchange/gbp/2023-04-23/

```

Returns

```
{
    "data": "Wrong details"
}
```

### The lowest and highest exchange rate within last N quotations

```
http://localhost:8000/min_and_max_value/currency/N
```

For example

```
http://localhost:8000/min_and_max_value/usd/50
```

Returns

```
{
    "data": {
        "currency": "USD",
        "number_of_quotations": 50,
        "min_value": 4.1905,
        "max_value": 4.4888
    }
}
```

If N greater than max number of quotations(255) or currency doesn't exist

```
http://localhost:8000/min_and_max_value/usd/260
```

Returns 

```
{
    "data": "Wrong details"
}
```


### The greatest difference between buy and sell price withi last N quotations

```
http://localhost:8000/difference/currency/N
```

For example

```
http://localhost:8000/difference/jpy/50
```

Returns

```
{
    "data": {
        "currency": "JPY",
        "number_of_quotations": 50,
        "max_value": 0.0007
    }
}
```

If N greater than max number of quotations(255) or currency doesn't exist

```
http://localhost:8000/difference/usd/260
```

Returns

```
{
    "data": "Wrong details"
}
```
## Running Tests

To run tests, run the following command

```
  python manage.py test
```

