# The Waroenks

Nama : Muhammad Farid Hasabi <br>
NPM  : 2306152512 <br>
Kelas : PBP D <br>
Link PWS : [The Waroenks](http://muhammad-farid31-thewaroenks.pbp.cs.ui.ac.id/)
<hr>

# TUGAS 6

## Manfaat JavaScript dalam pengembangan aplikasi web
  * Interaktif dan responsif
    Penggunaan JavaScript memungkinkan elemen-elemen dalam halaman web menjadi lebih interaktif dan responsif terhadap aksi pengguna. Misalnya, ketika pengguna klik atau hover tombol, muncul popup, atau terjadi animasi lainnya.
  * Validasi Input
    Dapat digunakan untuk memvalidasi data yang masuk kedalam form. Bertujuan untuk mengurangi kesalahan dan meningkatkan efiesiensi data.
  * Manipulasi DOM
    Dapat digunakan untuk memanipulasi Document Object Model (DOM) dengan mengubah struktur, gaya, dan konten halaman web secara dinamis tanpa perlu me-reload seluruh halaman.
  * Pengembangan Fullstack
    Dapat digunakan untuk pengembangan front-end maupun back-end. Tersedia banyak library seperti React, Angular, Vue.js untuk front-end, serta Node.js untuk back-end

## Fungsi dari penggunaan await ketika kita menggunakan fetch()
await adalah sebuah keyword dalam JavaScript yang digunakan untuk menghentikan eksekusi fungsi async sampai sebuah promise diselesaikan. await digunakan bersama dengan fetch() untuk menunggu respon dari server sebelum melanjutkan eksekusi kode selanjutnya.

### Yang terjadi ketika tidak menggunakan await
Jika kita tidak menggunakan await, kode akan langsung melanjutkan eksekusi tanpa menunggu respon dari server. Dapat menyebabkan data yang tidak tersedia dan kesalahan yang tidak bisa ditangani saat setelah proses eksekusi 


## Manfaat decorator csrf_exempt pada view yang digunakan pada AJAX POST
Decorator csrf_exempt dalam Django digunakan untuk menonaktifkan pemeriksaan Cross-Site Request Forgery (CSRF) pada suatu view. CSRF dirancang untuk melindungi pengguna dari serangan di mana penyerang memanipulasi pengguna yang sudah login untuk mengirimkan permintaan yang tidak sah ke server. Namun, dalam AJAX POST, permintaan berasal dari browser pengguna yang terautentikasi, sehingga risiko serangan CSRF tidak ada.


## Alasan mengapa pembersihan data input pengguna tidak dilakukan di frontend saja melainkan juga dilakukan pada backend.
* Fungsi Keamanan
  Penyerang dapat memanipulasi input jika hanya pembersihan data hanya dilakukan di front-end. Dengan adanya validasi ulang di backend, kita memiliki lapisan pertahanan tambahan untuk mencegah serangan seperti SQL injection, XSS, dan serangan lainnya.
* Konsistensi
  Membersihkan data di backend memastikan bahwa semua pengguna menggunakan aturan yang sama, sehingga data yang disimpan di database selalu konsisten.
* Pengujian
  Frontend memberikan umpan balik cepat kepada pengguna, sementara backend bertanggung jawab untuk menjaga integritas data. Karena backend memiliki akses ke seluruh logika aplikasi, ia dapat melakukan validasi yang lebih mendalam dan kompleks untuk mencegah serangan keamanan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
### 1. Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
  Untuk mengubah kode cards menjadi AJAX, saya membuat sebuah fungsi baru pada `views.py`
  ```python
@csrf_exempt
@require_POST
def add_product_by_ajax(request):
    product_name = strip_tags(request.POST.get("product_name", "")).strip()
    description = strip_tags(request.POST.get("description", "")).strip()
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    rating = request.POST.get("rating")
    user = request.user

    new_product = Product(
        product_name=product_name,
        description=description,
        price=price,
        stock=stock,
        rating=rating,
        user=user
    )
    new_product.save()

    return HttpResponse("CREATED", status=201)
  ```
  Kemudian lakukan routing pada `urls.py` dengan menambahkan baris kode berikut
  ```python
    ...
    path('create-ajax', add_product_by_ajax, name='add_product_by_ajax'),
  ```
  Kemudian saya menghapus beberapa baris yang sebelumnya diimplementasikan ke fungsi `create_product()` dan menggantinya dengan menambahkan div dengan `id="product_cards"`. Div ini bertujuan agar DOM dapat mengolah data melalui script Javascript dengan menambahkan fungsi ini pada block `script`:
  ```js
  async function getProducts() {
      return fetch("{% url 'main:show_json' %}")
          .then((res) => res.json())
          .catch((error) => {
              console.error("Error fetching products:", error);
          });
  }
  async function refreshProducts() {
    // Menghapus isi product_cards sebelum diisi ulang
    document.getElementById("product_cards").innerHTML = "";
    document.getElementById("product_cards").className = "";

    // Mendapatkan produk dari API atau fungsi getProducts()
    const products = await getProducts();
    let htmlString = "";
    let classNameString = "";

    // Jika tidak ada produk
    if (products.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/nothing.gif' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data Product pada The Waroenks.</p>
            </div>
        `;
    } else {
        // Jika produk tersedia, buat layout grid
        classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full m-10";

        // Loop melalui setiap produk
        products.forEach((item) => {
            const product_name = DOMPurify.sanitize(item.fields.product_name);
            const description = DOMPurify.sanitize(item.fields.description);
            const rating = item.fields.rating || 0;
            const starPercentage = (rating / 5) * 100;
            htmlString += `
              <div class="relative break-inside-avoid transform duration-300 ease-in-out hover:-translate-y-1 hover:scale-100 text-white">
                <div class="relative top-5 card shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-50 max-w-md" style="border-radius: 1rem;">
                  <div class="card-head p-4 rounded-t-lg" style="border-radius: 1rem 1rem 0 0;">
                    <div class="flex" style="justify-content: center;">
                      <a class="center relative mx-3 mt-6 mb-6 flex h-72 overflow-hidden rounded-lg" href="#">
                        <img class="object-cover" src="{% static '/image/food.png' %}" alt="product image" />
                      </a>
                    </div>
                    <h3 class="font-bold text-xl text-white mb-2 m-3">${product_name}</h3>
                    <p class="text-white m-3" style="word-wrap: break-word; text-align: justify; hyphens: auto;">${description}</p>
                  </div>
                  <div class="p-4">
                    <div class="star-rating p-2" data-rating="${rating}" style="display: inline-block; font-size: 0; position: relative;">
                      <div>
                        <div class="stars-outer" style="display: inline-block; position: relative; font-size: 30px; color: #ccc;">
                          <span style="color: #ccc;">★★★★★</span>
                          <div class="stars-inner" style="position: absolute; top: 0; left: 0; white-space: nowrap; overflow: hidden; color: #f8ce0b;">
                            <span>★★★★★</span>
                          </div>
                        </div>
                        <span class="ml-4 rounded px-2.5 py-0.5 text-xs text-black font-bold" style="background-color: #f8ce00; vertical-align: 5px;">${rating}</span>
                      </div>
                      <span class="rating-value">0.0</span>
                    </div>
                    <p class="font-light ml-3">${item.fields.stock > 0 ? 'In stock' : 'Sold out'}</p>
                    <p class="font-bold text-lg mb-2 ml-3">Rp. ${item.fields.price}</p>
                    <div class="mt-4">
                      <div class="relative pt-1"></div>
                    </div>
                  </div>
                  <div class="absolute -bottom-5 end-5 flex space-x-2">
                    <a href="/edit-product/${item.pk}" class="bg-white hover:bg-gray-200 rounded-full p-2 transition duration-300 shadow-md">
                      <img src="{% static '/image/pencil.png' %}" alt="Edit Product" class="w-9 h-9"/>
                    </a>
                    <a href="/delete/${item.pk}" class="bg-white hover:bg-gray-200 rounded-full p-2 transition duration-300 shadow-md">
                      <img src="{% static '/image/trash.png' %}" alt="Delete Product" class="w-9 h-9"/>
                    </a>
                  </div>
                </div>
              </div>
              `;
          });
      }
      // Menambahkan class untuk grid/konten produk
      document.getElementById("product_cards").className = classNameString;
      // Mengisi konten produk dengan kartu-kartu produk
      document.getElementById("product_cards").innerHTML = htmlString;

      // Setelah konten produk diisi, jalankan ulang rating bintang
      const ratingContainers = document.querySelectorAll(".star-rating");
      ratingContainers.forEach((ratingContainer) => {
          const rating = parseFloat(ratingContainer.dataset.rating); 
          const starTotal = 5.0;
          const starPercentage = (rating / starTotal) * 100; // Cari persentase
          const starPercentageRounded = `${Math.round(starPercentage)}%`; // Persentase dibulatkan
          const starsInner = ratingContainer.querySelector(".stars-inner");
          starsInner.style.width = starPercentageRounded; // Set width dari inner bintang
          const ratingValue = ratingContainer.querySelector(".rating-value");
          ratingValue.innerText = rating; // Set teks rating
      });
  }
  refreshProducts();
  ```
  ### 2. Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
  Untuk mengambil data product yang sesuai dengan data miliki user, saya menambahkan `user=user` pada add_product_by_ajax :
  ```python
  ...
    new_product = Product(
        product_name=product_name,
        description=description,
        price=price,
        stock=stock,
        rating=rating,
        user=user
    )
    new_product.save()
  ...
  ```

  ### 3. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.
  Pada `main.html`, didalam div dengan `id="product_card"` yang telah kita buat tadi,  
  ```html
    ...
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out ">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
          <!-- Modal header -->
          <div class="flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
              Add New Product
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex   items-center" id="closeModalBtn">
              <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
              </svg>
              <span class="sr-only">Close modal</span>
            </button>
            ......
            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
          <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
          <button type="submit" id="submitProduct" form="productForm" class="button text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
      </div>
  </div>
  ```
  Ini bertujuan untuk agar ketika button diklik, maka proses buka dan tutup modal akan berjalan, sehingga kita dapat menambahkan 2 fungsi baru di block script
  ```js
    function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  // Fungsi untuk menyembunyikan modal
  function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
      modal.classList.add('hidden');
    }, 150);
  }
  // Event listener untuk tombol Cancel dan Close
  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
  ```
  fungsi `show_modal()` akan menampilkan modal, dan fungsi `hide_modal()` akan menutup kembali modal ketika telah digunakan. Selain itu, saya juga menambahkan cancel dan close button agar kita bisa menutup modal ketika tidak jadi digunakan.

### Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.
Untuk validasi input data, saya menambahkan baris validasi pada fungsi add_product_by_ajax() yg telah kita buat tadi,
```python
    ...
    # Validasi Input
    if (not product_name or product_name != request.POST.get("product_name")) or (not description or description != request.POST.get("description")):
        return HttpResponse("Invalid Input!!!", status=400)
    ...
