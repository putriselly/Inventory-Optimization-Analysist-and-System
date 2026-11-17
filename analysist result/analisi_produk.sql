-- cek konistensi penulisan pada kolom id transaksi
-- SELECT id_produk
-- FROM data_produk
-- WHERE id_produk not LIKE 'PRD%'

-- join tabel data produk dan penjualan untuk mencari produk yang banyak terjual 
-- SELECT 
--     data_produk.id_produk,
--     data_produk.nama_produk,
--     data_produk.kategori,
--     SUM(data_penjualan.jumlah_terjual) AS total_terjual
-- FROM data_produk
-- INNER JOIN data_penjualan
-- ON data_produk.id_produk = data_penjualan.id_produk
-- GROUP BY 
--     data_produk.id_produk,
--     data_produk.nama_produk,
--     data_produk.kategori;

--  produk paling banyak terjual
-- SELECT 
--     nama_produk,
--     total_terjual
-- FROM (
--     SELECT 
--         data_produk.id_produk,
--         data_produk.nama_produk,
--         data_produk.kategori,
--         SUM(data_penjualan.jumlah_terjual) AS total_terjual
--     FROM data_produk
--     INNER JOIN data_penjualan
--     ON data_produk.id_produk = data_penjualan.id_produk
--     GROUP BY 
--         data_produk.id_produk,
--         data_produk.nama_produk,
--         data_produk.kategori
-- ) AS hasil
-- ORDER BY total_terjual DESC
-- LIMIT 1;

-- produk paling sedikit terjual
SELECT 
    nama_produk,
    total_terjual
FROM (
    SELECT 
        data_produk.id_produk,
        data_produk.nama_produk,
        data_produk.kategori,
        SUM(data_penjualan.jumlah_terjual) AS total_terjual
    FROM data_produk
    INNER JOIN data_penjualan
    ON data_produk.id_produk = data_penjualan.id_produk
    GROUP BY 
        data_produk.id_produk,
        data_produk.nama_produk,
        data_produk.kategori
) AS hasil
ORDER BY total_terjual
LIMIT 1;