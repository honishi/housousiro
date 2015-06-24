housousiro
==

<img src="./document/screenshot/screenshot.png">

* http://housousiro.herokuapp.com/ 

project setup
--
```
# for os x
# brew install pyenv pyenv-virtualenv

pyenv install 3.4.3
pyenv virtualenv 3.4.3 housousiro-3.4.3
pyenv rehash

pip install -r requirements.txt
```

run in local box
--
````
./main.py
````

deploy to heroku
--
```
git push heroku develop:master
```

license
--
copyright &copy; 2015 honishi, hiroyuki onishi.

distributed under the [MIT license][mit].
[mit]: http://www.opensource.org/licenses/mit-license.php
