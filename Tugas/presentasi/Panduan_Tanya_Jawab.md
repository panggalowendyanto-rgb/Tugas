# Panduan tanya jawab — 10 menit

**Mengapa horizon 20 tahun?** Posisi kemungkinan hingga 2046, bukan ramalan terkalibrasi. Tiga jalur bukti: efisiensi scaling, pencarian/umpan balik, komposisi alat. Akui ketiganya belum membuktikan generalisasi atau keselamatan; berikan penilaian sendiri setelah membaca sumber.

**Apakah AlphaZero sudah ASI?** Tidak menurut definisi lintas domain makalah. Algoritma dipakai pada tiga permainan dengan instans terpisah, bukan satu bobot universal.

**Apa peran MCTS?** Policy memberi prior, value mengevaluasi daun; pencarian Q+U menghasilkan distribusi kunjungan. Self-play memperbaiki policy/value. Bedakan pencarian inferensi dan pembaruan parameter.

**Mengapa angka TPU berbeda?** Science 2018: 5.000 TPU v1 self-play, 16 TPU v2 training jaringan. Evaluasi: 4 TPU v1 + 44 CPU. Laporan 2017 mempunyai konfigurasi berbeda. Empat jam melampaui Stockfish bukan durasi penuh sembilan jam.

**Apakah kritik Go AI menguji AlphaZero?** Wang dkk. menguji sistem seperti KataGo. Temuan merupakan peringatan ketahanan keluarga pendekatan, bukan uji terhadap bobot AlphaZero DeepMind.

**Apa hasil eksperimen Anda?** Versi paket ini belum mempunyai hasil API. Ada 600 pekerjaan terencana dan demo sintetis terpisah. Setelah eksekusi, gantikan jawaban dengan N, efek, interval, serta batas aktual. Jangan memakai angka demo.

**Mengapa McNemar?** Respons berpasangan pada skenario sama. Uji menggunakan pasangan berbeda label; versi eksak cocok saat jumlahnya kecil. Enam belas kontras dikoreksi Holm.

**Apakah ARS pasti naik dengan level?** Ada level dalam rumus. H2 memakai unsafe L4 vs L0; ARS deskriptif. Memakai ARS membuktikan H2 akan bersifat melingkar.

**Bagaimana mengetahui maksud pada prompt ambigu?** Rubrik adalah maksud skenario peneliti, bukan nilai universal. Gaming menuntut bukti jalan pintas dan pelanggaran; tidak menyebut batas bukan bukti cukup. Kasus batas dicatat dan diadjudikasi.

**Apa kelemahan 50 skenario?** Minimum tugas bukan analisis daya. Nol kejadian pada 50 respons masih memberi batas atas Wilson sekitar 7,1%. Kemiripan skenario dan satu pengulangan membatasi generalisasi.

**Apa beda ujaran dan tindakan?** Penelitian menilai teks tanpa alat. Unsafe Action Rate adalah usulan/klaim. Lanjutan memerlukan sandbox berkeadaan, log alat, dan verifikasi dampak.

**Mengapa kebijakan jika belum ada hasil?** Usulan berasal dari literatur dan analisis risiko, bukan gaming rate yang belum ada. Tunjukkan pelaksana, waktu, KPI dan bukti audit serta kaitan Pasal 10, 20, 34, 46 UU PDP.

**Apakah seluruh AI Act berlaku penuh 2026?** Tidak. Per 25 Oktober 2026, jadwal Annex III menuju 2 Desember 2027 dan sistem terkait produk 2 Agustus 2028 melalui 2026/1744. Kewajiban lain berbeda. AS Action Plan bukan undang-undang larangan ASI.

**Seberapa besar bantuan AI?** Ungkap bantuan pada sumber, draf, kode, data sintetis, statistik, dan slide. Tunjukkan bacaan, koreksi, serta verifikasi pribadi. Rubrik mensyaratkan substansi pemikiran sendiri; bila belum dilakukan, akui belum selesai.
