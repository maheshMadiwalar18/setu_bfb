import React, { useState, useEffect } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { 
  ArrowLeft, ArrowRight, User, MapPin, Briefcase, IndianRupee,
  GraduationCap, CheckCircle2, FileText, Check, Award, Search, HandCoins, Building
} from 'lucide-react';

type Step = 'questions' | 'loading' | 'results';

export const LifeEventPage: React.FC = () => {
  const [searchParams] = useSearchParams();
  const event = searchParams.get('event') || 'Going to College';
  const navigate = useNavigate();

  const [step, setStep] = useState<Step>('questions');
  const [formData, setFormData] = useState({
    state: '',
    age: '',
    gender: '',
    income: '',
    category: '',
    occupation: ''
  });
  const [schemes, setSchemes] = useState<any[]>([]);
  const [docList, setDocList] = useState<string[]>([]);

  const handleNext = async () => {
    setStep('loading');
    
    // Map income string to float
    let incomeFloat = 0;
    if (formData.income === '< 2L') incomeFloat = 150000;
    if (formData.income === '2L-5L') incomeFloat = 300000;
    if (formData.income === '> 5L') incomeFloat = 600000;

    // Map event to backend keyword
    let mappedNeed = event;
    const lowerEvent = event.toLowerCase();
    if (lowerEvent.includes('college')) mappedNeed = 'education';
    else if (lowerEvent.includes('business')) mappedNeed = 'business';
    else if (lowerEvent.includes('child')) mappedNeed = 'maternity';
    else if (lowerEvent.includes('marriage')) mappedNeed = 'marriage';
    else if (lowerEvent.includes('house')) mappedNeed = 'housing';
    else if (lowerEvent.includes('retirement')) mappedNeed = 'pension';
    else if (lowerEvent.includes('farmer')) mappedNeed = 'agriculture';
    else if (lowerEvent.includes('job')) mappedNeed = 'job';

    try {
      const res = await fetch('/api/wizard/match', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          state: formData.state || null,
          age: parseInt(formData.age) || null,
          gender: formData.gender || 'any',
          income_annual: incomeFloat,
          caste_category: formData.category || 'general',
          needs: [mappedNeed]
        })
      });
      const data = await res.json();
      setSchemes(data.schemes || []);
      
      const docs = new Set<string>();
      docs.add('Aadhaar Card');
      if (data.schemes) {
        data.schemes.forEach((s: any) => {
           if (s.documents_required) {
             s.documents_required.forEach((d: string) => docs.add(d));
           }
        });
      }
      setDocList(Array.from(docs).slice(0, 5));
      
      setStep('results');
    } catch (err) {
      console.error(err);
      setSchemes([]);
      setStep('results');
    }
  };

  const renderQuestions = () => (
    <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-6 md:p-8 max-w-2xl mx-auto mt-8 animate-fade-in">
      <div className="mb-6 text-center">
        <h2 className="text-2xl font-extrabold text-[#1A3A6B]">Tell us more about yourself</h2>
        <p className="text-slate-500 mt-2">We need a few details to find the exact schemes and benefits for your situation: <strong>"{event}"</strong></p>
      </div>

      <div className="space-y-5">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-bold text-slate-700 mb-1">State of Residence</label>
            <div className="relative">
              <MapPin className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" />
              <select
                className="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#00875A] focus:border-[#00875A] outline-hidden bg-slate-50"
                value={formData.state}
                onChange={(e) => setFormData({ ...formData, state: e.target.value })}
              >
                <option value="">Select State</option>
                <option value="Karnataka">Karnataka</option>
                <option value="Maharashtra">Maharashtra</option>
                <option value="Delhi">Delhi</option>
              </select>
            </div>
          </div>
          <div>
            <label className="block text-sm font-bold text-slate-700 mb-1">Gender</label>
            <div className="relative">
              <User className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" />
              <select
                className="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#00875A] focus:border-[#00875A] outline-hidden bg-slate-50"
                value={formData.gender}
                onChange={(e) => setFormData({ ...formData, gender: e.target.value })}
              >
                <option value="">Select Gender</option>
                <option value="female">Female</option>
                <option value="male">Male</option>
                <option value="other">Other</option>
              </select>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-bold text-slate-700 mb-1">Age</label>
            <div className="relative">
              <User className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" />
              <input
                type="number"
                className="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#00875A] focus:border-[#00875A] outline-hidden bg-slate-50"
                placeholder="e.g. 18"
                value={formData.age}
                onChange={(e) => setFormData({ ...formData, age: e.target.value })}
              />
            </div>
          </div>
          <div>
            <label className="block text-sm font-bold text-slate-700 mb-1">Category</label>
            <div className="relative">
              <CheckCircle2 className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" />
              <select
                className="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#00875A] focus:border-[#00875A] outline-hidden bg-slate-50"
                value={formData.category}
                onChange={(e) => setFormData({ ...formData, category: e.target.value })}
              >
                <option value="">Select</option>
                <option value="General">General</option>
                <option value="OBC">OBC</option>
                <option value="SC/ST">SC/ST</option>
              </select>
            </div>
          </div>
        </div>

        <div>
          <label className="block text-sm font-bold text-slate-700 mb-1">Annual Family Income</label>
          <div className="relative">
            <IndianRupee className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" />
            <select
              className="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#00875A] focus:border-[#00875A] outline-hidden bg-slate-50"
              value={formData.income}
              onChange={(e) => setFormData({ ...formData, income: e.target.value })}
            >
              <option value="">Select Income Range</option>
              <option value="< 2L">Less than ₹2,000,000</option>
              <option value="2L-5L">₹2,000,000 - ₹5,000,000</option>
              <option value="> 5L">More than ₹5,000,000</option>
            </select>
          </div>
        </div>

        <div>
          <label className="block text-sm font-bold text-slate-700 mb-1">Current Occupation</label>
          <div className="relative">
            <Briefcase className="absolute left-3 top-2.5 w-5 h-5 text-slate-400" />
            <input
              type="text"
              className="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#00875A] focus:border-[#00875A] outline-hidden bg-slate-50"
              placeholder="e.g. Student"
              value={formData.occupation}
              onChange={(e) => setFormData({ ...formData, occupation: e.target.value })}
            />
          </div>
        </div>

        <div className="pt-4 flex justify-between">
          <button 
            onClick={() => navigate('/')} 
            className="px-6 py-2 rounded-lg font-bold text-slate-600 bg-slate-100 hover:bg-slate-200 transition-colors"
          >
            Cancel
          </button>
          <button 
            onClick={handleNext}
            className="px-6 py-2 flex items-center space-x-2 rounded-lg font-bold text-white bg-[#00875A] hover:bg-[#00704A] transition-colors"
            disabled={!formData.state || !formData.age}
          >
            <span>Analyze Eligibility</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );

  const renderLoading = () => (
    <div className="flex flex-col items-center justify-center py-20 animate-fade-in">
      <div className="w-16 h-16 border-4 border-emerald-100 border-t-[#00875A] rounded-full animate-spin mb-6"></div>
      <h2 className="text-xl font-bold text-[#1A3A6B] mb-2">Analyzing your life event...</h2>
      <p className="text-slate-500 text-center max-w-sm">
        Our AI is checking thousands of government schemes to build your personalized roadmap.
      </p>
    </div>
  );

  const renderResults = () => (
    <div className="max-w-6xl mx-auto mt-6 space-y-8 animate-fade-in">
      {/* Header Summary */}
      <div className="bg-gradient-to-r from-[#1A3A6B] to-[#0B2545] rounded-2xl p-8 text-white shadow-lg relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex justify-between items-center">
          <div>
            <div className="flex items-center space-x-2 mb-2 text-emerald-300 font-bold text-sm">
              <CheckCircle2 className="w-4 h-4" />
              <span>Personalized Journey Generated</span>
            </div>
            <h1 className="text-3xl font-extrabold mb-2">Your Roadmap for: {event}</h1>
            <p className="text-slate-300 max-w-2xl">Based on your profile, we have identified relevant scholarships, financial aid, and a step-by-step process for you to follow.</p>
          </div>
          <GraduationCap className="w-24 h-24 text-white/20 hidden md:block" />
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Col: Scheme Recommendations */}
        <div className="lg:col-span-2 space-y-6">
          <h2 className="text-xl font-extrabold text-slate-800 border-b border-slate-200 pb-2">Eligible Programs & Benefits</h2>
          
          {schemes.slice(0, 3).map((scheme, idx) => (
            <div key={idx} className="bg-white p-5 rounded-xl border border-slate-200 shadow-xs hover:border-[#00875A] transition-all group">
              <div className="flex items-start justify-between">
                <div className="flex space-x-4">
                  <div className="w-12 h-12 bg-emerald-50 text-[#00875A] rounded-lg flex items-center justify-center shrink-0">
                    <Award className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="font-bold text-lg text-slate-900 group-hover:text-[#00875A] transition-colors">{scheme.name}</h3>
                    <p className="text-sm text-slate-500 mb-2">{scheme.ministry}</p>
                    {scheme.highlights && scheme.highlights.length > 0 && (
                      <div className="flex flex-wrap gap-2 mb-3">
                        {scheme.highlights.slice(0, 2).map((h: string, i: number) => (
                          <span key={i} className="bg-emerald-50 text-[#00875A] text-xs font-bold px-2.5 py-1 rounded">{h}</span>
                        ))}
                      </div>
                    )}
                    <p className="text-sm text-slate-700 leading-relaxed">{scheme.summary}</p>
                  </div>
                </div>
              </div>
              <div className="mt-4 pt-4 border-t border-slate-100 flex justify-end">
                <button onClick={() => navigate(`/schemes/${scheme.id}`)} className="text-sm font-bold text-[#00875A] hover:underline flex items-center">
                  View details <ArrowRight className="w-4 h-4 ml-1" />
                </button>
              </div>
            </div>
          ))}

          {schemes.length === 0 && (
            <div className="p-8 text-center bg-slate-50 rounded-xl border border-slate-200">
              <p className="text-slate-500">No specific schemes found. Try adjusting your profile.</p>
            </div>
          )}
        </div>

        {/* Right Col: Visual Roadmap */}
        <div className="lg:col-span-1 space-y-6">
          <h2 className="text-xl font-extrabold text-slate-800 border-b border-slate-200 pb-2">Your Action Roadmap</h2>
          <div className="bg-white rounded-xl shadow-xs border border-slate-200 p-6 relative">
            <div className="absolute left-9 top-10 bottom-10 w-0.5 bg-slate-200" />
            
            <div className="space-y-6 relative">
              <div className="flex items-start space-x-4">
                <div className="w-6 h-6 rounded-full bg-[#00875A] text-white flex items-center justify-center z-10 shrink-0 mt-0.5 shadow-[0_0_0_4px_white]">
                  <Check className="w-3.5 h-3.5" />
                </div>
                <div>
                  <h4 className="font-bold text-sm text-slate-900">Eligibility Check</h4>
                  <p className="text-xs text-slate-500 mt-1">Completed! You are eligible for {schemes.length} programs.</p>
                </div>
              </div>

              <div className="flex items-start space-x-4">
                <div className="w-6 h-6 rounded-full bg-amber-500 text-white flex items-center justify-center z-10 shrink-0 mt-0.5 shadow-[0_0_0_4px_white] animate-pulse">
                  <FileText className="w-3 h-3" />
                </div>
                <div>
                  <h4 className="font-bold text-sm text-slate-900">Document Collection</h4>
                  <p className="text-xs text-slate-500 mt-1 mb-2">Prepare the required documents:</p>
                  <ul className="text-xs text-slate-600 space-y-1 list-disc pl-4">
                    {docList.map((doc, idx) => (
                      <li key={idx}>{doc}</li>
                    ))}
                    {docList.length === 0 && <li>Aadhaar Card</li>}
                  </ul>
                </div>
              </div>

              <div className="flex items-start space-x-4">
                <div className="w-6 h-6 rounded-full bg-slate-200 text-slate-400 flex items-center justify-center z-10 shrink-0 mt-0.5 shadow-[0_0_0_4px_white]">
                  <Search className="w-3 h-3" />
                </div>
                <div>
                  <h4 className="font-bold text-sm text-slate-400">Application Submission</h4>
                  <p className="text-xs text-slate-400 mt-1">Apply on NSP Portal</p>
                </div>
              </div>

              <div className="flex items-start space-x-4">
                <div className="w-6 h-6 rounded-full bg-slate-200 text-slate-400 flex items-center justify-center z-10 shrink-0 mt-0.5 shadow-[0_0_0_4px_white]">
                  <CheckCircle2 className="w-3 h-3" />
                </div>
                <div>
                  <h4 className="font-bold text-sm text-slate-400">Verification</h4>
                  <p className="text-xs text-slate-400 mt-1">Institute & State level</p>
                </div>
              </div>

              <div className="flex items-start space-x-4">
                <div className="w-6 h-6 rounded-full bg-slate-200 text-slate-400 flex items-center justify-center z-10 shrink-0 mt-0.5 shadow-[0_0_0_4px_white]">
                  <HandCoins className="w-3 h-3" />
                </div>
                <div>
                  <h4 className="font-bold text-sm text-slate-400">Benefit Received</h4>
                  <p className="text-xs text-slate-400 mt-1">Direct Bank Transfer</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-[calc(100vh-100px)] bg-slate-50/50 py-8 px-4 sm:px-6 lg:px-8">
      <button 
        onClick={() => navigate(-1)}
        className="flex items-center space-x-1 text-sm font-bold text-slate-500 hover:text-slate-800 transition-colors mb-4"
      >
        <ArrowLeft className="w-4 h-4" />
        <span>Back</span>
      </button>

      {step === 'questions' && renderQuestions()}
      {step === 'loading' && renderLoading()}
      {step === 'results' && renderResults()}
    </div>
  );
};
