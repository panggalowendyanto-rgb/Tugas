# Paket tugas besar ASI — tenggat 26 Oktober 2026

Judul: **Evaluasi Keamanan Personal AI Agent Menuju Artificial Superintelligence: Analisis AlphaZero dan Eksperimen Specification Gaming pada Tingkat Otonomi AI dalam Aktivitas Sehari-hari**.

## Status yang harus dibaca dahulu

Paket menyediakan draf dokumen, aplikasi, bank prompt, dan analisis yang dapat dijalankan. **Belum ada eksperimen API resmi yang dieksekusi.** Data API kosong, identitas dua model belum dipilih, dan penilaian manusia belum dilakukan. Angka pada mode simulasi aplikasi adalah sintetis. Bagian eksperimen belum memenuhi kewajiban rubrik untuk menjalankan eksperimen; jangan mengumpulkannya seolah hasil empiris telah tersedia.

Argumen, analisis, dan kesimpulan di draf dibantu AI dan wajib ditinjau, disusun ulang berdasarkan pemikiran peneliti, dan disahkan peneliti sesuai ketentuan PDF. Identitas Nama/NIM belum diisi. Tidak ada skor kemiripan/plagiarisme yang diklaim.

## Isi

- `dokumen/Proposal_ASI_2_Halaman.pdf`: tepat 2 halaman.
- `dokumen/Makalah_ASI_IEEE_Draf.pdf`: 11 halaman isi, dua kolom bergaya IEEE, ditambah 1 halaman referensi dan 1 halaman lampiran penggunaan AI. Lima bagian wajib tersedia.
- `dokumen/Makalah_ASI_sumber.md`: sumber yang dapat disunting.
- `dokumen/Makalah_IEEEtran.tex`: sumber untuk kelas IEEEtran resmi. PDF yang disertakan dirender dengan ReportLab dengan tata letak dua kolom, bukan hasil kompilasi kelas IEEEtran. Bila dosen mensyaratkan berkas template resmi secara ketat, kompilasi sumber ini dengan instalasi LaTeX yang memiliki IEEEtran; periksa lagi jumlah halaman dan format setelah kompilasi. Sumber IEEEtran berhasil dikompilasi oleh editor LaTeX bawaan setelah perbaikan sintaks. PDF unduhan utama tetap render dua kolom ReportLab; tampilan dan jumlah halaman hasil kompilasi kelas resmi belum diekspor/diverifikasi.
- `presentasi/Presentasi_ASI_15_Menit_Final_v2.pptx`: slide editable dengan catatan pembicara dan alokasi total 15 menit.
- `presentasi/Naskah_Presentasi_dan_Waktu.md`: panduan penyampaian; tambah 10 menit tanya jawab.
- `presentasi/Panduan_Tanya_Jawab.md`: latihan penguasaan materi.
- `aplikasi/`: dashboard tanpa Streamlit, runner API, pengujian, dan README rinci.
- `data/skenario_50.json`: 50 skenario, masing-masing dua kondisi.
- `data/prompt_600.csv` dan `rencana_600.json`: 600 pekerjaan, 50 per model/kondisi/level; tidak berisi respons model.
- `data/hasil_api.json`: kosong (`[]`), bukan hasil fiktif.
- `analisis/analyze.py`: Wilson, McNemar eksak, Holm keluarga16, bootstrap pasangan.
- `analisis/agreement.py`: kesepakatan dan Cohen kappa dua penilai.
- `analisis/hasil/`: laporan aktual berstatus `NOT_EXECUTED`.
- `referensi/`: 26 entri total; 18 ilmiah, termasuk 13 terbit2022–2026; sumber kebijakan tidak masuk hitungan ilmiah.
- `PERNYATAAN_PENGGUNAAN_AI.md`, `PEMETAAN_RUBRIK.md`, `LAPORAN_VERIFIKASI.md`.

## Menjalankan aplikasi — tanpa instalasi

Ekstrak seluruh ZIP, kemudian buka `aplikasi/index.html` pada browser modern. Jangan membuka berkas HTML langsung dari dalam penampil ZIP. Semua aset lokal, tanpa CDN atau font internet. Pilih **Sumber → Data nyata** untuk melihat status empiris. Pilih **Simulasi** untuk mencoba filter, grafik, penilaian, dan ekspor. Ekspor cadangan JSON secara berkala karena penyimpanan browser bukan arsip penelitian permanen.

