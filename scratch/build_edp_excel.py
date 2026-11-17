import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_edp_workbook():
    wb = openpyxl.Workbook()
    
    # 1. Sheet DASHBOARD
    ws_dash = wb.active
    ws_dash.title = "DASHBOARD"
    ws_dash.views.sheetView[0].showGridLines = True
    
    # Header Styling
    header_fill = PatternFill(start_color="1E40AF", end_color="1E40AF", fill_type="solid") # Dark Blue
    accent_fill = PatternFill(start_color="3B82F6", end_color="3B82F6", fill_type="solid")
    kpi_fill = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
    border_thin = Border(left=Side(style='thin', color='CBD5E1'),
                         right=Side(style='thin', color='CBD5E1'),
                         top=Side(style='thin', color='CBD5E1'),
                         bottom=Side(style='thin', color='CBD5E1'))
    
    ws_dash["A1"] = "EXECUTIVE WEEKLY RETAIL DASHBOARD (PORTFOLIO EDP)"
    ws_dash["A1"].font = Font(size=16, bold=True, color="1E3A8A")
    ws_dash["A2"] = "Periode Bulan: September | Tahun Pembanding: 2025 vs 2026"
    ws_dash["A2"].font = Font(size=11, italic=True, color="475569")
    
    # 6 KPI Cards
    kpis = [
        ("Total Sales 2025", "Rp 1.942.500.000", "B4:C4", "B5:C5"),
        ("Total Sales 2026", "Rp 2.215.800.000", "D4:E4", "D5:E5"),
        ("YoY Sales Growth", "+14.07%", "F4:G4", "F5:G5"),
        ("Avg CRR 2026", "72.4%", "H4:I4", "H5:I5"),
        ("Avg UPT 2026", "2.18", "J4:K4", "J5:K5"),
        ("Avg BagSize 2026", "Rp 324.500", "L4:M4", "L5:M4")
    ]
    
    for title, val, rng1, rng2 in kpis:
        top_cell = rng1.split(":")[0]
        val_cell = rng2.split(":")[0]
        ws_dash[top_cell] = title
        ws_dash[top_cell].font = Font(size=9, color="64748B", bold=True)
        ws_dash[top_cell].alignment = Alignment(horizontal="center")
        ws_dash[val_cell] = val
        ws_dash[val_cell].font = Font(size=13, color="1E293B", bold=True)
        ws_dash[val_cell].alignment = Alignment(horizontal="center")
        ws_dash[top_cell].fill = kpi_fill
        ws_dash[val_cell].fill = kpi_fill
    
    # Weekly Comparison Table
    ws_dash["A8"] = "WEEK"
    ws_dash["B8"] = "% Growth Sales"
    ws_dash["C8"] = "% Growth In-Store"
    ws_dash["D8"] = "% Growth QTY"
    ws_dash["E8"] = "% Growth TRX"
    ws_dash["F8"] = "% Growth Traffic"
    ws_dash["G8"] = "% Growth UPT"
    ws_dash["H8"] = "% Growth BagSize"
    ws_dash["I8"] = "% Growth AUR"
    ws_dash["J8"] = "% Growth CRR"
    ws_dash["K8"] = "Insight / Analisis Otomatis"
    
    for col in range(1, 12):
        cell = ws_dash.cell(row=8, column=col)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    weekly_data = [
        ("WEEK 36", "+12.4%", "+10.8%", "+15.2%", "+8.9%", "+5.1%", "+5.8%", "+3.2%", "+2.1%", "+3.6%", "Pertumbuhan stabil, kenaikan sales didorong oleh peningkatan traffic dan basket size."),
        ("WEEK 37", "+18.7%", "+16.2%", "+20.1%", "+12.4%", "+7.8%", "+6.9%", "+5.6%", "+3.9%", "+4.3%", "Performa optimal pasca payday campaign, UPT melampaui target divisi."),
        ("WEEK 38", "+9.5%", "+8.1%", "+11.3%", "+6.2%", "+4.0%", "+4.8%", "+3.1%", "+1.8%", "+2.1%", "Pertumbuhan melandai pertengahan bulan, conversion rate tetap stabil di atas 70%."),
        ("WEEK 39", "+14.8%", "+13.0%", "+17.5%", "+10.1%", "+6.5%", "+6.7%", "+4.3%", "+2.5%", "+3.4%", "Aktivitas promosi weekend efektif mengerek volume QTY transaksi."),
        ("WEEK 40", "+15.2%", "+13.9%", "+16.8%", "+11.0%", "+6.9%", "+5.2%", "+3.8%", "+2.9%", "+3.8%", "Penutupan bulan September positif dengan peningkatan total omzet YoY 14.07%."),
        ("TOTAL / AVG", "+14.1%", "+12.4%", "+16.2%", "+9.7%", "+6.1%", "+5.9%", "+4.0%", "+2.6%", "+3.4%", "Secara kumulatif performa September 2026 tumbuh kuat dibandingkan 2025.")
    ]
    
    for r_idx, row in enumerate(weekly_data, start=9):
        is_total = (r_idx == 14)
        for c_idx, val in enumerate(row, start=1):
            cell = ws_dash.cell(row=r_idx, column=c_idx, value=val)
            cell.border = border_thin
            if is_total:
                cell.font = Font(bold=True, color="1E3A8A")
                cell.fill = PatternFill(start_color="DBEAFE", end_color="DBEAFE", fill_type="solid")
            else:
                cell.font = Font(size=10)
            if c_idx < 11:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")

    # 2. Sheet WEEKLY
    ws_weekly = wb.create_sheet(title="WEEKLY")
    ws_weekly.views.sheetView[0].showGridLines = True
    ws_weekly["A1"] = "REKAPITULASI MINGGUAN DENGAN FORMULA SUMIFS & ISOWEEKNUM"
    ws_weekly["A1"].font = Font(size=14, bold=True, color="1E3A8A")
    
    headers_weekly = [
        "WEEK_ISO", "YEAR", "SALES 2025", "SALES 2026", "YoY SALES", 
        "QTY 2025", "QTY 2026", "TRX 2025", "TRX 2026", "UPT 2026", "BAG SIZE 2026", "FORMULA SUMIFS ACTIVE"
    ]
    for c_idx, h in enumerate(headers_weekly, start=1):
        cell = ws_weekly.cell(row=3, column=c_idx, value=h)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="0D9488", end_color="0D9488", fill_type="solid") # Teal
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_thin

    weekly_rows = [
        ("36", "2026", 354890000, 398900000, "12.4%", 2840, 3271, 1320, 1438, 2.27, 277399, "=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,36)"),
        ("37", "2026", 412500000, 489600000, "18.7%", 3310, 3975, 1510, 1698, 2.34, 288339, "=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,37)"),
        ("38", "2026", 389400000, 426400000, "9.5%", 3120, 3472, 1420, 1508, 2.30, 282758, "=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,38)"),
        ("39", "2026", 378200000, 434100000, "14.8%", 3050, 3583, 1380, 1519, 2.36, 285780, "=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,39)"),
        ("40", "2026", 407510000, 469500000, "15.2%", 3260, 3807, 1490, 1654, 2.30, 283857, "=SUMIFS('DATA MENTAH'!$D:$D,'DATA MENTAH'!$U:$U,2026,'DATA MENTAH'!$W:$W,40)"),
    ]
    for r_idx, r in enumerate(weekly_rows, start=4):
        for c_idx, val in enumerate(r, start=1):
            cell = ws_weekly.cell(row=r_idx, column=c_idx, value=val)
            cell.border = border_thin
            if c_idx in [3, 4, 11]:
                cell.number_format = '#,##0'
            if c_idx == 12:
                cell.font = Font(name="Consolas", color="0F766E", size=9)

    # 3. Sheet DATA MENTAH
    ws_raw = wb.create_sheet(title="DATA MENTAH")
    ws_raw.views.sheetView[0].showGridLines = True
    
    raw_headers = [
        "DATE","STORE LOC","CITY","Total_SALES","Total_QTY","SALES_DP","QTY_DP","SALES_CV","QTY_CV",
        "TRX","TRAFFIC","Channel_BAZAR","Channel_S&T","Channel_B2B","Sales Div 1","Sales Div 2","Sales Div 3",
        "Sales Div 4","BUDGET","SELISIH +/-","YEAR","MONTH","WEEK_ISO","DAY_ID","WEEK"
    ]
    for c_idx, h in enumerate(raw_headers, start=1):
        cell = ws_raw.cell(row=1, column=c_idx, value=h)
        cell.font = Font(bold=True, color="FFFFFF", size=9)
        cell.fill = PatternFill(start_color="334155", end_color="334155", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
    
    # Auto-adjust column widths
    for ws in [ws_dash, ws_weekly, ws_raw]:
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 3, 12)
            
    ws_dash.column_dimensions['K'].width = 45
    ws_weekly.column_dimensions['L'].width = 55
    
    out_path = r"public\downloads\EDP_Retail_Weekly_Analytics.xlsx"
    wb.save(out_path)
    print("EDP Workbook created:", out_path)

if __name__ == "__main__":
    create_edp_workbook()
