# You Can't See Me
'...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in /problems/you-can-t-see-me_1_a7045a1e39ce834c26556a81c2b3a74f.

## Solution
There was a hidden file in this directory. I used `ls -alhrt` and I saw that there were no files there. However I failed to realize that the file called `. (dot)` was actually a plain data file rather than a directory (like the current directory).

```
-rw-rw-r--   1 hacksports hacksports   57 Mar 25  2019 .  
drwxr-xr-x   2 root       root       4.0K Mar 25  2019 .
drwxr-x--x 556 root       root        52K Mar 25  2019 ..
```

The solution is to execute `cat .*`:

```
cat: .: Is a directory
picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_f01e45c4}
cat: ..: Permission denied
```
