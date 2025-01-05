# Verify

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

`ssh -p 61149 ctf-player@rhea.picoctf.net`

Using the password `6abf4a82`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

Checksum: `b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2`

To decrypt the file once you've verified the hash, `run ./decrypt.sh files/<file>`.

## Solution

We are provided a set of files in `./files` and a checksum in the description. We need to find the correct file to decrypt.

We could use the `sha256sum` command and write something like this:

```shell
cd files
ls | xargs -I{} sha256sum {} | grep 'b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2'
```

```shell
b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2  451fd69b
```

This suggests that `451fd69b` should be decrypted. After decrypting the file, we find the flag.

```shell
decrypt.sh files/451fd69b
```

### Flag

<details>

```shell
picoCTF{trust_but_verify_451fd69b}
```

</details>
