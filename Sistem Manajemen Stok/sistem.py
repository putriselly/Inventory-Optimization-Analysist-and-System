import pandas as pd
from pathlib import Path
import math

# 1. MENENTUKAN LOKASI DATASET

folder_sistem = Path(__file__).resolve().parent
folder_dataset = folder_sistem.parent / "data set"

# # 2. MEMBACA DATASET

df_penjualan = pd.read_csv(folder_dataset / "data_penjualan.csv")
df_produk = pd.read_csv(folder_dataset / "data_produk.csv")
df_stok = pd.read_csv(folder_dataset / "data_stok_saat_ini.csv")

# print("Semua dataset berhasil dibaca.")

# # 3. MEMBERSIHKAN SPASI PADA DATA TEKS

for df in [df_penjualan, df_produk, df_stok]:
    kolom_teks = df.select_dtypes(include="object").columns

    for kolom in kolom_teks:
        df[kolom] = df[kolom].str.strip()

# # 4. MENGUBAH TIPE DATA

# # Mengubah tanggal menjadi datetime
df_penjualan["Tanggal_Waktu"] = pd.to_datetime(
    df_penjualan["Tanggal_Waktu"],
    format="%m/%d/%Y %H:%M",
    errors="coerce"
)

# # Mengubah kolom numerik menjadi angka
kolom_penjualan = [
    "Jumlah_Terjual", "Harga_Satuan", "Total_Harga"
]

kolom_produk = [
    "Harga_Modal", "Stok_Minimum"
]

kolom_stok = [
    "Stok_Saat_Ini"
]

for kolom in kolom_penjualan:
    df_penjualan[kolom] = pd.to_numeric(
        df_penjualan[kolom], errors="coerce"
    )

for kolom in kolom_produk:
    df_produk[kolom] = pd.to_numeric(
        df_produk[kolom], errors="coerce"
    )

for kolom in kolom_stok:
    df_stok[kolom] = pd.to_numeric(
        df_stok[kolom], errors="coerce"
    )

# # 5. MEMERIKSA DATA KOSONG

# print("\n--- PEMERIKSAAN DATA KOSONG ---")

# for nama, df in [
#     ("Penjualan", df_penjualan),
#     ("Produk", df_produk),
#     ("Stok", df_stok)
# ]:
#     print(f"\n{nama}:")
#     print(df.isnull().sum())

# # 6. MEMERIKSA DUPLIKAT

# print("\n--- PEMERIKSAAN DUPLIKAT ---")

# print("Penjualan:", df_penjualan.duplicated().sum())
# print("Produk:", df_produk.duplicated().sum())
# print("Stok:", df_stok.duplicated().sum())

# print(
#     "ID transaksi duplikat:",
#     df_penjualan["ID_Transaksi"].duplicated().sum()
# )

# print(
#     "ID produk duplikat:",
#     df_produk["ID_Produk"].duplicated().sum()
# )

# print(
#     "ID stok duplikat:",
#     df_stok["ID_Produk"].duplicated().sum()
# )

# # 7. MEMERIKSA KONSISTENSI DATA

# print("\n--- PEMERIKSAAN KONSISTENSI ---")

# # Memastikan ID produk penjualan tersedia di data produk
id_produk_penjualan = set(df_penjualan["ID_Produk"])
id_produk_master = set(df_produk["ID_Produk"])
id_produk_stok = set(df_stok["ID_Produk"])

# print(
#     "ID penjualan tidak ditemukan di data produk:",
#     id_produk_penjualan - id_produk_master
# )

# print(
#     "ID produk tidak ditemukan di data stok:",
#     id_produk_master - id_produk_stok
# )

# # Memeriksa kesesuaian total harga
total_seharusnya = (
    df_penjualan["Jumlah_Terjual"] *
    df_penjualan["Harga_Satuan"]
)

# print(
#     "Total harga tidak sesuai:",
#     (df_penjualan["Total_Harga"] != total_seharusnya).sum()
# )

# # 8. MEMERIKSA NILAI TIDAK WAJAR

# print("\n--- PEMERIKSAAN NILAI ---")

# print(
#     "Jumlah terjual <= 0:",
#     (df_penjualan["Jumlah_Terjual"] <= 0).sum()
# )

# print(
#     "Harga satuan <= 0:",
#     (df_penjualan["Harga_Satuan"] <= 0).sum()
# )

# print(
#     "Harga modal <= 0:",
#     (df_produk["Harga_Modal"] <= 0).sum()
# )

# print(
#     "Stok minimum < 0:",
#     (df_produk["Stok_Minimum"] < 0).sum()
# )

# print(
#     "Stok saat ini < 0:",
#     (df_stok["Stok_Saat_Ini"] < 0).sum()
# )

# # 9. HASIL AKHIR

# print("\n--- TIPE DATA SETELAH CLEANING ---")

