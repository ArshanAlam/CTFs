# In Out Error
Can you utilize stdin, stdout, and stderr to get the flag from this program? You can also find it in /problems/in-out-error_2_c33e2a987fbd0f75e78481b14bfd15f4 on the shell server

## Solution
The flag was in written to `stderr`.

### Exploit
```
cat input | ./in-out-error > /dev/null
```
