# The Waroenks

Nama : Muhammad Farid Hasabi <br>
NPM  : 2306152512 <br>
Kelas : PBP D <br>
Link PWS : [The Waroenks](http://muhammad-farid31-thewaroenks.pbp.cs.ui.ac.id/)
<hr>

# TUGAS 5

##  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Ketika beberapa selector diterapkan pada elemen yang sama, ada aturan prioritas yang menentukan gaya mana yang akan diterapkan. Urutan prioritas ini diurutkan sebagai berikut:
  1. Inline Styles (contoh style="color: tomato;") memiliki prioritas tertinggi karena gaya ini paling spesifik untuk elemen tersebut.
  2. ID Selector (contoh #first{ color: tomato; }) memiliki prioritas lebih tinggi dari class atau elemen karena setiap elemen hanya boleh memiliki satu ID unik.
  3. Class Selector (contoh .myClass { font-size: 10px; }) memiliki rioritas lebih rendah dari ID selector, tetapi lebih spesifik daripada element selector.
  4. Tag Selector (contoh p { font-family: Arial; }) memiliki prioritas rendah karena menargetkan semua elemen dengan jenis yang sama.
  5. Aturan Umum (contoh * { margin: 0; padding: 0; }) Mempengaruhi semua elemen di halaman dan memiliki prioritas paling rendah.
## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design adalah konsep pengembangan website yang memungkinkan tampilan website menyesuaikan diri secara otomatis dengan ukuran layar perangkat yang digunakan oleh pengguna. 
### Manfaat responsive design:
  * Pengalaman pengguna yang lebih baik: Pengguna dapat mengakses website dengan mudah dari berbagai perangkat.
  * SEO yang lebih baik: Website yang responsive cenderung memiliki peringkat yang lebih tinggi di mesin pencari.
  * Biaya pengembangan yang lebih rendah: Anda hanya perlu membuat satu versi website untuk semua perangkat.
### Contoh website yang responsive:
  * Instagram
  * Wikipedia
### Contoh website yang belum responsive:



## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

![image](https://github.com/user-attachments/assets/d1e00a22-7ac1-4478-8115-c87f7e35b4a6)

* Margin: Merupakan ruang kosong di luar batas suatu elemen. Margin digunakan untuk mengatur jarak antara elemen satu dengan elemen lainnya.
* Border: Adalah garis batas yang mengelilingi suatu elemen.
* Padding: Merupakan ruang kosong di dalam batas suatu elemen, antara konten dan batas elemen tersebut. Padding digunakan untuk memberikan ruang pada konten di dalam elemen.

### Implementasi
```css
.box {
  width: 200px;
  background-color: lightblue;
  border: 2px solid black;  /* */
  padding: 20px;
  margin: 20px;
}
```


## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
### Flex Box
Flexbox dirancang untuk tata letak satu dimensi, baik itu secara horizontal (baris) atau vertikal (kolom). Flexbox mudah digunakan untuk layout yang lebih sederhana, seperti navbar, header, atau footer. <br>
Contoh penggunaannya :
* Membuat navbar yang responsif
* Menyusun kartu produk dalam satu baris
* Membuat formulir dengan label dan input yang sejajar <br>
Implementasi :
```css
.container {
  display: flex;
  justify-content: space-between;
}
```
### Grid
Grid Layout adalah sistem tata letak dua dimensi yang lebih kuat dan fleksibel daripada Flexbox. Grid memungkinkan pengaturan elemen baik dalam baris maupun kolom secara bersamaan.Grid juga cocok untuk layout yang lebih rumit, seperti tata letak utama halaman web dengan sidebar dan konten utama. <br>
Contoh penggunaan : 
* Membuat layout halaman utama dengan sidebar dan konten utama
* Membuat galeri gambar dengan beberapa kolom
* Membuat tata letak tabel yang kompleks

Implementasi : 
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr;
}
```
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!

### Implementasi edit_product dan delete_product pada views.py
* Pada `views.py`,tambahkan beberapa kode sebagai berikut agar kita dapat mengimplementasi edit dan delete product pada aplikasi main 
```python
 def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
      form.save()
      return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

 def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    
    return HttpResponseRedirect(reverse('main:show_main'))
```
* Lakukan routing pada urls.py
```python
...
path('edit-product/<uuid:id>', edit_product, name='edit_product'),
path('delete/<uuid:id>', delete_product, name='delete_product'),
```

* Menambahkan file `edit_product.html` pada direktori `main/templates`
* Menambahkan button pada setiap product agar dapat diimplemen pada tiap produknya
```html
<tr>
 ...
 <td>
     <a href="{% url 'main:edit_product' product.pk %}">
         <button>
             Edit
         </button>
     </a>
 </td>
 <td>
     <a href="{% url 'main:delete_product' product.pk %}">
         <button>
             Delete
         </button>
     </a>
 </td>
</tr>
```
### Kustomisasi daftar product dan membuatnya menjadi responsif

* Buat direktori `static/css` pada root folder untuk menerapkan css pada template di aplikasi main dan Setting Static files pada `settings.py` sebagai berikut

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
...
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
...

```

* Menambahkan file  `global.css` pada `main/css` dan menghubungkan file css tersebut dengan cara 
```html
<head>
   ...
   <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
</head>
```












<hr>

# TUGAS 4

## Apa perbedaan antara HttpResponseRedirect() dan redirect()?

Fungsi `HTTPResponseRedirect()` merupakan class bawaan Django yang menyediakan respon HTTP 302 untuk mengarahkan pengguna ke URL yang telah ditentukan. Pada fungsi ini kita diharuskan untuk menentukan secara eksplisit URL tujuan.

fungsi `redirect()` merupakan fungsi yang dibangun atas `HTTPResponseRedirect`, bertujuan untuk menyederhanaakan proses pembuatan  respon tujuan. Fungsi ini juga lebih fleksibel karena bisa menerima URL, nama view, atau instance model, sehingga lebih mudah digunakan dalam berbagai situasi.

## Jelaskan cara kerja penghubungan model Product dengan User!

Pertama, import User dari model bawaaan Django. Model ini digunakan untuk menghubungkan data produk dengan data pengguna.
Kedua, mendefinisikan `foreign key` pada model product untuk menghubungkan satu pengguna dengan satu product atau sebaliknya.
Ketiga, menambahkan atribut tambahan berupa foreign key yang berelasi dengan model User dengan model Product. ini akan menyimpan informasi tentang siapa pemilik produk atau siapa yang membuatnya. 

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

### Perbedaan
Authentication adalah proses untuk memverifikasi pengguna. Biasanya dengan menggunakan kredensial berupa username dan password.<br>
Authorization adalah proses untuk menentukan hak akses pengguna setelah berhasil terautentikasi. <br>

### Proses saat user login
* pertama, proses authentication dengan meminta username dan password.
* Sistem akan memverifikasi kredensial dari pengguna.
* Jika berhasil, Django membuat sebuah objek User yang mewakili pengguna tersebut dan menyimpannya dalam request.user
* Proses otorisasi untuk mengontrol apa yang bisa dilakukan oleh pengguna berdasarkan peran dan izin mereka.

### Implementasi Authentication dan Authorization pada Django

* Authentication
  * Django menyediakan modul untuk autentikasi berupa `django.contrib.auth`  yang memiliki Model User untuk menangani autentikasi
  * Fungsi `authenticate()` dan `login()` digunakan untuk memeriksa kredensial dan mereturn valid jika berhasil
  * Saat pengguna login, pengguna akan diberikan sesi dan Django menyimpan sesi tersebut menggunakan cookies.
* Authorization
  * Pada tahap ini, Django menyediakan sistem permission untuk memberikan hak akses spesifik yang dapat diterapkan pada model.
  * Kemudian tambahkan `@login_required` untuk melindungi tampilan tertentu agar hanya bisa diakses oleh pengguna yang telah login.


## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
* Django akan membuat sebuah session ID yang unik dan mengirimkannya ke browser pengguna melalui cookie ketika pengguna berhasil login
* Django mengirimkan cookie yang berisi session ID ke browser pengguna dan disimpan di server.
* Setiap kali pengguna mengirimkan permintaan ke server, browser akan menyertakan cookie session ID. Django kemudian akan mengambil data session yang sesuai berdasarkan session ID tersebut
  
### Kegunaan Cookies
* Menyimpan preferensi pengguna, seperti tema situs, bahasa, atau produk yang sering dilihat.
* Melacak perilaku pengguna di situs web untuk tujuan analisis dan pemasaran.
* Dapat digunakan untuk menyimpan token otentikasi.

### Apakah cookies aman?
Tidak semua cookie aman digunakan. Jika cookies berisi informasi sensitif seperti ID pengguna atau token otentikasi dan tidak dienkripsi, ada risiko data ini dapat dicuri melalui serangan Man-in-the-Middle (MitM).


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Implementasi Fungsi Registrasi, Login, dan Logout
* Registrasi
  * MEnggunakan `UserCreationForm` bawaan Django untuk membuat form registrasi pengguna baru.
  * Buat view untuk menangani form dan menyimpan data ke database
  * Setelah proses registrasi berhasil, pengguna harus diarahkan (redirect) ke halaman login
  * Membuat file 'register.html' untuk menampilkan halaman registrasi
  ```python
    from django.contrib.auth.forms import UserCreationForm
    from django.shortcuts import render, redirect

    def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    ```
* Login
  *  Buat fungsi `login_user` pada  `views.py` yang berisi
   ```python
   def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
   ```
  *  routing login_user didalam `urlpatterns` 
  ```python
  urlpatterns = [
    ...
    path('login/', login_user, name='login'),
  ]
  ```

* Logout
  * Buat fungsi `logout_user` pada views.py
  ```python
  def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
  ```
  * Routing fungsi tersebut agar bisa diakses
  ```python
  urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
  ]
  ```
### Membuat Dua Akun Pengguna dengan Dummy Data
 
  1. Buka halaman login
  2. Klik `Register Now` untuk menuju ke halaman Register dan dapat melakukan registrasi akun 
  3. Klik Daftar, agar akun yang telah dibuat dapat tersimpan di database (Lakukan Register sebanyak 2 kali)
  4. Login dengan akun yang telah dibuat
  5. Terakhir tambahkan Product dengan mengklik button `Add New Product`
  6. isi semua form nya dan `Add product` untuk menyimpan data product di database. Lakukan sebanyak 3 kali untuk menambahkan 3 dummy data setiap akunnya.
  
  akun satu,
  ![image](https://github.com/user-attachments/assets/63691700-29e3-40af-ae33-9a9c6d5ba12d)
 
  akun dua, 
  ![Screenshot 2024-09-25 112919](https://github.com/user-attachments/assets/179d49c1-2351-483c-a936-ebc8fd74a202)


### Menghubungkan Model Product dengan User
Di dalam Product, tambahkan ForeignKey ke User agar setiap product dapat dikaitkan ke user masing-masing
```python
class Product(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Kemudian jalankan migrasi untuk memperbarui database

```sh
    python manage.py makemigration
    python manage.py migrate
```




### Menampilkan Detail Pengguna yang Sedang Login

* Tambahkan key dan value baru pada fungsi `show_main` di `views.py`.
  ```python
  context = {
        ...
        'name' : request.user.username,
        ...
  }
  ```

* Perbarui `main.html`  dengan menambahkan code berikut
  ```html
    <p>Welcome, <strong> {{ name }}</strong>!!!</p><br>
  ``` 

### Menerapkan Cookies untuk Last Login
Di dalam fungsi `login_user`, tambahkan beberapa code sebagai berikut
```python
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
lalu pada context dalam fungsi show_main, tambahkan key baru yaitu
```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
```
Terakhir, pada `main.html` tambahkan 
```html
<p>Last login: {{ last_login }}</p>
```
agar kita bisa melihat implementasi dari cookies.


<hr>

# TUGAS 3

## 1. Alasan Mengapa Kita Membutuhkan _Data Delivery_
Data delivery merupakan proses untuk memastikan bahwa data yang telah dihasilkan didalam suatu platform dapat disimpan dengan aman, efisien, dan juga akurat. Adapun alasan mengapa kita membutuhkan _Data Delivery_ antara lain:
- Pengambilan Keputusan yang Cepat dan Tepat: 
<br>Data delivery memungkinkan informasi yang relevan untuk dihantarkan ke pengguna atau sistem dengan cepat.
- Real-Time Analytics<br>
Data delivery memastikan bahwa data yang paling terbaru selalu tersedia, memungkinkan analisis yang lebih akurat dan responsif terhadap perubahan kondisi.
- Keterhubungan dan Integrasi<br>
Data delivery memastikan bahwa data dapat bergerak dengan mulus antara berbagai komponen sistem, memungkinkan integrasi yang efisien.
- Responsivitas Aplikasi Web<br>
Data delivery memungkinkan perubahan data (misalnya, hasil pencarian, pembaruan status, atau perubahan konfigurasi) untuk diterapkan tanpa harus memuat ulang seluruh halaman. Contoh teknologi yang memanfaatkan ini adalah AJAX (Asynchronous JavaScript and XML).

## 2.  XML dan JSON, dan  Mengapa JSON lebih populer dibandingkan XML?

Antara XML dan JSON keduanya memiliki kelebihan dan kekurangannya masing-masing. Kelebihan XML yaitu memiliki struktur data hierarkis dan juga memiliki fleksibilitas terhadap struktur data yang kompleks. Akan tetapi, XML juga memiliki kekurangan yaitu sintaksnya yang terlalu bertele-tele, susah dibaca, dan ukuran file yang besar. Di JSON sendiri memiliki struktur sederhana seperti "dictionary" yang merepresentasikan _key and value_ sehingga lebih mudah dibaca. Selain itu, JSON juga lebih ringan dan efisien terutama dalam pertukaran data dalam aplikasi web dan API.
<br>
JSON lebih populer karena :
- Ringan dan Efisien<br>
  JSON memiliki ukuran file yang lebih ringan dibanding XML, hal ini juga dapat memengaruhi kinerja dalam memproses data secara real-time.
- Struktur Data yang simple<br>
  JSON juga memiliki struktur data yang simple dan lebih mudah dibaca dibanding XML.
- Integrasi dengan Bahasa Pemrograman lainnya<br>
  JSON secara alami terintegrasi dengan bahasa JavaScript. Ini dapat memberikan kemudahan bagi pengembang aplikasi web.
- Tren Industri<br>
  Banyak API dan web service saat ini dalam menggunakan JSON sebagai format data standar. Ini dapat memudahkan para pengembang untuk berkontribusi dan memudahkan dalam pertukaran data.

## 3. Fungsi dari method `is_valid()` pada form Django

a. Validasi Data<br>
&emsp; Proses validasi dibutuhkan untuk mengecek data yang dimasukkan  oleh user sesuai dengan yang kriteria yang telah ditetapkan.<br><br>
b. Error Handling<br>
&emsp; Memunculkan pesan error saat data yang dimasukkan tidak sesuai dengan apa yang telah ditentukan. <br><br>
c. Cleaning Data<br>
&emsp;  Ketika data sudah valid, maka Django akan menyimpan data tersebut didalam atribut `cleaned_data`. Kumpulan data ini merupakan data yang sudah dibersihkan dan sesuai dengan ketentuan yang telah dibuat.
<br><br>
Method ini sangat kita butuhkan untuk memastikan bahwa data yang akan disimpan di dalam database adalah data yang valid dan konsisten sehingga ini dapat menjamin kualitas, menghindari kesalahan input data ke dalam sistem, dan juga dapat mencegah serangan injeksi SQL / XSS.

## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? 
* Mencegah serangan CSRF (Cross-Site Request Forgery)<br>
   `csrf_token` melindungi aplikasi web dari serangan CSRF yang terjadi ketika seorang penyerang membuat sebuah form tersembunyi di situs web mereka yang menargetkan situs web lain yang kita gunakan.
* Memastikan Autentikasi Pengguna.<br>
  `csrf_token` memastikan bahwa permintaan yang dikirimkan ke server berasal dari pengguna yang sebenarnya dan bukan dari sebuah injeksi script dari penyerang.

  ### Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?

  Aplikasi yang kita buat akan rentan terhadap serangan CSRF. Penyerang juga bisa memanipulasi data dengan mengirim permintaan palsu yang terlihat sah sehingga dapat berakibat fatal terutama jika melibatkan keuangan atau data pribadi yang sensitif.

  ### Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

  Penyerang dapat membuat form tersembunyi didalam web mereka yang secara otomatis mengirimkan permintaan POST ke situs web target. Penyerang juga dapat mengirim permintaan palsu dari situs mereka ke aplikasi target dengan menggunakan akses pengguna yang sudah terotentikasi dan server akan menerima permintaan yang terlihat sah sehingga penyerang dapat langsung mengakses dengan menggunakan data yang telah terkirim.

## 5. Proses Pembuatan Form

Langkah-langkah:
### Buat suatu file baru bernama `forms.py` yang terletak di aplikasi main.
  Buat suatu form baru bernama `ProductForm` yang menerima `ModelForm`
    
```python   
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "description", "price", "stock", "rating"]
```
### Membuat fungsi baru pada `views.py`

    Buat suatu fungsi baru bernama `create_product(request)` yang bertujuan untuk menambahkan data Product ketika mensubmit di dalam form

```python
    # views.py
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
```

### Membuat Template HTML

Setelah menambhakan fungsi pada `views.py`, buatlah template HTML pada `create_product.html` untuk menampilkan halaman form.

```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product" />
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
```

### Melakukan Routing pada `urls.py` 
Routing dilakukan untuk mengakses form yang telah dibuat dengan menambahkan perintah sebagai berikut.

```python
    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        ...
    ]
```

### Membuat 4 fungsi untuk menampilkan objek dengan XML, JSON, XML by ID, dan JSON by ID


Buka file `views.py` dan tambahkan 4 fungsi sebagai berikut

```python
# Untuk Menampilkan dalam XML
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Utk menampilkan dakam JSON
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# utk menampilkan dalam XML by ID
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# utk menampilkan dakam JSON by ID
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

```

### Membuat Routing pada `urls.py` di aplikasi main

Pada `urls.py` tambahkan beberapa line berikut pada `url_patterns`
```python
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'main'

url_patterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id')
]
```
Hal ini bertujuan agar semua fungsi yg telah dibuat di `views.py` dapat diakses oleh django.

## Screenshot Postman

### JSON

![image](https://github.com/user-attachments/assets/2d2a4043-a378-4bba-a49b-5f09055c9c27)

### XML 

![image](https://github.com/user-attachments/assets/5c064bc4-a066-4421-a5ea-f8513832613e)

### JSON by ID

![image](https://github.com/user-attachments/assets/d6b88e8b-3cc0-47c7-b4ca-75a220d59631)

### XML by ID

![image](https://github.com/user-attachments/assets/3766ee0a-6ca0-4112-9ef9-0f8afffacc4a)

<hr>

# TUGAS 2
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

## Menambahkan `'main'` pada INSTALLED_APPS di file `settings.py`

Setelah itu, saya membuka file `settings.py` dan langsung menambahkan `'main'` didalam array INSTALLED_APPS yang bertujuan agar aplikasi kita bisa diakses oleh django
```python
INSTALLED_APPS = [
    ...,
    'main',
]
```

## Melakukan routing untuk menjalankan aplikasi `main`

Setelah itu, saya membuka file `the_waroenks/urls.py` dan menambahkan kode seperti berikut 
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Tambahkan routing untuk aplikasi main
]
```
hal ini bertujuan untuk mengimport rute URL dari aplikasi `main` yang sedang kita buat

## Membuat model 

Dalam pembuatan model, saya membuka file `models.py` dan menambahkan beberapa model yang wajib yaitu `name, price, description` dan yang sekiranya saya butuhkan kedepannya

## Membuat fungsi di dalam `views.py`

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

## Membuat routing pada `urls.py` pada aplikasi `main`

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

## Menambahkan link pada ALLOWED_HOSTS
Sebelum kita mendeploy project ktia ke PWS, kita juga harus menambahkan link pws kita pada `settings.py` agar project yang akan kita deploy bisa diakses melalui PWS View Project.
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "muhammad-farid31-thewaroenks.pbp.cs.ui.ac.id"]
```

## Push PWS
Setelah melakukan semua langkah-langkah diatas, saya bisa melakukan `git add, commit, push` ke dalam github saya terlebih dahulu dan dilanjutkan untuk melakukan deploy ke PWS yang telah saya buat.

# Penjelasan bagan request client web dan kaitannya dengan urls.py, models.py, views.py, dan html.

![Untitled](https://github.com/user-attachments/assets/059acabe-ba40-407b-b92e-9ecea30a98c8)

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


# Fungsi git dalam pengembangan perangkat lunak

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

# Alasan Kenapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak
1. Django merupakan framework full-stack yang mencakup front-end maupun back-end. Ini dapat memungkinkan kita dapat memahami seluruh alur kerja aplikasi atau website. 
   
2. Memiliki banyak fitur bawaan yang sangat berkorelasi untuk developer. Fitur-fitur tersebut termasuk ORM (Object-Relational Mapping), manajemen sisi, sistem autentikasi, dsb.
   
3. Django memiliki struktur yang mudah dipahami, terutama dalam struktur projek yang jelas. Hal ini memudahkan kita untuk memahami alur kerja web, yg dimulai dari URL routing, view, model, template, hingga request dan respon client web.
   
4. Menggunakan pola arsitektur MVC (Model-View Controller) atau dikenal sebagai MVT yg merupakan best practice untuk memahami pengembangan aplikasi web.

# Alasan kenapa model pada Django disebut sebagai ORM?

ORM adalah suatu teknik yang memungkinkan kita memanipulasi data dalam database relasional menggunakan Object-oriented Programming (OOP) yang juga memungkinkan pengguna dapat berinteraksi dengan database melalui pyhton tanpa harus menggunakan query SQL. Kemudian, Mapping dalam Django secara otomatis dapat langsung memetakan atribut model ke tabel dalam database. Dengan demikian, alasan mengapa model pada Django disebut sebagai ORM


<hr>