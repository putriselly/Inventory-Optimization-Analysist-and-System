# Inventory Optimization System

A Python-based inventory management and optimization project designed to help retail businesses monitor stock levels and make better restocking decisions.

## Features
- Retail sales data analysis using Pandas.
- Product sales performance visualization.
- Transaction trend analysis by hour.
- Inventory monitoring.
- Reorder Point (ROP) calculation.
- Restock recommendations and order quantity estimation.
- Interactive dashboard built with Streamlit.

## Technologies
- Python
- Pandas
- Streamlit
- Matplotlib (if used in the analysis)

## Project Objective
To help businesses identify products that need restocking before they run out of stock, based on historical sales data and inventory calculations.

# HASIL ANALISIS DATA PENJUALAN DAN PRODUK

## A. Analisis Data Penjualan

### 1. Insight dan Temuan

Berdasarkan proses pemeriksaan dan analisis pada dataset penjualan, diperoleh beberapa temuan sebagai berikut:

1. **Tipe data tanggal dan waktu** pada kolom `Tanggal_Waktu` perlu dikonversi menjadi tipe data datetime agar dapat digunakan dalam analisis berdasarkan tanggal maupun waktu transaksi.

2. **Kolom `Harga_Satuan`** perlu dikonversi menjadi tipe data float agar dapat digunakan dalam perhitungan statistik dan analisis numerik.

3. **Kolom `Total_Harga`** juga perlu dikonversi menjadi tipe data float agar format datanya sesuai dengan kebutuhan analisis.

4. **Kolom `ID_Produk`** memiliki 40 nilai duplikat. Namun, duplikasi tersebut belum tentu merupakan kesalahan karena satu produk dapat muncul dalam beberapa transaksi. Oleh karena itu, perlu dilakukan pemeriksaan lebih lanjut untuk memastikan apakah duplikasi tersebut merupakan kondisi yang wajar atau kesalahan pencatatan.

5. **Kolom `Jumlah_Terjual`** memiliki nilai 5 dan 6 yang masing-masing hanya muncul satu kali, sedangkan nilai mediannya adalah 2. Kedua nilai tersebut tergolong jarang ditemukan sehingga dapat menjadi indikasi adanya kemungkinan kesalahan pencatatan. Namun, hal ini masih berupa dugaan karena pembelian dalam jumlah yang lebih besar tetap memungkinkan terjadi.

6. **Kolom `Harga_Satuan`** memiliki selisih antara mean dan median sekitar Rp3.000 atau 16%. Nilai mean yang lebih tinggi daripada median menunjukkan bahwa terdapat kemungkinan beberapa nilai harga yang relatif tinggi sehingga memengaruhi rata-rata. Meskipun demikian, kondisi ini belum cukup untuk menyimpulkan adanya kesalahan data.

7. **Kolom `Harga_Satuan`** memiliki nilai minimum Rp18.000 dan maksimum Rp55.000. Rentang harga tersebut terlihat cukup lebar, tetapi masih dapat dianggap wajar karena dataset mencakup berbagai jenis produk dengan harga yang berbeda-beda.

8. **Coefficient of Variation (CV) pada kolom `Harga_Satuan`** mencapai sekitar 62,1%. Nilai tersebut menunjukkan tingkat variasi harga yang cukup tinggi. Namun, tingginya variasi dapat disebabkan oleh perbedaan harga antarproduk sehingga belum tentu menunjukkan adanya kesalahan pencatatan.

9. **Coefficient of Variation (CV) pada kolom `Total_Harga`** mencapai sekitar 56,4%. Variasi tersebut dapat dipengaruhi oleh perbedaan harga satuan setiap produk serta jumlah barang yang dibeli dalam setiap transaksi. Oleh karena itu, nilai CV yang tinggi belum tentu menunjukkan adanya ketidakwajaran data.

### 2. Analisis Tren Penjualan

