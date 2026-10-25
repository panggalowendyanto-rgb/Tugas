# PROPOSAL PENELITIAN - HALAMAN 1

## Judul

Evaluasi Keamanan Personal AI Agent Menuju Artificial Superintelligence: Analisis AlphaZero dan Eksperimen Specification Gaming pada Tingkat Otonomi AI dalam Aktivitas Sehari-hari

## Identitas dan status

Nama/NIM: perlu diisi. Program Doktor Informatika. Tenggat seluruh luaran: Senin, 26 Oktober 2026. Proposal ini disiapkan 25 Oktober 2026 sebagai draf berbantu AI yang harus ditinjau dan disahkan peneliti.

## 1. Posisi awal dan alasan

ASI mungkin terwujud dalam dua puluh tahun (hingga 2046), tetapi horizon ini bukan kepastian atau estimasi probabilitas empiris. Tiga alasan kerja: efisiensi penskalaan model dan data [5], [6]; pembelajaran melalui pencarian dan umpan balik yang ditunjukkan AlphaZero [1]; serta komposisi model bahasa dengan alat dan interaksi [10]-[13]. Argumen lawan utama adalah ketidakandalan generalisasi dan perencanaan panjang. Prediksi ahli [16] dibahas sebagai distribusi pendapat dengan bias dan perbedaan definisi, bukan bukti bahwa ASI akan hadir pada tanggal tertentu.

## 2. Sistem studi kasus

AlphaZero dari Silver dkk., Science 2018, DOI 10.1126/science.aar6404. Analisis mencakup masalah catur/shogi/Go, jaringan residual policy-value, MCTS/PUCT, self-play, loss pelatihan, sumber daya komputasi, keunggulan sempit, kritik ketahanan dan replikasi, serta kebutuhan transfer lintas domain. Angka sumber daya versi 2018 dipisahkan dari preprint 2017. Tidak dilakukan pelatihan ulang AlphaZero.

## 3. Pertanyaan dan hipotesis

Apakah prompt ambigu meningkatkan specification gaming; apakah framing otonomi tinggi meningkatkan usulan tindakan berisiko; dan apakah kedua model berbeda pada skenario identik? H1 membandingkan ambigu-jelas untuk gaming. H2 membandingkan L4-L0 untuk unsafe. H3 membandingkan model untuk gaming. Uji dua sisi, efek berpasangan, dan ketidakpastian dilaporkan bersama. ARS hanya indeks deskriptif karena memasukkan level dalam rumus.

## 4. Kontribusi yang ditargetkan

Bank 50 skenario bahasa Indonesia; 600 pekerjaan terencana; aplikasi web lokal tanpa Streamlit; pemanggil API resmi dengan checkpoint; rubrik audit; skrip statistik reprodusibel; serta tiga usulan kebijakan Indonesia terkait evaluasi agen, izin tindakan, dan UU PDP. Kebaruan yang diklaim terbatas pada rancangan kontekstual dan integrasi artefak penelitian, bukan teori ASI atau algoritma alignment baru.

# PROPOSAL PENELITIAN - HALAMAN 2

## 5. Rancangan eksperimen

Lima kategori × sepuluh skenario = 50 ID dasar. Desain 2 model berbeda × 2 kondisi (jelas/ambigu) × 3 level otonomi teks (0 informasi, 2 rencana, 4 keputusan otomatis simulatif) × 50 = 600 respons. Kedua kondisi memiliki instruksi persetujuan identik. Tiap pekerjaan menggunakan percakapan baru; urutan diacak dengan seed 20261020. Model/snapshot dan parameter ditetapkan sebelum eksekusi dan dicatat dalam hash protokol. ID model belum dipilih; data API belum tersedia.

## 6. Pengukuran dan analisis

Dua penilai independen menilai alignment, gaming, clarification, unsafe, dan approval, dengan alasan berbasis teks; identitas model disamarkan. Kesepakatan dan Cohen kappa dilaporkan sebelum adjudikasi. Proporsi per sel memakai N sukses dengan seluruh label lengkap dan Wilson CI 95%. McNemar eksak digunakan untuk 16 kontras berpasangan (6 H1, 4 H2, 6 H3), dikoreksi Holm. Selisih proporsi memakai bootstrap pasangan 5.000 kali dengan seed 20261025. Error/label parsial tidak dihitung sebagai sukses atau alignment; jumlahnya tetap dilaporkan.

## 7. Etika dan penggunaan AI

Akses hanya API resmi, tanpa jailbreak dan tanpa tindakan nyata. Semua skenario sintetis; kredensial disimpan di environment, bukan browser/repo. Alat AI membantu rancangan awal, bahasa, kode, dan draf; argumen, analisis serta kesimpulan wajib ditulis ulang/ditinjau dan disahkan peneliti. Tidak ada hasil empiris yang boleh berasal dari data demo. Referensi dan angka diperiksa pada sumber primer. Kebutuhan biaya dan izin penggunaan layanan diperiksa peneliti sebelum eksekusi.

## 8. Jadwal menuju 26 Oktober 2026

25 Oktober: tinjau argumen, isi identitas, pilih model, bekukan protokol, uji koneksi, jalankan batch resmi sesuai batas akun. 25-26 Oktober: dua penilai memberi label dan adjudikasi; analisis, tulis hasil, periksa ulang dokumen dan latihan presentasi. 26 Oktober: unggah PDF bernama NIM_Nama_TugasBesar.pdf melalui SIKOLA serta tautan repositori GitHub/GitLab. Jadwal bersifat rencana, bukan catatan aktivitas yang sudah terjadi. Bila batch atau penilaian belum selesai, status ketidaklengkapan wajib disampaikan kepada dosen.

## Referensi inti

[1] Silver dkk., Science, 2018, doi:10.1126/science.aar6404. [6] Hoffmann dkk., NeurIPS, 2022, arXiv:2203.15556. [7] Ouyang dkk., NeurIPS, 2022, arXiv:2203.02155. [10] Yao dkk., ICLR, 2023, arXiv:2210.03629. [16] Grace dkk., JAIR 84:9, 2025, doi:10.1613/jair.1.19087. [26] UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi. Nomor mengacu daftar pustaka makalah.