# DISKO 1

Can you find the flag in this [disk image](./disko-1.dd.gz)?

# Solution

After downloading the [disk image](./disko-1.dd.gz), I ran `file` on it to determine if it's truly a compressed file:

```shell
file disko-1.dd.gz
```
```shell
disko-1.dd.gz: gzip compressed data, was "disko-1.dd", last modified: Thu May 15 18:48:28 2025, from Unix, original size modulo 2^32 52428800
```

Next I ran `strings` on the compressed file to determine if the flag is written as a string on the file.

```shell
strings disko-1.dd.gz | grep 'picoCTF'
```

This didn't return any results.

Next, I checked the size of the compressed file to ensure the uncompressed file is a reasonable size.

```shell
gzip -l disko-1.dd.gz
```
```shell
         compressed        uncompressed  ratio uncompressed_name
           20484476            52428800  60.9% disko-1.dd
```

The uncompressed file is `50 MB` in size, which seems reasonable. Next I extracted the contents of the compressed file:

```shell
gzip -d disko-1.dd.gz
```

This extracted a new `disko-1.dd` file in the current directory.

Executing `strings` on this new file resulted in the flag.

```shell
strings disko-1.dd | grep 'picoCTF'
```

## Flag

```shell
picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}
```

# Hints

1. Maybe Strings could help? If only there was a way to do that?