Analisis tren penjualan dilakukan untuk mengidentifikasi pola transaksi berdasarkan waktu, sehingga dapat digunakan sebagai bahan pertimbangan dalam menentukan strategi promosi dan peningkatan pelayanan toko.

Berdasarkan hasil analisis, diperoleh beberapa temuan:

1. **Berdasarkan tanggal transaksi**, jumlah transaksi terbanyak terjadi pada 3 November 2025, yaitu sebanyak 3 transaksi. Hal ini menunjukkan bahwa tanggal tersebut memiliki aktivitas transaksi yang relatif lebih tinggi dibandingkan tanggal lainnya dalam dataset.

2. **Berdasarkan waktu transaksi**, aktivitas transaksi paling banyak terjadi sekitar pukul 18.00 atau 6 sore, dengan total 5 transaksi. Temuan ini menunjukkan bahwa waktu sore menjelang malam merupakan salah satu periode dengan aktivitas transaksi yang cukup tinggi.

### 3. Kesimpulan dan Saran

Berdasarkan hasil pemeriksaan dan analisis data penjualan, ditemukan beberapa nilai yang memiliki karakteristik tertentu dan perlu mendapatkan perhatian lebih lanjut.

Pada kolom `Jumlah_Terjual`, nilai 5 dan 6 masing-masing hanya muncul satu kali, sedangkan median jumlah barang terjual adalah 2. Hal ini menunjukkan bahwa kedua nilai tersebut relatif jarang ditemukan. Meskipun demikian, belum dapat dipastikan bahwa nilai tersebut merupakan kesalahan pencatatan karena pembelian dalam jumlah besar masih mungkin terjadi.

Pada kolom `Harga_Satuan`, nilai mean lebih besar daripada median dengan selisih sekitar Rp3.000 atau 16%. Selain itu, terdapat rentang harga yang cukup lebar, yaitu antara Rp18.000 hingga Rp55.000. Kondisi tersebut kemungkinan dipengaruhi oleh perbedaan harga antarproduk sehingga belum dapat dikategorikan sebagai kesalahan data.

Sementara itu, nilai Coefficient of Variation (CV) pada gabungan seluruh harga satuan mencapai sekitar 62,1%, sedangkan CV pada kolom `Total_Harga` mencapai sekitar 56,4%. Tingginya variasi tersebut belum tentu menunjukkan adanya ketidakwajaran karena harga satuan setiap produk berbeda dan jumlah barang yang dibeli dalam setiap transaksi juga bervariasi.

Secara keseluruhan, hasil pemeriksaan belum menunjukkan bukti yang cukup untuk melakukan koreksi maupun penghapusan data pada kolom-kolom tersebut. Oleh karena itu, nilai yang ditemukan tetap dipertahankan. Beberapa temuan dicatat sebagai indikasi yang memerlukan verifikasi lebih lanjut apabila tersedia informasi pendukung, seperti katalog produk, nota transaksi, atau riwayat harga.

Berdasarkan hasil analisis tren penjualan, aktivitas transaksi terbanyak tercatat pada tanggal 3 November 2025 dan sekitar pukul 18.00. Temuan ini dapat dijadikan bahan pertimbangan dalam menyusun strategi penjualan. Toko dapat mempertimbangkan pelaksanaan promosi pada awal bulan untuk menarik minat pelanggan. Selain itu, peningkatan kualitas pelayanan pada sore hingga malam hari juga dapat dilakukan, misalnya dengan memastikan ketersediaan staf dan kesiapan produk agar pelanggan memperoleh pelayanan yang optimal ketika aktivitas transaksi meningkat.

---

## B. Analisis Data Produk

### 1. Insight dan Temuan

Berdasarkan proses pemeriksaan dan analisis pada dataset produk, diperoleh beberapa temuan sebagai berikut:

1. **Kolom `Harga_Modal`** perlu dikonversi menjadi tipe data float agar dapat digunakan dalam perhitungan statistik dan analisis numerik.

