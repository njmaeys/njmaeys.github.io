![](images/NMFA_Color_White.png)
This is my github.io hosted pages for my artwork

---
## API Wrapper

In the `src` dir I have a wrapper FastAPI around the Etsy V3 API for shop listings. It's a little jank if I'm being honest but it does what I need. This should always be able to keep the token and refresh up to speed.

**.env**
```
API_KEY=""
REDIRECT_URL="https://www.natemaeysfineart.com"
SHOP_ID="37858119"
```

**Running**

It's important to remember (for myself) that this is running on the living room ubuntu machine. If it ever has issues check the logs in `/src/app/nohup.out`. 

If I ever need to restart the service make sure to activate the virtualenv then run as a background process.

```shell
$ cd src/app
$
$ nohup python runner.py &
```

Also, for reasons I couldn't use a default port so it's running at `1024` and I need to specify that in the requests to the `A` record serving at `api.natemaeysfineart.com`.

**Certificates**

Eventually the certs will expire and Porkbun automatically creates new ones. Once they expire grab them and put them in the server and restart the app.

---
### Credits

Massively by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

Further Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Scrollex (github.com/ajlkn/jquery.scrollex)
		Responsive Tools (github.com/ajlkn/responsive-tools)
