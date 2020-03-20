# Leak Me

By executing `python -c "print('a'*255)" | nc 2018shell.picoctf.com 57659` we get the password that could be used to retrieve the flag.

## How does it work?
This exploit takes advantage of the fact that `strcat()` removes the null terminator from the destination string and appends the source string right after it. So by sending a long name, say 255 characters long, `strcat()` removes the null terminator of the name and appends `",\nPlease Enter the Password."` in the `password` buffer. Afterwards, the password is read from file and put in the password buffer. Finally after reading the password, the name is printed. Since the name is no longer null terminated, the password is also printed.


### The stack layout

|-------------------| <-- High Memory Address
| password          |
|-------------------|
| name              |
|-------------------|
| password_input    |
|-------------------| <-- Low Memory Address
