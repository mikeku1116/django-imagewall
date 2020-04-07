# django-imagewall #

## 專案介紹 ##

本專案ImageWall(圖片牆)在Django網站框架中，利用Python的Pillow圖片函式庫，開發上傳圖片的功能，並且利用Bootstrap的Card元件來顯示所有圖片，可以搭配[[Django教學9]6個步驟快速搞懂Django上傳圖片的功能](https://www.learncodewithmike.com/2020/04/django-image-upload.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ pipenv migrate`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /photos (例：http://127.0.0.1:8000/photos/) 後，即可看到上傳圖片的畫面。

![Alt text](https://1.bp.blogspot.com/-RxvqluMdUR8/Xox6_Liiz-I/AAAAAAAABys/-qd1fg168FkdrfmAaNb0COu4f4uREZGQgCKgBGAsYHg/s1600/django_imagewall.PNG "Optional title")
