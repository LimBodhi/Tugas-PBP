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