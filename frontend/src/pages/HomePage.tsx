import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { 
  Search, 
  ArrowRight, 
  GraduationCap, 
  HeartPulse, 
  Sprout, 
  Users, 
  Home, 
  Briefcase, 
  Accessibility, 
  UserCheck, 
  Shield, 
  TrendingUp, 
  Award, 
  Sun,
  MessageSquare,
  Sparkles,
  FileText,
  ChevronRight
} from 'lucide-react';
import { VoiceButton } from '../components/common/VoiceButton';
import { StatsCounter } from '../components/common/StatsCounter';
import { SchemeCard } from '../components/common/SchemeCard';
import { IndiaMap } from '../components/common/IndiaMap';
import { fetchPopularSchemes, fetchCategories } from '../services/api';
import { Scheme, SchemeCategory } from '../types';

export const HomePage: React.FC = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();
  const [searchQuery, setSearchQuery] = useState('');
  const [popularSchemes, setPopularSchemes] = useState<Scheme[]>([]);
  const [categories, setCategories] = useState<SchemeCategory[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [schemes, cats] = await Promise.all([
          fetchPopularSchemes(),
          fetchCategories()
        ]);
        setPopularSchemes(schemes);
        setCategories(cats);
      } catch (err) {
        console.error('Error loading home data:', err);
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) return;
    navigate(`/chat?q=${encodeURIComponent(searchQuery.trim())}`);
  };

  const handleVoiceTranscript = (transcript: string) => {
    if (transcript) {
      setSearchQuery(transcript);
      // Auto-redirect to /chat with query
      setTimeout(() => {
        navigate(`/chat?q=${encodeURIComponent(transcript)}`);
      }, 500);
    }
  };

  // Map string to Lucide icon
  const getCategoryIcon = (iconName: string) => {
    switch (iconName) {
      case 'GraduationCap': return GraduationCap;
      case 'HeartPulse': return HeartPulse;
      case 'Sprout': return Sprout;
      case 'Users': return Users;
      case 'Home': return Home;
      case 'Briefcase': return Briefcase;
      case 'Accessibility': return Accessibility;
      case 'UserCheck': return UserCheck;
      case 'Shield': return Shield;
      case 'TrendingUp': return TrendingUp;
      case 'Award': return Award;
      case 'Sun': return Sun;
      default: return Sprout;
    }
  };

  return (
    <div className="space-y-12 pb-16">
      {/* 1. HERO SECTION */}
      <section className="relative bg-[#1A3A6B] text-white py-16 sm:py-20 px-4 overflow-hidden border-b-4 border-setu-saffron">
        {/* Subtle Indian Geometric SVG Background Pattern Overlay */}
        <div className="absolute inset-0 opacity-10 pointer-events-none">
          <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <pattern id="indian-pattern" width="60" height="60" patternUnits="userSpaceOnUse">
                <circle cx="30" cy="30" r="15" fill="none" stroke="#FFFFFF" strokeWidth="1" />
                <path d="M30 0 L30 60 M0 30 L60 30" stroke="#FFFFFF" strokeWidth="0.5" />
                <rect x="25" y="25" width="10" height="10" transform="rotate(45 30 30)" fill="none" stroke="#FF6B00" strokeWidth="1" />
              </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#indian-pattern)" />
          </svg>
        </div>

        <div className="max-w-4xl mx-auto text-center relative z-10 space-y-6">
          <div className="inline-flex items-center space-x-2 bg-white/10 backdrop-blur-md px-3.5 py-1 rounded-full text-xs font-semibold border border-white/20 text-slate-100">
            <Sparkles className="w-3.5 h-3.5 text-setu-saffron" />
            <span>AI-Powered Citizen Services Gateway</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight">
            Discover Government Schemes Made For You
          </h1>

          <p className="text-sm sm:text-base text-slate-200 max-w-2xl mx-auto leading-relaxed">
            3,000+ central and state schemes. Find what you are eligible for in minutes through voice or simple questions.
          </p>

          {/* Large Search Bar with Voice */}
          <form onSubmit={handleSearchSubmit} className="max-w-2xl mx-auto mt-6">
            <div className="bg-white p-2 rounded-full shadow-2xl flex items-center border-2 border-slate-200 focus-within:border-setu-saffron transition-all">
              <div className="pl-3 text-slate-400">
                <Search className="w-5 h-5" />
              </div>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search schemes, or ask SETU anything..."
                className="w-full px-3 py-2 text-slate-800 text-sm sm:text-base outline-hidden bg-transparent"
              />
              <div className="flex items-center space-x-2 pr-1">
                <VoiceButton onTranscript={handleVoiceTranscript} size="md" />
                <button
                  type="submit"
                  className="bg-setu-saffron hover:bg-setu-saffron-dark text-white px-5 py-2.5 rounded-full font-bold text-xs sm:text-sm shadow-sm transition-all hidden sm:flex items-center space-x-1"
                >
                  <span>Search</span>
                </button>
              </div>
            </div>
          </form>

          {/* Quick Category Pills */}
          <div className="flex items-center justify-center flex-wrap gap-2 pt-2 text-xs">
            <span className="text-slate-300 font-medium mr-1">Popular Topics:</span>
            {[
              { label: 'Education', cat: 'education' },
              { label: 'Health', cat: 'health' },
              { label: 'Agriculture', cat: 'agriculture' },
              { label: 'Women', cat: 'women' },
              { label: 'Housing', cat: 'housing' },
              { label: 'SC/ST Scholarships', cat: 'education' },
              { label: 'Youth & Loans', cat: 'entrepreneurship' },
            ].map((pill, idx) => (
              <button
                key={idx}
                onClick={() => navigate(`/schemes?category=${pill.cat}`)}
                className="bg-white/15 hover:bg-white/30 text-white px-3 py-1 rounded-full transition-all border border-white/20"
              >
                {pill.label}
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* 2. STATS BAR */}
      <StatsCounter />

      {/* 3. CATEGORY CARDS GRID */}
      <section className="max-w-7xl mx-auto px-4 lg:px-8 space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-slate-200 pb-3">
          <div>
            <h2 className="text-2xl font-extrabold text-slate-900 tracking-tight">
              Explore Schemes by Category
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              Browse welfare programs organized by citizen sectors and beneficiary groups
            </p>
          </div>
          <Link
            to="/schemes"
            className="text-xs font-bold text-setu-blue hover:text-setu-saffron flex items-center space-x-1 transition-colors"
          >
            <span>View All Categories</span>
            <ChevronRight className="w-4 h-4" />
          </Link>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          {categories.map((cat) => {
            const Icon = getCategoryIcon(cat.icon);
            return (
              <div
                key={cat.id}
                onClick={() => navigate(`/schemes?category=${cat.id}`)}
                className="bg-white rounded-xl border border-slate-200 p-4 hover:border-setu-saffron hover:shadow-lg hover:-translate-y-1 transition-all cursor-pointer group flex flex-col justify-between"
              >
                <div className="flex items-start justify-between mb-3">
                  <div
                    className="w-11 h-11 rounded-lg flex items-center justify-center transition-transform group-hover:scale-105"
                    style={{ backgroundColor: `${cat.color}15` }}
                  >
                    <Icon className="w-6 h-6" style={{ color: cat.color }} />
                  </div>
                  <span className="text-[11px] font-bold text-slate-600 bg-slate-100 px-2 py-0.5 rounded-full">
                    {cat.count} schemes
                  </span>
                </div>

                <div>
                  <h3 className="font-bold text-sm text-slate-900 group-hover:text-setu-blue transition-colors">
                    {cat.name}
                  </h3>
                  <p className="text-[11px] text-slate-500 mt-0.5 font-medium line-clamp-1">
                    {cat.native_name}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 4. AI FINDER SECTION */}
      <section className="max-w-7xl mx-auto px-4 lg:px-8">
        <div className="bg-gradient-to-r from-[#1A3A6B] to-[#2952A3] rounded-2xl p-8 sm:p-10 text-white shadow-xl flex flex-col md:flex-row items-center justify-between gap-6 border-l-8 border-setu-saffron">
          <div className="space-y-2 max-w-xl text-center md:text-left">
            <span className="text-xs font-bold text-setu-saffron uppercase tracking-wider">
              Smart Eligibility Engine
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              Don't know where to start?
            </h2>
            <p className="text-sm text-slate-200">
              Answer 5 quick questions about your age, location, and requirements. SETU calculates your match across 3,000+ schemes instantly.
            </p>
          </div>

          <Link
            to="/find"
            className="bg-setu-saffron hover:bg-setu-saffron-dark text-white px-6 py-3.5 rounded-xl font-bold text-sm shadow-lg hover:shadow-xl transition-all flex items-center space-x-2 flex-shrink-0"
          >
            <span>Start Finding Schemes</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </section>

      {/* 5. POPULAR SCHEMES HORIZONTAL SCROLL */}
      <section className="max-w-7xl mx-auto px-4 lg:px-8 space-y-4">
        <div className="flex items-center justify-between border-b border-slate-200 pb-3">
          <div>
            <h2 className="text-2xl font-extrabold text-slate-900 tracking-tight">
              Popular Schemes This Month
            </h2>
            <p className="text-xs text-slate-500 mt-0.5">
              High-impact flagship welfare programs with maximum citizen enrollment
            </p>
          </div>
          <Link
            to="/schemes"
            className="text-xs font-bold text-setu-blue hover:text-setu-saffron flex items-center space-x-1"
          >
            <span>Explore All</span>
            <ChevronRight className="w-4 h-4" />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {popularSchemes.map((scheme) => (
            <SchemeCard
              key={scheme.id}
              scheme={scheme}
              showMatchBadge={false}
            />
          ))}
        </div>
      </section>

      {/* 6. HOW SETU WORKS */}
      <section className="bg-white border-y border-slate-200 py-12">
        <div className="max-w-7xl mx-auto px-4 lg:px-8 space-y-8">
          <div className="text-center space-y-1">
            <h2 className="text-2xl font-extrabold text-slate-900 tracking-tight">
              How SETU Works
            </h2>
            <p className="text-xs text-slate-500">
              Access government welfare support in 3 simple, guided steps
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
            {/* Step 1 */}
            <div className="bg-slate-50 border border-slate-200 rounded-xl p-6 text-center space-y-3 relative">
              <div className="w-12 h-12 rounded-full bg-blue-100 text-setu-blue font-extrabold text-lg flex items-center justify-center mx-auto border-2 border-setu-blue">
                1
              </div>
              <h3 className="font-bold text-base text-slate-900">
                Ask in Your Language
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Speak or type your requirement in any of 12 Indian languages using natural voice input.
              </p>
            </div>

            {/* Step 2 */}
            <div className="bg-slate-50 border border-slate-200 rounded-xl p-6 text-center space-y-3 relative">
              <div className="w-12 h-12 rounded-full bg-orange-100 text-setu-saffron font-extrabold text-lg flex items-center justify-center mx-auto border-2 border-setu-saffron">
                2
              </div>
              <h3 className="font-bold text-base text-slate-900">
                SETU Matches Schemes
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Our AI compares your profile against central and state rules to find guaranteed entitlements.
              </p>
            </div>

            {/* Step 3 */}
            <div className="bg-slate-50 border border-slate-200 rounded-xl p-6 text-center space-y-3 relative">
              <div className="w-12 h-12 rounded-full bg-emerald-100 text-setu-green font-extrabold text-lg flex items-center justify-center mx-auto border-2 border-setu-green">
                3
              </div>
              <h3 className="font-bold text-base text-slate-900">
                Apply with Step-by-Step Guidance
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Get document checklists, DigiLocker verification, and direct official portal application links.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* 7. STATE SCHEMES WITH INTERACTIVE INDIA MAP */}
      <section id="states" className="max-w-7xl mx-auto px-4 lg:px-8">
        <IndiaMap />
      </section>
    </div>
  );
};
