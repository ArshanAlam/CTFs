# Matryoshka doll

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](dolls.jpg)

## Solution

In this problem, you'll notice that the image `dolls.jpg` has the `jpg` extension however the file is a `PNG` image.

```shell
file dolls.jpg
```

```shell
dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
```

Furthermore, when I use `unzip -t` to *test* whether the file is a `zip` I get:

```shell
unzip -t dolls.jpg
```

```shell
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
    testing: base_images/2_c.jpg      OK
No errors detected in compressed data of dolls.jpg
```

This is indeed a `zip` file that we could `unzip`!

```shell
unzip dolls.jpg
```

```shell
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg
```

This will give us another file. We continue to `unzip` the nested files to eventually get the `flag.txt` file.

### Flag

Flag could be found in `base_images/base_images/base_images/flag.txt`.

<details>

```shell
picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}
```

</details>
