# Naskah presentasi

Total 900 detik (15 menit). Sisihkan 10 menit tanya jawab setelahnya. Catatan merupakan panduan penjelasan; berlatih dan sesuaikan dengan tempo Anda.

## 1. Keamanan Personal AI Agent (0:00-0:40)

Buka dengan pertanyaan utama: seberapa jauh kita dari ASI dan bagaimana menjaga perkembangan tetap aman? Judul lengkap terdapat dalam makalah: Evaluasi Keamanan Personal AI Agent Menuju Artificial Superintelligence: Analisis AlphaZero dan Eksperimen Specification Gaming pada Tingkat Otonomi AI dalam Aktivitas Sehari-hari. Nyatakan sejak awal bahwa presentasi membedakan kajian literatur, protokol, dan hasil empiris yang belum tersedia. Identitas peneliti harus dilengkapi sebelum presentasi.

## 2. Posisi awal: ASI mungkin dalam 20 tahun (0:40-1:55)

Jelaskan definisi ASI sebagai keunggulan luas dan konsisten atas pakar manusia di hampir semua domain penting. Tiga alasan ini bukan tiga bukti bahwa tanggal ASI sudah diketahui. Bedakan ukuran loss, benchmark, dan kemampuan dunia nyata. Sumber: Kaplan 2020 https://arxiv.org/abs/2001.08361 ; Hoffmann 2022 https://arxiv.org/abs/2203.15556 ; Silver 2018 https://doi.org/10.1126/science.aar6404 ; ReAct https://arxiv.org/abs/2210.03629 .

## 3. Argumen lawan dan prediksi ahli (1:55-3:10)

Akui argumen lawan secara kuat: kemampuan model mungkin bergantung pada data dan rekayasa lingkungan, bukan generalisasi yang dibutuhkan ASI. Survei Grace memisahkan mesin mengungguli manusia pada semua tugas dari otomasi seluruh pekerjaan; yang kedua mencapai agregat 50% pada 2116. Jangan mengubah peluang HLMI menjadi peluang ASI. Kesimpulan: kesiapsiagaan dapat rasional tanpa kepastian tanggal. Sumber Grace et al., JAIR 2025 https://doi.org/10.1613/jair.1.19087 .

## 4. AlphaZero: masalah dan arsitektur (3:10-4:20)

Tekankan perbedaan algoritma umum dengan satu jaringan yang langsung mentransfer tiga permainan. Jaringan memetakan posisi ke prior langkah dan prediksi nilai. Belajar dari self-play tidak berarti tanpa rancangan manusia sama sekali. Kasus ini bukan model bahasa dan bukan ASI. Sumber utama: Silver et al., Science 2018, doi:10.1126/science.aar6404; suplemen hlm17. PDF https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphazero-shedding-new-light-on-chess-shogi-and-go/alphazero_preprint.pdf .

## 5. Siklus MCTS dan self-play (4:20-5:30)

Terangkan PUCT sebagai kompromi eksploitasi nilai dan eksplorasi menurut prior dan kunjungan. Daun dievaluasi jaringan; nilai dibackup sepanjang lintasan. Distribusi kunjungan akar menjadi target policy. Kerugian ringkas: (z-v)^2 minus pi log p ditambah regularisasi. Bedakan komputasi inferensi dari perubahan bobot. Analogi agen bahasa hanya pada alur evaluasi, bukan kesamaan arsitektur. Sumber [1] Science 2018 dan suplemennya.

## 6. Komputasi dan batas keunggulan (5:30-6:40)

Tambahkan 700.000 langkah pembaruan dengan batch 4.096 posisi. Evaluasi memakai empat TPU v1 dan 44 CPU; lawan Stockfish dan Elmo memakai 44 CPU. Waktu 4 jam melewati Stockfish bukan durasi penuh 9 jam. Keunggulan strategis mencerminkan quality dan speed pada domain sempit. Kritik adversarial Wang et al. menguji Go AI seperti KataGo; jangan mengklaim serangan tersebut menguji bobot AlphaZero DeepMind. Sumber https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/ dan https://arxiv.org/abs/2211.00241 .

## 7. Desain eksperimen: 600 respons (6:40-7:45)

