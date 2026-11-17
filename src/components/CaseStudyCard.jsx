import React, { useState, useEffect } from "react";
import {
  FileSpreadsheet,
  Download,
  ExternalLink,
  Code2,
  ChevronDown,
  ChevronUp,
  Maximize2,
  X,
  ChevronLeft,
  ChevronRight,
  CheckCircle2,
  AlertCircle,
  TrendingUp,
  Copy,
  Check,
  Table,
  Layers,
  Sparkles,
} from "lucide-react";
import Swal from "sweetalert2";

export default function CaseStudyCard({ data }) {
  const [activeImageIndex, setActiveImageIndex] = useState(0);
  const [isLightboxOpen, setIsLightboxOpen] = useState(false);
  const [isFormulaOpen, setIsFormulaOpen] = useState(false);
  const [isLiveSheetOpen, setIsLiveSheetOpen] = useState(false);
  const [copiedIndex, setCopiedIndex] = useState(null);
  const [activeSheetTab, setActiveSheetTab] = useState(0);

  // Close lightbox on Escape
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") {
        setIsLightboxOpen(false);
        setIsLiveSheetOpen(false);
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  const handleCopyFormula = (formula, idx) => {
    navigator.clipboard.writeText(formula);
    setCopiedIndex(idx);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  const currentGalleryItem = data.gallery[activeImageIndex] || data.gallery[0];

  const handleNextImage = () => {
    setActiveImageIndex((prev) => (prev + 1) % data.gallery.length);
  };

  const handlePrevImage = () => {
    setActiveImageIndex((prev) => (prev - 1 + data.gallery.length) % data.gallery.length);
  };

  return (
    <div className="relative group mb-12">
      {/* Background Glow */}
      <div className="absolute -inset-1 bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 rounded-3xl blur-xl opacity-40 group-hover:opacity-70 transition duration-700 pointer-events-none" />

      {/* Main Container */}
      <div className="relative bg-[#0a0a1a]/95 backdrop-blur-xl border border-white/10 hover:border-indigo-500/40 rounded-3xl p-5 sm:p-7 md:p-8 transition-all duration-300">
        
        {/* HEADER SECTION */}
        <div className="border-b border-white/10 pb-6 mb-6">
          <div className="flex flex-wrap items-center gap-2.5 mb-3">
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-indigo-500/15 text-indigo-300 border border-indigo-500/30 flex items-center gap-1.5 shadow-sm">
              <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
              {data.badgeCategory}
            </span>
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 flex items-center gap-1.5 shadow-sm">
              <FileSpreadsheet className="w-3.5 h-3.5 text-emerald-400" />
              {data.badgeTool}
            </span>
            {data.badgeRole && (
              <span className="px-3 py-1 rounded-full text-xs font-semibold bg-purple-500/15 text-purple-300 border border-purple-500/30 shadow-sm">
                {data.badgeRole}
              </span>
            )}
          </div>

          <h3 className="text-xl sm:text-2xl md:text-3xl font-extrabold text-white tracking-tight leading-snug">
            {data.title}
          </h3>
          <p className="mt-2 text-sm sm:text-base text-indigo-200/80 font-medium leading-relaxed">
            {data.impactSummary}
          </p>
        </div>

        {/* SPLIT GRID: 2 COLUMNS */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          {/* KOLOM KIRI: VISUAL SHOWCASE */}
          <div className="lg:col-span-6 flex flex-col gap-4">
            
            {/* Main Interactive Hero Image */}
            <div 
              onClick={() => setIsLightboxOpen(true)}
              className="relative aspect-[16/10] w-full rounded-2xl overflow-hidden border border-white/10 bg-[#0d0d22] cursor-pointer group/img shadow-2xl"
            >
              <img
                src={currentGalleryItem.src}
                alt={currentGalleryItem.title}
                className="w-full h-full object-contain sm:object-cover transition-transform duration-500 group-hover/img:scale-105"
              />
              
              {/* Overlay hover prompt */}
              <div className="absolute inset-0 bg-black/40 opacity-0 group-hover/img:opacity-100 transition-opacity duration-300 flex flex-col items-center justify-center gap-2 backdrop-blur-[2px]">
                <div className="p-3 bg-white/10 rounded-full border border-white/20 text-white shadow-lg transform -translate-y-2 group-hover/img:translate-y-0 transition-transform duration-300">
                  <Maximize2 className="w-6 h-6" />
                </div>
                <span className="text-xs font-medium text-white px-3 py-1 rounded-full bg-black/60 border border-white/10">
                  Klik untuk Zoom / Lightbox
                </span>
              </div>

              {/* Caption pill on bottom of main image */}
              <div className="absolute bottom-2.5 left-2.5 right-2.5 px-3 py-1.5 rounded-xl bg-black/70 backdrop-blur-md border border-white/10 text-xs text-gray-200 flex items-center justify-between pointer-events-none">
                <span className="font-semibold truncate">{currentGalleryItem.title}</span>
                <span className="text-[10px] text-indigo-300 uppercase tracking-wider shrink-0 ml-2">Zoom 125%</span>
              </div>
            </div>

            {/* 3 Thumbnails */}
            <div className="grid grid-cols-3 gap-2.5">
              {data.gallery.map((item, idx) => {
                const isActive = idx === activeImageIndex;
                return (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => setActiveImageIndex(idx)}
                    className={`relative rounded-xl overflow-hidden aspect-[16/10] border transition-all duration-300 text-left ${
                      isActive
                        ? "border-indigo-500 ring-2 ring-indigo-500/50 scale-[1.02]"
                        : "border-white/10 hover:border-white/30 opacity-70 hover:opacity-100"
                    }`}
                  >
                    <img
                      src={item.src}
                      alt={item.title}
                      className="w-full h-full object-cover"
                    />
                    <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex items-end p-1.5">
                      <span className="text-[10px] font-medium text-white leading-tight line-clamp-1">
                        {item.thumbLabel || item.title}
                      </span>
                    </div>
                  </button>
                );
              })}
            </div>

            {/* Lightbox / Modal View */}
            {isLightboxOpen && (
              <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/85 backdrop-blur-md animate-fadeIn">
                <div
                  className="absolute inset-0"
                  onClick={() => setIsLightboxOpen(false)}
                />
                
                <div className="relative z-10 w-full max-w-5xl bg-[#0a0a1a] border border-white/20 rounded-2xl overflow-hidden shadow-2xl flex flex-col max-h-[92vh]">
                  {/* Modal Header */}
                  <div className="flex items-center justify-between px-5 py-3.5 border-b border-white/10 bg-white/5 shrink-0">
                    <div>
                      <h4 className="text-sm sm:text-base font-bold text-white flex items-center gap-2">
                        <FileSpreadsheet className="w-4 h-4 text-emerald-400" />
                        {currentGalleryItem.title}
                      </h4>
                      <p className="text-xs text-gray-400 mt-0.5">
                        {currentGalleryItem.desc}
                      </p>
                    </div>
                    <button
                      type="button"
                      onClick={() => setIsLightboxOpen(false)}
                      className="p-1.5 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition-colors"
                    >
                      <X className="w-5 h-5" />
                    </button>
                  </div>

                  {/* Modal Image Area */}
                  <div className="relative flex-1 overflow-auto p-2 sm:p-4 flex items-center justify-center bg-[#070714]">
                    <img
                      src={currentGalleryItem.src}
                      alt={currentGalleryItem.title}
                      className="max-h-[75vh] w-auto object-contain rounded-lg shadow-xl"
                    />

                    {/* Nav Prev */}
                    <button
                      type="button"
                      onClick={handlePrevImage}
                      className="absolute left-4 top-1/2 -translate-y-1/2 p-2.5 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white backdrop-blur-sm transition-all"
                    >
                      <ChevronLeft className="w-5 h-5" />
                    </button>

                    {/* Nav Next */}
                    <button
                      type="button"
                      onClick={handleNextImage}
                      className="absolute right-4 top-1/2 -translate-y-1/2 p-2.5 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white backdrop-blur-sm transition-all"
                    >
                      <ChevronRight className="w-5 h-5" />
                    </button>
                  </div>

                  {/* Modal Footer */}
                  <div className="px-5 py-2.5 border-t border-white/10 bg-white/5 flex items-center justify-between text-xs text-gray-400 shrink-0">
                    <span>
                      Gambar {activeImageIndex + 1} dari {data.gallery.length}
                    </span>
                    <span className="hidden sm:inline text-indigo-300">
                      Resolusi tajam untuk menyorot formula bar &amp; validasi angka
                    </span>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* KOLOM KANAN: CASE STUDY DETAIL */}
          <div className="lg:col-span-6 flex flex-col gap-5">
            
            {/* 1. Tantangan (Problem) */}
            <div className="p-4 sm:p-4.5 rounded-2xl bg-red-950/20 border border-red-500/20">
              <div className="flex items-center gap-2 text-red-400 font-bold text-xs uppercase tracking-wider mb-2">
                <AlertCircle className="w-4 h-4 shrink-0" />
                Tantangan (Problem)
              </div>
              <p className="text-xs sm:text-sm text-gray-300 leading-relaxed">
                {data.problem}
              </p>
            </div>

            {/* 2. Alur Kerja (Process Workflow) */}
            <div className="p-4 sm:p-4.5 rounded-2xl bg-indigo-950/20 border border-indigo-500/20">
              <div className="flex items-center gap-2 text-indigo-400 font-bold text-xs uppercase tracking-wider mb-2.5">
                <Layers className="w-4 h-4 shrink-0" />
                Alur Kerja &amp; Solusi (Process)
              </div>
              <p className="text-xs sm:text-sm text-gray-300 leading-relaxed mb-3">
                {data.process}
              </p>
              
              {/* 3-Step Visual Mini-Pipeline */}
              {data.workflowSteps && (
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 pt-2 border-t border-white/10">
                  {data.workflowSteps.map((step, sIdx) => (
                    <div key={sIdx} className="bg-white/5 rounded-xl p-2.5 border border-white/5 flex flex-col justify-between">
                      <span className="text-[10px] font-bold text-indigo-400 mb-1">
                        STEP 0{sIdx + 1}
                      </span>
                      <span className="text-xs text-gray-200 font-medium leading-snug">
                        {step}
                      </span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* 3. Hasil & Metrik (Impact) */}
            <div className="p-4 sm:p-4.5 rounded-2xl bg-emerald-950/20 border border-emerald-500/20">
              <div className="flex items-center gap-2 text-emerald-400 font-bold text-xs uppercase tracking-wider mb-2">
                <TrendingUp className="w-4 h-4 shrink-0" />
                Hasil &amp; Metrik (Impact)
              </div>
              <p className="text-xs sm:text-sm text-gray-300 leading-relaxed">
                {data.impact}
              </p>
            </div>

            {/* Pill Tags: Rumus / Tools */}
            <div className="flex flex-wrap gap-2 pt-1">
              {data.tags.map((tag, tIdx) => (
                <span
                  key={tIdx}
                  className="px-2.5 py-1 rounded-lg text-xs font-medium bg-white/5 border border-white/10 text-gray-300"
                >
                  {tag}
                </span>
              ))}
            </div>

            {/* ACCORDION: BEDAH LOGIKA RUMUS */}
            <div className="rounded-2xl border border-indigo-500/30 overflow-hidden bg-[#0d0d22] transition-all">
              <button
                type="button"
                onClick={() => setIsFormulaOpen(!isFormulaOpen)}
                className="w-full px-4 py-3 bg-indigo-500/10 hover:bg-indigo-500/15 flex items-center justify-between text-left transition-colors"
              >
                <div className="flex items-center gap-2 text-xs sm:text-sm font-semibold text-indigo-300">
                  <Code2 className="w-4 h-4 text-indigo-400" />
                  <span>Bedah Logika Rumus ({data.formulas?.length || 0} Formula Kunci)</span>
                </div>
                {isFormulaOpen ? (
                  <ChevronUp className="w-4 h-4 text-indigo-400" />
                ) : (
                  <ChevronDown className="w-4 h-4 text-indigo-400" />
                )}
              </button>

              {isFormulaOpen && (
                <div className="p-4 flex flex-col gap-3 border-t border-white/8 divide-y divide-white/5">
                  {data.formulas?.map((f, fIdx) => (
                    <div key={fIdx} className={fIdx > 0 ? "pt-3" : ""}>
                      <div className="flex items-center justify-between mb-1.5">
                        <span className="text-xs font-semibold text-gray-300">
                          {f.name}
                        </span>
                        <button
                          type="button"
                          onClick={() => handleCopyFormula(f.formula, fIdx)}
                          className="flex items-center gap-1 text-[11px] text-gray-400 hover:text-white px-2 py-0.5 rounded bg-white/5 hover:bg-white/10 transition-colors"
                        >
                          {copiedIndex === fIdx ? (
                            <>
                              <Check className="w-3 h-3 text-emerald-400" />
                              <span className="text-emerald-400">Tersalin</span>
                            </>
                          ) : (
                            <>
                              <Copy className="w-3 h-3" />
                              <span>Salin</span>
                            </>
                          )}
                        </button>
                      </div>

                      {/* Formula Code Block */}
                      <pre className="p-2.5 rounded-xl bg-black/60 border border-white/8 text-[11px] sm:text-xs text-sky-300 font-mono overflow-x-auto whitespace-pre-wrap select-all">
                        {f.formula}
                      </pre>
                      {f.explanation && (
                        <p className="text-[11px] text-gray-400 mt-1.5 leading-relaxed">
                          💡 <span className="text-gray-300">{f.explanation}</span>
                        </p>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* DUAL ACTION BUTTONS */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              {/* Primary: Preview Live Sheet */}
              <button
                type="button"
                onClick={() => setIsLiveSheetOpen(true)}
                className="w-full py-3 px-4 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-semibold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-lg shadow-indigo-600/30 hover:shadow-indigo-600/50 transition-all duration-300 group/btn"
              >
                <Table className="w-4 h-4 group-hover/btn:rotate-6 transition-transform" />
                <span>Preview Live Sheet</span>
              </button>

              {/* Secondary: Unduh Sampel (.xlsx) */}
              <a
                href={data.downloadUrl}
                download
                className="w-full py-3 px-4 rounded-xl bg-white/5 hover:bg-white/10 border border-white/15 hover:border-emerald-500/40 text-gray-200 hover:text-white font-semibold text-xs sm:text-sm flex items-center justify-center gap-2 transition-all duration-300"
              >
                <Download className="w-4 h-4 text-emerald-400" />
                <span>Unduh Sampel (.xlsx)</span>
              </a>
            </div>

          </div>
        </div>

        {/* MODAL: LIVE SHEET PREVIEW */}
        {isLiveSheetOpen && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/85 backdrop-blur-md animate-fadeIn">
            <div
              className="absolute inset-0"
              onClick={() => setIsLiveSheetOpen(false)}
            />
            
            <div className="relative z-10 w-full max-w-5xl bg-[#0a0a1a] border border-white/20 rounded-2xl overflow-hidden shadow-2xl flex flex-col max-h-[92vh]">
              {/* Header */}
              <div className="flex items-center justify-between px-5 py-4 border-b border-white/10 bg-white/5 shrink-0">
                <div className="flex items-center gap-3">
                  <div className="p-2 rounded-lg bg-emerald-500/20 text-emerald-400">
                    <FileSpreadsheet className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="text-base font-bold text-white">
                      Live Workbook Viewer: {data.sheetTitle}
                    </h3>
                    <p className="text-xs text-gray-400">
                      Pratinjau data interaktif langsung dari berkas Excel
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <a
                    href={data.downloadUrl}
                    download
                    className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 text-xs font-medium hover:bg-emerald-600/50 transition-colors"
                  >
                    <Download className="w-3.5 h-3.5" />
                    Unduh Workbook (.xlsx)
                  </a>
                  <button
                    type="button"
                    onClick={() => setIsLiveSheetOpen(false)}
                    className="p-1.5 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition-colors"
                  >
                    <X className="w-5 h-5" />
                  </button>
                </div>
              </div>

              {/* Sheet Tabs */}
              <div className="flex items-center gap-2 px-5 py-2.5 bg-[#070714] border-b border-white/10 overflow-x-auto shrink-0">
                {data.sheetTabs?.map((tab, idx) => (
                  <button
                    key={idx}
                    type="button"
                    onClick={() => setActiveSheetTab(idx)}
                    className={`px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition-all ${
                      activeSheetTab === idx
                        ? "bg-indigo-600 text-white shadow-sm"
                        : "text-gray-400 hover:text-gray-200 hover:bg-white/5"
                    }`}
                  >
                    {tab.name}
                  </button>
                ))}
              </div>

              {/* Sheet Table Viewer */}
              <div className="p-4 overflow-auto flex-1 bg-[#0b0c1b]">
                {data.sheetTabs?.[activeSheetTab]?.content}
              </div>

              {/* Footer */}
              <div className="px-5 py-3 border-t border-white/10 bg-white/5 flex flex-wrap items-center justify-between text-xs text-gray-400 shrink-0 gap-2">
                <span>
                  Menampilkan data sampel representatif dari sheet {data.sheetTabs?.[activeSheetTab]?.name}
                </span>
                <span className="text-indigo-400 font-medium">
                  Status: Siap diunduh &amp; tervalidasi 100%
                </span>
              </div>
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
