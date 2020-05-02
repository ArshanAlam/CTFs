# Ext Super Magic
We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the [filesystem](ext-super-magic.img) out of the black box. It looks a bit corrupted, but maybe there's something interesting in there. You can also find it in /problems/ext-super-magic_4_f196e59a80c3fdac37cc2f331692ef13 on the shell server.

## Solution
The biggest hint for this problem was in its description. We are dealing with an `Ext SuperMagic II-class ...`. This immediately made me realize that we are dealing with an [ext2 file system](https://en.wikipedia.org/wiki/Ext2).

### Exploit
I ran `fsck` on the provided image.
```
$ fsck $(pwd)/ext-super-magic.img
fsck from util-linux 2.29.2
e2fsck 1.43.4 (31-Jan-2017)
ext2fs_open2: Bad magic number in super-block
fsck.ext2: Superblock invalid, trying backup blocks...
fsck.ext2: Bad magic number in super-block while trying to open /home/perry/git/self/picoCTF/ext_super_magic/ext-super-magic.img

The superblock could not be read or does not describe a valid ext2/ext3/ext4
filesystem.  If the device is valid and it really contains an ext2/ext3/ext4
filesystem (and not swap or ufs or something else), then the superblock
is corrupt, and you might try running e2fsck with an alternate superblock:
    e2fsck -b 8193 <device>
     or
         e2fsck -b 32768 <device>
```

From the output above I discovered that the magic number was incorrect. I searched around and found this post [What's a file system's “magic” number in a super block?](https://superuser.com/questions/239088/whats-a-file-systems-magic-number-in-a-super-block). From this I learned that the magic number for an ext2 file system is `0x53 0xEF at positions 1080–1081`.

After some more searching I discovered a way to update bytes of a file at a given offset. So to fix this image I ran
```
$ printf  '\x53\xEF' | dd of=ext-super-magic.img bs=1 seek=1080 count=2 conv=notrunc                     
2+0 records in
2+0 records out
2 bytes copied, 5.5883e-05 s, 35.8 kB/s
```

Now we could mount the file system image:
```
$ fuse2fs ext-super-magic.img mount/
```

The flag is in an image within the mounted directory [mount/flag.jpg](flag.jpg).

### Flag
```
picoCTF{a7DB29eCf7dB9960f0A19Fdde9d00Af0}
```


## Hints
- Are there any [tools](https://en.wikipedia.org/wiki/Fsck) for diagnosing corrupted filesystems? What do they say if you run them on this one?
- How does a linux machine know what [type](https://www.garykessler.net/library/file_sigs.html) of file a [file](https://linux.die.net/man/1/file) is?
- You might find this [doc](https://www.nongnu.org/ext2-doc/ext2.html) helpful.
- Be careful with [endianness](https://en.wikipedia.org/wiki/Endianness) when making edits.
- Once you've fixed the corruption, you can use /sbin/[debugfs](https://linux.die.net/man/8/debugfs) to pull the flag file out.
