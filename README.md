🧩 Maze Solver BFS (Tkinter)

📌 Deskripsi

Program ini adalah aplikasi visualisasi pencarian jalur pada labirin menggunakan algoritma **Breadth-First Search (BFS)**. Aplikasi dibuat dengan bahasa pemrograman Python dan menggunakan library **Tkinter** untuk tampilan GUI.

Program akan:

* Menampilkan labirin dalam bentuk grid (27x27)
* Menentukan titik awal (**Start / S**) dan tujuan (**Exit / E**)
* Menjalankan algoritma BFS untuk menemukan jalur terpendek
* Menampilkan proses eksplorasi secara animasi
* Menunjukkan jalur akhir yang ditemukan


🎯 Tujuan

* Memahami konsep algoritma **BFS (Breadth-First Search)**
* Memvisualisasikan proses pencarian jalur
* Melatih penggunaan GUI dengan Tkinter

⚙️ Fitur Utama

* ✅ Visualisasi labirin 2D
* ✅ Animasi eksplorasi BFS
* ✅ Penandaan jalur terpendek
* ✅ Tombol **Mulai** dan **Reset**
* ✅ Status proses secara real-time
* ✅ Legenda warna untuk memudahkan pemahaman

🧠 Algoritma yang Digunakan

Program menggunakan algoritma Breadth-First Search (BFS) untuk mencari jalur terpendek dari titik Start (S) ke End (E).

Cara kerja BFS:

1. Mulai dari titik awal (S)
2. Jelajahi semua tetangga terdekat
3. Gunakan **queue (antrian)** untuk menyimpan jalur
4. Tandai node yang sudah dikunjungi
5. Berhenti saat mencapai tujuan (E)
6. Jalur pertama yang ditemukan adalah jalur terpendek

🎨 Keterangan Warna

| Warna      | Arti                  |
| ---------- | --------------------- |
| Biru tua   | Dinding               |
| Putih      | Jalan                 |
| Hijau muda | Sel yang dieksplorasi |
| Hijau tua  | Jalur terpendek       |
| Merah      | Posisi saat ini       |
| Tosca      | Start (S)             |
| Orange     | Exit (E)              |

▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstall

Cek dengan:
```bash
python --version
```

2. Jalankan program
```bash
python labirin.py
```

🖥️ Tampilan Aplikasi
Setelah dijalankan:
* Klik tombol **▶ Mulai** untuk memulai pencarian
* Program akan menampilkan proses BFS secara bertahap
* Jalur terpendek akan ditampilkan setelah eksplorasi selesai
* Klik **↺ Reset** untuk mengulang

📁 Struktur Program
* `MAZE` → Data labirin (grid)
* `bfs()` → Fungsi algoritma BFS
* `MazeApp` → Kelas utama GUI
* `start_animation()` → Animasi eksplorasi dan hasil
* `reset()` → Mengatur ulang tampilan

📊 Output Program
* Menampilkan jumlah langkah jalur terpendek
* Menampilkan jumlah sel yang dieksplorasi
* Visualisasi jalur dari Start ke Exit

🧑‍💻 Teknologi yang Digunakan
* Python
* Tkinter (GUI)
* Collections (deque untuk BFS)

📌 Kesimpulan
Program ini berhasil mengimplementasikan algoritma BFS untuk mencari jalur terpendek dalam labirin serta memvisualisasikannya secara interaktif. Dengan adanya animasi, pengguna dapat memahami bagaimana BFS bekerja secara bertahap.# tugas-strukdat5
