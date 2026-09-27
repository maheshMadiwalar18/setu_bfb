import React, { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import {
  Search,
  ExternalLink,
  Globe,
  Shield,
  ChevronRight,
  ArrowRight,
  RefreshCw,
  Newspaper,
  Building2,
  Landmark,
  Sparkles,
  CheckCircle2,
  Clock,
  Filter,
  X,
  ChevronDown,
  Star,
  IndianRupee,
  AlertCircle,
  Loader2,
  BookOpen,
  Share2,
  Zap,
} from 'lucide-react';

// ─── Types ───────────────────────────────────────────────────────────
interface GovScheme {
  title: string;
  description: string;
  apply_url: string;
  portal_url?: string;
  source: string;
  category: string;
  ministry?: string;
  benefit?: string;
  status?: string;
  state?: string;
  scraped_at?: string;
}

interface GovPortal {
  id: string;
  name: string;
  description: string;
  url: string;
  logo_text: string;
  category: string;
  ministry: string;
  features: string[];
  apply_url?: string;
  is_primary: boolean;
}

interface GovUpdate {
  title: string;
  url: string;
  source: string;
  date: string;
  type: string;
}

interface GovCategory {
  id: string;
  name: string;
  url: string;
  icon: string;
  gov_portal: string;
}

const API_BASE = '/api';

// ─── Category Color Map ─────────────────────────────────────────────
const CATEGORY_COLORS: Record<string, { bg: string; text: string; border: string; badge: string }> = {
  'Agriculture': { bg: 'bg-emerald-50', text: 'text-emerald-800', border: 'border-emerald-200', badge: 'bg-emerald-100' },
  'Health': { bg: 'bg-rose-50', text: 'text-rose-800', border: 'border-rose-200', badge: 'bg-rose-100' },
  'Education': { bg: 'bg-blue-50', text: 'text-blue-800', border: 'border-blue-200', badge: 'bg-blue-100' },
  'Housing': { bg: 'bg-amber-50', text: 'text-amber-800', border: 'border-amber-200', badge: 'bg-amber-100' },
  'Employment': { bg: 'bg-teal-50', text: 'text-teal-800', border: 'border-teal-200', badge: 'bg-teal-100' },
  'Insurance': { bg: 'bg-purple-50', text: 'text-purple-800', border: 'border-purple-200', badge: 'bg-purple-100' },
  'Banking': { bg: 'bg-indigo-50', text: 'text-indigo-800', border: 'border-indigo-200', badge: 'bg-indigo-100' },
  'Business & Entrepreneurship': { bg: 'bg-orange-50', text: 'text-orange-800', border: 'border-orange-200', badge: 'bg-orange-100' },
  'Skills & Employment': { bg: 'bg-cyan-50', text: 'text-cyan-800', border: 'border-cyan-200', badge: 'bg-cyan-100' },
  'Women & Child': { bg: 'bg-pink-50', text: 'text-pink-800', border: 'border-pink-200', badge: 'bg-pink-100' },
  'Social Welfare': { bg: 'bg-violet-50', text: 'text-violet-800', border: 'border-violet-200', badge: 'bg-violet-100' },
  'Utility & Sanitation': { bg: 'bg-lime-50', text: 'text-lime-800', border: 'border-lime-200', badge: 'bg-lime-100' },
  'Digital Services': { bg: 'bg-sky-50', text: 'text-sky-800', border: 'border-sky-200', badge: 'bg-sky-100' },
  'Multi-Service': { bg: 'bg-slate-50', text: 'text-slate-800', border: 'border-slate-200', badge: 'bg-slate-100' },
};

function getCatColor(category: string) {
  return CATEGORY_COLORS[category] || { bg: 'bg-slate-50', text: 'text-slate-800', border: 'border-slate-200', badge: 'bg-slate-100' };
}

// ─── Main Component ─────────────────────────────────────────────────
export const GovSchemesPage: React.FC = () => {
  // State
  const [activeView, setActiveView] = useState<'schemes' | 'portals'>('schemes');
  const [schemes, setSchemes] = useState<GovScheme[]>([]);
  const [portals, setPortals] = useState<GovPortal[]>([]);
  const [updates, setUpdates] = useState<GovUpdate[]>([]);
  const [categories, setCategories] = useState<GovCategory[]>([]);
  const [loading, setLoading] = useState(true);
  const [portalLoading, setPortalLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [showFilters, setShowFilters] = useState(false);
  const [lastScraped, setLastScraped] = useState('');
  const [refreshing, setRefreshing] = useState(false);

  // ─── Fetch Functions ────────────────────────────────────────────
  const fetchGovSchemes = useCallback(async (q = '', cat = '') => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (q) params.append('q', q);
      if (cat) params.append('category', cat);
      const res = await fetch(`${API_BASE}/gov-schemes/search?${params.toString()}`);
      if (res.ok) {
        const data = await res.json();
        setSchemes(data.schemes || []);
        setLastScraped(data.last_scraped || '');
      }
    } catch (err) {
      console.error('Failed to fetch gov schemes:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  const fetchPortals = useCallback(async () => {
    setPortalLoading(true);
    try {
      const res = await fetch(`${API_BASE}/gov-schemes/portals`);
      if (res.ok) {
        const data = await res.json();
        setPortals(data.portals || []);
      }
    } catch (err) {
      console.error('Failed to fetch portals:', err);
    } finally {
      setPortalLoading(false);
    }
  }, []);

  const fetchUpdates = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/gov-schemes/updates`);
      if (res.ok) {
        const data = await res.json();
        setUpdates(data.updates || []);
      }
    } catch (err) {
      console.error('Failed to fetch updates:', err);
    }
  }, []);

  const fetchCategories = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/gov-schemes/categories`);
      if (res.ok) {
        const data = await res.json();
        setCategories(data.categories || []);
      }
    } catch (err) {
      console.error('Failed to fetch categories:', err);
    }
  }, []);

  // ─── Effects ────────────────────────────────────────────────────
  useEffect(() => {
    fetchGovSchemes();
    fetchPortals();
    fetchUpdates();
    fetchCategories();
  }, [fetchGovSchemes, fetchPortals, fetchUpdates, fetchCategories]);

  // ─── Handlers ───────────────────────────────────────────────────
  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    fetchGovSchemes(searchQuery, selectedCategory);
  };

  const handleCategoryFilter = (cat: string) => {
    setSelectedCategory(cat === selectedCategory ? '' : cat);
    fetchGovSchemes(searchQuery, cat === selectedCategory ? '' : cat);
  };

  const handleRefresh = async () => {
    setRefreshing(true);
    await fetchGovSchemes(searchQuery, selectedCategory);
    await fetchUpdates();
    setTimeout(() => setRefreshing(false), 600);
  };

  // ─── Share Handler ──────────────────────────────────────────────
  const handleShare = (title: string, url: string) => {
    if (navigator.share) {
      navigator.share({ title, url }).catch(() => {});
    } else {
      navigator.clipboard.writeText(url);
      alert('Link copied to clipboard!');
    }
  };

  // ─── Render ─────────────────────────────────────────────────────
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white">
      {/* ═══ HERO BANNER ═══ */}
      <div className="relative overflow-hidden bg-gradient-to-br from-setu-blue via-[#1B3F7A] to-[#0F2952]">
        {/* Decorative elements */}
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-10 left-10 w-40 h-40 rounded-full bg-setu-saffron blur-3xl"></div>
          <div className="absolute bottom-10 right-20 w-60 h-60 rounded-full bg-blue-400 blur-3xl"></div>
          <div className="absolute top-1/2 left-1/2 w-32 h-32 rounded-full bg-emerald-400 blur-3xl"></div>
        </div>

        {/* Ashoka Chakra watermark */}
        <div className="absolute right-4 top-4 opacity-[0.04]">
          <svg width="200" height="200" viewBox="0 0 100 100">
            <circle cx="50" cy="50" r="45" fill="none" stroke="white" strokeWidth="2" />
            {Array.from({ length: 24 }).map((_, i) => (
              <line key={i} x1="50" y1="10" x2="50" y2="30" stroke="white" strokeWidth="1.5"
                transform={`rotate(${i * 15} 50 50)`} />
            ))}
          </svg>
        </div>

        <div className="relative max-w-7xl mx-auto px-4 lg:px-8 py-10 sm:py-14">
          {/* Breadcrumb */}
          <nav className="flex items-center space-x-2 text-xs text-blue-200/70 mb-6">
            <Link to="/" className="hover:text-white transition-colors">Home</Link>
            <ChevronRight className="w-3 h-3" />
            <span className="text-white font-semibold">Government Schemes Directory</span>
          </nav>

          <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6">
            <div className="space-y-3 max-w-2xl">
              <div className="flex items-center space-x-2.5">
                <div className="w-10 h-10 rounded-xl bg-setu-saffron/20 border border-setu-saffron/30 flex items-center justify-center">
                  <Landmark className="w-5 h-5 text-setu-saffron" />
                </div>
                <div className="flex items-center space-x-2">
                  <span className="text-xs font-bold text-setu-saffron bg-setu-saffron/10 border border-setu-saffron/20 px-2.5 py-0.5 rounded-full uppercase tracking-wider">
                    Live Data
                  </span>
                  <span className="text-xs text-blue-300/80">
                    Scraped from Official Gov Portals
                  </span>
                </div>
              </div>

              <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight leading-tight">
                Government Schemes
                <br />
                <span className="text-setu-saffron">Directory & Apply Portal</span>
              </h1>

              <p className="text-sm text-blue-100/80 leading-relaxed max-w-xl">
                Real-time access to 700+ government schemes from official portals.
                Search, explore eligibility, and apply directly on verified government websites.
              </p>
            </div>

            {/* Stats strip */}
            <div className="flex flex-wrap items-center gap-3">
              <div className="bg-white/10 backdrop-blur-sm border border-white/10 rounded-xl px-4 py-3 text-center min-w-[90px]">
                <div className="text-2xl font-black text-white">700+</div>
                <div className="text-[10px] text-blue-200/80 font-semibold uppercase tracking-wider">Schemes</div>
              </div>
              <div className="bg-white/10 backdrop-blur-sm border border-white/10 rounded-xl px-4 py-3 text-center min-w-[90px]">
                <div className="text-2xl font-black text-white">36</div>
                <div className="text-[10px] text-blue-200/80 font-semibold uppercase tracking-wider">States/UTs</div>
              </div>
              <div className="bg-white/10 backdrop-blur-sm border border-white/10 rounded-xl px-4 py-3 text-center min-w-[90px]">
                <div className="text-2xl font-black text-white">50+</div>
                <div className="text-[10px] text-blue-200/80 font-semibold uppercase tracking-wider">Ministries</div>
              </div>
            </div>
          </div>

          {/* ─── Search Bar ─── */}
          <form onSubmit={handleSearch} className="mt-8">
            <div className="flex items-center bg-white/95 backdrop-blur-sm rounded-2xl shadow-2xl shadow-black/20 overflow-hidden border border-white/30 max-w-3xl">
              <div className="flex items-center pl-5 pr-2 text-slate-400">
                <Search className="w-5 h-5" />
              </div>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search government schemes... e.g. PM Kisan, scholarship, housing loan"
                className="flex-1 py-4 px-2 bg-transparent text-sm text-slate-900 placeholder:text-slate-400 focus:outline-none"
              />
              <button
                type="button"
                onClick={() => setShowFilters(!showFilters)}
                className={`p-2.5 mr-1 rounded-xl transition-colors ${
                  showFilters ? 'bg-setu-blue text-white' : 'text-slate-400 hover:bg-slate-100'
                }`}
              >
                <Filter className="w-4 h-4" />
              </button>
              <button
                type="submit"
                className="bg-setu-saffron hover:bg-setu-saffron-dark text-white font-bold text-sm px-6 py-4 transition-colors flex items-center space-x-2"
              >
                <span>Search</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </form>

          {/* Category Filters */}
          {showFilters && (
            <div className="mt-4 flex flex-wrap gap-2 animate-fade-in max-w-3xl">
              {['Agriculture', 'Health', 'Education', 'Housing', 'Employment', 'Insurance', 'Banking', 'Business & Entrepreneurship', 'Women & Child', 'Social Welfare'].map(cat => (
                <button
                  key={cat}
                  onClick={() => handleCategoryFilter(cat)}
                  className={`text-xs font-semibold px-3 py-1.5 rounded-full border transition-all ${
                    selectedCategory === cat
                      ? 'bg-white text-setu-blue border-white shadow-md'
                      : 'bg-white/10 text-white/90 border-white/20 hover:bg-white/20'
                  }`}
                >
                  {cat}
                  {selectedCategory === cat && <X className="w-3 h-3 ml-1.5 inline" />}
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Saffron/White/Green border */}
        <div className="flex h-1">
          <div className="flex-1 bg-setu-saffron" />
          <div className="flex-1 bg-white" />
          <div className="flex-1 bg-setu-green" />
        </div>
      </div>

      {/* ═══ MAIN CONTENT ═══ */}
      <div className="max-w-7xl mx-auto px-4 lg:px-8 py-8">
        {/* Tab Switcher */}
        <div className="flex items-center justify-between mb-8">
          <div className="bg-white rounded-xl border border-slate-200 p-1 flex items-center space-x-1 shadow-sm">
            <button
              onClick={() => setActiveView('schemes')}
              className={`px-5 py-2.5 rounded-lg text-xs font-bold transition-all flex items-center space-x-2 ${
                activeView === 'schemes'
                  ? 'bg-setu-blue text-white shadow-md'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              <BookOpen className="w-4 h-4" />
              <span>Government Schemes ({schemes.length})</span>
            </button>
            <button
              onClick={() => setActiveView('portals')}
              className={`px-5 py-2.5 rounded-lg text-xs font-bold transition-all flex items-center space-x-2 ${
                activeView === 'portals'
                  ? 'bg-setu-blue text-white shadow-md'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              <Globe className="w-4 h-4" />
              <span>Official Portals ({portals.length})</span>
            </button>
          </div>

          <div className="flex items-center space-x-3">
            <button
              onClick={handleRefresh}
              className={`flex items-center space-x-1.5 text-xs font-semibold text-slate-600 hover:text-setu-blue transition-colors ${
                refreshing ? 'animate-spin' : ''
              }`}
              disabled={refreshing}
            >
              <RefreshCw className={`w-4 h-4 ${refreshing ? 'animate-spin' : ''}`} />
              <span className="hidden sm:inline">Refresh Data</span>
            </button>
            {lastScraped && (
              <span className="text-[10px] text-slate-400 flex items-center space-x-1 bg-slate-50 px-2 py-1 rounded border border-slate-200">
                <Clock className="w-3 h-3" />
                <span>Last updated: {new Date(lastScraped).toLocaleTimeString()}</span>
              </span>
            )}
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
          {/* ─── LEFT COLUMN: Main Content (8 cols) ─── */}
          <div className="lg:col-span-8 space-y-6">
            {/* SCHEMES VIEW */}
            {activeView === 'schemes' && (
              <>
                {loading ? (
                  <div className="space-y-4">
                    {[1, 2, 3, 4].map(i => (
                      <div key={i} className="bg-white rounded-2xl border border-slate-200 p-6 animate-pulse">
                        <div className="h-4 w-2/3 bg-slate-200 rounded mb-3" />
                        <div className="h-3 w-full bg-slate-100 rounded mb-2" />
                        <div className="h-3 w-5/6 bg-slate-100 rounded" />
                      </div>
                    ))}
                  </div>
                ) : schemes.length === 0 ? (
                  <div className="bg-white rounded-2xl border border-slate-200 p-12 text-center space-y-3">
                    <AlertCircle className="w-12 h-12 text-slate-300 mx-auto" />
                    <h3 className="text-lg font-bold text-slate-700">No schemes found</h3>
                    <p className="text-sm text-slate-500">Try a different search term or clear filters</p>
                    <button
                      onClick={() => { setSearchQuery(''); setSelectedCategory(''); fetchGovSchemes(); }}
                      className="mt-4 px-4 py-2 bg-setu-blue text-white text-xs font-bold rounded-lg hover:bg-setu-blue-dark transition-colors"
                    >
                      Show All Schemes
                    </button>
                  </div>
                ) : (
                  <div className="space-y-4">
                    {/* Results header */}
                    <div className="flex items-center justify-between text-xs text-slate-500">
                      <span>
                        Showing <strong className="text-slate-900">{schemes.length}</strong> government schemes
                        {selectedCategory && <> in <strong className="text-setu-blue">{selectedCategory}</strong></>}
                      </span>
                      <span className="flex items-center space-x-1.5 text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">
                        <Shield className="w-3 h-3" />
                        <span className="font-semibold">Official Verified Data</span>
                      </span>
                    </div>

                    {/* Scheme Cards */}
                    {schemes.map((scheme, idx) => {
                      const catColor = getCatColor(scheme.category);
                      return (
                        <div
                          key={idx}
                          className="group bg-white rounded-2xl border border-slate-200 hover:border-setu-blue/30 hover:shadow-lg hover:shadow-blue-500/5 transition-all duration-300 overflow-hidden"
                        >
                          <div className="p-6 space-y-4">
                            {/* Top badges row */}
                            <div className="flex flex-wrap items-center gap-2">
                              <span className={`text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full border ${catColor.text} ${catColor.badge} ${catColor.border}`}>
                                {scheme.category}
                              </span>
                              {scheme.status === 'Open' && (
                                <span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center space-x-1">
                                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                                  <span>Open for Applications</span>
                                </span>
                              )}
                              <span className="text-[10px] font-medium text-slate-400 ml-auto flex items-center space-x-1">
                                <Globe className="w-3 h-3" />
                                <span>{scheme.source}</span>
                              </span>
                            </div>

                            {/* Title & Description */}
                            <div>
                              <h3 className="text-lg font-extrabold text-slate-900 group-hover:text-setu-blue transition-colors leading-tight">
                                {scheme.title}
                              </h3>
                              <p className="text-sm text-slate-600 mt-1.5 leading-relaxed line-clamp-2">
                                {scheme.description}
                              </p>
                            </div>

                            {/* Meta info row */}
                            <div className="flex flex-wrap items-center gap-3 text-xs">
                              {scheme.benefit && (
                                <div className="flex items-center space-x-1.5 bg-emerald-50 text-emerald-800 px-3 py-1.5 rounded-lg border border-emerald-200 font-bold">
                                  <IndianRupee className="w-3.5 h-3.5" />
                                  <span>{scheme.benefit}</span>
                                </div>
                              )}
                              {scheme.ministry && (
                                <div className="flex items-center space-x-1.5 text-slate-500">
                                  <Building2 className="w-3.5 h-3.5 text-slate-400" />
                                  <span className="truncate max-w-[200px]">{scheme.ministry}</span>
                                </div>
                              )}
                              {scheme.state && (
                                <div className="flex items-center space-x-1.5 text-slate-500">
                                  <Landmark className="w-3.5 h-3.5 text-slate-400" />
                                  <span>{scheme.state}</span>
                                </div>
                              )}
                            </div>

                            {/* Action Buttons */}
                            <div className="flex items-center gap-2.5 pt-2 border-t border-slate-100">
                              <a
                                href={scheme.apply_url}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="inline-flex items-center space-x-2 bg-setu-saffron hover:bg-setu-saffron-dark text-white font-bold text-xs px-5 py-2.5 rounded-xl shadow-sm hover:shadow-md transition-all group/btn"
                              >
                                <Zap className="w-4 h-4" />
                                <span>Apply Now</span>
                                <ExternalLink className="w-3 h-3 opacity-60 group-hover/btn:opacity-100 transition-opacity" />
                              </a>
                              {scheme.portal_url && (
                                <a
                                  href={scheme.portal_url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="inline-flex items-center space-x-1.5 bg-white hover:bg-slate-50 text-slate-700 font-semibold text-xs px-4 py-2.5 rounded-xl border border-slate-200 hover:border-slate-300 transition-all"
                                >
                                  <Globe className="w-3.5 h-3.5 text-setu-blue" />
                                  <span>Visit Portal</span>
                                </a>
                              )}
                              <button
                                onClick={() => handleShare(scheme.title, scheme.apply_url)}
                                className="ml-auto p-2 rounded-lg text-slate-400 hover:text-setu-blue hover:bg-blue-50 transition-colors"
                                title="Share"
                              >
                                <Share2 className="w-4 h-4" />
                              </button>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}
              </>
            )}

            {/* PORTALS VIEW */}
            {activeView === 'portals' && (
              <>
                {portalLoading ? (
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    {[1, 2, 3, 4].map(i => (
                      <div key={i} className="bg-white rounded-2xl border border-slate-200 p-6 animate-pulse h-48" />
                    ))}
                  </div>
                ) : (
                  <div className="space-y-6">
                    {/* Primary Portals */}
                    <div>
                      <h3 className="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 flex items-center space-x-2">
                        <Star className="w-4 h-4 text-setu-saffron" />
                        <span>Flagship Government Portals</span>
                      </h3>
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        {portals.filter(p => p.is_primary).map(portal => (
                          <PortalCard key={portal.id} portal={portal} onShare={handleShare} />
                        ))}
                      </div>
                    </div>

                    {/* Secondary Portals */}
                    <div>
                      <h3 className="text-sm font-bold text-slate-900 uppercase tracking-wider mb-4 flex items-center space-x-2">
                        <Globe className="w-4 h-4 text-setu-blue" />
                        <span>Other Government Service Portals</span>
                      </h3>
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        {portals.filter(p => !p.is_primary).map(portal => (
                          <PortalCard key={portal.id} portal={portal} onShare={handleShare} />
                        ))}
                      </div>
                    </div>
                  </div>
                )}
              </>
            )}
          </div>

          {/* ─── RIGHT COLUMN: Sidebar (4 cols) ─── */}
          <div className="lg:col-span-4 space-y-6">
            {/* Live Updates */}
            <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
              <div className="bg-gradient-to-r from-setu-blue to-setu-blue-dark px-5 py-3.5 flex items-center space-x-2">
                <Newspaper className="w-4 h-4 text-setu-saffron" />
                <h3 className="text-sm font-bold text-white">Latest Updates</h3>
                <span className="ml-auto w-2 h-2 rounded-full bg-emerald-400 animate-pulse" title="Live"></span>
              </div>
              <div className="divide-y divide-slate-100">
                {updates.slice(0, 5).map((update, idx) => (
                  <a
                    key={idx}
                    href={update.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block p-4 hover:bg-slate-50 transition-colors group"
                  >
                    <div className="flex items-start space-x-3">
                      <div className="w-8 h-8 rounded-lg bg-blue-50 border border-blue-100 flex items-center justify-center flex-shrink-0 group-hover:bg-blue-100 transition-colors">
                        <Zap className="w-4 h-4 text-setu-blue" />
                      </div>
                      <div className="min-w-0">
                        <p className="text-xs font-semibold text-slate-800 group-hover:text-setu-blue transition-colors leading-tight line-clamp-2">
                          {update.title}
                        </p>
                        <div className="flex items-center space-x-2 mt-1.5 text-[10px] text-slate-400">
                          <span className="flex items-center space-x-1">
                            <Clock className="w-3 h-3" />
                            <span>{update.date}</span>
                          </span>
                          <span>•</span>
                          <span className="font-medium text-slate-500">{update.source}</span>
                        </div>
                      </div>
                    </div>
                  </a>
                ))}
              </div>
            </div>

            {/* Quick Links to MyScheme Categories */}
            <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
              <div className="px-5 py-3.5 border-b border-slate-100 flex items-center space-x-2">
                <Sparkles className="w-4 h-4 text-setu-saffron" />
                <h3 className="text-sm font-bold text-slate-900">Browse by Category</h3>
              </div>
              <div className="p-3 space-y-1">
                {categories.slice(0, 10).map((cat) => (
                  <a
                    key={cat.id}
                    href={cat.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center justify-between p-2.5 rounded-xl hover:bg-slate-50 transition-colors group text-xs"
                  >
                    <div className="flex items-center space-x-2.5">
                      <span className="text-base">{cat.icon}</span>
                      <span className="font-semibold text-slate-700 group-hover:text-setu-blue transition-colors">
                        {cat.name}
                      </span>
                    </div>
                    <ChevronRight className="w-3.5 h-3.5 text-slate-300 group-hover:text-setu-blue transition-colors" />
                  </a>
                ))}
              </div>
              <div className="px-5 pb-4">
                <a
                  href="https://www.myscheme.gov.in/search"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="block text-center text-xs font-bold text-setu-blue bg-blue-50 hover:bg-blue-100 border border-blue-200 rounded-xl py-2.5 transition-colors"
                >
                  View All Categories on myScheme.gov.in →
                </a>
              </div>
            </div>

            {/* Verified Badge */}
            <div className="bg-gradient-to-br from-emerald-50 to-green-50 rounded-2xl border border-emerald-200 p-5 space-y-3">
              <div className="flex items-center space-x-2">
                <Shield className="w-5 h-5 text-emerald-600" />
                <h4 className="text-sm font-bold text-emerald-900">Official Data Sources</h4>
              </div>
              <p className="text-[11px] text-emerald-800/80 leading-relaxed">
                All scheme data is sourced from official Indian Government portals including
                myscheme.gov.in, india.gov.in, and respective ministry websites. Apply links
                point directly to official government registration pages.
              </p>
              <div className="flex flex-wrap gap-1.5 pt-1">
                {['myscheme.gov.in', 'india.gov.in', 'pmkisan.gov.in', 'pmjay.gov.in', 'nrega.nic.in'].map(domain => (
                  <span key={domain} className="text-[9px] font-mono font-semibold bg-emerald-100/80 text-emerald-700 px-2 py-0.5 rounded-md border border-emerald-200">
                    {domain}
                  </span>
                ))}
              </div>
            </div>

            {/* Need Help CTA */}
            <Link
              to="/chat"
              className="block bg-gradient-to-r from-setu-saffron to-[#FF8533] rounded-2xl p-5 text-white shadow-md hover:shadow-lg hover:shadow-orange-500/20 transition-all group"
            >
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-xl bg-white/20 flex items-center justify-center">
                  <Sparkles className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="font-bold text-sm">Need Help Finding a Scheme?</h4>
                  <p className="text-xs text-white/80 mt-0.5">Ask SETU AI Assistant →</p>
                </div>
              </div>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

// ─── Portal Card Component ───────────────────────────────────────────
const PortalCard: React.FC<{ portal: GovPortal; onShare: (title: string, url: string) => void }> = ({
  portal,
  onShare,
}) => {
  const catColor = getCatColor(portal.category);

  return (
    <div className="bg-white rounded-2xl border border-slate-200 hover:border-setu-blue/30 hover:shadow-lg hover:shadow-blue-500/5 transition-all duration-300 overflow-hidden group">
      <div className="p-5 space-y-3">
        {/* Header */}
        <div className="flex items-start justify-between">
          <div className="flex items-center space-x-2.5">
            <div className={`w-10 h-10 rounded-xl flex items-center justify-center text-xs font-black ${catColor.bg} ${catColor.text} border ${catColor.border}`}>
              {portal.logo_text.substring(0, 2).toUpperCase()}
            </div>
            <div>
              <h4 className="text-sm font-bold text-slate-900 group-hover:text-setu-blue transition-colors leading-tight">
                {portal.name}
              </h4>
              <span className={`text-[10px] font-semibold uppercase tracking-wider ${catColor.text}`}>
                {portal.category}
              </span>
            </div>
          </div>
          {portal.is_primary && (
            <span className="text-[10px] font-bold text-setu-saffron bg-setu-saffron/10 border border-setu-saffron/20 px-2 py-0.5 rounded-full">
              ★ Flagship
            </span>
          )}
        </div>

        {/* Description */}
        <p className="text-xs text-slate-600 leading-relaxed line-clamp-2">
          {portal.description}
        </p>

        {/* Features */}
        <div className="flex flex-wrap gap-1.5">
          {portal.features.map((feat, i) => (
            <span
              key={i}
              className="text-[10px] font-medium bg-slate-50 text-slate-600 px-2 py-0.5 rounded-md border border-slate-200"
            >
              {feat}
            </span>
          ))}
        </div>

        {/* Ministry */}
        <div className="flex items-center space-x-1.5 text-[10px] text-slate-400">
          <Building2 className="w-3 h-3" />
          <span className="truncate">{portal.ministry}</span>
        </div>

        {/* Actions */}
        <div className="flex items-center gap-2 pt-1.5 border-t border-slate-100">
          {portal.apply_url ? (
            <a
              href={portal.apply_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-1.5 bg-setu-saffron hover:bg-setu-saffron-dark text-white font-bold text-[11px] px-3.5 py-2 rounded-lg shadow-sm transition-all"
            >
              <Zap className="w-3.5 h-3.5" />
              <span>Apply / Register</span>
            </a>
          ) : null}
          <a
            href={portal.url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center space-x-1.5 bg-white hover:bg-slate-50 text-slate-700 font-semibold text-[11px] px-3.5 py-2 rounded-lg border border-slate-200 transition-all"
          >
            <Globe className="w-3.5 h-3.5 text-setu-blue" />
            <span>Visit Portal</span>
          </a>
          <button
            onClick={() => onShare(portal.name, portal.apply_url || portal.url)}
            className="ml-auto p-1.5 rounded-lg text-slate-400 hover:text-setu-blue hover:bg-blue-50 transition-colors"
          >
            <Share2 className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
};
