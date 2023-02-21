# keygenme-py

[keygenme-trial.py](keygenme-trial.py)

## Hints

(None)

### Solution

After downloading the [keygenme-trial.py](keygenme-trial.py) file, I executed the [file](https://en.wikipedia.org/wiki/File_(command)) command on it.

```shell
$ file keygenme-trial.py 
keygenme-trial.py: Python script, ASCII text executable, with very long lines
```

After confirming that the file is a [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) script, I decided to view the script. The application has a main loop that allows us to `Enter License Key`.

```shell
$ python keygenme-trial.py 

===============================================
Welcome to the Arcane Calculator, SCHOFIELD!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy. 
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, SCHOFIELD (a/b/c/d)?
```

Tracing the logic, we discover that the `Enter License Key` will result in the execution of `enter_license()` and ultimately `check_key(key, username_trial)`.

```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False



        return True
```

Examining the code above, we discover that to crack the key we'll have to solve for `key_part_dynamic1_trail`. Reviewing the code, we see that the `key_part_dynamic1_trail` is calculated by taking the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the `username_trial → b"SCHOFIELD"`. Thus, we could write a [Keygen](https://en.wikipedia.org/wiki/Keygen) to generate the key and thereby the flag.

```python
import hashlib

def crack_dynamic(username: bytes) -> str:
  result = list()
  hash_dex_digest = hashlib.sha256(username).hexdigest()

  result.append(hash_dex_digest[4])
  result.append(hash_dex_digest[5])
  result.append(hash_dex_digest[3])
  result.append(hash_dex_digest[6])
  result.append(hash_dex_digest[2])
  result.append(hash_dex_digest[7])
  result.append(hash_dex_digest[1])
  result.append(hash_dex_digest[8])

  return "".join(result)


if __name__ == "__main__":
  key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
  cracked_dynamic_part = crack_dynamic(b"SCHOFIELD")
  key_part_static2_trial = "}"

  key = "{}{}{}".format(key_part_static1_trial, cracked_dynamic_part, key_part_static2_trial)
  print(key)
```

Running the script above will print the license key which is also the flag.

```shell
$ python crack_key.py 
picoCTF{1n_7h3_|<3y_of_e584b363}

$ python keygenme-trial.py 

===============================================
Welcome to the Arcane Calculator, SCHOFIELD!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy. 
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, SCHOFIELD (a/b/c/d)? c

Enter your license key: picoCTF{1n_7h3_|<3y_of_e584b363}

Full version written to 'keygenme.py'.

Exiting trial version...

===================================================

Welcome to the Arcane Calculator, tron!

===================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) Estimate Astral Slingshot Approach Vector
(c) Exit Arcane Calculator
What would you like to do, tron (a/b/c)? c
Bye!
```

#### Flag

```
picoCTF{1n_7h3_|<3y_of_e584b363}
```
