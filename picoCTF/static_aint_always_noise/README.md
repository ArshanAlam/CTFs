# Static ain't always noise

Can you look at the data in this binary: [static](static)? This [BASH script](ltdis.sh) might help!

## Hints

(no hints)


### Solution

After downloading the [static](static) file, I executed the `file` command on it.

```shell
$ file static 
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=277d07901cf99a335a8107fbdd6642d9c6140bb5, not stripped
```

After seeing that the binary file is `not stripped` I decided to run the [strings](https://en.wikipedia.org/wiki/Strings_(Unix)) command on the binary. The reasoning behind this is that the flag could possibly be a statically defined string.

```shell
$ strings static 
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
AWAVI
AUATL
[]A\A]A^A_
Oh hai! Wait what? A flag? Yes, it's around here somewhere!
;*3$"
picoCTF{d15a5m_t34s3r_f5aeda17}
GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7698
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
static.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
_edata
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
flag
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```


I noticed the flag in the output. We could use [grep](https://en.wikipedia.org/wiki/Grep) to get only the flag string.

```shell
$ strings static | grep -o "picoCTF{.*}"
picoCTF{d15a5m_t34s3r_f5aeda17}
```


#### Flag

```shell
picoCTF{d15a5m_t34s3r_f5aeda17}
```