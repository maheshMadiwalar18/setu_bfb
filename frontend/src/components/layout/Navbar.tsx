import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { Layers, MapPin, Building2, Compass, MessageSquareCode, Sparkles, Home } from 'lucide-react';

export const Navbar: React.FC = () => {
  const { t } = useTranslation();
  const location = useLocation();

  return (
    <nav className="bg-[#0B2545] text-white sticky top-[61px] z-40 shadow-xs no-print">
      <div className="max-w-7xl mx-auto px-4 lg:px-8 flex items-center justify-between">
        {/* Navigation Tabs */}
        <div className="flex items-center space-x-1 sm:space-x-3 overflow-x-auto py-1.5 text-xs sm:text-sm font-medium scrollbar-none">
          <NavLink
            to="/"
            end
            className={({ isActive }) =>
              `flex items-center space-x-1.5 px-3 py-1.5 rounded-md transition-all whitespace-nowrap ${
                isActive
                  ? 'bg-white/15 text-white font-bold'
                  : 'text-slate-200 hover:text-white hover:bg-white/10'
              }`
            }
          >
            <Home className="w-3.5 h-3.5 text-emerald-400" />
            <span>Home</span>
          </NavLink>

          <NavLink
            to="/schemes"
            className={({ isActive }) =>
              `flex items-center space-x-1.5 px-3 py-1.5 rounded-md transition-all whitespace-nowrap ${
                isActive
                  ? 'bg-white/15 text-white font-bold'
                  : 'text-slate-200 hover:text-white hover:bg-white/10'
              }`
            }
          >
            <Layers className="w-3.5 h-3.5 text-emerald-400" />
            <span>Categories</span>
          </NavLink>

          <a
            href="/#states"
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-md text-slate-200 hover:text-white hover:bg-white/10 transition-all whitespace-nowrap"
          >
            <MapPin className="w-3.5 h-3.5 text-emerald-400" />
            <span>States/UTs</span>
          </a>

          <NavLink
            to="/schemes?type=central"
            className="flex items-center space-x-1.5 px-3 py-1.5 rounded-md text-slate-200 hover:text-white hover:bg-white/10 transition-all whitespace-nowrap"
          >
            <Building2 className="w-3.5 h-3.5 text-emerald-400" />
            <span>Central Ministries</span>
          </NavLink>

          <NavLink
            to="/find"
            className={({ isActive }) =>
              `flex items-center space-x-1.5 px-3 py-1.5 rounded-md transition-all whitespace-nowrap ${
                isActive
                  ? 'bg-white/15 text-white font-bold'
                  : 'text-slate-200 hover:text-white hover:bg-white/10'
              }`
            }
          >
            <Compass className="w-3.5 h-3.5 text-amber-400" />
            <span>Find Schemes for You</span>
          </NavLink>
        </div>

        {/* Right side AI Assistant */}
        <div className="py-1.5 flex items-center space-x-2">
          <NavLink
            to="/chat"
            className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-full font-bold text-xs transition-all shadow-xs ${
              location.pathname === '/chat'
                ? 'bg-[#00875A] text-white'
                : 'bg-emerald-700/50 hover:bg-[#00875A] text-white border border-emerald-500/40'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5 text-amber-300 animate-pulse" />
            <span className="hidden sm:inline">SETU AI Assistant</span>
            <span className="sm:hidden">AI</span>
          </NavLink>
        </div>
      </div>
    </nav>
  );
};
