import os

def generate_svgs():
    output_dir = r"public\assets\case-studies"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. EDP Dashboard Main
    svg1 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6366F1"/>
      <stop offset="100%" stop-color="#8B5CF6"/>
    </linearGradient>
    <linearGradient id="bar25" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#64748B"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
    <linearGradient id="bar26" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Excel Window Frame -->
  <rect width="1000" height="620" rx="14" fill="url(#bgGrad)" stroke="#334155" stroke-width="1.5"/>
  
  <!-- Excel Title Bar -->
  <rect width="1000" height="42" rx="14" fill="#090D16"/>
  <rect y="28" width="1000" height="14" fill="#090D16"/>
  <circle cx="24" cy="21" r="5" fill="#EF4444"/>
  <circle cx="42" cy="21" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="21" r="5" fill="#10B981"/>
  <text x="500" y="26" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Microsoft Excel - EDP_Weekly_Retail_Analytics.xlsx [Sheet: DASHBOARD (Zoom 125%)]
  </text>

  <!-- Excel Ribbon Bar & Formula Bar -->
  <rect y="42" width="1000" height="34" fill="#1E293B" stroke="#334155" stroke-width="1"/>
  <rect x="16" y="48" width="46" height="22" rx="4" fill="#334155"/>
  <text x="39" y="63" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">B4</text>
  <text x="76" y="63" fill="#64748B" font-family="system-ui, sans-serif" font-size="12" font-style="italic">fx</text>
  <rect x="96" y="48" width="888" height="22" rx="4" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <text x="110" y="63" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11">
    =SUMIFS('DATA MENTAH'!$D:$D, 'DATA MENTAH'!$U:$U, 2026, 'DATA MENTAH'!$V:$V, "September")
  </text>

  <!-- Sheet Content Area -->
  <g transform="translate(24, 92)">
    <!-- Header Banner -->
    <rect width="952" height="52" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
    <text x="20" y="26" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="16" font-weight="bold">EXECUTIVE WEEKLY RETAIL DASHBOARD</text>
    <text x="20" y="42" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">Periode: September 2026 | Benchmark: September 2025 (Store Demo Nusantara)</text>
    <rect x="800" y="14" width="136" height="26" rx="6" fill="#10B981" fill-opacity="0.2" stroke="#10B981" stroke-width="1"/>
    <text x="868" y="31" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">● AUTOMATED FEED</text>

    <!-- 6 KPI CARDS -->
    <g transform="translate(0, 66)">
      <!-- KPI 1 -->
      <rect x="0" y="0" width="148" height="74" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1" filter="url(#shadow)"/>
      <text x="14" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">SALES 2025</text>
      <text x="14" y="46" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Rp 1.942 M</text>
      <text x="14" y="63" fill="#64748B" font-family="system-ui, sans-serif" font-size="9">Total Omzet Sept</text>

      <!-- KPI 2 -->
      <rect x="160" y="0" width="148" height="74" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.2" filter="url(#shadow)"/>
      <text x="174" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">SALES 2026</text>
      <text x="174" y="46" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">Rp 2.215 M</text>
      <text x="174" y="63" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9">+14.07% vs LY</text>

      <!-- KPI 3 -->
      <rect x="320" y="0" width="148" height="74" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.2" filter="url(#shadow)"/>
      <text x="334" y="22" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="600">YOY GROWTH</text>
      <text x="334" y="46" fill="#34D399" font-family="system-ui, sans-serif" font-size="16" font-weight="bold">+14.07%</text>
      <text x="334" y="63" fill="#10B981" font-family="system-ui, sans-serif" font-size="9">▲ Target Exceeded</text>

      <!-- KPI 4 -->
      <rect x="480" y="0" width="148" height="74" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1" filter="url(#shadow)"/>
      <text x="494" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">AVG CRR (CONV)</text>
      <text x="494" y="46" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">72.40%</text>
      <text x="494" y="63" fill="#64748B" font-family="system-ui, sans-serif" font-size="9">Conversion Rate</text>

      <!-- KPI 5 -->
      <rect x="640" y="0" width="148" height="74" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1" filter="url(#shadow)"/>
      <text x="654" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">AVG UPT (BASKET)</text>
      <text x="654" y="46" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">2.18 pcs</text>
      <text x="654" y="63" fill="#34D399" font-family="system-ui, sans-serif" font-size="9">▲ +5.9% vs LY</text>

      <!-- KPI 6 -->
      <rect x="800" y="0" width="152" height="74" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1" filter="url(#shadow)"/>
      <text x="814" y="22" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="600">AVG BAG SIZE</text>
      <text x="814" y="46" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">Rp 324.5K</text>
      <text x="814" y="63" fill="#34D399" font-family="system-ui, sans-serif" font-size="9">▲ +4.0% vs LY</text>
    </g>

    <!-- CHART AREA & COMPARISON TABLE (SPLIT) -->
    <g transform="translate(0, 154)">
      <!-- Left: YoY Comparison Bar Chart -->
      <rect width="520" height="210" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <text x="16" y="24" fill="#F1F5F9" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">Weekly Sales Trend (2025 vs 2026)</text>
      
      <!-- Legend -->
      <rect x="360" y="14" width="10" height="10" rx="2" fill="#64748B"/>
      <text x="376" y="23" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">2025</text>
      <rect x="420" y="14" width="10" height="10" rx="2" fill="#38BDF8"/>
      <text x="436" y="23" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">2026</text>

      <!-- Grid lines -->
      <line x1="30" y1="50" x2="490" y2="50" stroke="#334155" stroke-dasharray="3,3"/>
      <line x1="30" y1="90" x2="490" y2="90" stroke="#334155" stroke-dasharray="3,3"/>
      <line x1="30" y1="130" x2="490" y2="130" stroke="#334155" stroke-dasharray="3,3"/>
      <line x1="30" y1="170" x2="490" y2="170" stroke="#475569"/>

      <!-- Bars: W36 -->
      <rect x="60" y="78" width="22" height="92" rx="3" fill="url(#bar25)"/>
      <rect x="86" y="62" width="22" height="108" rx="3" fill="url(#bar26)"/>
      <text x="84" y="186" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">W36</text>
      <text x="97" y="55" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" text-anchor="middle">+12.4%</text>

      <!-- Bars: W37 -->
      <rect x="150" y="65" width="22" height="105" rx="3" fill="url(#bar25)"/>
      <rect x="176" y="40" width="22" height="130" rx="3" fill="url(#bar26)"/>
      <text x="174" y="186" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">W37</text>
      <text x="187" y="33" fill="#34D399" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" text-anchor="middle">+18.7%</text>

      <!-- Bars: W38 -->
      <rect x="240" y="74" width="22" height="96" rx="3" fill="url(#bar25)"/>
      <rect x="266" y="60" width="22" height="110" rx="3" fill="url(#bar26)"/>
      <text x="264" y="186" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">W38</text>
      <text x="277" y="53" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" text-anchor="middle">+9.5%</text>

      <!-- Bars: W39 -->
      <rect x="330" y="76" width="22" height="94" rx="3" fill="url(#bar25)"/>
      <rect x="356" y="52" width="22" height="118" rx="3" fill="url(#bar26)"/>
      <text x="354" y="186" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">W39</text>
      <text x="367" y="45" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" text-anchor="middle">+14.8%</text>

      <!-- Bars: W40 -->
      <rect x="420" y="68" width="22" height="102" rx="3" fill="url(#bar25)"/>
      <rect x="446" y="45" width="22" height="125" rx="3" fill="url(#bar26)"/>
      <text x="444" y="186" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" text-anchor="middle">W40</text>
      <text x="457" y="38" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="9" font-weight="bold" text-anchor="middle">+15.2%</text>

      <!-- Right: Automated Narrative Insight Box -->
      <g transform="translate(536, 0)">
        <rect width="416" height="210" rx="8" fill="#1E293B" stroke="#6366F1" stroke-width="1.2"/>
        <rect x="0" y="0" width="416" height="34" rx="8" fill="#312E81"/>
        <rect x="0" y="24" width="416" height="10" fill="#312E81"/>
        <text x="16" y="22" fill="#A5B4FC" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">
          ⚡ FORMULA-DRIVEN EXECUTIVE INSIGHT
        </text>

        <!-- Bullet 1 -->
        <circle cx="22" cy="56" r="4" fill="#38BDF8"/>
        <text x="36" y="55" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Week 37 Lonjakan Tertinggi (+18.7%)</text>
        <text x="36" y="70" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Kombinasi promo Payday mendongkrak UPT ke angka 2.34.</text>

        <!-- Bullet 2 -->
        <circle cx="22" cy="100" r="4" fill="#34D399"/>
        <text x="36" y="99" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Conversion Rate Solid (72.4%)</text>
        <text x="36" y="114" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Traffic ritel terkonversi optimal dengan kenaikan BagSize +4.0%.</text>

        <!-- Bullet 3 -->
        <circle cx="22" cy="144" r="4" fill="#F59E0B"/>
        <text x="36" y="143" fill="#F8FAFC" font-family="system-ui, sans-serif" font-size="11" font-weight="600">Formula Logika Otomatis</text>
        <text x="36" y="158" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">Dihasilkan otomatis via formula concatenation &amp; IF condition.</text>

        <!-- Formula tag snippet -->
        <rect x="16" y="174" width="384" height="24" rx="4" fill="#0F172A" stroke="#334155" stroke-width="1"/>
        <text x="24" y="190" fill="#FBBF24" font-family="'Consolas', monospace" font-size="9.5">
          =IF(C14&gt;0, "Pertumbuhan positif " &amp; TEXT(C14,"0.0%"), "Evaluasi")
        </text>
      </g>
    </g>
  </g>

  <!-- Sheet Tab Navigation at Bottom -->
  <rect y="586" width="1000" height="34" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <rect x="16" y="590" width="110" height="30" rx="4" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="71" y="609" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">DASHBOARD</text>
  <rect x="132" y="590" width="90" height="30" rx="4" fill="#1E293B"/>
  <text x="177" y="609" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">WEEKLY</text>
  <rect x="228" y="590" width="120" height="30" rx="4" fill="#1E293B"/>
  <text x="288" y="609" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11" text-anchor="middle">DATA MENTAH</text>
</svg>"""
    
    with open(os.path.join(output_dir, "edp-dashboard-main.svg"), "w", encoding="utf-8") as f:
        f.write(svg1)
        
    # 2. EDP Formula Weekly
    svg2 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <!-- Frame -->
  <rect width="1000" height="620" rx="14" fill="url(#bg2)" stroke="#334155" stroke-width="1.5"/>
  
  <!-- Window Header -->
  <rect width="1000" height="42" rx="14" fill="#090D16"/>
  <rect y="28" width="1000" height="14" fill="#090D16"/>
  <circle cx="24" cy="21" r="5" fill="#EF4444"/>
  <circle cx="42" cy="21" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="21" r="5" fill="#10B981"/>
  <text x="500" y="26" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Sheet: WEEKLY - Formula Bar Focus &amp; Dynamic SUMIFS (Zoom 130%)
  </text>

  <!-- FORMULA BAR FOCUS (HIGHLIGHTED) -->
  <rect y="42" width="1000" height="48" fill="#1E293B" stroke="#0EA5E9" stroke-width="1.5"/>
  <rect x="16" y="52" width="56" height="28" rx="4" fill="#0369A1"/>
  <text x="44" y="70" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">D4</text>
  <text x="88" y="71" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">fx</text>
  
  <rect x="110" y="50" width="874" height="32" rx="5" fill="#020617" stroke="#38BDF8" stroke-width="1.2"/>
  <text x="124" y="71" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="13" font-weight="600">
    =SUMIFS('DATA MENTAH'!$D:$D, 'DATA MENTAH'!$U:$U, 2026, 'DATA MENTAH'!$W:$W, $A4)
  </text>

  <!-- Table headers -->
  <g transform="translate(24, 106)">
    <!-- Column Letters -->
    <rect width="952" height="24" fill="#334155"/>
    <text x="40" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">A</text>
    <text x="110" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">B</text>
    <text x="210" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">C</text>
    <text x="340" y="16" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">D [ACTIVE CELL]</text>
    <text x="470" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">E</text>
    <text x="560" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">F</text>
    <text x="660" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">G (UPT)</text>
    <text x="790" y="16" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">H (BAG SIZE)</text>

    <!-- Table Header Row -->
    <g transform="translate(0, 24)">
      <rect width="952" height="34" fill="#0D9488"/>
      <text x="20" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">WEEK_ISO</text>
      <text x="96" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">YEAR</text>
      <text x="180" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">SALES 2025</text>
      <text x="310" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">SALES 2026 (SUMIFS)</text>
      <text x="460" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">YoY %</text>
      <text x="540" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">TRX</text>
      <text x="640" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">UPT (=QTY/TRX)</text>
      <text x="770" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">BAG SIZE (=SALES/TRX)</text>
    </g>

    <!-- Rows -->
    <!-- Row 4 (WEEK 36) - Active / Selected -->
    <g transform="translate(0, 58)">
      <rect width="952" height="42" fill="#1E293B" stroke="#334155" stroke-width="0.5"/>
      <rect x="290" y="0" width="160" height="42" fill="#0284C7" fill-opacity="0.2" stroke="#38BDF8" stroke-width="2"/>
      <text x="30" y="26" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="12" font-weight="bold">36</text>
      <text x="100" y="26" fill="#94A3B8" font-family="'Consolas', monospace" font-size="12">2026</text>
      <text x="180" y="26" fill="#94A3B8" font-family="'Consolas', monospace" font-size="12">354,890,000</text>
      <text x="310" y="26" fill="#38BDF8" font-family="'Consolas', monospace" font-size="13" font-weight="bold">398,900,000</text>
      <text x="460" y="26" fill="#34D399" font-family="'Consolas', monospace" font-size="12" font-weight="bold">+12.4%</text>
      <text x="546" y="26" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="12">1,438</text>
      <text x="660" y="26" fill="#FBBF24" font-family="'Consolas', monospace" font-size="12" font-weight="bold">2.27 pcs</text>
      <text x="780" y="26" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="12">Rp 277,399</text>
    </g>

    <!-- Row 5 (WEEK 37) -->
    <g transform="translate(0, 100)">
      <rect width="952" height="42" fill="#0F172A" stroke="#334155" stroke-width="0.5"/>
      <text x="30" y="26" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="12" font-weight="bold">37</text>
      <text x="100" y="26" fill="#94A3B8" font-family="'Consolas', monospace" font-size="12">2026</text>
      <text x="180" y="26" fill="#94A3B8" font-family="'Consolas', monospace" font-size="12">412,500,000</text>
      <text x="310" y="26" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="12">489,600,000</text>
      <text x="460" y="26" fill="#34D399" font-family="'Consolas', monospace" font-size="12" font-weight="bold">+18.7%</text>
      <text x="546" y="26" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="12">1,698</text>
      <text x="660" y="26" fill="#FBBF24" font-family="'Consolas', monospace" font-size="12" font-weight="bold">2.34 pcs</text>
      <text x="780" y="26" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="12">Rp 288,339</text>
    </g>

    <!-- Row 6 (WEEK 38) -->
    <g transform="translate(0, 142)">
      <rect width="952" height="42" fill="#1E293B" stroke="#334155" stroke-width="0.5"/>
      <text x="30" y="26" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="12" font-weight="bold">38</text>
      <text x="100" y="26" fill="#94A3B8" font-family="'Consolas', monospace" font-size="12">2026</text>
      <text x="180" y="26" fill="#94A3B8" font-family="'Consolas', monospace" font-size="12">389,400,000</text>
      <text x="310" y="26" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="12">426,400,000</text>
      <text x="460" y="26" fill="#34D399" font-family="'Consolas', monospace" font-size="12" font-weight="bold">+9.5%</text>
      <text x="546" y="26" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="12">1,508</text>
      <text x="660" y="26" fill="#FBBF24" font-family="'Consolas', monospace" font-size="12" font-weight="bold">2.30 pcs</text>
      <text x="780" y="26" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="12">Rp 282,758</text>
    </g>

    <!-- Annotation Callouts -->
    <g transform="translate(100, 220)">
      <rect width="750" height="110" rx="8" fill="#1E1B4B" stroke="#818CF8" stroke-width="1.5"/>
      <text x="24" y="32" fill="#A5B4FC" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">
        📌 DUA LOGIKA FORMULA UTAMA DI SHEET INI:
      </text>
      <text x="24" y="60" fill="#E0E7FF" font-family="'Consolas', monospace" font-size="11.5">
        1. Dynamic Aggregate: =SUMIFS('DATA MENTAH'!$D:$D, 'DATA MENTAH'!$U:$U, $C$2, 'DATA MENTAH'!$W:$W, $A4)
      </text>
      <text x="24" y="85" fill="#E0E7FF" font-family="'Consolas', monospace" font-size="11.5">
        2. Basket Size &amp; UPT: =ROUND(Total_QTY / TRX, 2)  |  BagSize: =ROUND(Total_SALES / TRX, 0)
      </text>
    </g>
  </g>
</svg>"""
    
    with open(os.path.join(output_dir, "edp-formula-weekly.svg"), "w", encoding="utf-8") as f:
        f.write(svg2)

    # 3. EDP Raw Data
    svg3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="620" rx="14" fill="url(#bg3)" stroke="#334155" stroke-width="1.5"/>
  <rect width="1000" height="42" rx="14" fill="#090D16"/>
  <rect y="28" width="1000" height="14" fill="#090D16"/>
  <circle cx="24" cy="21" r="5" fill="#EF4444"/>
  <circle cx="42" cy="21" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="21" r="5" fill="#10B981"/>
  <text x="500" y="26" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Sheet: DATA MENTAH - Struktur Transaksi &amp; Validasi Selisih Divisi (SELISIH +/- = 0)
  </text>

  <!-- Formula Bar -->
  <rect y="42" width="1000" height="42" fill="#1E293B" stroke="#334155" stroke-width="1"/>
  <rect x="16" y="50" width="50" height="24" rx="4" fill="#334155"/>
  <text x="41" y="66" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">T2</text>
  <text x="80" y="66" fill="#64748B" font-family="system-ui, sans-serif" font-size="13">fx</text>
  <rect x="100" y="50" width="884" height="24" rx="4" fill="#0F172A" stroke="#334155" stroke-width="1"/>
  <text x="114" y="66" fill="#10B981" font-family="'Consolas', monospace" font-size="11.5">
    =ROUND(Total_SALES - (Sales_Div_1 + Sales_Div_2 + Sales_Div_3 + Sales_Div_4), 2)  [HASIL: 0 / BALANCED]
  </text>

  <g transform="translate(24, 100)">
    <!-- Column Headers -->
    <rect width="952" height="34" fill="#334155"/>
    <text x="16" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">DATE</text>
    <text x="110" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">STORE LOCATION</text>
    <text x="270" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">TOTAL SALES</text>
    <text x="380" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">QTY</text>
    <text x="440" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">TRX</text>
    <text x="500" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">DIV 1 - 4 (SUM)</text>
    <text x="650" y="22" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">SELISIH (+/-)</text>
    <text x="770" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">ISOWEEKNUM</text>
    <text x="880" y="22" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">YEAR</text>

    <!-- Row 1 -->
    <g transform="translate(0, 34)">
      <rect width="952" height="38" fill="#1E293B" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">2026-09-01</text>
      <text x="110" y="24" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">999 - STORE NUSANTARA</text>
      <text x="270" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">61,858,000</text>
      <text x="380" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">526</text>
      <text x="440" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">188</text>
      <text x="500" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">61,858,000</text>
      <rect x="646" y="8" width="68" height="22" rx="4" fill="#065F46"/>
      <text x="680" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0 (OK)</text>
      <text x="800" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">36</text>
      <text x="886" y="24" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">2026</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(0, 72)">
      <rect width="952" height="38" fill="#0F172A" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">2026-09-02</text>
      <text x="110" y="24" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">999 - STORE NUSANTARA</text>
      <text x="270" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">46,846,000</text>
      <text x="380" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">370</text>
      <text x="440" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">148</text>
      <text x="500" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">46,846,000</text>
      <rect x="646" y="8" width="68" height="22" rx="4" fill="#065F46"/>
      <text x="680" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0 (OK)</text>
      <text x="800" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">36</text>
      <text x="886" y="24" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">2026</text>
    </g>

    <!-- Row 3 -->
    <g transform="translate(0, 110)">
      <rect width="952" height="38" fill="#1E293B" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">2026-09-03</text>
      <text x="110" y="24" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">999 - STORE NUSANTARA</text>
      <text x="270" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">46,200,000</text>
      <text x="380" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">361</text>
      <text x="440" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">154</text>
      <text x="500" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">46,200,000</text>
      <rect x="646" y="8" width="68" height="22" rx="4" fill="#065F46"/>
      <text x="680" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0 (OK)</text>
      <text x="800" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">36</text>
      <text x="886" y="24" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">2026</text>
    </g>

    <!-- Row 4 -->
    <g transform="translate(0, 148)">
      <rect width="952" height="38" fill="#0F172A" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">2026-09-04</text>
      <text x="110" y="24" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">999 - STORE NUSANTARA</text>
      <text x="270" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">101,723,000</text>
      <text x="380" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">820</text>
      <text x="440" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">379</text>
      <text x="500" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">101,723,000</text>
      <rect x="646" y="8" width="68" height="22" rx="4" fill="#065F46"/>
      <text x="680" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0 (OK)</text>
      <text x="800" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">36</text>
      <text x="886" y="24" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">2026</text>
    </g>

    <!-- Explanation Box -->
    <g transform="translate(0, 210)">
      <rect width="952" height="90" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <text x="20" y="26" fill="#34D399" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">
        ✓ ZERO-ERROR VALIDATION INTEGRITY
      </text>
      <text x="20" y="48" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">
        • Kolom SELISIH (+/-) menjamin total omzet toko selalu persis sama dengan penjumlahan divisi 1 hingga 4.
      </text>
      <text x="20" y="68" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">
        • Kolom ISOWEEKNUM mengekstrak pekan standar internasional secara otomatis dari kolom DATE transaksi harian.
      </text>
    </g>
  </g>
</svg>"""

    with open(os.path.join(output_dir, "edp-raw-data.svg"), "w", encoding="utf-8") as f:
        f.write(svg3)

    # 4. SNT Target Weekly (Main Cover for Project 2)
    svg4 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E1B4B"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="620" rx="14" fill="url(#bg4)" stroke="#4338CA" stroke-width="1.5"/>
  <rect width="1000" height="42" rx="14" fill="#090D16"/>
  <rect y="28" width="1000" height="14" fill="#090D16"/>
  <circle cx="24" cy="21" r="5" fill="#EF4444"/>
  <circle cx="42" cy="21" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="21" r="5" fill="#10B981"/>
  <text x="500" y="26" fill="#A5B4FC" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Microsoft Excel - SNT_Omnichannel_Reconciliation.xlsx [Sheet: TARGET SNT OKTOBER (Zoom 125%)]
  </text>

  <!-- Formula Bar -->
  <rect y="42" width="1000" height="42" fill="#1E1B4B" stroke="#4338CA" stroke-width="1"/>
  <rect x="16" y="50" width="50" height="24" rx="4" fill="#3730A3"/>
  <text x="41" y="66" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Q9</text>
  <text x="80" y="66" fill="#818CF8" font-family="system-ui, sans-serif" font-size="13">fx</text>
  <rect x="100" y="50" width="884" height="24" rx="4" fill="#0F172A" stroke="#4338CA" stroke-width="1"/>
  <text x="114" y="66" fill="#A5B4FC" font-family="'Consolas', monospace" font-size="11.5">
    =SUM(P4:P8)  [TOTAL ACTUAL SALES NET 1.11 = Rp 64,402,000 | ACHIEVEMENT: 108.06%]
  </text>

  <g transform="translate(24, 96)">
    <!-- Header Summary Banner -->
    <rect width="952" height="54" rx="8" fill="#312E81" stroke="#6366F1" stroke-width="1"/>
    <text x="20" y="26" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="15" font-weight="bold">
      REKAPITULASI PENJUALAN SIKLUS MINGGUAN (MINGGU - SABTU)
    </text>
    <text x="20" y="43" fill="#C7D2FE" font-family="system-ui, sans-serif" font-size="11">
      Admin S&amp;T Omnichannel | Target: Rp 59,600,000 | Actual Net: Rp 64,402,000 (108.1%)
    </text>
    <rect x="790" y="14" width="146" height="26" rx="6" fill="#10B981" fill-opacity="0.25" stroke="#34D399" stroke-width="1"/>
    <text x="863" y="31" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" text-anchor="middle">
      ✓ TARGET TERCAPAI
    </text>

    <!-- Table of Weeks -->
    <g transform="translate(0, 68)">
      <rect width="952" height="32" fill="#4338CA"/>
      <text x="16" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">PERIODE MINGGU (MINGGU - SABTU)</text>
      <text x="270" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">TARGET TRX</text>
      <text x="360" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">ACT TRX</text>
      <text x="430" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">ACH TRX</text>
      <text x="510" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">TARGET SALES</text>
      <text x="640" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">ACTUAL SALES (NET 1.11)</text>
      <text x="820" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">ACH SALES</text>
      <text x="910" y="21" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">UPT</text>

      <!-- Week 1 -->
      <g transform="translate(0, 32)">
        <rect width="952" height="34" fill="#1E1B4B" stroke="#312E81" stroke-width="0.5"/>
        <text x="16" y="22" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="11">Week 1 (01 - 03 Okt | Parsial)</text>
        <text x="280" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">39</text>
        <text x="370" y="22" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">43</text>
        <text x="434" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">110.3%</text>
        <text x="510" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">Rp 6,000,000</text>
        <text x="640" y="22" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 6,842,000</text>
        <text x="824" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">114.0%</text>
        <text x="914" y="22" fill="#FBBF24" font-family="'Consolas', monospace" font-size="11">1.35</text>
      </g>

      <!-- Week 2 -->
      <g transform="translate(0, 66)">
        <rect width="952" height="34" fill="#0F172A" stroke="#312E81" stroke-width="0.5"/>
        <text x="16" y="22" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="11">Week 2 (04 - 10 Okt | Min - Sab)</text>
        <text x="280" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">88</text>
        <text x="370" y="22" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">94</text>
        <text x="434" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">106.8%</text>
        <text x="510" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">Rp 13,400,000</text>
        <text x="640" y="22" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 14,210,000</text>
        <text x="824" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">106.0%</text>
        <text x="914" y="22" fill="#FBBF24" font-family="'Consolas', monospace" font-size="11">1.34</text>
      </g>

      <!-- Week 3 -->
      <g transform="translate(0, 100)">
        <rect width="952" height="34" fill="#1E1B4B" stroke="#312E81" stroke-width="0.5"/>
        <text x="16" y="22" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="11">Week 3 (11 - 17 Okt | Min - Sab)</text>
        <text x="280" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">88</text>
        <text x="370" y="22" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">91</text>
        <text x="434" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">103.4%</text>
        <text x="510" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">Rp 13,400,000</text>
        <text x="640" y="22" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 13,890,000</text>
        <text x="824" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">103.7%</text>
        <text x="914" y="22" fill="#FBBF24" font-family="'Consolas', monospace" font-size="11">1.31</text>
      </g>

      <!-- Week 4 -->
      <g transform="translate(0, 134)">
        <rect width="952" height="34" fill="#0F172A" stroke="#312E81" stroke-width="0.5"/>
        <text x="16" y="22" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="11">Week 4 (18 - 24 Okt | Min - Sab)</text>
        <text x="280" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">88</text>
        <text x="370" y="22" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">96</text>
        <text x="434" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">109.1%</text>
        <text x="510" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">Rp 13,400,000</text>
        <text x="640" y="22" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 14,850,000</text>
        <text x="824" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">110.8%</text>
        <text x="914" y="22" fill="#FBBF24" font-family="'Consolas', monospace" font-size="11">1.36</text>
      </g>

      <!-- Week 5 -->
      <g transform="translate(0, 168)">
        <rect width="952" height="34" fill="#1E1B4B" stroke="#312E81" stroke-width="0.5"/>
        <text x="16" y="22" fill="#E0E7FF" font-family="system-ui, sans-serif" font-size="11">Week 5 (25 - 31 Okt | Min - Sab)</text>
        <text x="280" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">88</text>
        <text x="370" y="22" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">95</text>
        <text x="434" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">108.0%</text>
        <text x="510" y="22" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">Rp 13,400,000</text>
        <text x="640" y="22" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 14,610,000</text>
        <text x="824" y="22" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">109.0%</text>
        <text x="914" y="22" fill="#FBBF24" font-family="'Consolas', monospace" font-size="11">1.35</text>
      </g>

      <!-- Total Row (Highlighted) -->
      <g transform="translate(0, 202)">
        <rect width="952" height="38" fill="#312E81" stroke="#818CF8" stroke-width="1.5"/>
        <text x="16" y="24" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11.5" font-weight="bold">TOTAL MINGGUAN (= BULANAN)</text>
        <text x="280" y="24" fill="#C7D2FE" font-family="'Consolas', monospace" font-size="12" font-weight="bold">391</text>
        <text x="370" y="24" fill="#FFFFFF" font-family="'Consolas', monospace" font-size="12" font-weight="bold">419</text>
        <text x="434" y="24" fill="#34D399" font-family="'Consolas', monospace" font-size="12" font-weight="bold">107.2%</text>
        <text x="510" y="24" fill="#C7D2FE" font-family="'Consolas', monospace" font-size="12" font-weight="bold">Rp 59,600,000</text>
        <text x="640" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="13" font-weight="bold">Rp 64,402,000</text>
        <text x="824" y="24" fill="#34D399" font-family="'Consolas', monospace" font-size="12" font-weight="bold">108.1%</text>
        <text x="914" y="24" fill="#FBBF24" font-family="'Consolas', monospace" font-size="12" font-weight="bold">1.34</text>
      </g>
    </g>

    <!-- Mini Progress Bars Visualisation -->
    <g transform="translate(0, 318)">
      <rect width="952" height="74" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <text x="20" y="24" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">
        Pencapaian Target Bulanan (108.1%)
      </text>
      <rect x="20" y="34" width="912" height="16" rx="8" fill="#0F172A"/>
      <rect x="20" y="34" width="912" height="16" rx="8" fill="#10B981"/>
      <text x="20" y="62" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10">
        Rp 0
      </text>
      <text x="932" y="62" fill="#34D399" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" text-anchor="end">
        Surplus: +Rp 4,802,000 (Over Target)
      </text>
    </g>
  </g>
</svg>"""

    with open(os.path.join(output_dir, "snt-target-weekly.svg"), "w", encoding="utf-8") as f:
        f.write(svg4)

    # 5. SNT Input Nota & Validation
    svg5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bg5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="620" rx="14" fill="url(#bg5)" stroke="#334155" stroke-width="1.5"/>
  <rect width="1000" height="42" rx="14" fill="#090D16"/>
  <rect y="28" width="1000" height="14" fill="#090D16"/>
  <circle cx="24" cy="21" r="5" fill="#EF4444"/>
  <circle cx="42" cy="21" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="21" r="5" fill="#10B981"/>
  <text x="500" y="26" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Sheet: 04 OKTOBER - Input Nota Omnichannel &amp; Validasi Keseimbangan [CEK HARUS 0]
  </text>

  <!-- Formula Bar Focus -->
  <rect y="42" width="1000" height="46" fill="#1E293B" stroke="#10B981" stroke-width="1.5"/>
  <rect x="16" y="52" width="56" height="26" rx="4" fill="#065F46"/>
  <text x="44" y="69" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" text-anchor="middle">H2</text>
  <text x="88" y="70" fill="#34D399" font-family="system-ui, sans-serif" font-size="14" font-weight="bold">fx</text>
  <rect x="108" y="50" width="876" height="30" rx="4" fill="#020617" stroke="#34D399" stroke-width="1.2"/>
  <text x="122" y="70" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="12.5">
    =ROUND(F2 - (J2 + N2), 2)  [CEK KESEIMBANGAN: NILAI HARUS 0]  |  NET 1.11: =ROUND(K2 / 1.11, 0)
  </text>

  <g transform="translate(24, 102)">
    <rect width="952" height="34" fill="#334155"/>
    <text x="16" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">CHANNEL</text>
    <text x="90" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">NO STRUK</text>
    <text x="180" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">TOTAL STRUK</text>
    <text x="280" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">METODE</text>
    <text x="350" y="22" fill="#34D399" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">CEK (HARUS 0)</text>
    <text x="470" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">NET DP</text>
    <text x="560" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">NET DP (1.11)</text>
    <text x="670" y="22" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">NET CV</text>
    <text x="760" y="22" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">NET CV (1.11)</text>
    <text x="870" y="22" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold">SALES</text>

    <!-- Row 1 -->
    <g transform="translate(0, 34)">
      <rect width="952" height="38" fill="#1E293B" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#38BDF8" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">HAPTIK</text>
      <text x="90" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">310001</text>
      <text x="180" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 149,500</text>
      <text x="280" y="24" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">QRIS</text>
      <rect x="350" y="8" width="60" height="22" rx="4" fill="#065F46"/>
      <text x="380" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0</text>
      <text x="470" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">149,500</text>
      <text x="560" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">134,685</text>
      <text x="670" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="760" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="870" y="24" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">INTAN</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(0, 72)">
      <rect width="952" height="38" fill="#0F172A" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#A855F7" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">TIKTOK</text>
      <text x="90" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">310003</text>
      <text x="180" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 89,500</text>
      <text x="280" y="24" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">QRIS</text>
      <rect x="350" y="8" width="60" height="22" rx="4" fill="#065F46"/>
      <text x="380" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0</text>
      <text x="470" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="560" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="670" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">89,500</text>
      <text x="760" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">80,631</text>
      <text x="870" y="24" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">SITI</text>
    </g>

    <!-- Row 3 -->
    <g transform="translate(0, 110)">
      <rect width="952" height="38" fill="#1E293B" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#22C55E" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">WHATSAPP</text>
      <text x="90" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">310004</text>
      <text x="180" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 89,500</text>
      <text x="280" y="24" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">VA BCA</text>
      <rect x="350" y="8" width="60" height="22" rx="4" fill="#065F46"/>
      <text x="380" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0</text>
      <text x="470" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">89,500</text>
      <text x="560" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">80,631</text>
      <text x="670" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="760" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="870" y="24" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">DIMAS</text>
    </g>

    <!-- Row 4 -->
    <g transform="translate(0, 148)">
      <rect width="952" height="38" fill="#0F172A" stroke="#334155" stroke-width="0.5"/>
      <text x="16" y="24" fill="#22C55E" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">WHATSAPP</text>
      <text x="90" y="24" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">310006</text>
      <text x="180" y="24" fill="#F8FAFC" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 299,000</text>
      <text x="280" y="24" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">QRIS</text>
      <rect x="350" y="8" width="60" height="22" rx="4" fill="#065F46"/>
      <text x="380" y="23" fill="#6EE7B7" font-family="'Consolas', monospace" font-size="11" font-weight="bold" text-anchor="middle">0</text>
      <text x="470" y="24" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">299,000</text>
      <text x="560" y="24" fill="#38BDF8" font-family="'Consolas', monospace" font-size="11" font-weight="bold">269,369</text>
      <text x="670" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="760" y="24" fill="#64748B" font-family="'Consolas', monospace" font-size="11">-</text>
      <text x="870" y="24" fill="#E2E8F0" font-family="system-ui, sans-serif" font-size="10">FAJAR</text>
    </g>

    <!-- Annotation Callouts -->
    <g transform="translate(0, 210)">
      <rect width="952" height="96" rx="8" fill="#14532D" stroke="#22C55E" stroke-width="1.2"/>
      <text x="20" y="28" fill="#86EFAC" font-family="system-ui, sans-serif" font-size="13" font-weight="bold">
        🛡️ VALIDASI MUTLAK: CEK HARUS 0 &amp; DPP 1.11
      </text>
      <text x="20" y="52" fill="#DCFCE7" font-family="system-ui, sans-serif" font-size="11">
        • Setiap nota dicek silang: Total Struk = (Gross DP + Gross CV). Jika selisih != 0, baris otomatis merah (Conditional Formatting).
      </text>
      <text x="20" y="74" fill="#DCFCE7" font-family="system-ui, sans-serif" font-size="11">
        • Kolom Net (1.11) secara otomatis mengeliminasi komponen PPN 11% sehingga omzet yang diakui murni merupakan Dasar Pengenaan Pajak (DPP).
      </text>
    </g>
  </g>
</svg>"""

    with open(os.path.join(output_dir, "snt-input-nota.svg"), "w", encoding="utf-8") as f:
        f.write(svg5)

    # 6. SNT Audit & Leaderboard
    svg6 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bg6" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>

  <rect width="1000" height="620" rx="14" fill="url(#bg6)" stroke="#334155" stroke-width="1.5"/>
  <rect width="1000" height="42" rx="14" fill="#090D16"/>
  <rect y="28" width="1000" height="14" fill="#090D16"/>
  <circle cx="24" cy="21" r="5" fill="#EF4444"/>
  <circle cx="42" cy="21" r="5" fill="#F59E0B"/>
  <circle cx="60" cy="21" r="5" fill="#10B981"/>
  <text x="500" y="26" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">
    Sheet: SELISIH OKTOBER &amp; LEADERBOARD - Log Rekonsiliasi Bank + Rangking Performa Sales
  </text>

  <g transform="translate(24, 60)">
    <!-- LEFT: Audit Rekonsiliasi Mutasi Bank -->
    <g transform="translate(0, 0)">
      <rect width="470" height="340" rx="8" fill="#1E293B" stroke="#EF4444" stroke-width="1"/>
      <rect width="470" height="36" rx="8" fill="#991B1B"/>
      <text x="16" y="23" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">
        LOG REKONSILIASI HARIAN (31 HARI)
      </text>

      <!-- Subheaders -->
      <g transform="translate(16, 48)">
        <text x="0" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">TGL</text>
        <text x="70" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">SELISIH</text>
        <text x="150" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">STATUS &amp; ALASAN AUDIT</text>
      </g>

      <!-- Log 04 Okt (Kelebihan) -->
      <g transform="translate(16, 74)">
        <rect width="438" height="50" rx="6" fill="#78350F" fill-opacity="0.25" stroke="#F59E0B" stroke-width="1"/>
        <text x="10" y="22" fill="#FCD34D" font-family="'Consolas', monospace" font-size="11" font-weight="bold">04/10</text>
        <text x="70" y="22" fill="#FCD34D" font-family="'Consolas', monospace" font-size="11" font-weight="bold">+Rp 150.000</text>
        <text x="160" y="20" fill="#FEF3C7" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">SELISIH (+): Transfer Masuk POS Pending</text>
        <text x="160" y="36" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="9">Uang masuk mutasi, menunggu konfirmasi stok barang.</text>
      </g>

      <!-- Log 12 Okt (Retur Kurang) -->
      <g transform="translate(16, 134)">
        <rect width="438" height="50" rx="6" fill="#7F1D1D" fill-opacity="0.25" stroke="#EF4444" stroke-width="1"/>
        <text x="10" y="22" fill="#FCA5A5" font-family="'Consolas', monospace" font-size="11" font-weight="bold">12/10</text>
        <text x="70" y="22" fill="#FCA5A5" font-family="'Consolas', monospace" font-size="11" font-weight="bold">-Rp 49.900</text>
        <text x="160" y="20" fill="#FEE2E2" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">SELISIH (-): Retur / Tukar Size</text>
        <text x="160" y="36" fill="#FECACA" font-family="system-ui, sans-serif" font-size="9">Selisih kurang bayar dari penyesuaian struk retur.</text>
      </g>

      <!-- Log 21 Okt (Deposit) -->
      <g transform="translate(16, 194)">
        <rect width="438" height="50" rx="6" fill="#78350F" fill-opacity="0.25" stroke="#F59E0B" stroke-width="1"/>
        <text x="10" y="22" fill="#FCD34D" font-family="'Consolas', monospace" font-size="11" font-weight="bold">21/10</text>
        <text x="70" y="22" fill="#FCD34D" font-family="'Consolas', monospace" font-size="11" font-weight="bold">+Rp 85.000</text>
        <text x="160" y="20" fill="#FEF3C7" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">SELISIH (+): Kelebihan Bayar Pelanggan</text>
        <text x="160" y="36" fill="#FDE68A" font-family="system-ui, sans-serif" font-size="9">Dicatat sebagai saldo deposit untuk transaksi berikutnya.</text>
      </g>

      <!-- Remaining 28 Days Balanced -->
      <g transform="translate(16, 256)">
        <rect width="438" height="38" rx="6" fill="#065F46" fill-opacity="0.25" stroke="#10B981" stroke-width="1"/>
        <text x="14" y="24" fill="#34D399" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">
          ✓ 28 HARI LAINNYA: MATCH PERSIS (Selisih = Rp 0)
        </text>
      </g>
    </g>

    <!-- RIGHT: Leaderboard Sales Person via INDEX/MATCH -->
    <g transform="translate(486, 0)">
      <rect width="466" height="340" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1"/>
      <rect width="466" height="36" rx="8" fill="#065F46"/>
      <text x="16" y="23" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">
        LEADERBOARD SALES PERSON (INDEX/MATCH)
      </text>

      <!-- Rank Headers -->
      <g transform="translate(16, 48)">
        <text x="0" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">RK</text>
        <text x="36" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">NAMA SALES</text>
        <text x="190" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">DIVISI</text>
        <text x="260" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">TRX</text>
        <text x="320" y="14" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">TOTAL OMZET</text>
      </g>

      <!-- Rank 1 -->
      <g transform="translate(16, 72)">
        <rect width="434" height="30" rx="4" fill="#FBBF24" fill-opacity="0.15" stroke="#F59E0B" stroke-width="0.8"/>
        <text x="10" y="19" fill="#FBBF24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">🥇 1</text>
        <text x="40" y="19" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">RINA KUSUMAWATI</text>
        <text x="190" y="19" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">DIV 1</text>
        <text x="266" y="19" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">52</text>
        <text x="320" y="19" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 9,840,000</text>
      </g>

      <!-- Rank 2 -->
      <g transform="translate(16, 108)">
        <rect width="434" height="30" rx="4" fill="#94A3B8" fill-opacity="0.1" stroke="#64748B" stroke-width="0.5"/>
        <text x="10" y="19" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">🥈 2</text>
        <text x="40" y="19" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">DIMAS PRASETYO</text>
        <text x="190" y="19" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">DIV 1</text>
        <text x="266" y="19" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">48</text>
        <text x="320" y="19" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 8,910,000</text>
      </g>

      <!-- Rank 3 -->
      <g transform="translate(16, 144)">
        <rect width="434" height="30" rx="4" fill="#B45309" fill-opacity="0.1" stroke="#B45309" stroke-width="0.5"/>
        <text x="10" y="19" fill="#F59E0B" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">🥉 3</text>
        <text x="40" y="19" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="11" font-weight="bold">SITI NURHALIZA</text>
        <text x="190" y="19" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="10.5">DIV 2</text>
        <text x="266" y="19" fill="#CBD5E1" font-family="'Consolas', monospace" font-size="11">46</text>
        <text x="320" y="19" fill="#34D399" font-family="'Consolas', monospace" font-size="11" font-weight="bold">Rp 8,420,000</text>
      </g>

      <!-- Rank 4 -->
      <g transform="translate(16, 180)">
        <text x="16" y="19" fill="#64748B" font-family="system-ui, sans-serif" font-size="11">4</text>
        <text x="40" y="19" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">BAGUS WICAKSONO</text>
        <text x="190" y="19" fill="#64748B" font-family="system-ui, sans-serif" font-size="10.5">DIV 2</text>
        <text x="266" y="19" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">43</text>
        <text x="320" y="19" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">Rp 7,650,000</text>
      </g>

      <!-- Rank 5 -->
      <g transform="translate(16, 212)">
        <text x="16" y="19" fill="#64748B" font-family="system-ui, sans-serif" font-size="11">5</text>
        <text x="40" y="19" fill="#CBD5E1" font-family="system-ui, sans-serif" font-size="11">DEWI ANGGRAINI</text>
        <text x="190" y="19" fill="#64748B" font-family="system-ui, sans-serif" font-size="10.5">DIV 3</text>
        <text x="266" y="19" fill="#94A3B8" font-family="'Consolas', monospace" font-size="11">42</text>
        <text x="320" y="19" fill="#E2E8F0" font-family="'Consolas', monospace" font-size="11">Rp 7,520,000</text>
      </g>

      <!-- Formula syntax callout -->
      <g transform="translate(16, 250)">
        <rect width="434" height="66" rx="6" fill="#022C22" stroke="#059669" stroke-width="1"/>
        <text x="12" y="22" fill="#6EE7B7" font-family="system-ui, sans-serif" font-size="10" font-weight="bold">
          ⚡ AUTO-LOOKUP VIA FORMULA INDEX/MATCH:
        </text>
        <text x="12" y="44" fill="#A7F3D0" font-family="'Consolas', monospace" font-size="10">
          =INDEX('DATA SALES'!$B:$B, MATCH(A2, 'DATA SALES'!$A:$A, 0))
        </text>
      </g>
    </g>

    <!-- Bottom summary tag -->
    <g transform="translate(0, 360)">
      <rect width="952" height="74" rx="8" fill="#1E293B" stroke="#334155" stroke-width="1"/>
      <text x="20" y="28" fill="#FFFFFF" font-family="system-ui, sans-serif" font-size="12" font-weight="bold">
        REKONSILIASI KEUANGAN &amp; AKUNTABILITAS TINGKAT TINGGI
      </text>
      <text x="20" y="50" fill="#94A3B8" font-family="system-ui, sans-serif" font-size="11">
        Setiap rupiah selisih diidentifikasi secara transparan dengan kategori audit jelas (deposit/retur/pending), sementara komisi dan omzet tim sales terhitung otomatis tanpa manipulasi data.
      </text>
    </g>
  </g>
</svg>"""

    with open(os.path.join(output_dir, "snt-audit-leaderboard.svg"), "w", encoding="utf-8") as f:
        f.write(svg6)

    print("All 6 SVGs generated successfully in:", output_dir)

if __name__ == "__main__":
    generate_svgs()
