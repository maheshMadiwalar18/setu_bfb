import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck, ExternalLink, Globe, Landmark, Layers } from 'lucide-react';

export const Footer: React.FC = () => {
  const currentDate = "26 September 2025";

  return (
    <footer className="bg-[#12284C] text-slate-300 pt-12 pb-8 border-t-4 border-setu-saffron no-print">
      <div className="max-w-7xl mx-auto px-4 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 pb-10 border-b border-slate-700/60">
          {/* Col 1: Identity & Seal */}
          <div className="space-y-3 md:col-span-1">
            <div className="flex items-center space-x-2">
              <span className="font-extrabold text-xl tracking-tight text-white">SETU</span>
              <span className="text-slate-400 font-light">|</span>
              <span className="font-bold text-lg text-setu-saffron font-serif">सेतु</span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              National AI-Powered Government Schemes Discovery & Access Platform for Indian Citizens.
            </p>
            <div className="pt-2 flex items-center space-x-2 text-[11px] text-emerald-400 font-medium">
              <ShieldCheck className="w-4 h-4" />
              <span>GIGW Compliant | WCAG 2.0 AA Certified</span>
            </div>
          </div>

          {/* Col 2: Quick Links */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold uppercase tracking-wider text-white border-b border-slate-700 pb-1.5 inline-block">
              Portals & Services
            </h4>
            <ul className="space-y-1.5 text-xs text-slate-300">
              <li>
                <Link to="/find" className="hover:text-setu-saffron transition-colors">
                  Eligibility Wizard
                </Link>
              </li>
              <li>
                <Link to="/schemes" className="hover:text-setu-saffron transition-colors">
                  All Central & State Schemes
                </Link>
              </li>
              <li>
                <Link to="/chat" className="hover:text-setu-saffron transition-colors">
                  SETU AI Assistant (Multilingual)
                </Link>
              </li>
              <li>
                <Link to="/csc" className="hover:text-setu-saffron transition-colors">
                  CSC VLE Operator Portal
                </Link>
              </li>
            </ul>
          </div>

          {/* Col 3: National Initiatives */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold uppercase tracking-wider text-white border-b border-slate-700 pb-1.5 inline-block">
              Government Networks
            </h4>
            <ul className="space-y-1.5 text-xs text-slate-300">
              <li>
                <a
                  href="https://myscheme.gov.in"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center space-x-1 hover:text-setu-saffron transition-colors"
                >
                  <span>MyScheme National Portal</span>
                  <ExternalLink className="w-3 h-3 text-slate-400" />
                </a>
              </li>
              <li>
                <a
                  href="https://www.india.gov.in"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center space-x-1 hover:text-setu-saffron transition-colors"
                >
                  <span>National Portal of India</span>
                  <ExternalLink className="w-3 h-3 text-slate-400" />
                </a>
              </li>
              <li>
                <a
                  href="https://www.digilocker.gov.in"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center space-x-1 hover:text-setu-saffron transition-colors"
                >
                  <span>DigiLocker Verification</span>
                  <ExternalLink className="w-3 h-3 text-slate-400" />
                </a>
              </li>
              <li>
                <a
                  href="https://scholarships.gov.in"
                  target="_blank"
                  rel="noreferrer"
                  className="flex items-center space-x-1 hover:text-setu-saffron transition-colors"
                >
                  <span>National Scholarship Portal</span>
                  <ExternalLink className="w-3 h-3 text-slate-400" />
                </a>
              </li>
            </ul>
          </div>

          {/* Col 4: Authenticity & Tech Seal */}
          <div className="space-y-2">
            <h4 className="text-xs font-bold uppercase tracking-wider text-white border-b border-slate-700 pb-1.5 inline-block">
              Governance & Standards
            </h4>
            <div className="bg-slate-800/80 p-3 rounded-lg border border-slate-700 text-[11px] space-y-1 text-slate-300">
              <p className="font-semibold text-white flex items-center space-x-1.5">
                <Landmark className="w-3.5 h-3.5 text-setu-saffron" />
                <span>Ministry Coordination</span>
              </p>
              <p>Contents owned and maintained by participating Central & State Ministries.</p>
              <p className="pt-1 text-slate-400">Technical infrastructure hosted by NIC Data Centres.</p>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-6 flex flex-col md:flex-row items-center justify-between text-xs text-slate-400 space-y-3 md:space-y-0">
          <div>
            <p>(C) 2025 SETU | Government of India. All Rights Reserved.</p>
            <p className="text-[11px] text-slate-500">NIC coordination | Last updated: {currentDate}</p>
          </div>

          <div className="flex items-center space-x-5 text-xs">
            <Link to="/about" className="hover:text-white transition-colors">About SETU</Link>
            <a href="#privacy" className="hover:text-white transition-colors">Privacy Policy</a>
            <a href="#terms" className="hover:text-white transition-colors">Terms of Service</a>
            <a href="#accessibility" className="hover:text-white transition-colors">Accessibility Statement</a>
          </div>
        </div>
      </div>
    </footer>
  );
};