Jika browser membatasi berkas lokal, jalankan dari folder paket:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory aplikasi
```

Buka `http://127.0.0.1:8000`. Hentikan server dengan Ctrl+C. Gunakan `python` pada Windows jika `python3` tidak tersedia.

## Menjalankan eksperimen resmi

Python3.10+; pustaka standar, tidak ada pip wajib. Node hanya diperlukan untuk tes pengembang. API resmi memerlukan akun, koneksi internet dan dapat menimbulkan biaya sesuai pemakaian.

1. Tinjau dan bekukan hipotesis, bank prompt, rubrik serta aturan penilaian. Baca `dokumen/Makalah_ASI_sumber.md` Bagian III.
2. Masuk folder `aplikasi`. Salin `config.example.json` ke `config.json`; isi dua ID model resmi berbeda yang didukung akun. Tetapkan parameter sesuai dokumentasi model dan simpan konfigurasinya. Endpoint contoh menggunakan OpenAI Chat Completions resmi. Belum dipilih dua model aktual dan tidak ada klaim akses API.
3. Masukkan API key melalui environment lokal, bukan browser atau berkas konfigurasi. Pada zsh/macOS:

```sh
read -s OPENAI_API_KEY
export OPENAI_API_KEY
```

4. Periksa rencana tanpa biaya, kemudian uji koneksi dua respons:

```sh
python3 runner.py --config config.json --dry-run
python3 runner.py --config config.json --output results.json --execute --limit 2
```

5. Bila protokol tetap sama, lanjutkan batch; checkpoint melewati pekerjaan sukses. Bila protokol diubah setelah uji coba, gunakan output studi baru.

```sh
python3 runner.py --config config.json --output results.json --execute
```

6. Impor `results.json` ke aplikasi. Berikan dua penilai salinan independen; sembunyikan identitas model pada salinan penilaian. Simpan ekspor awal masing-masing. Aplikasi tidak otomatis membutakan identitas; peneliti harus mengatur salinan dan pemetaan model. Jangan mengedit ID respons.
7. Hitung kesepakatan sebelum adjudikasi; kemudian simpan ekspor konsensus sebagai `data/hasil_api_dinilai.json`.

```sh
python3 analisis/agreement.py penilai1.json penilai2.json --out analisis/agreement.json
python3 analisis/analyze.py --input data/hasil_api_dinilai.json --out analisis/hasil_nyata
```

Perintah di atas dijalankan dari akar paket; sesuaikan lokasi ekspor penilai. Skrip analisis hanya menerima sumber `real`; sumber `demo`, `manual`, dan `planned` dikeluarkan. Jalur aplikasi publik manual memerlukan audit provenance dan perluasan protokol, tidak otomatis diperlakukan setara data API.

8. Periksa status COMPLETE dan 12 sel × 50 dinilai. Sel belum lengkap tidak mendukung kesimpulan konfirmatori. Perbarui tabel hasil dan pembahasan dengan angka aktual; jangan menyalin demo. Isi identitas, pernyataan AI, dan simpulan pribadi.

## Reproduksibilitas dan batas

Seed pengacakan runner20261020; bootstrap20261025. H1 enam kontras, H2 empat, H3 enam; Holm untuk16 uji. Dashboard memiliki enam uji model eksploratif Bonferroni; angka itu bukan analisis utama makalah. Gunakan keluaran `analisis/analyze.py` untuk pelaporan konfirmatori. Identitas model yang berubah, hash campuran, dan duplikat ditolak.

Skor ARS berbobot level tidak membuktikan H2. Pembagi hanya respons sukses dengan lima label lengkap. Error, data hilang dan respons belum dinilai dilaporkan terpisah. Hasil berasal dari simulasi teks, bukan tindakan nyata. Satu respons per skenario/sel; multi-run memerlukan desain dan analisis baru.

## Pengumpulan

Unggah PDF melalui SIKOLA dengan nama **NIM_Nama_TugasBesar.pdf** setelah identitas benar dan hasil aktual diperbarui. Rubrik meminta tautan repositori GitHub/GitLab; ZIP ini menyediakan sumber untuk diunggah, tetapi belum ada repositori daring yang dibuat. Buat repositori milik peneliti dan unggah kode, prompt, config tanpa key, serta data mentah yang aman dipublikasikan. Jangan unggah API key, riwayat pribadi, atau data peserta. Tenggat **Senin, 26 Oktober 2026**; rubrik memberikan15menit presentasi dan10menit tanya jawab.
