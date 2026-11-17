/**
 * Default Project Data
 * Diambil langsung dari Laporan Akhir D3 Manajemen Informatika (CV. Widi Elektrical)
 * dan Laporan Praktik Kerja Lapangan (Dinas Perkim Kabupaten Kediri)
 * oleh Widi Putri Audy (NIM: 2331730042)
 */

export const defaultProjects = [
  {
    id: "widi-elektrical-web",
    Title: "Sistem Informasi Manajemen Jasa CV Widi Elektrical",
    Description:
      "Aplikasi web end-to-end untuk digitalisasi operasional jasa servis AC di CV. Widi Elektrical Kediri. Mengatasi permasalahan pesanan fiktif (ghosting) melalui integrasi Payment Gateway Midtrans (DP 50% & pelunasan), pemesanan multi-kuantitas dengan validasi operasional Carbon, integrasi titik koordinat GPS/peta interaktif, sistem penjadwalan dinamis anti-bentrok (schedules table), serta broadcast pengingat otomatis via WhatsApp Gateway (Fonnte) & Cron Job.",
    Img: "/assets/projects/widi-elektrical.jpg",
    Link: null,
    Github: "Private",
    Category: "Full-Stack Web App",
    Role: "Full-Stack Web Developer & System Analyst (Tugas Akhir D3)",
    Period: "Januari – April 2026",
    Institution: "CV. Widi Elektrical • PSDKU Polinema di Kota Kediri",
    TechStack: [
      "Laravel",
      "PHP",
      "MySQL",
      "Midtrans",
      "WhatsApp API",
      "HTML",
      "CSS",
      "Javascript",
      "Bootstrap",
    ],
    Features: [
      "Dual-Payment Gateway Midtrans (DP 50% & Pelunasan Otomatis via Webhook)",
      "Pemesanan Multi-Kuantitas (Pesan beberapa jenis & unit servis dalam 1 checkout via pivot order_service)",
      "Validasi Waktu Operasional Ketat (Pustaka Carbon: Blokir pesanan hari Minggu, jam 08:00–17:00, & same-day minimal jeda 6 jam)",
      "Peta Interaktif & HTML5 Geolocation API (Ekstraksi koordinat Latitude/Longitude presisi untuk navigasi teknisi)",
      "Manajemen Jadwal Dinamis Anti-Bentrok (Tabel transaksional schedules dengan evaluasi status Busy/Ready linear)",
      "Penugasan Tim Multi-Teknisi (Admin dapat menugaskan >1 teknisi per pesanan via order_user)",
      "Broadcast WhatsApp Gateway (Fonnte API: Notifikasi invoice, detail tugas & rute Maps langsung ke ponsel teknisi)",
      "Automated Task Scheduling & Cron Job (Reminder tugas H-1 pukul 16:00 WIB dan pengingat H-3 jam keberangkatan)",
      "Verifikasi & Moderasi Portofolio Kerja (Teknisi upload foto bukti lapangan -> Admin approve -> Tayang publik)",
      "Dasbor Finansial & Auto-Reset Omzet Bulanan (whereMonth/whereYear kalkulasi murni transaksi sukses Paid, abaikan cancel)",
    ],
  },
  {
    id: "perkim-kediri-web",
    Title: "Website Profil dan Layanan Publik Dinas Perkim Kabupaten Kediri",
    Description:
      "Portal resmi informasi dan layanan publik digital Dinas Perumahan dan Kawasan Permukiman (DISPERKIM) Kabupaten Kediri. Memfasilitasi masyarakat untuk pengajuan layanan online (PJU, Bantuan Perumahan RTLH, Perbaikan Fasilitas) dengan upload foto bukti, pengecekan status pengajuan mandiri berbasis NIK 16-digit, kanal aspirasi kritik & saran dua arah, serta panel admin terpadu untuk verifikasi, tindak lanjut, dan publikasi berita dinas.",
    Img: "/assets/projects/perkim-kediri.jpg",
    Link: null,
    Github: "Private",
    Category: "Public Service & E-Gov",
    Role: "Web Developer & UI/UX Designer (Praktik Kerja Lapangan / PKL)",
    Period: "1 Juli – 22 Agustus 2025",
    Institution: "Dinas Perumahan dan Kawasan Permukiman Kab. Kediri",
    TechStack: [
      "PHP",
      "MySQL",
      "HTML",
      "CSS",
      "Javascript",
      "Bootstrap",
    ],
    Features: [
      "Portal Resmi E-Government Dinas Perkim Kab. Kediri (Visi Misi, Struktur Organisasi, Profil, & Layanan Daerah)",
      "Formulir Pengajuan Layanan Masyarakat Online (PJU, Perbaikan Fasilitas Umum, Bantuan RTLH/MBR, Penataan Lingkungan)",
      "Upload Foto Bukti Lapangan Pendukung (Validasi file image hingga 5MB untuk verifikasi kondisi riil)",
      "Pengecekan Status Pengajuan Mandiri Berbasis NIK (Transparansi pelacakan berkas permohonan tanpa perlu antre)",
      "Kanal Aspirasi Publik Dua Arah (Formulir Kritik & Saran terintegrasi dengan balasan resmi dari administrator)",
      "Portal Berita & Informasi Terkini (Publikasi kegiatan dinas, penambahan PJU 6 wilayah, tanggap bencana Mojo)",
      "Panel Admin Moderasi Pengajuan (Ubah status pengajuan Diproses/Ditolak/Selesai dilengkapi catatan verifikasi dinas)",
      "Sistem Keamanan Autentikasi Admin Terproteksi (Login multi-session & CSRF security)",
      "Desain Responsif Multi-Device (Bootstrap 5 grid optimal untuk layar desktop, tablet, dan smartphone)",
    ],
  },
];
