Nama  : Lim Bodhi Wijaya

NPM   : 2206082410

Kelas : PBP C

[Tugas 2](#Tugas-2)

[Tugas 3](#Tugas-3)

[Tugas 4](#Tugas-4)

[Tugas 5](#Tugas-5)

# Tugas 2

#### Link Adaptable: https://system-kelola-stok-produk-pbp.adaptable.app/main/

### **1. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti *tutorial*).**

Hal pertama yang saya lakukan adalah membuat *file* bernama `Tugas_2`, kemudian saya mengaktifkan *virtual environment* dengan menggunakan kode `env\Scripts\activate.bat`. Selanjutnya saya membuat projek dengan menggunakan kode `django-admin startproject Tugas_2 .`. Setelah itu saya membuat aplikasi dengan kode `python manage.py startapp main`. Kemudian saya membuat program *views* milik app untuk melakukan *return template* dan *response* berisi data nama aplikasi, nama, dan kelas. Setelah itu saya membuat *class items* di models.py milik app beserta dengan *attribute class*-nya.

### **2. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.**

<img src="Diagram Tugas 2 PBP.png" alt="Diagram hubungan urls, views, model serta html">
pertama *user* atau *client* akan meminta *request* ke url yang sesuai pada `urls.py`, kemudian django akan membuka file tersebut dan meminta tampilan dengan menggunakan `view.py`, selanjutnya model `model.py` akan menangani permintaan *user* terkait data dan template yang berisi file html yang digunakan sebagai kerangka tampilan. Setelah selesai diproses data - data tersebut dikembalikan dan ditampilkan kepada *user*.

### **3. Jelaskan mengapa kita menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?**

Penggunaan *virtual environment* dilakukan untuk mengisolasi *environment* pembuatan aplikasi web berbasis django agar tidak terjadi konflik saat *development* dengan *environment* asli pada laptop. Dengan menggunakan *virtual environment* kita dapat melakukan *upgrade* maupun *downgrade* pada aplikasi penunjang *development* tanpa mempengaruhi *environment* utama pada laptop kita. Proyek django tetap dapat dibuat tanpa menggunakan *virtual environment* terlebih dahulu, namun, sangat disarankan untuk dapat membuat *virtual environment* untuk mencegah konflik/*error*.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola arsitektur perangkat lunak yang umum digunakan dalam pengembangan aplikasi web. Ketiga pola arsitektur tersebut memiliki konsep yang mirip dalam memisahkan visualisasi, pemrosesan, dan manajemen data. Ketiga pola arsitektur tersebut bertujuan untuk meningkatkan fleksibilitas, kemudahan pengujian, dan pemeliharaan aplikasi yang mudah.

**Model-View-Controller (MVC)**

[1] Model MVC terbagi menjadi tiga komponen utama yaitu **model** yang bertugas mengelola data dan mengatur logika aplikasi, **view** yang berperan mengatur tampilan yang ditampilkan ke pengguna (*user*), dan **controller** yang berperan dalam mengatur dan memberikan *update* ke model dan *view*.

[2] **Kelebihan**

- *Businiss logic* terpisah dari model.
- Mendukung teknik asinkron.
- Modifikasi yang dilakukan di salah satu komponen tidak mempengaruhi komponen lain.
- Proses pengembangan lebih cepat.

**Kekurangan**

- *Controller* dapat berisi proses yang sangat besar sehingga sulit dikelola.
- *Unit testing* realtif lebih merepotkan.
- Kompleksitas aplikasi akan terus meningkat.

*source*: 
[1] <a href="URL">https://www.geeksforgeeks.org/mvc-framework-introduction/</a>

[2] <a href="URL">https://lobothijau.medium.com/arsitektur-mvc-vs-mvp-vs-mvvm-di-pemrograman-android-387d9c99e893</a>

**Model-View-Template (MVT)**

Model MVT terbagi menjadi tiga komponen utama yaitu **model** yang bertugas untuk mengatur logika aplikasi dan mengelola data, **view** yang berperan mengatur bagaimana data yang dikelola oleh model kemudian ditampilkan ke pengguna (*user*), dan **templates** yang berfungsi mengatur tampilan antarmuka pengguna serta memisahkan antara kode HTML dengan logika aplikasi.

**Model-View-ViewModel (MVVM)**

[1] Model MVVM memiliki tiga komponen utama yaitu **model** yang bertugas untuk mengatur logika aplikasi dan mengelola data, **view** berperan dalam mengatur tampilan yang akan dilihat oleh pengguna (*user*), dan **viewmodel** yang berperan dalam menghubungkan model dan *view*, serta mengatur tampilan sesuai format yang diinginkan oleh *user*.

[2] **Kelebihan**

- Tidak ada hubungan erat antar *view* dan *view* model.
- Tidak ada *interface* antara *view* dan model.
- Mudah untuk menulis *unit testing* dan kodenya pun *event-driven*.

**Kekurangan**

- Harus membuat *observable* untuk setiap komponen UI.
- Kode yang ditulis cenderung banyak.

*source*: 
[1] <a href="URL">https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm</a>

[2] <a href="URL">https://lobothijau.medium.com/arsitektur-mvc-vs-mvp-vs-mvvm-di-pemrograman-android-387d9c99e893</a>

**Perbedaan dari ketiga *framework***

*Controller* pada MVC yang berperan dalam dalam memberikan *update* ke model dan *view*, akan tetapi peran *view* pada MVC serupa dengan *template* pada MVT sedangkan *view* pada MVT berperan dalam mengatur tampilan antar muka agar sesuai dengan keinginan pengguna. Pada MVVM komponen *viewmodel* menjadi perantara dalam mengatur model dan *view* yang akan ditampilkan pada pengguna. 


# Tugas 3

## Perbedaan antara form `post` dan form `get` pada django

**Post**

- Nilai variabel tidak ditampilkan pada URL
- Umumnya digunakan untuk menginput data dari *form*
- Tidak ada batasan panjang *string*
- Digunakan untuk mengirimkan data - data penting
- Lebih aman 

**Get**

- Nilai variabel ditampilkan pada URL
- Umumnya digunakan untuk menginput data melalui *link*
- Terdapat batasan panjang *string* sebesar 2047 karakter
- Digunakan untuk data - data yang bersifat umum
- Kurang aman

*source*
<a href="URL">https://gist.github.com/rririanto/442f0590578ca3f8648aeba1e25f8762</a>

## perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data

### Extensible Markup Language (XML)
Extensible Markup Language (XML) menyimpan data dalam hirarki berbentuk pohon (*tree*) yang diawali dengan *root element* yang berbeda - beda tergantung pada setiap kategori kemudian diikuti oleh *branches* hingga *leaves*. XML mendukung pengiriman data berupa JSON, *namespace*, boolean, dll. Contoh XML:

``` python
<person>
  <name>Bodhi</name>
  <age>19</age>
</person>
```

### JavaScript Object Notation (JSON)
 JavaScript Object Notation (JSON) merupakan format yang digunakan untuk membaca, menyimpan, serta bertukar informasi dengan *webserver*. JSON umumnya menyimpan data dengan format *array* sehingga memudahkan proses *transfer data*, namun mengakibatkan kurang terbacanya kode json pada manusia. Format JSON mendukung pengiriman data berupa tipe data primitif seperti string, angka, boolean, hingga objek. Contoh JSON:

 ``` python
 {
  "person": {
    "name": "Bodhi",
    "age": 19
  }
}
 ```

### Hypertext Markup Language (HTML)
Hypertext Markup Language (HTML) umumnya digunakan sebagai kerangka penyusunan dan pembuatan laman pada web maupun aplikasi. HTML sendiri tidak melakukan pengiriman data. Contoh HTML:

``` python 
<!DOCTYPE html>
<html>
<head>
  <title>Contoh HTML</title>
</head>
<body>
  <h1>Selamat datang!</h1>
  <p>Ini adalah contoh halaman HTML.</p>
</body>
</html>
```

*source*:
- <a href="URL">https://www.dicoding.com/blog/apa-itu-json/</a>
- <a href="URL">https://aws.amazon.com/id/compare/the-difference-between-json-xml/</a>
- <a href="URL">https://www.hostinger.co.id/tutorial/apa-itu-html</a>

## Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern
- Dapat menyimpan data dalam bentuk array sehingga proses *transfer* data menjadi lebih mudah
- Sintaks lebih ringan dan berukuran lebih kecil
- Mendukung beberapa bahasa pemrograman sehingga mudah digunakan
- Lebih cepat dalam hal *parsing* data dari sisi *server*

*source* : <a href="URL">https://www.dicoding.com/blog/apa-itu-json/</a>

## Proses Pengerjaan Tugas 3

1. Membuat berkas html yang nantinya akan digunakan sebagai template untuk tampilan web lainnya

``` python
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
2. Membuat struktur forms input 

``` python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
3. Membuat fungsi untuk menambahkan input

``` python 
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
4. membuat berkas html untuk *create product*

``` python
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
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
5. Membuat tampilan produk yang telah ditambahkan

``` python
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

### Mengembalikan data sesuai dengan format yang diinginkan
1. Menambahkan fungsi untuk menampilkan data dalam bentuk HTML
``` python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'nama',
        'class': 'kelas PBP',
        'products': products
    }

    return render(request, "main.html", context)
```
kemudian tambahkan kode berikut pada `main.html` setelah blok `{% block content %}`

``` python
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

{% endblock content %}
```
2. Menambahkan fungsi untuk menampilkan data dalam bentuk XML
``` python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

2. Menambahkan fungsi untuk menampilkan data dalam bentuk JSON
``` python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
3. Menambahkan fungsi untuk menampilkan data berdasarkan id XML
``` python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
4. Menambahkan fungsi untuk menampilkan data berdasarkan id JSON
``` python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## Screenshoot hasil akses URL pada postman
<img src="Postman_HTML (1).jpg" alt="Postman HTML (Pretty)">
<img src="Postman_HTML (2).jpg" alt="Postman HTML (Preview)">
<img src="Postman_JSON (1).jpg" alt="Postman JSON (Pretty)">
<img src="Postman_JSON (2).jpg" alt="Postman JSON (Preview)">
<img src="Postman_XML (1).jpg" alt="Postman XML (Pretty)">
<img src="Postman_XML (2).jpg" alt="Postman XML (Preview)">
<img src="Postman_JSON_byID (1).jpg" alt="Postman JSON ID 1">
<img src="Postman_JSON_byID (2).jpg" alt="Postman JSON ID 2">
<img src="Postman_XML_byID (1).jpg" alt="Postman XML ID 1">
<img src="Postman_XML_byID (2).jpg" alt="Postman XML ID 2">

# Tugas 4

## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm merupakan sebuah *built-in* modul pada *framework* django untuk membuat akun untuk pengguna baru. Modul ini berupa *pre-defined form* yang memudahkan user dalam membuat akun. Pada *form* tersebut sudah ada beberapa *default field* seperti *username* dan *password*. Pada bagian *password* terdapat authentikasi yang mengharuskan *password* bukan merupakan *commonly used password*. Berikut merupakan kelebihan dan kekurangan dari django UserCreationForm:

Kelebihan:
- Mudah digunakan dan diaplikasikan pada *web app*.
- Memiliki validasi *password* bawaan untuk meningkatkan keamanan akun.
- Bisa dilakukan kustomisasi pada *field* apa yang perlu diisi saat membuat akun seperti email dll.

Kekurangan:
- Tidak mendukung authentikasi eksternal seperti (OAuth).
- Kurang mendukung untuk verifikasi lebih lanjut seperti verifikasi nomor telpon maupun email.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi merupakan sebuah proses verifikasi terhadap *user* saat ini. Pada proses authentikasi akan dilakukan lebih lanjut seperti apakah *user* tersebut merupakan *user* yang valid, jika tidak maka tidak bisa mengakses *web app* dan perlu melakukan registrasi akun terlebih dahulu. Sedangkan otorisasi melakukan pengecekan terhadap akun *user* apakah memiliki akses dalam melakukan tugas - tugas atau mengakses data tertentu. Kedua hal tersebut tentunya dibutuhkan karena authentikasi dapat membatasi *user* yang tidak terdaftar (*illegal user*) dalam mengakses *web app*. Sedangkan otorisasi memastikan hanya pihak - pihak tertentu dengan akses yang dapat melakukan tugas penting maupun memperoleh data penting sehingga keamanan dari *web app* dapat lebih terjamin.

## Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?
*cookies* merupakan sekumpulan data kecil yang digunakan untuk menyimpan daata - data hasil interaksi antara *client side* dengan *server side*. Pada dasarnya *cookie* terbagi menjadi *session cookie* yang akan dihapus ketika *user* menutup *browser*, dan *persistant cookie* yang akan tetap tersimpan di *database* yang nantinya dapat diakses kembali apabila dibutuhkan. Penggunaan *cookie* pada django dilakukan dengan cara pertama akan dilakukan pembacaan pada *cookie* dari *browser*, kemudian model django akan menyimpan data *cookie* pada *session mode*l, kemudian akan dilakukan perubahan informasi pada sesi pengguna, dan kemudian *cookie* yang telah di modifikasi dikirimkan kembali ke *web browser*.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan *cookies* secara default dalam pengembangan web tidak aman karena *cookies* dapat digunakan untuk melakukan *tracking* terhadap *user* yang menggunakan *web app* tersebut. Selain itu, *cookies* juga dapat digunakan untuk melakukan *session hijacking* yang dapat mengakibatkan *user* kehilangan akses terhadap akunnya. Selain itu, terdapat pula kemungkinan terjadinya *cookies poisoning*. Oleh karena itu, perlu dilakukan pengaturan terhadap *cookies* yang digunakan pada *web app* agar dapat lebih aman.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

pertama - tama saya membuat sebuah fungsi bernama register yang akan digunakan untuk mendaftarkan pengguna baru. Berikut merupakan kode dari fungsi tersebut:

``` python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context) 
```
Selanjutnya saya membuat tampilan dari form register tersebut dengan menggunakan kode berikut:

``` python
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
selanjutnya dibuat juga fungsi login dan logout seperti berikut:

``` python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
``` python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

serta dibuat juga tampilan untuk login seperti berikut:

``` python
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
serta dibuat juga tampilan untuk logout dengan menyisipkan kode pada `main.html` seperti berikut:
``` python
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```
Untuk mengaplikasikan sesi login, ditambahkan kode berikut pada `views.py` pada direktori main dibagian atas show_main sebagai berikut:
``` python
...
@login_required(login_url='/login')
def show_main(request):
...
```
kemudian untuk mendapatkan *last login* dari user, maka perlu diubah kode `if user is not None` menjadi seperti berikut:
``` python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
Pada fungsi show_main, tambahkan potongan kode `last_login`: request.COOKIES['last_login'] ke dalam variabel `context`. Kemudian perlu juga dilakukan perubahan pada fungsi logout sebagai berikut:
``` python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
setelah itu tambahkan data *last login* pada `main.html` sebagai berikut:
``` python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
Selanjutnya untuk mengintegrasikan *user* dengan *product*, maka perlu dilakukan perubahan pada `models.py` pada direktori main sebagai berikut:
``` python
...
from django.contrib.auth.models import User
...
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
kemudian perlu dilakukan perubahan pada `views.py` pada fungsi `create_product` yand ada di direktori main sebagai berikut:
``` python
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
Setelah itu, ubah kode pada fungsi `show_main` pada `views.py` sebagai berikut:
``` python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```
Langkah terakhir adalah melakukan migrasi pada model agar perubahan yang dilakukan dapat dilaksanakan.

## Screenshoot hasil pembuatan 2 user dengan 3 data dummy
`username = user1`
`password = Usr1PBP2023`
<img src="User 1.jpg" alt="User 1">

`username = user2`
`password = Usr2PBP2023`
<img src="User 2.jpg" alt="User 2">

# Tugas 5

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
### Universal Selector (*)
Universal Selector digunakan untuk memilih semua elemen yang ada pada halaman web.  Universal Selector dapat digunakan pada saat kita ingin mengatur *style* pada semua elemen yang ada pada halaman web.
```python
* {
   color: blue;
   background-color: white;
  }
```
### Type Selector
Type Selector digunakan untuk memilih elemen berdasarkan tipe elemen tersebut. Type Selector dapat digunakan pada saat kita ingin mengatur *style* pada elemen yang memiliki tipe yang sama.
```python
h1 {text-decoration: underline;}
p {font-size:14px;}
```

### Class Selector
Class selector digunakan untuk memilih elemen berdasarkan nama kelas yang diberikan. Class Selector dapat digunakan pada saat kita ingin mengatur *style* pada elemen yang memiliki kelas yang sama.
```python
p {color: blue;
   font-size: 14px;
   font-weight: bold;
  }
```

### ID Selector
ID Selector digunakan untuk memilih elemen berdasarkan nama ID yang diberikan. ID Selector dapat digunakan pada saat kita ingin mengatur *style* pada elemen yang memiliki ID yang sama.
```python
#id1 {color: blue;
   font-size: 14px;
   font-weight: bold;
  }
```

### Attribute Selector
Attribute Selector digunakan untuk memilih elemen berdasarkan atribut yang diberikan. Attribute Selector dapat digunakan pada saat kita ingin mengatur *style* pada elemen yang memiliki atribut yang sama.
```python
input[type="text"] {
   background-color: yellow;
  }
```

Referensi : <a href="URL">https://www.duniailkom.com tutorial-belajar-css-mengenal-jenis-jenis-selector-dasar-css/</a>

##  Jelaskan HTML5 Tag yang kamu ketahui
HTML5 terdiri dari beberapa tag seperti berikut:
- `<header>` : tag ini digunakan untuk menunjukkan bagian atas dari halaman web.
- `<nav>` : tag ini digunakan untuk menunjukkan bagian navigasi dari halaman web.
- `<section>` : tag ini digunakan untuk menunjukkan bagian utama dari halaman web.
- `<article>` : tag ini digunakan untuk menunjukkan bagian konten dari halaman web.
- `<aside>` : tag ini digunakan untuk menunjukkan bagian samping dari halaman web.
- `<footer>` : tag ini digunakan untuk menunjukkan bagian bawah dari halaman web.
- `<video>` : tag ini digunakan untuk menunjukkan video pada halaman web.
- `<audio>` : tag ini digunakan untuk menunjukkan audio pada halaman web.
- `<canvas>` : tag ini digunakan untuk menunjukkan gambar pada halaman web.
- `<p>` : tag ini digunakan untuk menunjukkan paragraf pada halaman web.
- `<div>` : tag ini digunakan untuk menunjukkan divisi pada halaman web.
- `<span>` : tag ini digunakan untuk menunjukkan bagian dari halaman web.
- `<href>` : tag ini digunakan untuk menunjukkan link pada halaman web.
- `<img>` : tag ini digunakan untuk menunjukkan gambar pada halaman web.

## Jelaskan perbedaan antara margin dan padding
Margin merupakan jarak antara elemen dengan elemen lainnya
```python
p {
   margin-top: 100px;
   margin-bottom: 100px;
   margin-right: 150px;
   margin-left: 80px;
  }
```
Padding merupakan jarak antara elemen dengan konten yang ada di dalam elemen tersebut
```python
p {
   padding-top: 100px;
   padding-bottom: 100px;
   padding-right: 150px;
   padding-left: 80px;
  }
```

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
### Tailwind
- Dibuat untuk menghasilkan elemen UI yang fungsional, rapi, dan fleksibel.
- Lebih fokus pada pengembangan komponen secara modular.
- Memiliki gaya desain yang minimalis dan lebih mudah disesuaikan dengan kebutuhan pengguna.
- Memiliki ukuran file yang lebih kecil dibandingkan dengan Bootstrap.

### Bootstrap
- Lebih besar dalam hal ukuran file karena menyediakan banyak fitur dan komponen.
- Lebih fokus pada pengembangan aplikasi secara keseluruhan.
- Memiliki gaya desain yang lebih konsisten dan mudah diimplementasikan.
- Memiliki lebih banyak dokumentasi dan dukungan komunitas.

### Bagaimana menentukan framework mana yang harus digunakan?
Bootstrap:
- Cocok untuk proyek besar yang membutuhkan banyak fitur dan komponen.
- Cocok untuk pengembangan aplikasi secara keseluruhan.
- Cocok untuk pengguna yang membutuhkan dokumentasi dan dukungan komunitas yang lebih banyak.

Tailwind CSS:
- Cocok untuk proyek kecil hingga menengah yang membutuhkan fleksibilitas dan kustomisasi yang lebih besar.
- Cocok untuk pengembangan komponen secara modular.
- Cocok untuk pengguna yang ingin mengurangi ukuran file dan lebih fokus pada performa.

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* 
Menambahkan style pada masing - masing file html baik menggunakan *class* maupun *style selector* seperti *padding, ukuran,* dll.