```
Validasi akan mereturn respon dengan `status = 400` dan pesan "Invalid Input".
Kemudian saya juga membuat fungsi baru pada script yaitu add_product agar kita bisa menambahkan data product kita melalui button AJAX terbaru,
```js
 // JavaScript (client-side)
  function addProduct() {
      const form = document.querySelector('#productForm');
      const formData = new FormData(form);

      // Validasi input
      const productName = formData.get('product_name').trim();
      const description = formData.get('description').trim();

      fetch("{% url 'main:add_product_by_ajax' %}", {
          method: "POST",
          body: formData,
      })
      .then(response => {
          if (response.ok) {
              hideModal(); // menutup ketika berhasil
              refreshProducts(); // refresh page
              form.reset(); // reset isi field pada form
              document.querySelector("[data-modal-toggle='crudModal']").click();
          } else {
              return response.text(); // return pesan error 
          }
      })
      .then(data => {
          // alert error jika ada data invalid
          if (data) {
              form.reset(); // reset form
              alert(data);
          }
      })
      return false;
  }
  // Event listener untuk submit form
  document.getElementById("productForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addProduct();
  });
```
fungsi ini akan menambahkan product ketika berhasil, dan memunculkan pesan error jika terdapat invalid input pada field.





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
Responsive design adalah konsep pengembangan website yang memungkinkan tampilan website menyesuaikan diri secara otomatis dengan ukuran layar perangkat yang digunakan oleh pengguna. Penerapan responsive design sangatlah penting karena memiliki beberapa manfaat, antara lain :
  * Pengalaman pengguna yang lebih baik: Pengguna dapat mengakses website dengan mudah dari berbagai perangkat.
  * SEO yang lebih baik: Website yang responsive cenderung lebih mudah dicar pada search engine seperti google, dll.
  * Biaya pengembangan yang lebih rendah: kita hanya perlu membuat satu versi website untuk semua perangkat.
### Contoh website yang responsive:
  * Instagram
  * Wikipedia
### Contoh website yang belum responsive:
  * SIAK-NG

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

![image](https://github.com/user-attachments/assets/d1e00a22-7ac1-4478-8115-c87f7e35b4a6)

* Margin: Merupakan ruang kosong di luar batas/border suatu elemen. Margin digunakan untuk mengatur jarak antara elemen satu dengan elemen lainnya.
* Border: Adalah garis batas yang mengelilingi suatu elemen.
* Padding: Merupakan ruang kosong di dalam batas/border suatu elemen, antara konten dan batas elemen tersebut. Padding digunakan untuk memberikan ruang pada konten di dalam elemen.

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
* Buat file `navbar.html` pada direktori `/templates` di root folder untuk kustomisasi navbar dan juga tambahkan `card_product.html` untuk kustomisasi card per product pada `main.html`.
* Terakhir, kustomisasi kembali semua file yang diperlukan untuk dikustom agar lebih menarik.












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
  JSON secara alami terintegrasi dengan bahasa JavaScript yang dapat memberikan kemudahan bagi pengembang aplikasi web.
- Tren Industri<br>
  Banyak API dan web service saat ini dalam menggunakan JSON sebagai format data standar sehingga dapat memudahkan para pengembang untuk berkontribusi dan memudahkan dalam pertukaran data.

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