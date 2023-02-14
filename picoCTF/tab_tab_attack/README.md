# Tab, Tab, Attack

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](Addadshashanammu.zip)

## Hints

1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

### Solution

After downloading the file [Addadshashanammu.zip](Addadshashanammu.zip), I executed the [file](https://en.wikipedia.org/wiki/File_(command)) command on it to determine if it's indeed a [zip](https://en.wikipedia.org/wiki/ZIP_(file_format)) file.

```shell
$ file Addadshashanammu.zip 
Addadshashanammu.zip: Zip archive data, at least v1.0 to extract
```

Once I verified that it's a zip file, I used the `unzip` command to extract the archive.

```shell
$ unzip Addadshashanammu.zip 
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
  ```

Using [tab completion](https://en.wikipedia.org/wiki/Command-line_completion) in Bash, I continued to press tab until no more directories were being appended to the path.

```shell
cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
```

I changed into that directory, and found an [ELF file](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format). The flag was printed after executing that file.

```shell
$ ls
fang-of-haynekhtnamet

$ file fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b71f20bc162221a31840f68a978261097ecadac2, not stripped


$ ./fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}
```

#### Flag

```
picoCTF{l3v3l_up!_t4k3_4_r35t!_6f332f10}
```
