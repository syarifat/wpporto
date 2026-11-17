import React, { useEffect, useState, useCallback } from "react";

import { supabase } from "../supabase"; 

import PropTypes from "prop-types";
import AppBar from "@mui/material/AppBar";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import CardProject from "../components/CardProject";
import TechStackIcon from "../components/TechStackIcon";
import AOS from "aos";
import "aos/dist/aos.css";
import Certificate from "../components/Certificate";
import { Code, Award, Boxes, FileSpreadsheet, LayoutGrid, Building2, Wrench } from "lucide-react";
import CaseStudyCard from "../components/CaseStudyCard";
import { caseStudiesData } from "../data/caseStudiesData";
import { defaultProjects } from "../data/defaultProjects";
import { toSlug } from "../utils/slug";


const ToggleButton = ({ onClick, isShowingMore }) => (
  <button
    onClick={onClick}
    className="
      px-3 py-1.5
      text-slate-300 
      hover:text-white 
      text-sm 
      font-medium 
      transition-all 
      duration-300 
      ease-in-out
      flex 
      items-center 
      gap-2
      bg-white/5 
      hover:bg-white/10
      rounded-md
      border 
      border-white/10
      hover:border-white/20
      backdrop-blur-sm
      group
      relative
      overflow-hidden
    "
  >
    <span className="relative z-10 flex items-center gap-2">
      {isShowingMore ? "See Less" : "See More"}
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="16"
        height="16"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className={`
          transition-transform 
          duration-300 
          ${isShowingMore ? "group-hover:-translate-y-0.5" : "group-hover:translate-y-0.5"}
        `}
      >
        <polyline points={isShowingMore ? "18 15 12 9 6 15" : "6 9 12 15 18 9"}></polyline>
      </svg>
    </span>
    <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-purple-500/50 transition-all duration-300 group-hover:w-full"></span>
  </button>
);


