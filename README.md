# number-integer-to-number-string
Convert number into polish words [Polish documentation](https://pceuropa.net/blog/pl/konwersja-liczby-na-slowa-python/)

Browser <- Js AJAX -> REST API (django) <->
[numbetostring.py](https://github.com/pceuropa/number-integer-to-number-string/blob/master/app/numbersinword.py) (python3)

Class numbersinword convert number to list. 
On groups of number (by 3 number) iterate two functions: first set name of groups (ex. milionów, tysięcy) second set
name of number in group (ex. sto dwadzieścia). At the end method toString() scale and return string (or False if
exception)


## Download and install packages
```
git clone https://github.com/pceuropa/number-integer-to-number-string.git
cd number-integer-to-number-string
pip3 install -r requirements.txt
```


## Run app django
```
./manage.py runserver
```

## Tests
```
./manage.py test

```
## Execute only python method (without Web API)
```
python3 app/numbersinword.py
```
