import streamlit as st
import sistem

st.sidebar.title("Inventory System")
st.sidebar.write("Dashboard Manajemen Stok")
st.sidebar.divider()

halaman = st.sidebar.radio(
    "Navigasi",
    ["Ringkasan", "Analisis Penjualan", "Manajemen Stok"]
)

df = sistem.df_analisis
total_produk = len(df)
total_penjualan = df["Total_Terjual"].sum()
perlu_restock = (df["Rekomendasi"] == "Perlu Restock").sum()
stok_aman = total_produk - perlu_restock

if halaman == 'Ringkasan':
    st.header("Ringkasan Persediaan")
    kolom1, kolom2, kolom3, kolom4 = st.columns(4)
    with kolom1:
        st.metric("Total Produk", total_produk)
    with kolom2:
        st.metric("Total Penjualan", total_penjualan)
    with kolom3:
        st.metric("Perlu Restock", perlu_restock)
    with kolom4:
        st.metric("Stok Aman", stok_aman)

elif halaman == 'Analisis Penjualan':
    st.header("Grafik Penjualan Produk")
    st.bar_chart(sistem.df_analisis, x="Nama_Produk", y="Total_Terjual")

    st.header("Tren Penjualan Berdasarkan Jam")
    df_jam = sistem.df_penjualan.copy()
    df_jam["Jam"] = df_jam["Tanggal_Waktu"].dt.hour
    penjualan_per_jam = df_jam.groupby("Jam")["ID_Transaksi"].nunique().reset_index(name="Jumlah_Transaksi")
    st.line_chart(
        penjualan_per_jam,
        x="Jam",
        y="Jumlah_Transaksi"
    )

else:
    st.header("Kondisi Persediaan")
    st.dataframe(
        sistem.df_analisis[
            ["Nama_Produk", "Stok_Saat_Ini", "ROP", "Rekomendasi"]
        ]
    )

    st.header("Rekomendasi Restock")
    df_restock = sistem.df_analisis[
        sistem.df_analisis["Rekomendasi"] == "Perlu Restock"
    ]
    st.dataframe(
        df_restock[
            ["Nama_Produk", "Stok_Saat_Ini", "ROP", "Target_Stok", "Jumlah_Pesanan"]
        ]
    )

# python -m streamlit run "Sistem Manajemen Stok/dashboard.py"
