Nama  : Lim Bodhi Wijaya

NPM   : 2206082410

Kelas : PBP C

[Tugas 2](#Tugas-2)

[Tugas 3](#Tugas-3)

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