import React from "react";

export const caseStudiesData = [
  // =========================================================================
  // PROJECT 1: EDP RETAIL WEEKLY PERFORMANCE
  // =========================================================================
  {
    id: "edp-weekly-reporting",
    title: "Retail Weekly Performance & KPI Dashboard (EDP)",
    badgeCategory: "DATA ANALYTICS & REPORTING",
    badgeTool: "MICROSOFT EXCEL",
    badgeRole: "EDP / STORE DATA",
    impactSummary:
      "Memangkas waktu rekap mingguan dan menyajikan insight pertumbuhan YoY ritel serta efisiensi toko (UPT, BagSize, AUR, CRR) secara otomatis.",
    downloadUrl: "/downloads/EDP_Retail_Weekly_Analytics.xlsx",
    sheetTitle: "EDP_Weekly_Retail_Analytics.xlsx",
    
    // Gallery with 3 specific crops (120-130% zoom)
    gallery: [
      {
        src: "/assets/case-studies/edp-dashboard-main.svg",
        thumbLabel: "Dashboard Cover (6 KPI)",
        title: "Executive Dashboard: 6 KPI Cards & YoY Comparison",
        desc: "Potongan sheet DASHBOARD yang menyorot 6 kartu KPI eksekutif dan grafik batang perbandingan Sales 2025 vs 2026.",
      },
      {
        src: "/assets/case-studies/edp-formula-weekly.svg",
        thumbLabel: "Formula Bar (SUMIFS)",
        title: "Sheet WEEKLY: Formula Bar Aktif & Metrik Ritel",
        desc: "Formula Bar aktif menyorot rumus dinamis SUMIFS, UPT (=QTY/TRX), BagSize, dan Conversion Rate (CRR).",
      },
      {
        src: "/assets/case-studies/edp-raw-data.svg",
        thumbLabel: "Data Mentah (SELISIH 0)",
        title: "Sheet DATA MENTAH: Validasi Selisih Divisi & ISOWEEKNUM",
        desc: "Struktur data transaksi harian ribuan baris dengan validasi selisih divisi (SELISIH +/- = 0) dan ekstraksi nomor pekan ISO.",
      },
    ],

    // STAR framework text
    problem:
      "Data transaksi harian ritel terdiri dari ribuan baris yang terpecah per divisi dan channel, sehingga sulit dibaca tren pertumbuhannya secara cepat oleh manajemen untuk pengambilan keputusan promo mingguan.",
    
    process:
      "Membangun pipeline pelaporan otomatis berbasis ISOWEEKNUM dan SUMIFS dinamis yang mengonversi data mentah harian menjadi komparasi mingguan (Year-over-Year) serta menghitung metrik efisiensi toko (UPT, BagSize, AUR, Conversion Rate) beserta generator narasi analisis otomatis.",
    
    workflowSteps: [
      "Data Mentah & Ekstraksi ISOWEEKNUM",
      "Otomatisasi Rumus Dinamis SUMIFS",
      "Dashboard Eksekutif & Narasi Otomatis",
    ],

    impact:
      "Memangkas 85% waktu rekap laporan mingguan toko, mengeliminasi human error saat konsolidasi multi-divisi, dan menyajikan insight pertumbuhan ritel secara visual dalam satu lembar dashboard siap pakai.",

    tags: [
      "Microsoft Excel",
      "SUMIFS Dinamis",
      "ISOWEEKNUM",
      "UPT & BagSize",
      "YoY Growth",
      "Data Validation",
      "Executive Charting",
    ],

    formulas: [
      {
        name: "SUMIFS Dinamis (Konsolidasi Omzet Mingguan)",
        formula: "=SUMIFS('DATA MENTAH'!$D:$D, 'DATA MENTAH'!$U:$U, $C$2, 'DATA MENTAH'!$W:$W, $A4)",
        explanation:
          "Menjumlahkan total penjualan ('DATA MENTAH'!$D:$D) secara dinamis dengan kriteria Tahun ($C$2) dan Pekan ISO ($A4).",
      },
      {
        name: "Units Per Transaction (UPT / Kedalaman Keranjang)",
        formula: "=ROUND(Total_QTY / TRX, 2)",
        explanation:
          "Mengukur rata-rata jumlah barang yang dibeli pelanggan per struk transaksi.",
      },
      {
        name: "Bag Size (Nilai Belanja Rata-Rata)",
        formula: "=ROUND(Total_SALES / TRX, 0)",
        explanation:
          "Menghitung rata-rata nominal rupiah per keranjang belanja pelanggan.",
      },
      {
        name: "Conversion Rate (CRR)",
        formula: "=ROUND((TRX / TRAFFIC) * 100, 2) & \" %\"",
        explanation:
          "Persentase pengunjung toko yang berhasil dikonversi menjadi transaksi kasir.",
      },
      {
        name: "Narasi Analisis Otomatis (Dynamic Text Insight)",
        formula: '=IF(E9>0, "Pertumbuhan positif " & TEXT(E9, "0.0%") & " didorong kenaikan UPT", "Evaluasi traffic")',
        explanation:
          "Menghasilkan kalimat rekomendasi eksekutif secara dinamis berdasarkan angka persentase pertumbuhan.",
      },
    ],

    // Live Sheet preview tabs
    sheetTabs: [
      {
        name: "DASHBOARD",
        content: (
          <div className="space-y-4 text-xs font-sans">
            {/* KPI Cards Preview */}
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2">
              <div className="p-3 rounded-xl bg-slate-900 border border-slate-700">
                <span className="text-[10px] text-slate-400 font-semibold block">SALES 2025</span>
                <span className="text-sm font-bold text-slate-200">Rp 1.942.500.000</span>
              </div>
              <div className="p-3 rounded-xl bg-slate-900 border border-sky-500/40">
                <span className="text-[10px] text-sky-400 font-semibold block">SALES 2026</span>
                <span className="text-sm font-bold text-white">Rp 2.215.800.000</span>
              </div>
              <div className="p-3 rounded-xl bg-slate-900 border border-emerald-500/40">
                <span className="text-[10px] text-emerald-400 font-semibold block">YOY GROWTH</span>
                <span className="text-sm font-bold text-emerald-400">+14.07%</span>
              </div>
              <div className="p-3 rounded-xl bg-slate-900 border border-slate-700">
                <span className="text-[10px] text-slate-400 font-semibold block">AVG CRR</span>
                <span className="text-sm font-bold text-slate-200">72.40%</span>
              </div>
              <div className="p-3 rounded-xl bg-slate-900 border border-slate-700">
                <span className="text-[10px] text-slate-400 font-semibold block">AVG UPT</span>
                <span className="text-sm font-bold text-amber-300">2.18 pcs</span>
              </div>
              <div className="p-3 rounded-xl bg-slate-900 border border-slate-700">
                <span className="text-[10px] text-slate-400 font-semibold block">AVG BAG SIZE</span>
                <span className="text-sm font-bold text-slate-200">Rp 324.500</span>
              </div>
            </div>

            {/* Table */}
            <div className="overflow-x-auto rounded-xl border border-slate-800">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="bg-blue-950 text-blue-200 font-semibold">
                    <th className="p-2.5 border-b border-slate-800">WEEK</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">% Growth Sales</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">% Growth In-Store</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">% Growth QTY</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">% Growth TRX</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">% Growth UPT</th>
                    <th className="p-2.5 border-b border-slate-800">Insight Otomatis</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800 text-slate-300">
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-bold text-white">WEEK 36</td>
                    <td className="p-2 text-center text-emerald-400 font-semibold">+12.4%</td>
                    <td className="p-2 text-center">+10.8%</td>
                    <td className="p-2 text-center">+15.2%</td>
                    <td className="p-2 text-center">+8.9%</td>
                    <td className="p-2 text-center text-amber-300">+5.8%</td>
                    <td className="p-2 text-slate-400">Pertumbuhan stabil, kenaikan sales didorong traffic dan basket size.</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-bold text-white">WEEK 37</td>
                    <td className="p-2 text-center text-emerald-400 font-semibold">+18.7%</td>
                    <td className="p-2 text-center">+16.2%</td>
                    <td className="p-2 text-center">+20.1%</td>
                    <td className="p-2 text-center">+12.4%</td>
                    <td className="p-2 text-center text-amber-300">+6.9%</td>
                    <td className="p-2 text-slate-400">Performa optimal pasca payday campaign, UPT melampaui target.</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-bold text-white">WEEK 38</td>
                    <td className="p-2 text-center text-emerald-400 font-semibold">+9.5%</td>
                    <td className="p-2 text-center">+8.1%</td>
                    <td className="p-2 text-center">+11.3%</td>
                    <td className="p-2 text-center">+6.2%</td>
                    <td className="p-2 text-center text-amber-300">+4.8%</td>
                    <td className="p-2 text-slate-400">Pertumbuhan melandai pertengahan bulan, CRR stabil di atas 70%.</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-bold text-white">WEEK 39</td>
                    <td className="p-2 text-center text-emerald-400 font-semibold">+14.8%</td>
                    <td className="p-2 text-center">+13.0%</td>
                    <td className="p-2 text-center">+17.5%</td>
                    <td className="p-2 text-center">+10.1%</td>
                    <td className="p-2 text-center text-amber-300">+6.7%</td>
                    <td className="p-2 text-slate-400">Aktivitas promosi weekend efektif mengerek volume QTY transaksi.</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-bold text-white">WEEK 40</td>
                    <td className="p-2 text-center text-emerald-400 font-semibold">+15.2%</td>
                    <td className="p-2 text-center">+13.9%</td>
                    <td className="p-2 text-center">+16.8%</td>
                    <td className="p-2 text-center">+11.0%</td>
                    <td className="p-2 text-center text-amber-300">+5.2%</td>
                    <td className="p-2 text-slate-400">Penutupan bulan September positif dengan peningkatan total omzet YoY.</td>
                  </tr>
                  <tr className="bg-blue-950/40 font-bold text-white">
                    <td className="p-2.5">TOTAL / AVG</td>
                    <td className="p-2.5 text-center text-emerald-400">+14.1%</td>
                    <td className="p-2.5 text-center">+12.4%</td>
                    <td className="p-2.5 text-center">+16.2%</td>
                    <td className="p-2.5 text-center">+9.7%</td>
                    <td className="p-2.5 text-center text-amber-300">+5.9%</td>
                    <td className="p-2.5 text-blue-300">Secara kumulatif performa September 2026 tumbuh kuat vs 2025.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        ),
      },
      {
        name: "WEEKLY (SUMIFS)",
        content: (
          <div className="overflow-x-auto rounded-xl border border-slate-800 text-xs">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-teal-950 text-teal-200 font-semibold">
                  <th className="p-2.5 border-b border-slate-800">WEEK_ISO</th>
                  <th className="p-2.5 border-b border-slate-800">YEAR</th>
                  <th className="p-2.5 border-b border-slate-800 text-right">SALES 2025</th>
                  <th className="p-2.5 border-b border-slate-800 text-right">SALES 2026</th>
                  <th className="p-2.5 border-b border-slate-800 text-center">YoY %</th>
                  <th className="p-2.5 border-b border-slate-800 text-center">TRX</th>
                  <th className="p-2.5 border-b border-slate-800 text-center">UPT</th>
                  <th className="p-2.5 border-b border-slate-800">FORMULA SUMIFS REF</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800 text-slate-300 font-mono">
                <tr>
                  <td className="p-2 font-bold text-white">36</td>
                  <td className="p-2 text-slate-400">2026</td>
                  <td className="p-2 text-right">354.890.000</td>
                  <td className="p-2 text-right text-sky-400 font-bold">398.900.000</td>
                  <td className="p-2 text-center text-emerald-400">+12.4%</td>
                  <td className="p-2 text-center">1.438</td>
                  <td className="p-2 text-center text-amber-300 font-bold">2.27</td>
                  <td className="p-2 text-teal-400 font-mono text-[10px]">=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,36)</td>
                </tr>
                <tr>
                  <td className="p-2 font-bold text-white">37</td>
                  <td className="p-2 text-slate-400">2026</td>
                  <td className="p-2 text-right">412.500.000</td>
                  <td className="p-2 text-right text-sky-400 font-bold">489.600.000</td>
                  <td className="p-2 text-center text-emerald-400">+18.7%</td>
                  <td className="p-2 text-center">1.698</td>
                  <td className="p-2 text-center text-amber-300 font-bold">2.34</td>
                  <td className="p-2 text-teal-400 font-mono text-[10px]">=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,37)</td>
                </tr>
                <tr>
                  <td className="p-2 font-bold text-white">38</td>
                  <td className="p-2 text-slate-400">2026</td>
                  <td className="p-2 text-right">389.400.000</td>
                  <td className="p-2 text-right text-sky-400 font-bold">426.400.000</td>
                  <td className="p-2 text-center text-emerald-400">+9.5%</td>
                  <td className="p-2 text-center">1.508</td>
                  <td className="p-2 text-center text-amber-300 font-bold">2.30</td>
                  <td className="p-2 text-teal-400 font-mono text-[10px]">=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,38)</td>
                </tr>
              </tbody>
            </table>
          </div>
        ),
      },
      {
        name: "DATA MENTAH",
        content: (
          <div className="overflow-x-auto rounded-xl border border-slate-800 text-xs">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-slate-900 text-slate-300 font-semibold">
                  <th className="p-2 border-b border-slate-800">DATE</th>
                  <th className="p-2 border-b border-slate-800">STORE LOC</th>
                  <th className="p-2 border-b border-slate-800 text-right">Total_SALES</th>
                  <th className="p-2 border-b border-slate-800 text-center">QTY</th>
                  <th className="p-2 border-b border-slate-800 text-center">TRX</th>
                  <th className="p-2 border-b border-slate-800 text-center text-emerald-400">SELISIH +/-</th>
                  <th className="p-2 border-b border-slate-800 text-center text-sky-400">WEEK_ISO</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800 text-slate-300 font-mono">
                <tr>
                  <td className="p-2">2026-09-01</td>
                  <td className="p-2 font-sans text-slate-400">STORE DEMO NUSANTARA</td>
                  <td className="p-2 text-right font-bold text-white">61.858.000</td>
                  <td className="p-2 text-center">526</td>
                  <td className="p-2 text-center">188</td>
                  <td className="p-2 text-center text-emerald-400 font-bold">0 (OK)</td>
                  <td className="p-2 text-center text-sky-400">36</td>
                </tr>
                <tr>
                  <td className="p-2">2026-09-02</td>
                  <td className="p-2 font-sans text-slate-400">STORE DEMO NUSANTARA</td>
                  <td className="p-2 text-right font-bold text-white">46.846.000</td>
                  <td className="p-2 text-center">370</td>
                  <td className="p-2 text-center">148</td>
                  <td className="p-2 text-center text-emerald-400 font-bold">0 (OK)</td>
                  <td className="p-2 text-center text-sky-400">36</td>
                </tr>
                <tr>
                  <td className="p-2">2026-09-03</td>
                  <td className="p-2 font-sans text-slate-400">STORE DEMO NUSANTARA</td>
                  <td className="p-2 text-right font-bold text-white">46.200.000</td>
                  <td className="p-2 text-center">361</td>
                  <td className="p-2 text-center">154</td>
                  <td className="p-2 text-center text-emerald-400 font-bold">0 (OK)</td>
                  <td className="p-2 text-center text-sky-400">36</td>
                </tr>
                <tr>
                  <td className="p-2">2026-09-04</td>
                  <td className="p-2 font-sans text-slate-400">STORE DEMO NUSANTARA</td>
                  <td className="p-2 text-right font-bold text-white">101.723.000</td>
                  <td className="p-2 text-center">820</td>
                  <td className="p-2 text-center">379</td>
                  <td className="p-2 text-center text-emerald-400 font-bold">0 (OK)</td>
                  <td className="p-2 text-center text-sky-400">36</td>
                </tr>
              </tbody>
            </table>
          </div>
        ),
      },
    ],
  },

  // =========================================================================
  // PROJECT 2: ADMIN S&T OMNICHANNEL SALES TRACKING & RECONCILIATION
  // =========================================================================
  {
    id: "snt-omnichannel-tracking",
    title: "Omnichannel Sales Tracking & Daily Reconciliation (S&T)",
    badgeCategory: "DATA ANALYTICS & REPORTING",
    badgeTool: "MICROSOFT EXCEL",
    badgeRole: "ADMIN SALES & REKONSILIASI",
    impactSummary:
      "Memastikan 100% nota transaksi harian lintas 3 channel (WA, TikTok, Haptik) dan multi-payment terekonsiliasi seimbang ke target mingguan/bulanan tanpa selisih mutasi.",
    downloadUrl: "/downloads/SNT_Omnichannel_Reconciliation.xlsx",
    sheetTitle: "SNT_Omnichannel_Reconciliation.xlsx",

    gallery: [
      {
        src: "/assets/case-studies/snt-target-weekly.svg",
        thumbLabel: "Rekap Siklus Mingguan",
        title: "Sheet TARGET SNT OKTOBER: Rekap Siklus Minggu-Sabtu",
        desc: "Konsolidasi nota harian ke 5 blok siklus mingguan (Minggu-Sabtu) hingga total bulanan beserta grafik pencapaian target 108.1%.",
      },
      {
        src: "/assets/case-studies/snt-input-nota.svg",
        thumbLabel: "Input Nota & Validasi",
        title: "Sheet INPUT NOTA: Validasi CEK (HARUS 0) & Pemisahan Net 1.11",
        desc: "Tabel pencatatan nota transaksi omnichannel dengan validasi keseimbangan otomatis dan eliminasi PPN 11% (DPP murni).",
      },
      {
        src: "/assets/case-studies/snt-audit-leaderboard.svg",
        thumbLabel: "Audit Selisih & Sales Rank",
        title: "Sheet SELISIH OKTOBER & Leaderboard Sales Person",
        desc: "Log audit selisih mutasi bank/QRIS harian (alasan selisih) disandingkan dengan peringkat performa sales person via INDEX/MATCH.",
      },
    ],

    problem:
      "Transaksi omnichannel (WhatsApp, TikTok, Haptik) dengan metode pembayaran beragam (QRIS, VA, Transfer) membutuhkan pencatatan nota harian yang akurat hingga rekap mingguan dan bulanan tanpa celah selisih transaksi dan mutasi bank.",

    process:
      "Mengelola pencatatan nota terintegrasi lintas 31 lembar harian dengan validasi keseimbangan otomatis (CEK HARUS 0), pemisahan DPP/Nett (1.11), pelacakan performa Sales Person via INDEX/MATCH, serta pengelompokan akumulasi siklus Minggu–Sabtu hingga tutup buku bulanan.",

    workflowSteps: [
      "Input Nota & Validasi Keseimbangan (CEK 0)",
      "Pemisahan DPP Net 1.11 & Lookup Sales",
      "Akumulasi Siklus Minggu-Sabtu & Audit Bank",
    ],

    impact:
      "Memastikan 100% nota harian terkonsolidasi ke target mingguan/bulanan, mempermudah audit selisih mutasi bank harian, dan menghasilkan data komisi sales person yang transparan dan akurat.",

    tags: [
      "Microsoft Excel",
      "INDEX / MATCH",
      "Validasi CEK (HARUS 0)",
      "DPP / Net 1.11",
      "Siklus Minggu-Sabtu",
      "Audit Rekonsiliasi Bank",
      "Leaderboard Sales",
    ],

    formulas: [
      {
        name: "Validasi Keseimbangan Nota (CEK HARUS 0)",
        formula: '=IF(ROUND(F2 - (J2 + N2), 2) = 0, 0, "CEK SELISIH")',
        explanation:
          "Memastikan Total Struk (F2) sama persis dengan Gross DP (J2) + Gross CV (N2). Jika tidak 0, baris ditandai warna merah.",
      },
      {
        name: "Pemisahan DPP Murni (Net 1.11)",
        formula: "=ROUND(K2 / 1.11, 0)",
        explanation:
          "Mengeliminasi komponen PPN 11% sehingga omzet yang diakui murni merupakan Dasar Pengenaan Pajak (DPP).",
      },
      {
        name: "Lookup Nama & Divisi Sales Person (INDEX/MATCH)",
        formula: "=INDEX('DATABASE SALES'!$B:$B, MATCH(A2, 'DATABASE SALES'!$A:$A, 0))",
        explanation:
          "Mengambil nama sales person berdasarkan barcode ID transaksi tanpa resiko formula error VLOOKUP.",
      },
      {
        name: "Akumulasi Siklus Mingguan (Minggu - Sabtu)",
        formula: '=SUMIFS(Harian!$F:$F, Harian!$A:$A, ">="&$L5, Harian!$A:$A, "<="&$M5)',
        explanation:
          "Menjumlahkan transaksi harian yang berada dalam rentang tanggal awal (Minggu) dan akhir (Sabtu) siklus pelaporan.",
      },
      {
        name: "Audit Rekonsiliasi Mutasi Bank",
        formula: "=Total_Struk_Bruto - Mutasi_Masuk_Bank",
        explanation:
          "Mendeteksi selisih antara pencatatan kasir/admin dengan riil uang yang masuk ke rekening bank / QRIS.",
      },
    ],

    sheetTabs: [
      {
        name: "TARGET SNT OKTOBER",
        content: (
          <div className="space-y-4 text-xs font-sans">
            <div className="p-3 rounded-xl bg-indigo-950/60 border border-indigo-500/30 flex items-center justify-between">
              <div>
                <span className="text-[10px] text-indigo-300 font-bold uppercase tracking-wider block">TARGET VS ACTUAL BULANAN</span>
                <span className="text-base font-extrabold text-white">Target: Rp 59.600.000 | Actual Net: Rp 64.402.000</span>
              </div>
              <span className="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">
                ACHIEVEMENT: 108.1% (SURPLUS)
              </span>
            </div>

            <div className="overflow-x-auto rounded-xl border border-slate-800">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="bg-indigo-950 text-indigo-200 font-semibold">
                    <th className="p-2.5 border-b border-slate-800">PERIODE MINGGU (MIN - SAB)</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">TARGET TRX</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">ACT TRX</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">ACH TRX</th>
                    <th className="p-2.5 border-b border-slate-800 text-right">TARGET SALES</th>
                    <th className="p-2.5 border-b border-slate-800 text-right">ACTUAL SALES (NET 1.11)</th>
                    <th className="p-2.5 border-b border-slate-800 text-center text-emerald-400">ACH SALES</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800 text-slate-300 font-mono">
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-sans font-medium text-white">Week 1 (01 - 03 Okt | Parsial)</td>
                    <td className="p-2 text-center text-slate-400">39</td>
                    <td className="p-2 text-center text-white font-bold">43</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">110.3%</td>
                    <td className="p-2 text-right text-slate-400">6.000.000</td>
                    <td className="p-2 text-right text-white font-bold">6.842.000</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">114.0%</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-sans font-medium text-white">Week 2 (04 - 10 Okt | Min - Sab)</td>
                    <td className="p-2 text-center text-slate-400">88</td>
                    <td className="p-2 text-center text-white font-bold">94</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">106.8%</td>
                    <td className="p-2 text-right text-slate-400">13.400.000</td>
                    <td className="p-2 text-right text-white font-bold">14.210.000</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">106.0%</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-sans font-medium text-white">Week 3 (11 - 17 Okt | Min - Sab)</td>
                    <td className="p-2 text-center text-slate-400">88</td>
                    <td className="p-2 text-center text-white font-bold">91</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">103.4%</td>
                    <td className="p-2 text-right text-slate-400">13.400.000</td>
                    <td className="p-2 text-right text-white font-bold">13.890.000</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">103.7%</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-sans font-medium text-white">Week 4 (18 - 24 Okt | Min - Sab)</td>
                    <td className="p-2 text-center text-slate-400">88</td>
                    <td className="p-2 text-center text-white font-bold">96</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">109.1%</td>
                    <td className="p-2 text-right text-slate-400">13.400.000</td>
                    <td className="p-2 text-right text-white font-bold">14.850.000</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">110.8%</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-sans font-medium text-white">Week 5 (25 - 31 Okt | Min - Sab)</td>
                    <td className="p-2 text-center text-slate-400">88</td>
                    <td className="p-2 text-center text-white font-bold">95</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">108.0%</td>
                    <td className="p-2 text-right text-slate-400">13.400.000</td>
                    <td className="p-2 text-right text-white font-bold">14.610.000</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">109.0%</td>
                  </tr>
                  <tr className="bg-indigo-950/60 font-bold text-white">
                    <td className="p-2.5 font-sans">TOTAL MINGGUAN (= BULANAN)</td>
                    <td className="p-2.5 text-center text-indigo-300">391</td>
                    <td className="p-2.5 text-center text-white">419</td>
                    <td className="p-2.5 text-center text-emerald-400">107.2%</td>
                    <td className="p-2.5 text-right text-indigo-300">59.600.000</td>
                    <td className="p-2.5 text-right text-emerald-300">64.402.000</td>
                    <td className="p-2.5 text-center text-emerald-400">108.1%</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        ),
      },
      {
        name: "SELISIH & AUDIT",
        content: (
          <div className="space-y-4 text-xs font-sans">
            <div className="overflow-x-auto rounded-xl border border-slate-800">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="bg-red-950 text-red-200 font-semibold">
                    <th className="p-2.5 border-b border-slate-800">TANGGAL</th>
                    <th className="p-2.5 border-b border-slate-800 text-right">NOMINAL SELISIH</th>
                    <th className="p-2.5 border-b border-slate-800 text-center">STATUS</th>
                    <th className="p-2.5 border-b border-slate-800">AUDIT LOG / ALASAN SELISIH</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800 text-slate-300 font-mono">
                  <tr className="bg-amber-950/20">
                    <td className="p-2 font-bold text-white">04/10/2026</td>
                    <td className="p-2 text-right font-bold text-amber-400">+Rp 150.000</td>
                    <td className="p-2 text-center text-amber-300 font-bold">SELISIH (+)</td>
                    <td className="p-2 font-sans text-amber-200">Transfer customer Rp150.000 masuk rekening namun belum ditransaksikan ke POS (menunggu konfirmasi barang).</td>
                  </tr>
                  <tr className="bg-red-950/20">
                    <td className="p-2 font-bold text-white">12/10/2026</td>
                    <td className="p-2 text-right font-bold text-red-400">-Rp 49.900</td>
                    <td className="p-2 text-center text-red-300 font-bold">SELISIH (-)</td>
                    <td className="p-2 font-sans text-red-200">Customer melakukan retur tukar size/produk selisih kurang bayar Rp49.900.</td>
                  </tr>
                  <tr className="bg-amber-950/20">
                    <td className="p-2 font-bold text-white">21/10/2026</td>
                    <td className="p-2 text-right font-bold text-amber-400">+Rp 85.000</td>
                    <td className="p-2 text-center text-amber-300 font-bold">SELISIH (+)</td>
                    <td className="p-2 font-sans text-amber-200">Kelebihan transfer customer Rp85.000, dicatat sebagai saldo deposit transaksi berikutnya.</td>
                  </tr>
                  <tr className="hover:bg-slate-900/60">
                    <td className="p-2 font-bold text-white">28 Hari Lainnya</td>
                    <td className="p-2 text-right text-emerald-400 font-bold">Rp 0</td>
                    <td className="p-2 text-center text-emerald-400 font-bold">MATCH (100%)</td>
                    <td className="p-2 font-sans text-slate-400">Rekonsiliasi sesuai persis (Struk kasir = Mutasi masuk bank/QRIS).</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        ),
      },
      {
        name: "LEADERBOARD SALES",
        content: (
          <div className="overflow-x-auto rounded-xl border border-slate-800 text-xs">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-emerald-950 text-emerald-200 font-semibold">
                  <th className="p-2.5 border-b border-slate-800 text-center">RANK</th>
                  <th className="p-2.5 border-b border-slate-800">NAMA SALES PERSON</th>
                  <th className="p-2.5 border-b border-slate-800 text-center">DIVISI</th>
                  <th className="p-2.5 border-b border-slate-800 text-center">TOTAL TRX</th>
                  <th className="p-2.5 border-b border-slate-800 text-right">TOTAL OMZET (BRUTO)</th>
                  <th className="p-2.5 border-b border-slate-800">FORMULA LOOKUP</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800 text-slate-300">
                <tr className="bg-amber-950/15">
                  <td className="p-2 text-center font-bold text-amber-300">🥇 1</td>
                  <td className="p-2 font-bold text-white">RINA KUSUMAWATI</td>
                  <td className="p-2 text-center text-slate-400">DIV 1</td>
                  <td className="p-2 text-center font-mono">52</td>
                  <td className="p-2 text-right font-mono text-emerald-400 font-bold">Rp 9.840.000</td>
                  <td className="p-2 font-mono text-[10px] text-teal-400">=INDEX('SALES'!$B:$B, MATCH(A2, 'SALES'!$A:$A, 0))</td>
                </tr>
                <tr className="bg-slate-900/40">
                  <td className="p-2 text-center font-bold text-slate-300">🥈 2</td>
                  <td className="p-2 font-bold text-white">DIMAS PRASETYO</td>
                  <td className="p-2 text-center text-slate-400">DIV 1</td>
                  <td className="p-2 text-center font-mono">48</td>
                  <td className="p-2 text-right font-mono text-emerald-400 font-bold">Rp 8.910.000</td>
                  <td className="p-2 font-mono text-[10px] text-teal-400">=INDEX('SALES'!$B:$B, MATCH(A3, 'SALES'!$A:$A, 0))</td>
                </tr>
                <tr className="bg-amber-900/10">
                  <td className="p-2 text-center font-bold text-amber-500">🥉 3</td>
                  <td className="p-2 font-bold text-white">SITI NURHALIZA</td>
                  <td className="p-2 text-center text-slate-400">DIV 2</td>
                  <td className="p-2 text-center font-mono">46</td>
                  <td className="p-2 text-right font-mono text-emerald-400 font-bold">Rp 8.420.000</td>
                  <td className="p-2 font-mono text-[10px] text-teal-400">=INDEX('SALES'!$B:$B, MATCH(A4, 'SALES'!$A:$A, 0))</td>
                </tr>
                <tr>
                  <td className="p-2 text-center text-slate-500">4</td>
                  <td className="p-2 text-slate-200">BAGUS WICAKSONO</td>
                  <td className="p-2 text-center text-slate-400">DIV 2</td>
                  <td className="p-2 text-center font-mono">43</td>
                  <td className="p-2 text-right font-mono text-slate-300">Rp 7.650.000</td>
                  <td className="p-2 font-mono text-[10px] text-teal-400">=INDEX('SALES'!$B:$B, MATCH(A5, 'SALES'!$A:$A, 0))</td>
                </tr>
                <tr>
                  <td className="p-2 text-center text-slate-500">5</td>
                  <td className="p-2 text-slate-200">DEWI ANGGRAINI</td>
                  <td className="p-2 text-center text-slate-400">DIV 3</td>
                  <td className="p-2 text-center font-mono">42</td>
                  <td className="p-2 text-right font-mono text-slate-300">Rp 7.520.000</td>
                  <td className="p-2 font-mono text-[10px] text-teal-400">=INDEX('SALES'!$B:$B, MATCH(A6, 'SALES'!$A:$A, 0))</td>
                </tr>
              </tbody>
            </table>
          </div>
        ),
      },
    ],
  },
];
