# Buttons
There is a website running at [http://2018shell.picoctf.com:65107](http://2018shell.picoctf.com:65107). Try to see if you can push their buttons.

## Solution
There are two pages, each with a button. After pressing the button on the second page the request fails. The form is generated on the second page however no button is created to submit the form. So the solution is to create a submit button in the form using Chrome DevTools and pressing submit. This could be emulated by sending a post request to that page using curl `curl -XPOST http://2018shell.picoctf.com:65107/button2.php`.
