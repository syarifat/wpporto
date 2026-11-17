import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_snt_workbook():
    wb = openpyxl.Workbook()
    
    # 1. Sheet TARGET SNT OKTOBER
    ws_target = wb.active
    ws_target.title = "TARGET SNT OKTOBER"
    ws_target.views.sheetView[0].showGridLines = True
    
    border_thin = Border(left=Side(style='thin', color='CBD5E1'),
                         right=Side(style='thin', color='CBD5E1'),
                         top=Side(style='thin', color='CBD5E1'),
                         bottom=Side(style='thin', color='CBD5E1'))
                         
    ws_target["A1"] = "REKAPITULASI PENJUALAN HARIAN, MINGGUAN (MINGGU-SABTU), & BULANAN S&T"
    ws_target["A1"].font = Font(size=14, bold=True, color="1E3A8A")
    
    # Target Table Headers
    target_headers = [
        "TGL", "HARI", "TARGET TRX", "TARGET SALES", "ACTUAL TRX", "ACTUAL SALES (NET 1.11)", 
        "ACTUAL QTY", "ACH TRX %", "ACH SALES %", "",
        "PERIODE MINGGU (MINGGU - SABTU)", "TARGET TRX", "ACTUAL TRX", "ACH TRX %", 
        "TARGET SALES", "ACTUAL SALES", "ACH SALES %", "QTY", "AUR", "BAG SIZE"
    ]
    
    for c_idx, h in enumerate(target_headers, start=1):
        cell = ws_target.cell(row=3, column=c_idx, value=h)
        cell.font = Font(bold=True, color="FFFFFF", size=9)
        cell.fill = PatternFill(start_color="4338CA", end_color="4338CA", fill_type="solid") # Indigo
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border_thin
        
    weeks_summary = [
        ("Week 1 (01 - 03 Okt | Parsial)", 39, 43, "110.3%", 6000000, 6842000, "114.0%", 58, 117965, 1.35),
        ("Week 2 (04 - 10 Okt | Min - Sab)", 88, 94, "106.8%", 13400000, 14210000, "106.0%", 126, 112777, 1.34),
        ("Week 3 (11 - 17 Okt | Min - Sab)", 88, 91, "103.4%", 13400000, 13890000, "103.7%", 119, 116722, 1.31),
        ("Week 4 (18 - 24 Okt | Min - Sab)", 88, 96, "109.1%", 13400000, 14850000, "110.8%", 131, 113358, 1.36),
        ("Week 5 (25 - 31 Okt | Min - Sab)", 88, 95, "108.0%", 13400000, 14610000, "109.0%", 128, 114140, 1.35),
        ("TOTAL MINGGUAN (= BULANAN)", 391, 419, "107.2%", 59600000, 64402000, "108.1%", 562, 114594, 1.34)
    ]
    
    for r_idx, w in enumerate(weeks_summary, start=4):
        is_total = (r_idx == 9)
        for c_idx, val in enumerate(w, start=11):
            cell = ws_target.cell(row=r_idx, column=c_idx, value=val)
            cell.border = border_thin
            if is_total:
                cell.font = Font(bold=True, color="1E3A8A")
                cell.fill = PatternFill(start_color="E0E7FF", end_color="E0E7FF", fill_type="solid")
            if c_idx in [15, 16, 19]:
                cell.number_format = '#,##0'

    # Leaderboard Sales Person
    ws_target["A12"] = "LEADERBOARD PERFORMA SALES PERSON (OKTOBER 2026)"
    ws_target["A12"].font = Font(size=12, bold=True, color="1E3A8A")
    
    lb_headers = ["RANK", "BARCODE", "NAMA SALES PERSON", "DIVISI", "TOTAL TRX", "TOTAL OMZET (BRUTO)", "FORMULA INDEX/MATCH"]
    for c_idx, h in enumerate(lb_headers, start=1):
        cell = ws_target.cell(row=13, column=c_idx, value=h)
        cell.font = Font(bold=True, color="FFFFFF", size=9)
        cell.fill = PatternFill(start_color="15803D", end_color="15803D", fill_type="solid") # Green
        cell.alignment = Alignment(horizontal="center")
        cell.border = border_thin
        
    sales_persons = [
        (1, "101001", "RINA KUSUMAWATI", "DIV 1", 52, 9840000, "=INDEX('DATA SALES'!$B:$B, MATCH(A14, 'DATA SALES'!$A:$A, 0))"),
        (2, "101002", "DIMAS PRASETYO", "DIV 1", 48, 8910000, "=INDEX('DATA SALES'!$B:$B, MATCH(A15, 'DATA SALES'!$A:$A, 0))"),
        (3, "101003", "SITI NURHALIZA", "DIV 2", 46, 8420000, "=INDEX('DATA SALES'!$B:$B, MATCH(A16, 'DATA SALES'!$A:$A, 0))"),
        (4, "101004", "BAGUS WICAKSONO", "DIV 2", 43, 7650000, "=INDEX('DATA SALES'!$B:$B, MATCH(A17, 'DATA SALES'!$A:$A, 0))"),
        (5, "101005", "DEWI ANGGRAINI", "DIV 3", 42, 7520000, "=INDEX('DATA SALES'!$B:$B, MATCH(A18, 'DATA SALES'!$A:$A, 0))"),
        (6, "101006", "FAJAR NUGROHO", "DIV 3", 40, 7120000, "=INDEX('DATA SALES'!$B:$B, MATCH(A19, 'DATA SALES'!$A:$A, 0))"),
        (7, "101007", "PUTRI MAHARANI", "DIV 4", 39, 6980000, "=INDEX('DATA SALES'!$B:$B, MATCH(A20, 'DATA SALES'!$A:$A, 0))"),
        (8, "101008", "REZA PAHLEVI", "DIV 4", 38, 6840000, "=INDEX('DATA SALES'!$B:$B, MATCH(A21, 'DATA SALES'!$A:$A, 0))"),
        (9, "101009", "INTAN PERMATASARI", "DIV 1", 37, 6590000, "=INDEX('DATA SALES'!$B:$B, MATCH(A22, 'DATA SALES'!$A:$A, 0))"),
        (10, "101010", "HENDRA GUNAWAN", "DIV 3", 34, 6120000, "=INDEX('DATA SALES'!$B:$B, MATCH(A23, 'DATA SALES'!$A:$A, 0))"),
    ]
    
    for r_idx, sp in enumerate(sales_persons, start=14):
        for c_idx, val in enumerate(sp, start=1):
            cell = ws_target.cell(row=r_idx, column=c_idx, value=val)
            cell.border = border_thin
            if c_idx == 6:
                cell.number_format = '#,##0'
            if c_idx == 7:
                cell.font = Font(name="Consolas", color="166534", size=9)

    # 2. Sheet SELISIH OKTOBER
    ws_selisih = wb.create_sheet(title="SELISIH OKTOBER")
    ws_selisih.views.sheetView[0].showGridLines = True
    ws_selisih["A1"] = "LOG AUDIT REKONSILIASI MUTASI BANK / QRIS HARIAN (OKTOBER 2026)"
    ws_selisih["A1"].font = Font(size=14, bold=True, color="991B1B") # Red
    
    selisih_headers = ["TANGGAL", "NOMINAL SELISIH", "STATUS", "KETERANGAN / AUDIT LOG ALASAN"]
    for c_idx, h in enumerate(selisih_headers, start=1):
        cell = ws_selisih.cell(row=3, column=c_idx, value=h)
        cell.font = Font(bold=True, color="FFFFFF", size=9)
        cell.fill = PatternFill(start_color="B91C1C", end_color="B91C1C", fill_type="solid")
        cell.border = border_thin
        
    audit_logs = [
        ("01/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("02/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("03/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("04/10/2026", 150000, "SELISIH (+)", "Transfer customer Rp150.000 masuk rekening namun belum ditransaksikan ke POS (menunggu konfirmasi barang)."),
        ("05/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("06/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("07/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("08/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("09/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("10/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("11/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("12/10/2026", -49900, "SELISIH (-)", "Customer melakukan retur tukar size/produk selisih kurang bayar Rp49.900."),
        ("13/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("14/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("15/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("16/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("17/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("18/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("19/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("20/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("21/10/2026", 85000, "SELISIH (+)", "Kelebihan transfer customer Rp85.000, dicatat sebagai saldo deposit transaksi berikutnya."),
        ("22/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("23/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("24/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("25/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("26/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("27/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("28/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("29/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("30/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)"),
        ("31/10/2026", 0, "MATCH", "Rekonsiliasi sesuai (Struk POS = Mutasi Bank/QRIS)")
    ]
    
    for r_idx, log in enumerate(audit_logs, start=4):
        for c_idx, val in enumerate(log, start=1):
            cell = ws_selisih.cell(row=r_idx, column=c_idx, value=val)
            cell.border = border_thin
            if c_idx == 2:
                cell.number_format = '#,##0'
                if val > 0:
                    cell.fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
                elif val < 0:
                    cell.fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

    # 3. Sheet INPUT NOTA HARIAN (Struk & Validasi)
    ws_nota = wb.create_sheet(title="INPUT NOTA HARIAN")
    ws_nota.views.sheetView[0].showGridLines = True
    
    nota_headers = [
        "DIVISI","CV/DP","BRAND","BY","NO STRUK","TOTAL STRUK","PEMBAYARAN","CEK (HARUS 0)",
        "Gross DP","Net DP","Net DP (1.11)","Qty DP","Gross CV","Net CV","Net CV (1.11)","Qty CV",
        "SALES PERSON","BARCODE","SKU PRODUK","METODE PENGIRIMAN","ALAMAT CUST","MEMBER (V)","NO RESI"
    ]
    for c_idx, h in enumerate(nota_headers, start=1):
        cell = ws_nota.cell(row=1, column=c_idx, value=h)
        cell.font = Font(bold=True, color="FFFFFF", size=9)
        cell.fill = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
        cell.border = border_thin
        
    # Auto-adjust column widths
    for ws in [ws_target, ws_selisih, ws_nota]:
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 3, 12)
            
    ws_target.column_dimensions['G'].width = 60
    ws_selisih.column_dimensions['D'].width = 75
    
    out_path = r"public\downloads\SNT_Omnichannel_Reconciliation.xlsx"
    wb.save(out_path)
    print("SNT Workbook created:", out_path)

if __name__ == "__main__":
    create_snt_workbook()
