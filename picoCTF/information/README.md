# Information

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](cat.jpg).


## Hints

1. Look at the details of the file
1. Make sure to submit the flag as `picoCTF{XXXXX}`


### Solution

After downloading the [cat.jpg](cat.jpg) file, I immediately ran `file` on it to verify that it's indeed an image.

```shell
$ file cat.jpg 
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```

After verifying that the file is an image, I used `exiftool` to review the [Exif](https://en.wikipedia.org/wiki/Exif) metadata.

```shell
$ exiftool cat.jpg 
ExifTool Version Number         : 12.16
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:15 14:24:46-04:00
File Access Date/Time           : 2023:01:16 22:52:44-05:00
File Inode Change Date/Time     : 2023:01:16 22:52:39-05:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

The `License` metadata resembles [Base64](https://en.wikipedia.org/wiki/Base64) encoded data. Thus, I tried to decode the `License` and found the flag.

```shell
$ echo 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
picoCTF{the_m3tadata_1s_modified}
```


#### Flag

```
picoCTF{the_m3tadata_1s_modified}
```
