Python 3 and higher

## What:
simple_brute_force

## Why:
Brute force all possible easy and short passwords to enter the site

## How:
Python Run command in Terminal:
```
> python main.py localhost 9090  # "localhost" - server address and "9090" - port
password
```

-------------------------------------------------------------------------------

## What:
typical_passwords_hacker

## Why:
Capable of cracking more complex passwords using a database of 1,000 real
passwords with a case change of different letters

## How:
Python Run command in Terminal:
```
> python main.py localhost 9090  # "localhost" - server address and "9090" - port
qWeRTy
```

-------------------------------------------------------------------------------

## What:
exception_catcher

## Why:
Able to crack a login with a dictionary of different logins and a complex
password randomly generated from several characters.
Cracker relies on a server return vulnerability: "An exception occurred during
login" when it found one valid character.
The server uses JSON.
1. Will try all logins with an empty password.
2. When it finds a login, it will try all possible passwords of length 1.
3. When an exception occurs, it knows that it has found the first letter of the
password.
4. Uses the found login and the found letter to find the second letter of the
password.
5. Repeats until it receives a success message.
Finally, the program outputs the username and password combination in JSON
format.

## How:
1. Run test_server
2. Python Run command in Terminal:
> python main.py localhost 9090
{"login": "new_user", "password": "Sg967s"}

-------------------------------------------------------------------------------

## What:
ping_exception_catcher

## Why:
The same as the previous cracker, but now it calculates the time period for which
the response arrives and finds out which initial characters are suitable for the
password.
As a result, it uses the time vulnerability to find the password.

## How:
Python Run command in Terminal:
> python main.py localhost 9090  # "localhost" - server address and "9090" - port
{"login": "admin3", "password": "mlqDz33x"}