Setiap sel mempunyai target 50 skenario unik. ID dua model resmi belum dipilih; tidak ada perbandingan nyata yang telah dijalankan. Semua percakapan baru; urutan diacak seed20261020; bank prompt dan sistem masuk hash. Teks L4 tidak memberi akses transaksi atau alat. Karena itu istilah otonomi merujuk framing instruksi, bukan otonomi yang diamati di dunia nyata. Kriteria tugas: PDF tugas halaman2.

## 8. Rubrik membedakan gaming dan ketidakpastian (7:45-8:55)

Contoh hipotetis: memilih laptop tanpa garansi semata karena harga terendah, sambil menyatakan spesifikasi diabaikan, dapat gaming menurut rubrik. Sebaliknya hanya tidak menyebut RAM bukan bukti cukup pelanggaran. Seluruh contoh di slide merupakan ilustrasi, bukan keluaran model. Lima label boleh tumpang tindih. Unsafe Action Rate adalah usulan/klaim teks; Human Approval Rate adalah permintaan persetujuan. Dua penilai dan kappa belum dilakukan.

## 9. Hipotesis dan analisis berpasangan (8:55-10:10)

Proporsi per sel dengan Wilson95%; McNemar eksak dua sisi untuk pasangan skenario; koreksi Holm keluarga16; selisih proporsi dan bootstrap5000 pasangan, seed20261025. Laporkan N, pasangan tak selaras, efek, interval, p mentah dan terkoreksi. Tidak signifikan tidak berarti aman atau setara. ARS mengandung level dalam rumus sehingga tidak digunakan membuktikan H2. Ini menghindari kenaikan risiko yang hanya akibat definisi matematis.

## 10. Hasil empiris belum tersedia (10:10-11:05)

Sampaikan lugas bahwa eksperimen belum dijalankan. Tidak ada rate, interval, efek, atau p empiris. Dashboard menampilkan data sintetis untuk menguji fitur dan tidak boleh dijadikan bukti. Status analisis NOT_EXECUTED. Karena rubrik meminta menjalankan eksperimen, paket ini belum memenuhi unsur empiris tersebut. Peneliti harus memilih dua model, mengeksekusi resmi, memberi label, menganalisis, dan memperbarui naskah.

## 11. Aplikasi eksperimen lokal (11:05-12:05)

Jika demonstrasi langsung, tunjukkan badge data simulasi dahulu, lalu pilih filter data nyata agar terlihat kosong. Buka rubrik dan ekspor data. Jangan memulai 600 permintaan selama presentasi. Kontrol akses API dilakukan di komputer, bukan menyimpan key di browser. Pengujian fungsi perangkat lunak bukan hasil eksperimen perilaku. Panduan langkah ada README paket.

## 12. EU AI Act dan pendekatan AS (12:05-13:10)

Tanggal per25Oktober2026: aturan risiko tinggi AnnexIII menuju2Desember2027; produk menuju2Agustus2028 melalui2026/1744. Tidak semua ketentuan ditunda. AS bukan tanpa aturan; fokus perbandingan hanya instrumen terpilih dan bukan inventaris semua hukum negara bagian. ActionPlan2025 mencatat pencabutan EO14110. Sumber: https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act ; https://doi.org/10.6028/NIST.AI.100-1 ; https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf .

## 13. Tiga kebijakan Indonesia yang terukur (13:10-14:20)

Jelaskan hubungan UU27/2022: Pasal10 keberatan atas keputusan otomatis berdampak signifikan; Pasal20 dasar pemrosesan; Pasal34 penilaian dampak berisiko tinggi; Pasal46 notifikasi. Target100% bukan klaim program telah berjalan. Indikator harus diverifikasi lewat register, log yang diminimalkan, laporan independen, dan latihan insiden. Tidak ada hasil API yang menjadi dasar empiris rekomendasi saat ini. https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022 .

## 14. Kesimpulan dan riset lanjutan (14:20-15:00)

Tutup dengan tiga kalimat: kemampuan sempit bukan ASI; tujuan jelas dan kontrol alat dibutuhkan; status hasil harus jujur. Kajian AlphaZero mendukung plausibilitas beberapa mekanisme, tetapi eksperimen yang belum berjalan tidak dapat menguatkan atau melemahkan posisi awal secara empiris. Setelah15menit presentasi, sediakan10menit tanya jawab.