2. **Coefficient of Variation (CV) pada kolom `Harga_Modal`** mencapai sekitar 78%. Nilai ini menunjukkan variasi harga modal yang cukup tinggi. Namun, kondisi tersebut belum tentu menunjukkan adanya kesalahan data karena setiap produk dapat memiliki harga modal yang berbeda-beda.

3. **Coefficient of Variation (CV) pada kolom `Stok_Minimum`** mencapai sekitar 50%. Nilai tersebut menunjukkan adanya variasi jumlah stok minimum antarproduk. Hal ini masih dapat dianggap wajar karena setiap produk memiliki tingkat permintaan dan kebutuhan persediaan yang berbeda.

### 2. Analisis Produk (Market Basket Analysis / Produk Terlaris)

Analisis produk dilakukan untuk mengetahui produk dengan tingkat penjualan tertinggi dan terendah. Informasi ini dapat digunakan sebagai bahan pertimbangan dalam menentukan strategi penjualan dan pengelolaan persediaan.

Berdasarkan hasil analisis penjualan, diperoleh beberapa temuan:

1. **Produk dengan jumlah penjualan tertinggi** adalah Roti Cokelat, dengan total penjualan sebanyak 24 buah.

2. **Produk dengan jumlah penjualan terendah** adalah Kopi Bubuk 250g, dengan total penjualan sebanyak 4 buah.

### 3. Kesimpulan dan Saran

Berdasarkan proses pembersihan dan analisis data produk, dapat disimpulkan bahwa terdapat variasi nilai yang cukup tinggi pada beberapa kolom numerik, khususnya harga modal produk. Nilai CV pada kolom `Harga_Modal` mencapai sekitar 78%, yang menunjukkan tingkat variasi harga modal antarproduk cukup tinggi. Namun, kondisi tersebut belum tentu menandakan adanya kesalahan data karena setiap produk dapat memiliki harga modal yang berbeda-beda. Oleh karena itu, nilai-nilai tersebut tidak dapat langsung dianggap sebagai kesalahan tanpa pemeriksaan lebih lanjut.

Selain itu, hasil analisis penjualan menunjukkan bahwa Roti Cokelat merupakan produk dengan jumlah penjualan tertinggi, yaitu sebanyak 24 buah. Sementara itu, Kopi Bubuk 250g menjadi produk dengan jumlah penjualan terendah, yaitu sebanyak 4 buah.

Secara keseluruhan, hasil analisis memberikan gambaran mengenai variasi harga modal serta tingkat penjualan setiap produk. Informasi tersebut dapat dimanfaatkan sebagai bahan pertimbangan dalam menentukan strategi penjualan dan pengelolaan persediaan.

Berdasarkan hasil analisis tersebut, terdapat beberapa saran yang dapat dipertimbangkan:

1. **Meningkatkan persediaan Roti Cokelat.** Mengingat Roti Cokelat merupakan produk dengan jumlah penjualan tertinggi, toko dapat mempertimbangkan untuk menambah persediaannya guna memenuhi permintaan pelanggan dan mengurangi risiko kehabisan stok.

2. **Mempertimbangkan penambahan variasi produk sejenis.** Tingginya penjualan Roti Cokelat dapat menjadi pertimbangan untuk menyediakan variasi produk roti lainnya, seperti roti stroberi, roti keju, atau varian rasa lainnya guna menarik minat pelanggan.

3. **Melakukan evaluasi terhadap persediaan Kopi Bubuk 250g.** Karena produk ini memiliki jumlah penjualan terendah, toko dapat mengevaluasi jumlah persediaan yang disediakan agar tidak terjadi penumpukan stok. Namun, produk tersebut tidak harus langsung dikurangi atau dihilangkan karena masih terdapat kemungkinan adanya permintaan dari pelanggan tertentu.

4. **Melakukan pemantauan penjualan secara berkala.** Toko sebaiknya terus memantau perkembangan penjualan setiap produk agar keputusan penambahan maupun pengurangan persediaan didasarkan pada pola permintaan yang lebih konsisten.