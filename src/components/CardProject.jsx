import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { ExternalLink, ArrowRight, Eye, X, Maximize2 } from "lucide-react";
import { toSlug } from "../utils/slug";

const CardProject = ({ Img, Title, Description, Link: ProjectLink, id }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  // Close modal on Escape key
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === "Escape") setIsModalOpen(false);
    };
    if (isModalOpen) {
      window.addEventListener("keydown", handleKeyDown);
    }
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isModalOpen]);

  const handleLiveDemo = (e) => {
    if (!ProjectLink) {
      e.preventDefault();
    }
  };

  const handleDetails = (e) => {
    if (!id) {
      e.preventDefault();
      alert("Project details are not available");
    }
  };

  return (
    <>
      <div className="group relative w-full">
        <div className="relative overflow-hidden rounded-xl bg-gradient-to-br from-slate-900/90 to-slate-800/90 backdrop-blur-lg border border-white/10 shadow-2xl transition-all duration-300 hover:shadow-purple-500/20">
          <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 via-purple-500/10 to-pink-500/10 opacity-50 group-hover:opacity-70 transition-opacity duration-300"></div>

          <div className="relative p-5 z-10">
            {/* Image Thumbnail with Click-to-Zoom */}
            <div
              className="relative overflow-hidden rounded-lg aspect-[16/9] bg-slate-950 cursor-pointer group/img"
              onClick={() => setIsModalOpen(true)}
              title="Klik untuk melihat tangkapan layar penuh"
            >
              <img
                src={Img}
                alt={Title}
                className="w-full h-full object-cover object-top transform group-hover/img:scale-105 transition-transform duration-500"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover/img:opacity-100 transition-opacity duration-300 flex items-end justify-between p-3">
                <span className="text-xs text-white flex items-center gap-1.5 font-medium">
                  <Maximize2 className="w-3.5 h-3.5 text-purple-400" />
                  Lihat Screenshot Web
                </span>
                <span className="text-[10px] text-gray-400">Klik untuk perbesar</span>
              </div>
              <div className="absolute top-2 right-2 px-2 py-0.5 rounded-md bg-black/60 backdrop-blur-md text-[10px] text-purple-300 font-medium border border-purple-500/30">
                Dokumentasi Riil
              </div>
            </div>

            <div className="mt-4 space-y-3">
              <h3 className="text-xl font-semibold bg-gradient-to-r from-blue-200 via-purple-200 to-pink-200 bg-clip-text text-transparent">
                {Title}
              </h3>

              <p className="text-gray-300/80 text-sm leading-relaxed line-clamp-2">
                {Description}
              </p>

              <div className="pt-4 flex items-center justify-between gap-2">
                {ProjectLink ? (
                  <a
                    href={ProjectLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    onClick={handleLiveDemo}
                    className="inline-flex items-center space-x-2 text-blue-400 hover:text-blue-300 transition-colors duration-200"
                  >
                    <span className="text-sm font-medium">Live Demo</span>
                    <ExternalLink className="w-4 h-4" />
                  </a>
                ) : (
                  <button
                    type="button"
                    onClick={() => setIsModalOpen(true)}
                    className="inline-flex items-center space-x-1.5 px-2.5 py-1.5 rounded-lg bg-purple-500/10 hover:bg-purple-500/20 text-purple-300 border border-purple-500/20 transition-all text-xs font-medium"
                    title="Lihat tangkapan layar website"
                  >
                    <Eye className="w-3.5 h-3.5" />
                    <span>Lihat Screenshot</span>
                  </button>
                )}

                {id ? (
                  <Link
                    to={`/project/${toSlug(Title)}`}
                    onClick={handleDetails}
                    className="inline-flex items-center space-x-2 px-4 py-2 rounded-lg bg-white/5 hover:bg-white/10 text-white/90 transition-all duration-200 hover:scale-105 active:scale-95 focus:outline-none focus:ring-2 focus:ring-purple-500/50"
                  >
                    <span className="text-sm font-medium">Details</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                ) : (
                  <span className="text-gray-500 text-sm">
                    Details Not Available
                  </span>
                )}
              </div>
            </div>

            <div className="absolute inset-0 border border-white/0 group-hover:border-purple-500/50 rounded-xl transition-colors duration-300 -z-50"></div>
          </div>
        </div>
      </div>

      {/* Modal / Lightbox Pratinjau Tangkapan Layar Penuh */}
      {isModalOpen && (
        <div
          className="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-3 sm:p-6 animate-fadeIn"
          onClick={() => setIsModalOpen(false)}
        >
          <div
            className="relative w-full max-w-4xl max-h-[92vh] bg-[#0c0d1f] border border-white/15 rounded-2xl flex flex-col shadow-2xl overflow-hidden"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Modal Header */}
            <div className="flex items-center justify-between px-5 py-3.5 border-b border-white/10 bg-white/[0.02]">
              <div className="flex items-center gap-2.5">
                <span className="px-2 py-0.5 rounded text-[11px] font-semibold bg-purple-500/20 text-purple-300 border border-purple-500/30">
                  Tangkapan Layar Web
                </span>
                <h4 className="text-sm sm:text-base font-bold text-white truncate max-w-[280px] sm:max-w-md">
                  {Title}
                </h4>
              </div>
              <div className="flex items-center gap-3">
                {id && (
                  <Link
                    to={`/project/${toSlug(Title)}`}
                    className="hidden sm:inline-flex items-center gap-1.5 px-3 py-1 text-xs font-medium text-blue-300 bg-blue-500/10 border border-blue-500/30 rounded-lg hover:bg-blue-500/20 transition-colors"
                  >
                    <span>Buka Detail Studi Kasus</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                )}
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  className="p-1.5 rounded-lg text-gray-400 hover:text-white hover:bg-white/10 transition-colors"
                  aria-label="Tutup"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Scrollable Full Screenshot Area */}
            <div className="overflow-y-auto p-3 sm:p-5 flex-1 bg-black/40 flex flex-col items-center">
              <div className="w-full max-w-3xl rounded-xl overflow-hidden border border-white/10 shadow-2xl bg-slate-950">
                <img
                  src={Img}
                  alt={Title}
                  className="w-full h-auto object-contain select-none"
                />
              </div>
              <p className="mt-3 text-xs text-gray-400 text-center">
                Gulir ke bawah untuk melihat seluruh halaman antarmuka website.
              </p>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default CardProject;
