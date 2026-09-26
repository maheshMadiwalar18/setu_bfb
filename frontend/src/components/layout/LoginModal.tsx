import React, { useState } from 'react';
import { X, Smartphone, ShieldCheck, ArrowRight, CheckCircle2 } from 'lucide-react';

interface LoginModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSuccess: (user: any) => void;
}

export const LoginModal: React.FC<LoginModalProps> = ({ isOpen, onClose, onSuccess }) => {
  const [phone, setPhone] = useState('');
  const [otp, setOtp] = useState('');
  const [step, setStep] = useState<'phone' | 'otp' | 'success'>('phone');
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const handleSendOtp = (e: React.FormEvent) => {
    e.preventDefault();
    if (phone.length < 10) return;
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      setStep('otp');
    }, 600);
  };

  const handleVerifyOtp = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      setStep('success');
      const user = {
        name: "Sunita Devi",
        phone: phone,
        aadhaar_last4: "4521",
        state: "Karnataka",
        isLoggedIn: true
      };
      setTimeout(() => {
        onSuccess(user);
        onClose();
        setStep('phone');
      }, 1000);
    }, 800);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-xs p-4 animate-fade-in no-print">
      <div className="bg-white rounded-xl shadow-2xl max-w-md w-full overflow-hidden border border-slate-200">
        {/* Modal Header */}
        <div className="bg-setu-blue text-white p-5 flex items-center justify-between border-b-2 border-setu-saffron">
          <div className="flex items-center space-x-2.5">
            <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center border border-white/20">
              <ShieldCheck className="w-5 h-5 text-setu-saffron" />
            </div>
            <div>
              <h3 className="font-bold text-base">Citizen Portal Login</h3>
              <p className="text-xs text-slate-300">National Single Sign-On (MeriPehchaan / OTP)</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-300 hover:text-white transition-colors p-1 rounded-md hover:bg-white/10"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6">
          {step === 'phone' && (
            <form onSubmit={handleSendOtp} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 uppercase tracking-wider mb-1.5">
                  Mobile Number (Aadhaar linked)
                </label>
                <div className="relative flex items-center">
                  <span className="absolute left-3 text-sm font-medium text-slate-500 border-r border-slate-300 pr-2">
                    +91
                  </span>
                  <input
                    type="tel"
                    maxLength={10}
                    required
                    value={phone}
                    onChange={(e) => setPhone(e.target.value.replace(/\D/g, ''))}
                    placeholder="Enter 10-digit mobile number"
                    className="w-full pl-14 pr-4 py-2.5 bg-slate-50 border border-slate-300 rounded-lg text-sm text-slate-900 focus:bg-white focus:border-setu-blue focus:ring-1 focus:ring-setu-blue transition-all"
                  />
                  <Smartphone className="absolute right-3 w-4 h-4 text-slate-400" />
                </div>
                <p className="text-[11px] text-slate-500 mt-1.5">
                  A 6-digit one-time password (OTP) will be sent to your number.
                </p>
              </div>

              <button
                type="submit"
                disabled={loading || phone.length < 10}
                className="w-full py-2.5 bg-setu-blue hover:bg-setu-blue-dark text-white rounded-lg font-semibold text-sm transition-colors flex items-center justify-center space-x-2 disabled:opacity-50"
              >
                <span>{loading ? 'Sending OTP...' : 'Get OTP'}</span>
                <ArrowRight className="w-4 h-4" />
              </button>

              <div className="pt-2 text-center text-[11px] text-slate-500">
                Protected by National Informatics Centre standard security protocols.
              </div>
            </form>
          )}

          {step === 'otp' && (
            <form onSubmit={handleVerifyOtp} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 uppercase tracking-wider mb-1.5">
                  Enter 6-Digit OTP
                </label>
                <input
                  type="text"
                  maxLength={6}
                  required
                  autoFocus
                  value={otp}
                  onChange={(e) => setOtp(e.target.value.replace(/\D/g, ''))}
                  placeholder="e.g. 123456 (Enter any 6 digits)"
                  className="w-full px-4 py-2.5 bg-slate-50 border border-slate-300 rounded-lg text-center tracking-widest text-lg font-bold text-slate-900 focus:bg-white focus:border-setu-blue focus:ring-1 focus:ring-setu-blue"
                />
                <div className="flex items-center justify-between text-xs text-slate-500 mt-2">
                  <span>Sent to +91 {phone}</span>
                  <button
                    type="button"
                    onClick={() => setStep('phone')}
                    className="text-setu-blue hover:underline font-medium"
                  >
                    Change Number
                  </button>
                </div>
              </div>

              <button
                type="submit"
                disabled={loading || otp.length < 4}
                className="w-full py-2.5 bg-setu-saffron hover:bg-setu-saffron-dark text-white rounded-lg font-semibold text-sm transition-colors flex items-center justify-center space-x-2 disabled:opacity-50"
              >
                <span>{loading ? 'Verifying...' : 'Verify & Proceed'}</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </form>
          )}

          {step === 'success' && (
            <div className="py-6 text-center space-y-3">
              <div className="w-12 h-12 bg-emerald-100 rounded-full flex items-center justify-center mx-auto text-setu-green">
                <CheckCircle2 className="w-8 h-8" />
              </div>
              <h4 className="font-bold text-slate-900 text-base">Authentication Successful</h4>
              <p className="text-xs text-slate-600">Welcome back, Sunita Devi. Redirecting to your dashboard...</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
