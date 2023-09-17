#Tugas 2

Link Adaptable: https://system-kelola-stok-produk-pbp.adaptable.app/main/

1. Hal pertama yang saya lakukan adalah membuat file bernama `Tugas_2`, kemudian saya mengaktifkan virtual environment dengan menggunakan kode "env\Scripts\activate.bat". Selanjutnya saya membuat projek dengan menggunakan kode "django-admin startproject Tugas_2 .". Setelah itu saya membuat aplikasi dengan kode "python manage.py startapp main" Setelah itu saya membuat program views milik app untuk melakukan return template dan response berisi data nama aplikasi, nama, dan kelas. Setelah itu saya membuat class items di models.py milik app beserta dengan attribute class-nya.

2. 

3. Penggunaan virtual environment dilakukan untuk mengisolasi environment pembuatan aplikasi web berbasis django agar tidak terjadi konflik saat development dengan environment asli pada laptop. Dengan menggunakan virtual environment kita dapat melakukan upgrade maupun downgrade pada aplikasi penunjang development tanpa mempengaruhi environment utama pada laptop kita. Proyek django tetap dapat dibuat tanpa menggunakan virtual environment terlebih dahulu, namun, sangat disarankan untuk dapat membuat virtual environment untuk mencegah konflik/error.

4. MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola arsitektur perangkat lunak yang umum digunakan dalam pengembangan aplikasi web. Ketiga pola arsitektur tersebut memiliki konsep yang mirip dalam memisahkan visualisasi, pemrosesan, dan manajemen data. Ketiga pola arsitektur tersebut bertujuan untuk meningkatkan fleksibilitas, kemudahan pengujian, dan pemeliharaan aplikasi yang mudah.

MVC (Model-View-Controller):
    Model MVC terbagi menjadi tiga komponen utama yaitu model yang bertugas mengatur struktur data dan berkomunikasi dengan database, view yang berperan mengambil data dan mengatur tampilan yang ditampilkan ke pengguna (user), dan controller yang berperan dalam mengatur dan memberikan update ke model dan view

MVT (Model-View-Templates)
    Model MVT terbagi menjadi tiga komponen utama yaitu model yang bertugas untuk mengurus struktur data, view yang berperan mengatur tampilan yang ditampilkan ke pengguna (user), dan templates yang berfungsi 