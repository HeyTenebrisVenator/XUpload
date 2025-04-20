# XUpload
XUpload is a script made with python that allow you to search for web pages that have some file upload function

What do you like to test?

*XSS?*

*SQLI?*

*RCE?*

What would you do if i tell you that you can test all those flaws only in one situation? Yes, you got it! File Upload!

The *XUpload* is a tool developed to make your life easier when we are talking about looking for upload features.

## HOW TO USE IT?

First, you need to download the file

To do this, you run the code:

```sudo git clone https://github.com/HeyTenebrisVenator/XUpload.git```

After that, you'll need to install the requirements.txt, that contains the libraries needed to run correctly

```sudo pip install -r requirements.txt```

So, after all this, you need to run the script:

```sudo python3 xupload.py```

OK! So now we can search for upload fields!

But first, you'll need to give to the script a file containing URLs.

```Where is the file with the URLs  >>  urls.txt```

Great, now you give a directory with a file where the results will be saved

```Where do you want to save the output? leave in blank if you don't want to save  >>   save.txt```

And then, how many processes do you want running?

```How many processes do you want? (Recomended: 4)  >>  4```


# HOW IT WORKS?

The script will get the URLs from the list that you gave to it.

And then, it'll make a requests, asking for the html of the page.

fter that, the script will look for *key works*, such as *<input* and *type="file"*
