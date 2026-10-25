# Laporan verifikasi

Tanggal: 20 Oktober 2026.

Lulus:
- Empat unit test Python: 600 pekerjaan dan 50 skenario unik di setiap sel; dua model berbeda; urutan tetap dengan seed; hash berubah saat prompt berubah; penyimpanan JSON atomik.
- Test JavaScript: pembagi mengecualikan error dan label kosong; risiko batas 0/100; CI Wilson; uji McNemar pada pasangan dengan hasil yang diketahui; 600 demo berlabel lengkap.
- Pemeriksaan sintaks app.js, metrics.js, data.js dan runner.py.
- Dry run: 600 pekerjaan, 50 skenario, tanpa panggilan jaringan.
- Pemeriksaan referensi aset lokal dan 50 ID skenario unik.

Batas verifikasi:
- Tidak ada API model berbayar yang dipanggil: model nyata dan API key belum dipilih/disediakan. Runner belum diuji terhadap kredensial/provider nyata.
- Browser pengujian menolak URL file:// berdasarkan kebijakan protokol. Pemeriksaan visual/interaksi browser tidak selesai; tidak ada workaround server yang dipakai. Tampilan responsif, penyimpanan file-origin, dialog, unduh, dan impor perlu smoke test pada browser pengguna.
- Statistik teruji dengan kasus deterministik, bukan validasi ilmiah indeks ARS. Demo tidak merupakan temuan penelitian.


Pembaruan25Oktober2026: empat tes runner, tes metrik, pemeriksaan sintaks dan dry run600 pekerjaan lulus kembali. Browser lokal diverifikasi untuk dashboard, pemisahan simulasi/data nyata, dan navigasi konfigurasi50skenario. Laporan tingkat paket ada di ../LAPORAN_VERIFIKASI.md.