# print("\nDATA PENJUALAN")
# print(df_penjualan.info())

# print("\nDATA PRODUK")
# print(df_produk.info())

# print("\nDATA STOK")
# print(df_stok.info())

# print("\nProses pembacaan dan pemeriksaan data selesai.")

# 10. MENGHITUNG TOTAL PRODUK TERJUAL

total_penjualan = (
    df_penjualan
    .groupby("ID_Produk")["Jumlah_Terjual"]
    .sum()
    .reset_index()
)

total_penjualan = total_penjualan.rename(
    columns={"Jumlah_Terjual": "Total_Terjual"}
)

# print("\n--- TOTAL PRODUK TERJUAL ---")
# print(total_penjualan)

# 11. MENGHITUNG RATA-RATA PENJUALAN HARIAN

tanggal_awal = df_penjualan["Tanggal_Waktu"].min()
tanggal_akhir = df_penjualan["Tanggal_Waktu"].max()

jumlah_hari = (tanggal_akhir - tanggal_awal).days + 1

total_penjualan["Rata_Rata_Harian"] = (
    total_penjualan["Total_Terjual"] / jumlah_hari
)

# print("\n--- RATA-RATA PENJUALAN HARIAN ---")
# print(total_penjualan)
# print("\nJumlah hari pengamatan:", jumlah_hari)

df_analisis = (
    df_produk
    .merge(total_penjualan, on="ID_Produk", how="left")
    .merge(df_stok, on="ID_Produk", how="left")
)

df_analisis["Total_Terjual"] = df_analisis["Total_Terjual"].fillna(0)
df_analisis["Rata_Rata_Harian"] = df_analisis["Rata_Rata_Harian"].fillna(0)

# print("\n--- DATA GABUNGAN ---")
# print(df_analisis)

df_analisis["Estimasi_Daya_Tahan_Hari"] = (
    df_analisis["Stok_Saat_Ini"] /
    df_analisis["Rata_Rata_Harian"].replace(0, pd.NA)
)

# print("\n--- ESTIMASI DAYA TAHAN STOK ---")
# print(
#     df_analisis[
#         ["ID_Produk", "Nama_Produk", "Stok_Saat_Ini",
#          "Rata_Rata_Harian", "Estimasi_Daya_Tahan_Hari"]
#     ]
# )

lead_time = 5
safety_stock = 2

df_analisis["ROP"] = (
    df_analisis["Rata_Rata_Harian"] * lead_time
    + safety_stock
).apply(math.ceil)

# print("\n--- REORDER POINT ---")
# print(
#     df_analisis[
#         ["ID_Produk", "Nama_Produk", "Rata_Rata_Harian", "ROP"]
#     ]
# )

def tentukan_rekomendasi(baris):
    if baris["Stok_Saat_Ini"] <= baris["ROP"]:
        return "Perlu Restock"
    else:
        return "Stok Aman"

df_analisis["Rekomendasi"] = df_analisis.apply(
    tentukan_rekomendasi, axis=1
)

# print("\n--- REKOMENDASI RESTOCK ---")
# print(
#     df_analisis[
#         ["ID_Produk", "Nama_Produk", "Stok_Saat_Ini", "ROP", "Rekomendasi"]
#     ]
# )

hari_persediaan = 14

df_analisis["Target_Stok"] = (
    df_analisis["Rata_Rata_Harian"] *
    (lead_time + hari_persediaan)
    + safety_stock
).apply(math.ceil)

df_analisis["Jumlah_Pesanan"] = df_analisis.apply(
    lambda baris: max(
        0,
        baris["Target_Stok"] - baris["Stok_Saat_Ini"]
    ) if baris["Stok_Saat_Ini"] <= baris["ROP"] else 0,
    axis=1
)

print("\n--- REKOMENDASI JUMLAH PEMESANAN ---")
print(
    df_analisis[
        ["ID_Produk", "Nama_Produk", "Stok_Saat_Ini",
         "ROP", "Target_Stok", "Jumlah_Pesanan"]
    ]
)

df_analisis["Estimasi_Biaya"] = (
    df_analisis["Jumlah_Pesanan"] *
    df_analisis["Harga_Modal"]
)

df_restock = df_analisis[
    df_analisis["Jumlah_Pesanan"] > 0
].copy()

df_restock = df_restock.sort_values(
    by="Estimasi_Daya_Tahan_Hari",
    ascending=True
)

print("\n--- DAFTAR REKOMENDASI RESTOCK ---")
print(
    df_restock[
        ["ID_Produk", "Nama_Produk", "Stok_Saat_Ini",
         "ROP", "Jumlah_Pesanan", "Harga_Modal", "Estimasi_Biaya"]
    ]
)

total_biaya = df_restock["Estimasi_Biaya"].sum()

print("\nTotal estimasi biaya pembelian: Rp{:,.0f}".format(total_biaya))


