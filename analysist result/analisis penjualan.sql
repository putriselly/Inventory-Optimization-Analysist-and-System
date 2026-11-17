-- konistensi penulisan id transaksi --
-- SELECT id_transaksi
-- FROM data_penjualan
-- where id_transaksi NOT LIKE 'TRX%'

-- konsistensi penomoran pada id transakasi
-- SELECT id_transaksi
-- FROM data_penjualan
-- WHERE SUBSTR(id_transaksi, 4) > '0050'

-- menentukan dan cek konsistensi format tanggal dan waktu
-- SELECT *
-- FROM data_penjualan
-- WHERE Tanggal_Waktu != STRFTIME(
--     '%Y-%m-%d %H:%M:%S',
--     Tanggal_Waktu
-- );

-- cek validasi bulan pada tanggal dan waktu
-- SELECT *
-- FROM data_penjualan
-- WHERE CAST(STRFTIME('%m', Tanggal_Waktu) AS INTEGER) NOT BETWEEN 1 AND 12;

-- cek validasi tanggal
-- SELECT *
-- FROM data_penjualan
-- WHERE CAST(STRFTIME('%d', Tanggal_Waktu) AS INTEGER) not BETWEEN 1 AND 31;

-- cek validasi tahun
-- SELECT 
-- 	STRFTIME('%Y', Tanggal_Waktu) as tahun,
-- 	COUNT(STRFTIME('%Y', Tanggal_Waktu)) AS banyak_tahun
-- FROM data_penjualan
-- GROUP by STRFTIME('%Y', Tanggal_Waktu)

-- cek validasi jam
-- SELECT *
-- FROM data_penjualan
-- WHERE CAST(STRFTIME('%H', Tanggal_Waktu) AS INTEGER) NOT BETWEEN 00.00 AND 23.59;

-- cek validasi menit
-- SELECT *
-- FROM data_penjualan
-- WHERE CAST(STRFTIME('%M', Tanggal_Waktu) AS INTEGER) not BETWEEN 00 AND 59;

-- cek jumlah terjual dengan mean = 2
-- SELECT jumlah_terjual, COUNT(jumlah_terjual) as banyak_terjual
-- FROM data_penjualan
-- GROUP BY jumlah_terjual

-- cek hubungan jumlah terjual, harga satuan, dan total harga
-- SELECT jumlah_terjual, harga_satuan, total_harga
-- FROM data_penjualan
-- where jumlah_terjual * harga_satuan != total_harga

-- Analisis Tren Penjualan (tanggal)
-- SELECT STRFTIME('%d', Tanggal_Waktu), COUNT(STRFTIME('%d', Tanggal_Waktu)) as banyak_waktu
-- FROM data_penjualan
-- GROUP by STRFTIME('%d', Tanggal_Waktu)

-- SELECT 
-- 	STRFTIME('%d', Tanggal_Waktu) as tanggal, 
--     COUNT(STRFTIME('%d', Tanggal_Waktu)) as banyak_transaksi
-- FROM data_penjualan
-- GROUP by tanggal
-- ORDER BY banyak_transaksi DESC
-- LIMIT 1;

-- SELECT
-- 	STRFTIME('%d', Tanggal_Waktu) as tanggal, 
--     COUNT(STRFTIME('%d', Tanggal_Waktu)) as banyak_transaksi
-- FROM data_penjualan
-- GROUP by tanggal
-- HAVING banyak_transaksi > 3
-- ORDER BY banyak_transaksi DESC

-- Analisis Tren Penjualan (jam)
SELECT 
	STRFTIME('%H', Tanggal_Waktu) as jam, 
    COUNT(STRFTIME('%H', Tanggal_Waktu)) as banyak_transaksi
FROM data_penjualan
GROUP by jam
ORDER BY banyak_transaksi DESC
LIMIT 1;

-- SELECT 
-- 	STRFTIME('%H', Tanggal_Waktu) as jam, 
--     COUNT(STRFTIME('%H', Tanggal_Waktu)) as banyak_transaksi
-- FROM data_penjualan
-- GROUP by jam
-- HAVING banyak_transaksi > 5
-- ORDER BY banyak_transaksi DESC
-- LIMIT 1;




