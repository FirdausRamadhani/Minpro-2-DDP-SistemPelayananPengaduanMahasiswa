# Minpro-2-DDP-SistemPelayananPengaduanMahasiswa

Nama      : Firdaus Ramadhani

NIM       : 2609116004

Kelas     : A

## Mini Project 2

### Sistem Pelayanan Pengaduan Mahasiswa

Sistem ini merupakan program sederhana yang berfungsi untuk melaporkan masalah yang dialami mahasiswa. Dalam program ini terdapat 2 akun yaitu akun "Mahasiswa" dan "Admin". "Mahasiswa" dapat melaporkan keluhannya terkait kampus dan keluhan itu dapat dilihat dan diakses dengan akun "Admin". Pembaruan program ini dari sebelumnya yaitu tambahan "cooldown" ketika user salah memasukkan password atau username 3 kali. Lalu ada juga menu mahasiswa yang diperbarui dimana mahasiswa bisa menghapus atau mengedit keluhannya (misalnya jika ada typo atau tidak jadi melapor). 

#### Yang ada dalam program ini 

`def` atau `function` => untuk membuat fungsi tersendiri seperti fungsi login, menu mahasiswa dan menu admin agar terlihat lebih rapih.

`library` => library yg saya gunakan adalah `import pwinput` untuk mengenkripsi password, `import time` untuk sedikit memberi jeda di beberapa program, dan `import os` untuk membersihkan terminal agar terlihat rapih.

`dictionary` => dictionary saya gunakan untuk tempat menyimpan data akun.

`If-Else` => conditional atau fungsi percabangan sebagai validasi pilihan dan menjadi dasar dari opsi yang dapat dipilih user.

`list` => list kosong untuk menjadi ruang tersimpannya data pengaduan dan status pengaduan.

`tuple` => tuple untuk menjadi variabel data status yang sudah ditetapkan dan tidak bisa diubah.

`while` => perulangan agar menu ditampilkan terus menerus.

`for` => untuk mengurut angka sebagai countdown 10 detik dan menunjukkan output pengaduan yang telah ditambahkan atau statusny diubah

#### Flowchart 

<img width="2645" height="2199" alt="MINPRO1-Page-2 drawio" src="https://github.com/user-attachments/assets/24a9f2d9-28db-46c1-9e93-8230869e4e5a" />

#### Output dan Penjelasan alur pemrograman

<img width="313" height="151" alt="start" src="https://github.com/user-attachments/assets/a135af31-48c3-4e3a-ac33-30c4257fdeb9" />

Output awal ketika start menunjukkan pilihan untuk login ke sistem atau keluar sistem.

<img width="337" height="293" alt="MENU MAHASISWA" src="https://github.com/user-attachments/assets/0ed5cac7-fbc0-4d71-aa36-aee182052f02" />

Output ketika pilih login dan login sebagai akun mahasiswa. password disamarkan karena library `pwinput.`

<img width="360" height="414" alt="MHS MENAMBAH PENGADUAN" src="https://github.com/user-attachments/assets/96daddae-08cb-4764-ba6f-4c49e5fe6854" />

Menu pertama dari akun mahasiswa, yaitu membuat pengaduan. While bekerja dan kembali ke menu mahasiswa

<img width="330" height="344" alt="MHS STATUS" src="https://github.com/user-attachments/assets/f9f98004-dec3-41cc-a60e-9d259b235adc" />

Ketika sudah membuat beberapa pengaduan, dengan menu kedua mahasiswa bisa melihat status dan pengaduan yang telah dibuat.

<img width="372" height="313" alt="MHS EDIT ADUAN" src="https://github.com/user-attachments/assets/4fb7135b-82d7-4ac6-a639-d56e7306745b" />

Output pada menu ketiga, yaitu mahasiswa dapat mengedit atau mengubah apa yang telah ia adukan untuk mengantisipasi jika ada kesalahan pengetikan (typo).

<img width="474" height="558" alt="MHS HAPUS ADUAN" src="https://github.com/user-attachments/assets/921f7563-45d2-4b90-beca-e4b03643e55a" />

