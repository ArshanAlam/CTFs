# GET aHEAD

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:45028/](http://mercury.picoctf.net:45028/)


## Hints

1. Maybe you have more than 2 choices
1. Check out tools like Burpsuite to modify your requests and look at the responses


### Solution

The trick to this challenge is to realize that there are more than two types of requests; here is a list of [request methods](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods).


Looking at the source code, we see that we could submit two types of requests. Namely `GET` and `POST`. However, considering that HTML has more request methods, it's possible that the backend does not properly handle those requests.


```html
<!doctype html>
<html>
<head>
    <title>Red</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<style>body {background-color: red;}</style>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red"/>
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue"/>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
```


Thus, to test our hypothesis we use [cURL](https://en.wikipedia.org/wiki/CURL) to fetch the headers only!


```shell
$ curl --head http://mercury.picoctf.net:45028

HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_775f2530}
Content-type: text/html; charset=UTF-8
```

In the header, we find the flag.


#### Flag

```
picoCTF{r3j3ct_th3_du4l1ty_775f2530}
```