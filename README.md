# number-integer-to-number-string
Convert integer to number in polish words

Browser <- Js AJAX -> REST API (django) <->
[numbetostring.py](https://github.com/pceuropa/number-integer-to-number-string/blob/master/app/numbersinword.py) (python3)

2. Class numbersinword convert number to list. 
   On groups of number (by 3 number) iterate two functions: first set name of groups (ex. milionów, tysięcy) second set
   name of number in group (ex. sto dwadzieścia). At the end method toString() scale and return string (or False if
   exception)

## Run app django
```
./manage.py runserver
```

## Tests
```
./manage.py test
```
## Run only python methon to convert
```
python3 app/numbersinword.py
```
