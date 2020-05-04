# Lying Out

Some odd [traffic](traffic.png) has been detected on the network, can you identify it? More [info](info.txt) here. Connect with `nc 2018shell.picoctf.com 39410` to help us answer some questions.


### info.txt
```
$ cat info.txt 
You've been given a dataset of 4800 internet traffic logs for your
organization's website. This dataset covers the number of unique IP addresses
sending requests to the site in 15-minute "buckets", across a 24-hour day.
The attached plot will help you see the daily pattern of traffic. You should
see 3 spikes of traffic: one in the morning, one at midday, and one in the
evening.

Your organization needs your help to figure out whether some recent activity
indicates unusual behavior. It looks like some logs have higher-than-usual
traffic in their time bucket: many more unique IP addresses are trying to
access the site than usual. This might be evidence that someone is trying to
do something shady on your site.
```


# Solution
Identify anomalous traffic by looking at the [traffic image](traffic.png) and the printed output.


```
$ nc 2018shell.picoctf.com 39410
You'll need to consult the file `traffic.png` to answer the following questions.


Which of these logs have significantly higher traffic than is usual for their time of day? You can see usual traffic on the attached plot. There may be multiple logs with higher than usual traffic, so answer all of them! Give your answer as a list of `log_ID` values separated by spaces. For example, if you want to answer that logs 2 and 7 are the ones with higher than usual traffic, type 2 7.

log_ID      time  num_IPs
0        0  00:15:00    10235
1        1  04:15:00     9594
2        2  06:30:00     9772
3        3  08:15:00    14902
4        4  12:15:00    14847
5        5  15:00:00    11662
6        6  15:15:00    11624
7        7  15:30:00    10718
8        8  16:15:00    10079
9        9  16:45:00     9984
10      10  17:15:00    11241
11      11  20:00:00     9775
12      12  20:45:00    11598
13      13  23:45:00    10020

```

My answer was `3 5 6 12`.

```
3 5 6 12
Correct!


Great job. You've earned the flag: picoCTF{w4y_0ut_940df760}
```