Pada menu keempat, mahasiswa dapat menghapus pengaduan yg telah dibuat untuk mengantisipasi jika mahasiswa ingin membatalkannya. 

<img width="368" height="289" alt="PILIH LOGOUT" src="https://github.com/user-attachments/assets/6e139921-525e-42af-b7b9-ec9231b94617" />

Terakhir menu logout dari akun mahasiswa yang akan langsung kembali ke tampilan paling awal.

<img width="323" height="271" alt="MENU ADMIN" src="https://github.com/user-attachments/assets/31227205-c6f3-49b5-855d-5d82e7c972c4" />

Ketika memilih login lagi di tampilan awal. semua output dari mahasiswa/akun sebelumnya di terminal akan diclear karena library `os.` Dan ini output dari menu admin.

<img width="292" height="326" alt="ADM LIAT STAT" src="https://github.com/user-attachments/assets/637a393a-6459-423c-b2f7-d17ace6cf091" />

Ini output dari menu pertama, yaitu liat pengaduan beserta statusnya

<img width="373" height="569" alt="ADM UBAH STATUS" src="https://github.com/user-attachments/assets/77aa3f61-914a-448c-8bc9-5b11e982cdef" />

Ini output dari menu ubah status, admin bisa mengubah status dari pengaduan 

<img width="451" height="578" alt="ADM HAPUS ADUAN" src="https://github.com/user-attachments/assets/2134886b-c966-4bbd-9bf7-ace6fdd236c9" />

Ini output dari menu hapus pengaduan, admin bisa menghapus pengaduan yang sekiranya statusnya sudah selesai (perbedaan status dari output sebelumnya dikarenakan saya telah mengubah semua status), dan ketika di hapus status sudah ikut terhapus. jadi ketika ada pengaduan baru statusnya baru lagi, tidak seperti sebelumnya yang statusnya nyangkut dari yang lama

<img width="383" height="274" alt="ADM LOGOUT" src="https://github.com/user-attachments/assets/1d434e8a-1727-4fcf-8fef-28d0d6dac16b" />

Logout akun admin 

<img width="373" height="435" alt="LOGIN MHS LAGI" src="https://github.com/user-attachments/assets/19804299-c4fb-40bd-bf38-e091949ebffb" />
<img width="335" height="370" alt="MHS TAMBAH ADUAN LAGIIII" src="https://github.com/user-attachments/assets/a22f9a7e-b82f-4cd1-9547-5f7b80aae217" />

dan ketika login sebagai mahasiswa lagi untuk menambahkan pengaduan. statusnya sudah tidak ambigu.

#### Berikut adalah validasi-validasi inputan :

<img width="370" height="381" alt="SALAH ISI USN ATAY U PW" src="https://github.com/user-attachments/assets/ea31280d-90f8-47c9-81c5-95eb701e565c" />
<br/>
<img width="458" height="290" alt="ADM SALAH USN PW" src="https://github.com/user-attachments/assets/2cb1026e-bb1e-4331-a969-a7c30d2a7fd7" />
<br/>
<img width="458" height="446" alt="COOLDOWN 10 DETIK SALAH PW" src="https://github.com/user-attachments/assets/950126da-6afb-46dd-8f34-0fee7b43c0c4" />

Ini ketika salah memasukkan username atau password. Ketika sudah mengisi sebanyak 3 kali maka sistem akan meng-cooldown proses login selama 10 detik.

<img width="348" height="180" alt="MHS INPUT TDK VALID " src="https://github.com/user-attachments/assets/879011d0-dee2-4317-a218-bcbc653ee14c" />

<img width="374" height="150" alt="TDK VALID LG" src="https://github.com/user-attachments/assets/d69e4e91-d812-46b5-b7a6-b3c51a6604e6" />

Ini ketika memilih opsi diluar pilihan yang tersedia.

<img width="319" height="127" alt="KELUAR PROGRAM" src="https://github.com/user-attachments/assets/88dff640-a9bc-4fe3-8492-2994beaf5892" />

<img width="536" height="62" alt="END" src="https://github.com/user-attachments/assets/c9084328-986f-4b9e-ac15-bab7206e914a" />

Tampilan akhir ketika memilih keluar program. 
