import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { Home, Compass, Layers, MapPin, Building2, Info, MessageSquareCode } from 'lucide-react';

export const Navbar: React.FC = () => {
  const { t } = useTranslation();
  const location = useLocation();

  const navLinks = [
    { to: '/', label: t('nav.home'), icon: Home },
    { to: '/find', label: t('nav.findScheme'), icon: Compass },
    { to: '/schemes', label: t('nav.allSchemes'), icon: Layers },
    { to: '/csc', label: t('nav.cscPortal'), icon: Building2 },
    { to: '/about', label: t('nav.about'), icon: Info },
  ];

  return (
    <nav className="bg-setu-blue text-white sticky top-0 z-40 shadow-md no-print border-b border-setu-blue-dark">
      <div className="max-w-7xl mx-auto px-4 lg:px-8 flex items-center justify-between">
        {/* Navigation Items */}
        <div className="flex items-center space-x-1 sm:space-x-2 overflow-x-auto py-0 text-sm font-medium">
          {navLinks.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.to;
            return (
              <NavLink
                key={item.to}
                to={item.to}
                className={`flex items-center space-x-2 px-3.5 py-3.5 border-b-[3px] transition-all whitespace-nowrap ${
                  isActive
                    ? 'border-setu-saffron text-white font-bold bg-white/5'
                    : 'border-transparent text-slate-200 hover:text-white hover:border-slate-400 hover:bg-white/5'
                }`}
              >
                <Icon className={`w-4 h-4 ${isActive ? 'text-setu-saffron' : 'text-slate-300'}`} />
                <span>{item.label}</span>
              </NavLink>
            );
          })}
        </div>

        {/* SETU AI Chat Live Trigger Button */}
        <div className="py-2">
          <NavLink
            to="/chat"
            className={`flex items-center space-x-2 px-4 py-2 rounded-full font-semibold text-xs transition-all shadow-sm ${
              location.pathname === '/chat'
                ? 'bg-setu-saffron text-white ring-2 ring-white/40'
                : 'bg-white/10 hover:bg-setu-saffron text-white border border-white/20'
            }`}
          >
            <MessageSquareCode className="w-4 h-4 text-setu-saffron group-hover:text-white" />
            <span className="hidden sm:inline">SETU AI Assistant</span>
            <span className="sm:hidden">AI Chat</span>
          </NavLink>
        </div>
      </div>
    </nav>
  );
};
