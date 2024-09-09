# The Waroenk

Link PWS : [The Waroenk](http://muhammad-farid31-thewaroenks.pbp.cs.ui.ac.id/)

## Membuat Project Django baru

Pertama-tama saya membuat virutal environment dengan menggunakan perintah 
```
python -m venv env
env\Scripts\activate
```
hal ini bertujuan agar project baru yg saya buat terisolasi dengan project lainnya dan juga untuk menghindari konflik pada dependency antar proyek
Kemudian, tentu saja saya menginstall dependencies yang dibutuhkan pada project django ini. Caranya bisa dengan menulis dependencies (yg ingin diinstall) di suatu file bernama `requirements.txt` yg berisikan 
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
Setelah dibuat, saya menginstallnya dengan menggunakan perintah
```
pip install -r requirements.txt
```
Kemudian, saya membuat proyek baru bernama `the_waroenks` dengan menggunakan perintah
```
django-admin startproject the_waroenks .
```
dan langsung membuat aplikasi dengan nama `main` dengan perintah
```
python manage.py startapp main
```

### Menambahkan `'main'` pada INSTALLED_APPS di file `settings.py`

Setelah itu, saya membuka file `settings.py` dan langsung menambahkan `'main'` didalam array INSTALLED_APPS yang bertujuan agar aplikasi kita bisa diakses oleh django
```python
INSTALLED_APPS = [
    ...,
    'main',
]
```

### Melakukan routing untuk menjalankan aplikasi `main`

Setelah itu, saya membuka file `the_waroenks/urls.py` dan menambahkan kode seperti berikut 
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Tambahkan routing untuk aplikasi main
]
```
hal ini bertujuan untuk mengimport rute URL dari aplikasi `main` yang sedang kita buat

### Membuat model 

Dalam pembuatan model, saya membuka file `models.py` dan menambahkan beberapa model yang wajib yaitu `name, price, description` dan yang sekiranya saya butuhkan kedepannya

### Membuat fungsi di dalam `views.py`

Di dalam `views.py`, kita harus membuat suatu fungsi yang bertujuan untuk mengumpulkan data-data yang berada di model dan akan ditampilkan kedalam template HTML. Disini saya membuat suatu fungsi bernama `show_main(request)` yang berisi beberapa object yang ingin ditampilkan pada HTML.
```python
from django.shortcuts import render

def show_main(request):
    context = {
        ...
        'app_name' : 'The Waroenks',
        'name': 'Muhammad Farid Hasabi',
        ...
    }

    return render(request, "main.html", context) # Mengirimkan data context ke main.html
```

### Membuat routing pada `urls.py` pada aplikasi `main`

Setelah tadi membuat routing untuk akses aplikasi main, saya membuat file `urls.py` pada folder aplikasi `main` dan menulis beberpa kode sebagai berikut
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
hal ini bertujuan agar dapat menghubungkan permintaan pengguna dari URL tertentu ke fungsi di `views.py` yang akan menampilkan data dari model atau `main.html`. 

### Menambahkan link pada ALLOWED_HOSTS
Sebelum kita mendeploy project ktia ke PWS, kita juga harus menambahkan link pws kita pada `settings.py` agar project yang akan kita deploy bisa diakses melalui PWS View Project.
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "muhammad-farid31-thewaroenks.pbp.cs.ui.ac.id"]
```

### Push PWS
Setelah melakukan semua langkah-langkah diatas, saya bisa melakukan `git add, commit, push` ke dalam github saya terlebih dahulu dan dilanjutkan untuk melakukan deploy ke PWS yang telah saya buat.

## Penjelasan bagan request client web dan kaitannya dengan urls.py, models.py, views.py, dan html.

![django_77d5263d13](https://github.com/user-attachments/assets/840247fb-c9ab-402d-95b2-401bf3963ac6)

1. Client Request:
<br>Pengguna (client) mengakses URL tertentu melalui browser atau aplikasi.

2. urls.py:
<br>Django mencocokkan URL yang diminta oleh pengguna dengan pola yang telah dibuat dan diteruskan ke views

3. Views (views.py):
<br>View adalah fungsi yang mengatur logika, mengambil data dari model, mengambil request dari client, memprosesnya, dan mengembalikan respons.

4. Models (models.py):
<br>Berisi tabel database dan hubungan antara tabel yang diperlukan kemudian dikembalikan ke views.py

5. Templates (HTML files):
<br>Mengatur tampilan halaman dan dirender oleh views.py dengan data yang telah disiapkan.

6. Server/Client Response:
<br>Setelah view memproses permintaan, server mengirimkan kembali respons ke client.


## Fungsi git dalam pengembangan perangkat lunak

1. Version Control
   <br> Git dapat melacak setiap perubahan yang dilakukan oleh pengembang sehingga mereka dapat mudah untuk mengetahui kesalahan dan perubahan yang telah mereka lakukan.
2. Kolaborasi
   <br>Git dapat memberikan akses untuk banyak pengguna yang memungkingkan untuk bekerja secara bersamaan tanpa ada bentrok satu sama lain. Pengembang dapat membuat branch terpisah dan dapat digabungkan dengan merge.

3. Branching dan Merging
   <br>Git memberikan fleksibilitas kepada pengembang yang memungkingkan pengembang dapat menambah, memperbaiki, merubah kode dalam cabang terpisah dari kode utama. Branching dapat memudahkan pemngembang untuk bekerja sama secara paralel yang kemudian dapat dimerge ke dalam kode utama.

4.  Backup dan recovery
    <br>Apabila terjadi masalah atau kerusakan file lokal, maka git dapat dengan mudah untuk memulihkan kode dari repo pusat.

5. Open Source Contribution
   <br>Pengembang dapat membuat fork dari proyek, menambah fitur, dan mengirimkan perubahan kembali ke proyek utama melalui pull request.

## Alasan Kenapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak
1. Django merupakan framework full-stack yang mencakup front-end maupun back-end. Ini dapat memungkinkan kita dapat memahami seluruh alur kerja aplikasi atau website. 
   
2. Memiliki banyak fitur bawaan yang sangat berkorelasi untuk developer. Fitur-fitur tersebut termasuk ORM (Object-Relational Mapping), manajemen sisi, sistem autentikasi, dsb.
   
3. Django memiliki struktur yang mudah dipahami, terutama dalam struktur projek yang jelas. Hal ini memudahkan kita untuk memahami alur kerja web, yg dimulai dari URL routing, view, model, template, hingga request dan respon client web.
   
4. Menggunakan pola arsitektur MVC (Model-View Controller) atau dikenal sebagai MVT yg merupakan best practice untuk memahami pengembangan aplikasi web.

# Alasan kenapa model pada Django disebut sebagai ORM?

ORM adalah suatu teknik yang memungkinkan kita memanipulasi data dalam database relasional menggunakan Object-oriented Programming (OOP) yang juga memungkinkan pengguna dapat berinteraksi dengan database melalui pyhton tanpa harus menggunakan query SQL. Kemudian, Mapping dalam Django secara otomatis dapat langsung memetakan atribut model ke tabel dalam database. Dengan demikian, alasan mengapa model pada Django disebut sebagai ORM