function TabPanel({ children, value, index, ...other }) {
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: { xs: 1, sm: 3 } }}>
          <Typography component="div">{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

const techStacks = [
  { icon: "html.svg", language: "HTML" },
  { icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg", language: "Python" },
  { icon: "javascript.svg", language: "JavaScript" },
  { icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/laravel/laravel-original.svg", language: "Laravel" },
  { icon: "https://upload.wikimedia.org/wikipedia/commons/1/19/Microsoft_Office_Word_%282019%E2%80%932025%29.svg", language: "Microsoft Word" },
  { icon: "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/microsoftexcel.svg", language: "Microsoft Excel" },
  { icon: "https://cdn.simpleicons.org/googlesheets/34A853", language: "Spreadsheets" },
  { icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/figma/figma-original.svg", language: "Figma" },
  { icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/canva/canva-original.svg", language: "Canva" },
  { icon: "https://cdn.jsdelivr.net/npm/simple-icons@v13/icons/adobepremierepro.svg", language: "Adobe" },
  { icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original.svg", language: "MySQL" },
  { icon: "firebase.svg", language: "Firebase" },
  { icon: "bootstrap.svg", language: "Bootstrap" },
  { icon: "https://cdn-icons-png.flaticon.com/512/9850/9850812.png", language: "Database" },
];

export default function FullWidthTabs() {
  const [value, setValue] = useState(0);
  const [projects, setProjects] = useState([]);
  const [certificates, setCertificates] = useState([]);
  const [showAllProjects, setShowAllProjects] = useState(false);
  const [showAllCertificates, setShowAllCertificates] = useState(false);
  const [selectedProjectFilter, setSelectedProjectFilter] = useState("all"); // 'all', 'widi', 'perkim'
  const [selectedCaseStudyId, setSelectedCaseStudyId] = useState("edp-weekly-reporting"); // 'edp-weekly-reporting', 'snt-omnichannel-tracking', or 'all'
  const isMobile = window.innerWidth < 768;
  const initialItems = isMobile ? 4 : 6;

  useEffect(() => {
    AOS.init({
      once: false,
    });
  }, []);

  const fetchData = useCallback(async () => {
    try {
      // Mengambil data dari Supabase secara paralel
      const [projectsResponse, certificatesResponse] = await Promise.all([
        supabase.from("projects").select("*").order('id', { ascending: false }),
        supabase.from("certificates").select("*").order('id', { ascending: false }), 
      ]);

      // Error handling untuk setiap request
      if (projectsResponse.error) throw projectsResponse.error;
      if (certificatesResponse.error) throw certificatesResponse.error;

      // Supabase mengembalikan data dalam properti 'data'
      const projectData = projectsResponse.data || [];
      const certificateData = certificatesResponse.data || [];

      // Gabungkan dan perbarui dengan defaultProjects (agar gambar screenshot asli & status tanpa live demo langsung aktif)
      let combinedProjects = projectData.map((item) => {
        const matchingDefault = defaultProjects.find(
          (dp) => toSlug(dp.Title) === toSlug(item.Title)
        );
        if (matchingDefault) {
          return {
            ...item,
            Img: matchingDefault.Img,
            Link: matchingDefault.Link,
            TechStack: matchingDefault.TechStack,
            Features: matchingDefault.Features,
            Role: matchingDefault.Role,
            Period: matchingDefault.Period,
            Institution: matchingDefault.Institution,
          };
        }
        return item;
      });

      defaultProjects.forEach((dp) => {
        if (!combinedProjects.some((p) => toSlug(p.Title) === toSlug(dp.Title))) {
          combinedProjects.unshift(dp);
        }
      });

      setProjects(combinedProjects);
      setCertificates(certificateData);

      // Store in localStorage
      localStorage.setItem("projects", JSON.stringify(combinedProjects));
      localStorage.setItem("certificates", JSON.stringify(certificateData));
      
      // Dispatch custom event to notify other components (like About)
      window.dispatchEvent(new Event("portfolioDataUpdated"));
    } catch (error) {
      console.error("Error fetching data from Supabase:", error.message);
      // Fallback jika offline / database belum berisi
      const cachedProjects = localStorage.getItem('projects');
      if (!cachedProjects) {
        setProjects(defaultProjects);
        localStorage.setItem("projects", JSON.stringify(defaultProjects));
      }
    }
  }, []);

  useEffect(() => {
    // Coba ambil dari localStorage dulu untuk load lebih cepat
    const cachedProjects = localStorage.getItem('projects');
    const cachedCertificates = localStorage.getItem('certificates');

    if (cachedProjects) {
      const parsed = JSON.parse(cachedProjects);
      let combined = parsed.map((item) => {
        const matchingDefault = defaultProjects.find(
          (dp) => toSlug(dp.Title) === toSlug(item.Title)
        );
        if (matchingDefault) {
          return {
            ...item,
            Img: matchingDefault.Img,
            Link: matchingDefault.Link,
            TechStack: matchingDefault.TechStack,
            Features: matchingDefault.Features,
            Role: matchingDefault.Role,
            Period: matchingDefault.Period,
            Institution: matchingDefault.Institution,
          };
        }
        return item;
      });

      defaultProjects.forEach((dp) => {
        if (!combined.some((p) => toSlug(p.Title) === toSlug(dp.Title))) {
          combined.unshift(dp);
        }
      });
      setProjects(combined);
      localStorage.setItem('projects', JSON.stringify(combined));
    } else {
      setProjects(defaultProjects);
      localStorage.setItem('projects', JSON.stringify(defaultProjects));
    }

    if (cachedCertificates) {
      setCertificates(JSON.parse(cachedCertificates));
    }
    
    fetchData(); // Tetap panggil fetchData untuk sinkronisasi data terbaru
  }, [fetchData]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const toggleShowMore = useCallback((type) => {
    if (type === 'projects') {
      setShowAllProjects(prev => !prev);
    } else {
      setShowAllCertificates(prev => !prev);
    }
  }, []);

  const filteredProjects = projects.filter((project) => {
    if (selectedProjectFilter === "all") return true;
    if (selectedProjectFilter === "widi") {
      return project.Title?.toLowerCase().includes("widi");
    }
    if (selectedProjectFilter === "perkim") {
      return project.Title?.toLowerCase().includes("perkim");
    }
    return true;
  });

  const displayedProjects = showAllProjects ? filteredProjects : filteredProjects.slice(0, initialItems);
  const displayedCertificates = showAllCertificates ? certificates : certificates.slice(0, initialItems);

  // Sisa dari komponen (return statement) tidak ada perubahan
  return (
    <div className="md:px-[10%] px-[5%] w-full sm:mt-0 mt-[3rem] bg-[#030014] overflow-hidden" id="Portofolio">
      {/* Header section - unchanged */}
      <div className="text-center pb-10" data-aos="fade-up" data-aos-duration="1000">
        <h2 className="inline-block text-3xl md:text-5xl font-bold text-center mx-auto text-transparent bg-clip-text bg-gradient-to-r from-[#6366f1] to-[#a855f7]">
          <span style={{
            color: '#6366f1',
            backgroundImage: 'linear-gradient(45deg, #6366f1 10%, #a855f7 93%)',
            WebkitBackgroundClip: 'text',
            backgroundClip: 'text',
            WebkitTextFillColor: 'transparent'
          }}>
            Portfolio Showcase
          </span>
        </h2>
        <p className="text-slate-400 max-w-2xl mx-auto text-sm md:text-base mt-2">
          Explore my journey through projects, certifications, and technical expertise. 
          Each section represents a milestone in my continuous learning path.
        </p>
      </div>

      <Box sx={{ width: "100%" }}>
        {/* AppBar and Tabs section - unchanged */}
        <AppBar
          position="static"
          elevation={0}
          sx={{
            bgcolor: "transparent",
            border: "1px solid rgba(255, 255, 255, 0.1)",
            borderRadius: "20px",
            position: "relative",
            overflow: "hidden",
            "&::before": {
              content: '""',
              position: "absolute",
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              background: "linear-gradient(180deg, rgba(139, 92, 246, 0.03) 0%, rgba(59, 130, 246, 0.03) 100%)",
              backdropFilter: "blur(10px)",
              zIndex: 0,
            },
          }}
          className="md:px-4"
        >
          {/* Tabs remain unchanged */}
          <Tabs
            value={value}
            onChange={handleChange}
            textColor="secondary"
            indicatorColor="secondary"
            variant="fullWidth"
            sx={{
              minHeight: "70px",
              "& .MuiTab-root": {
                fontSize: { xs: "0.9rem", md: "1rem" },
                fontWeight: "600",
                color: "#94a3b8",
                textTransform: "none",
                transition: "all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                padding: "20px 0",
                zIndex: 1,
                margin: "8px",
                borderRadius: "12px",
                "&:hover": {
                  color: "#ffffff",
                  backgroundColor: "rgba(139, 92, 246, 0.1)",
                  transform: "translateY(-2px)",
                  "& .lucide": {
                    transform: "scale(1.1) rotate(5deg)",
                  },
                },
                "&.Mui-selected": {
                  color: "#fff",
                  background: "linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(59, 130, 246, 0.2))",
                  boxShadow: "0 4px 15px -3px rgba(139, 92, 246, 0.2)",
                  "& .lucide": {
                    color: "#a78bfa",
                  },
                },
              },
              "& .MuiTabs-indicator": {
                height: 0,
              },
              "& .MuiTabs-flexContainer": {
                gap: "8px",
              },
            }}
          >
            <Tab
              icon={<Code className="mb-2 w-5 h-5 transition-all duration-300" />}
              label="Projects"
              {...a11yProps(0)}
            />
            <Tab
              icon={<FileSpreadsheet className="mb-2 w-5 h-5 transition-all duration-300" />}
              label="Data Analytics"
              {...a11yProps(1)}
            />
            <Tab
              icon={<Award className="mb-2 w-5 h-5 transition-all duration-300" />}
              label="Certificates"
              {...a11yProps(2)}
            />
            <Tab
              icon={<Boxes className="mb-2 w-5 h-5 transition-all duration-300" />}
              label="Tech Stack"
              {...a11yProps(3)}
            />
          </Tabs>
        </AppBar>

        <div>
          {/* TAB 0: WEB PROJECTS */}
          <TabPanel value={value} index={0}>
            <div className="container mx-auto">
              {/* Header Title */}
              <div className="text-center max-w-2xl mx-auto mb-8" data-aos="fade-up">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold mb-3">
                  <Code className="w-4 h-4" />
                  <span>Web Applications &amp; Digital Services</span>
                </div>
                <h3 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                  Featured Web Development Projects
                </h3>
                <p className="mt-2 text-xs sm:text-sm text-gray-400">
                  Implementasi sistem informasi manajemen berbasis Laravel &amp; Midtrans serta portal e-government publik hasil Tugas Akhir dan PKL.
                </p>
              </div>

              {/* Project Filter Switcher Pills - Pemilihan mana yang mau ditampilkan */}
              <div className="flex flex-wrap items-center justify-center gap-3 mb-10" data-aos="fade-up" data-aos-delay="100">
                <button
                  type="button"
                  onClick={() => setSelectedProjectFilter("all")}
                  className={`px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    selectedProjectFilter === "all"
                      ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 scale-105 border border-indigo-400/40"
                      : "bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10"
                  }`}
                >
                  <LayoutGrid className="w-4 h-4" />
                  <span>Semua Proyek</span>
                </button>

                <button
                  type="button"
                  onClick={() => setSelectedProjectFilter("widi")}
                  className={`px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    selectedProjectFilter === "widi"
                      ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 scale-105 border border-indigo-400/40"
                      : "bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10"
                  }`}
                >
                  <Wrench className="w-4 h-4 text-rose-400" />
                  <span>CV. Widi Elektrical (Laravel)</span>
                </button>

                <button
                  type="button"
                  onClick={() => setSelectedProjectFilter("perkim")}
                  className={`px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    selectedProjectFilter === "perkim"
                      ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 scale-105 border border-indigo-400/40"
                      : "bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10"
                  }`}
                >
                  <Building2 className="w-4 h-4 text-amber-400" />
                  <span>Dinas Perkim Kediri (PHP/Bootstrap)</span>
                </button>
              </div>

              {/* Projects Grid */}
              <div className="flex justify-center items-center overflow-hidden">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 2xl:grid-cols-3 gap-5 w-full">
                  {displayedProjects.map((project, index) => (
                    <div
                      key={project.id || index}
                      data-aos={index % 3 === 0 ? "fade-up-right" : index % 3 === 1 ? "fade-up" : "fade-up-left"}
                      data-aos-duration={index % 3 === 0 ? "1000" : index % 3 === 1 ? "1200" : "1000"}
                    >
                      <CardProject
                        Img={project.Img}
                        Title={project.Title}
                        Description={project.Description}
                        Link={project.Link}
                        id={project.id}
                      />
                    </div>
                  ))}
                </div>
              </div>

              {filteredProjects.length > initialItems && (
                <div className="mt-6 w-full flex justify-start">
                  <ToggleButton
                    onClick={() => toggleShowMore("projects")}
                    isShowingMore={showAllProjects}
                  />
                </div>
              )}
            </div>
          </TabPanel>

          {/* TAB 1: DATA ANALYTICS & EXCEL CASE STUDIES */}
          <TabPanel value={value} index={1}>
            <div className="container mx-auto">
              {/* Header Title */}
              <div className="text-center max-w-2xl mx-auto mb-8" data-aos="fade-up">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold mb-3">
                  <FileSpreadsheet className="w-4 h-4" />
                  <span>Visual Case Studies</span>
                </div>
                <h3 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                  Data Analytics &amp; Reporting Showcase
                </h3>
                <p className="mt-2 text-xs sm:text-sm text-gray-400">
                  Pilih salah satu proyek di bawah ini untuk melihat detail case study, alur kerja, validasi otomatis, dan bedah rumus formula.
                </p>
              </div>

              {/* Proyek Selector (Pill Switcher) - Pilih mana yang mau ditampilkan */}
              <div className="flex flex-wrap items-center justify-center gap-3 mb-10" data-aos="fade-up" data-aos-delay="100">
                <button
                  type="button"
                  onClick={() => setSelectedCaseStudyId("edp-weekly-reporting")}
                  className={`px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    selectedCaseStudyId === "edp-weekly-reporting"
                      ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 scale-105 border border-indigo-400/40"
                      : "bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10"
                  }`}
                >
                  <FileSpreadsheet className="w-4 h-4 text-emerald-400" />
                  <span>1. Retail Weekly Analytics (EDP)</span>
                </button>

                <button
                  type="button"
                  onClick={() => setSelectedCaseStudyId("snt-omnichannel-tracking")}
                  className={`px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    selectedCaseStudyId === "snt-omnichannel-tracking"
                      ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 scale-105 border border-indigo-400/40"
                      : "bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10"
                  }`}
                >
                  <FileSpreadsheet className="w-4 h-4 text-indigo-400" />
                  <span>2. Omnichannel Reconciliation (S&amp;T)</span>
                </button>

                <button
                  type="button"
                  onClick={() => setSelectedCaseStudyId("all")}
                  className={`px-4 sm:px-5 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-300 flex items-center gap-2.5 ${
                    selectedCaseStudyId === "all"
                      ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg shadow-indigo-600/30 scale-105 border border-indigo-400/40"
                      : "bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white border border-white/10"
                  }`}
                >
                  <LayoutGrid className="w-4 h-4" />
                  <span>Tampilkan Keduanya</span>
                </button>
              </div>

              {/* Render Selected Case Study */}
              <div className="flex flex-col gap-8">
                {caseStudiesData
                  .filter((cs) => selectedCaseStudyId === "all" || cs.id === selectedCaseStudyId)
                  .map((caseStudy) => (
                    <div key={caseStudy.id} data-aos="fade-up" data-aos-duration="800">
                      <CaseStudyCard data={caseStudy} />
                    </div>
                  ))}
              </div>
            </div>
          </TabPanel>

          {/* TAB 2: CERTIFICATES */}
          <TabPanel value={value} index={2}>
            <div className="container mx-auto flex justify-center items-center overflow-hidden">
              <div className="grid grid-cols-1 md:grid-cols-3 md:gap-5 gap-4">
                {displayedCertificates.map((certificate, index) => (
                  <div
                    key={certificate.id || index}
                    data-aos={index % 3 === 0 ? "fade-up-right" : index % 3 === 1 ? "fade-up" : "fade-up-left"}
                    data-aos-duration={index % 3 === 0 ? "1000" : index % 3 === 1 ? "1200" : "1000"}
                  >
                    <Certificate ImgSertif={certificate.Img} />
                  </div>
                ))}
              </div>
            </div>
            {certificates.length > initialItems && (
              <div className="mt-6 w-full flex justify-start">
                <ToggleButton
                  onClick={() => toggleShowMore("certificates")}
                  isShowingMore={showAllCertificates}
                />
              </div>
            )}
          </TabPanel>

          {/* TAB 3: TECH STACK */}
          <TabPanel value={value} index={3}>
            <div className="container mx-auto flex justify-center items-center overflow-hidden pb-[5%]">
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 lg:gap-8 gap-5">
                {techStacks.map((stack, index) => (
                  <div
                    key={index}
                    data-aos={index % 3 === 0 ? "fade-up-right" : index % 3 === 1 ? "fade-up" : "fade-up-left"}
                    data-aos-duration={index % 3 === 0 ? "1000" : index % 3 === 1 ? "1200" : "1000"}
                  >
                    <TechStackIcon TechStackIcon={stack.icon} Language={stack.language} />
                  </div>
                ))}
              </div>
            </div>
          </TabPanel>
        </div>
      </Box>
    </div>
  );
}