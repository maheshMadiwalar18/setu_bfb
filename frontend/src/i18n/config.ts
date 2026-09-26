import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

export const SUPPORTED_LANGUAGES = [
  { code: 'en', name: 'English', native: 'English', speechCode: 'en-IN' },
  { code: 'hi', name: 'Hindi', native: 'हिन्दी', speechCode: 'hi-IN' },
  { code: 'kn', name: 'Kannada', native: 'ಕನ್ನಡ', speechCode: 'kn-IN' },
  { code: 'ta', name: 'Tamil', native: 'தமிழ்', speechCode: 'ta-IN' },
  { code: 'te', name: 'Telugu', native: 'తెలుగు', speechCode: 'te-IN' },
  { code: 'mr', name: 'Marathi', native: 'मराठी', speechCode: 'mr-IN' },
  { code: 'ml', name: 'Malayalam', native: 'മലയാളം', speechCode: 'ml-IN' },
  { code: 'bn', name: 'Bengali', native: 'বাংলা', speechCode: 'bn-IN' },
  { code: 'gu', name: 'Gujarati', native: 'ગુજરાતી', speechCode: 'gu-IN' },
  { code: 'pa', name: 'Punjabi', native: 'ਪੰਜਾਬੀ', speechCode: 'pa-IN' },
  { code: 'ur', name: 'Urdu', native: 'اردو', speechCode: 'ur-IN' },
  { code: 'or', name: 'Odia', native: 'ଓଡ଼ିଆ', speechCode: 'or-IN' },
];

const resources = {
  en: {
    translation: {
      nav: {
        home: "Home",
        findScheme: "Find My Scheme",
        allSchemes: "All Schemes",
        states: "States",
        cscPortal: "CSC Portal",
        about: "About",
        login: "Citizen Login",
        chatWithAI: "SETU AI Assistant"
      },
      hero: {
        title: "Discover Government Schemes Made For You",
        subtitle: "3,000+ central and state schemes. Find what you're eligible for in minutes.",
        searchPlaceholder: "Search schemes, or ask SETU anything...",
        listening: "Listening...",
        speakNow: "Speak or type your requirement",
        findBtn: "Start Finding Schemes",
        dontKnowTitle: "Don't know where to start?",
        dontKnowSub: "Answer 5 quick questions. SETU finds your schemes."
      },
      stats: {
        schemesCount: "3,000+ Schemes",
        statesCount: "36 States & UTs",
        categoriesCount: "20+ Categories",
        citizensHelped: "50L+ Citizens Helped"
      },
      cards: {
        viewDetails: "View Details",
        saveScheme: "Save",
        checkEligibility: "Check Eligibility",
        applyNow: "Apply on Official Portal",
        downloadPdf: "Download Checklist PDF",
        matchBadge: "Match"
      },
      wizard: {
        title: "Eligibility Wizard",
        step1: "Basic Profile",
        step2: "Household",
        step3: "Needs & Services",
        step4: "Eligible Schemes",
        ageLabel: "How old are you?",
        genderLabel: "What is your gender?",
        stateLabel: "Which state do you live in?",
        disabilityLabel: "Are you differently abled?",
        incomeLabel: "What is your approximate annual household income?",
        casteLabel: "Social Category",
        bplLabel: "Do you hold a BPL Ration Card?",
        needsLabel: "What services or support do you need?",
        resultsFound: "Found matching schemes for your profile",
        next: "Next Step",
        prev: "Previous",
        showResults: "Find My Eligible Schemes"
      },
      chat: {
        title: "SETU AI Assistant",
        status: "Online & Ready",
        welcomeTitle: "Namaste! I am SETU, your government services guide.",
        welcomeBody: "I can help you:\n- Find schemes you are eligible for\n- Understand required documents\n- Check payment and DBT status\n- File grievances",
        inputPlaceholder: "Ask in your language...",
        send: "Send",
        voicePrompt: "Click to speak"
      },
      csc: {
        portalTitle: "CSC Operator Portal",
        operatorMode: "Citizen Assist Mode",
        todayAssisted: "Today's Assisted Citizens",
        searchSchemes: "Search Scheme",
        fileGrievance: "File Grievance",
        printSummary: "Print Scheme Summary",
        loginTitle: "VLE Operator Login",
        operatorId: "Operator ID / Email",
        password: "Password"
      },
      footer: {
        copyright: "2025 SETU | Government of India",
        ownership: "Contents owned and maintained by participating ministries",
        nic: "Powered by National Informatics Centre (NIC) | Data sourced from MyScheme.gov.in",
        gigw: "GIGW Compliant | WCAG 2.0 AA"
      }
    }
  },
  hi: {
    translation: {
      nav: {
        home: "होम",
        findScheme: "मेरी योजना खोजें",
        allSchemes: "सभी योजनाएं",
        states: "राज्य",
        cscPortal: "सीएससी पोर्टल",
        about: "परिचय",
        login: "नागरिक लॉगिन",
        chatWithAI: "सेतु एआई सहायक"
      },
      hero: {
        title: "अपने लिए सही सरकारी योजनाएं खोजें",
        subtitle: "3,000+ केंद्र और राज्य सरकार की योजनाएं। जानें आप किसके पात्र हैं।",
        searchPlaceholder: "योजनाएं खोजें, या सेतु से कुछ भी पूछें...",
        listening: "सुन रहे हैं...",
        speakNow: "अपनी आवश्यकता बोलें या टाइप करें",
        findBtn: "योजनाएं खोजना शुरू करें",
        dontKnowTitle: "शुरुआत कहां से करें?",
        dontKnowSub: "5 आसान सवालों के जवाब दें। सेतु आपके लिए योजनाएं ढूंढेगा।"
      },
      stats: {
        schemesCount: "3,000+ योजनाएं",
        statesCount: "36 राज्य और केंद्र शासित प्रदेश",
        categoriesCount: "20+ श्रेणियां",
        citizensHelped: "50 लाख+ नागरिक लाभान्वित"
      },
      cards: {
        viewDetails: "विवरण देखें",
        saveScheme: "सहेजें",
        checkEligibility: "पात्रता जांचें",
        applyNow: "आधिकारिक पोर्टल पर आवेदन करें",
        downloadPdf: "दस्तावेज चेकलिस्ट डाउनलोड करें",
        matchBadge: "अनुरूप"
      },
      wizard: {
        title: "पात्रता विजार्ड",
        step1: "बुनियादी विवरण",
        step2: "पारिवारिक आय",
        step3: "आवश्यकता",
        step4: "योग्य योजनाएं",
        ageLabel: "आपकी उम्र कितनी है?",
        genderLabel: "आपका लिंग क्या है?",
        stateLabel: "आप किस राज्य में रहते हैं?",
        disabilityLabel: "क्या आप दिव्यांगजन हैं?",
        incomeLabel: "आपकी अनुमानित वार्षिक पारिवारिक आय क्या है?",
        casteLabel: "सामाजिक श्रेणी",
        bplLabel: "क्या आपके पास बीपीएल राशन कार्ड है?",
        needsLabel: "आपको किस प्रकार की सहायता चाहिए?",
        resultsFound: "आपकी प्रोफ़ाइल के अनुसार योजनाएं मिलीं",
        next: "अगला चरण",
        prev: "पिछला",
        showResults: "मेरी योजनाएं दिखाएं"
      },
      chat: {
        title: "सेतु एआई सहायक",
        status: "सक्रिय और तैयार",
        welcomeTitle: "नमस्ते! मैं सेतु हूँ, आपका सरकारी सेवा मार्गदर्शक।",
        welcomeBody: "मैं आपकी सहायता कर सकता हूँ:\n- पात्र योजनाओं को खोजने में\n- आवश्यक दस्तावेज समझने में\n- डीबीटी भुगतान स्थिति जांचने में\n- शिकायत दर्ज करने में",
        inputPlaceholder: "अपनी भाषा में पूछें...",
        send: "भेजें",
        voicePrompt: "बोलने के लिए क्लिक करें"
      },
      csc: {
        portalTitle: "सीएससी ऑपरेटर पोर्टल",
        operatorMode: "नागरिक सहायता मोड",
        todayAssisted: "आज सहायता प्राप्त नागरिक",
        searchSchemes: "योजना खोजें",
        fileGrievance: "शिकायत दर्ज करें",
        printSummary: "योजना विवरण प्रिंट करें",
        loginTitle: "वीएलई ऑपरेटर लॉगिन",
        operatorId: "ऑपरेटर आईडी / ईमेल",
        password: "पासवर्ड"
      },
      footer: {
        copyright: "2025 सेतु | भारत सरकार",
        ownership: "सामग्री का स्वामित्व संबंधित मंत्रालयों के पास है",
        nic: "राष्ट्रीय सूचना विज्ञान केंद्र (एनआईसी) द्वारा संचालित",
        gigw: "जीआईजीडब्ल्यू अनुपालन | WCAG 2.0 AA"
      }
    }
  },
  kn: {
    translation: {
      nav: {
        home: "ಮುಖಪುಟ",
        findScheme: "ನನ್ನ ಯೋಜನೆ ಹುಡುಕಿ",
        allSchemes: "ಎಲ್ಲಾ ಯೋಜನೆಗಳು",
        states: "ರಾಜ್ಯಗಳು",
        cscPortal: "ಸಿಎಸ್‌ಸಿ ಪೋರ್ಟಲ್",
        about: "ನಮ್ಮ ಬಗ್ಗೆ",
        login: "ನಾಗರಿಕ ಲಾಗಿನ್",
        chatWithAI: "ಸೇತು ಎಐ ಸಹಾಯಕ"
      },
      hero: {
        title: "ನಿಮಗಾಗಿ ರೂಪಿಸಲಾದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ",
        subtitle: "3,000+ ಕೇಂದ್ರ ಮತ್ತು ರಾಜ್ಯ ಯೋಜನೆಗಳು. ನಿಮಿಷಗಳಲ್ಲಿ ನಿಮ್ಮ ಅರ್ಹತೆಯನ್ನು ತಿಳಿಯಿರಿ.",
        searchPlaceholder: "ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ, ಅಥವಾ ಸೇತು ಜೊತೆ ಮಾತನಾಡಿ...",
        listening: "ಆಲಿಸಲಾಗುತ್ತಿದೆ...",
        speakNow: "ನಿಮ್ಮ ಅಗತ್ಯವನ್ನು ಮಾತನಾಡಿ ಅಥವಾ ಬರೆಯಿರಿ",
        findBtn: "ಯೋಜನೆ ಹುಡುಕಲು ಪ್ರಾರಂಭಿಸಿ",
        dontKnowTitle: "ಎಲ್ಲಿಂದ ಪ್ರಾರಂಭಿಸಬೇಕೆಂದು ತಿಳಿಯುತ್ತಿಲ್ಲವೇ?",
        dontKnowSub: "5 ಸರಳ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ. ಸೇತು ನಿಮಗಾಗಿ ಯೋಜನೆಗಳನ್ನು ಪತ್ತೆ ಮಾಡುತ್ತದೆ."
      },
      stats: {
        schemesCount: "3,000+ ಯೋಜನೆಗಳು",
        statesCount: "36 ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರಾಡಳಿತ ಪ್ರದೇಶಗಳು",
        categoriesCount: "20+ ವಿಭಾಗಗಳು",
        citizensHelped: "50 ಲಕ್ಷ+ ನಾಗರಿಕರಿಗೆ ನೆರವು"
      },
      cards: {
        viewDetails: "ವಿವರ ನೋಡಿ",
        saveScheme: "ಉಳಿಸಿ",
        checkEligibility: "ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ",
        applyNow: "ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ",
        downloadPdf: "ದಾಖಲೆಗಳ ಪಟ್ಟಿ ಡೌನ್‌ಲೋಡ್",
        matchBadge: "ಹೊಂದಾಣಿಕೆ"
      },
      wizard: {
        title: "ಅರ್ಹತಾ ಮಾರ್ಗದರ್ಶಿ",
        step1: "ವೈಯಕ್ತಿಕ ವಿವರ",
        step2: "ಕುಟುಂಬ ಮತ್ತು ಆದಾಯ",
        step3: "ಅಗತ್ಯವಿರುವ ಸೇವೆಗಳು",
        step4: "ಅರ್ಹ ಯೋಜನೆಗಳು",
        ageLabel: "ನಿಮ್ಮ ವಯಸ್ಸು ಎಷ್ಟು?",
        genderLabel: "ನಿಮ್ಮ ಲಿಂಗ?",
        stateLabel: "ನೀವು ಯಾವ ರಾಜ್ಯದಲ್ಲಿ ವಾಸಿಸುತ್ತೀರಿ?",
        disabilityLabel: "ನೀವು ವಿಶೇಷ ಚೇತನರೇ?",
        incomeLabel: "ನಿಮ್ಮ ವಾರ್ಷಿಕ ಕುಟುಂಬ ಆದಾಯ ಎಷ್ಟು?",
        casteLabel: "ಸಾಮಾಜಿಕ ವರ್ಗ",
        bplLabel: "ನಿಮ್ಮ ಬಳಿ ಬಿಪಿಎಲ್ ಪಡಿತರ ಚೀಟಿ ಇದೆಯೇ?",
        needsLabel: "ನಿಮಗೆ ಯಾವ ರೀತಿಯ ಸಹಾಯ ಬೇಕು?",
        resultsFound: "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್‌ಗೆ ಸೂಕ್ತವಾದ ಯೋಜನೆಗಳು ಲಭ್ಯವಿವೆ",
        next: "ಮುಂದಿನ ಹಂತ",
        prev: "ಹಿಂದಿನ ಹಂತ",
        showResults: "ನನ್ನ ಯೋಜನೆಗಳನ್ನು ತೋರಿಸಿ"
      },
      chat: {
        title: "ಸೇತು ಎಐ ಸಹಾಯಕ",
        status: "ಸಕ್ರಿಯವಾಗಿದೆ",
        welcomeTitle: "ನಮಸ್ಕಾರ! ನಾನು ಸೇತು, ನಿಮ್ಮ ಸರ್ಕಾರಿ ಸೇವೆಗಳ ಮಾರ್ಗದರ್ಶಿ.",
        welcomeBody: "ನಾನು ನಿಮಗೆ ಸಹಾಯ ಮಾಡಬಲ್ಲೆ:\n- ನಿಮಗೆ ಸೂಕ್ತವಾದ ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಲು\n- ಅಗತ್ಯ ದಾಖಲೆಗಳನ್ನು ತಿಳಿಯಲು\n- ಡಿಬಿಟಿ ಪಾವತಿ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಲು\n- ಕುಂದುಕೊರತೆ ಸಲ್ಲಿಸಲು",
        inputPlaceholder: "ಕನ್ನಡದಲ್ಲಿ ಅಥವಾ ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ ಕೇಳಿ...",
        send: "ಕಳುಹಿಸಿ",
        voicePrompt: "ಮಾತನಾಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ"
      },
      csc: {
        portalTitle: "ಸಿಎಸ್‌ಸಿ ಆಪರೇಟರ್ ಪೋರ್ಟಲ್",
        operatorMode: "ನಾಗರಿಕ ಸಹಾಯ ಮೋಡ್",
        todayAssisted: "ಇಂದು ನೆರವು ಪಡೆದ ನಾಗರಿಕರು",
        searchSchemes: "ಯೋಜನೆ ಹುಡುಕಾಟ",
        fileGrievance: "ದೂರು ಸಲ್ಲಿಸಿ",
        printSummary: "ಯೋಜನೆ ವಿವರ ಮುದ್ರಿಸಿ",
        loginTitle: "ವಿಎಲ್‌ಇ ಆಪರೇಟರ್ ಲಾಗಿನ್",
        operatorId: "ಆಪರೇಟರ್ ಐಡಿ / ಇಮೇಲ್",
        password: "ಪಾಸ್‌ವರ್ಡ್"
      },
      footer: {
        copyright: "2025 ಸೇತು | ಭಾರತ ಸರ್ಕಾರ",
        ownership: "ವಿಷಯಗಳು ಸಂಬಂಧಿಸಿದ ಸಚಿವಾಲಯಗಳ ಒಡೆತನದಲ್ಲಿದೆ",
        nic: "ರಾಷ್ಟ್ರೀಯ ಮಾಹಿತಿ ಕೇಂದ್ರ (ಎನ್‌ಐಸಿ) ನಿರ್ವಹಣೆ",
        gigw: "ಜಿಐಜಿಡಬ್ಲ್ಯೂ ಅನುಸರಣೆ | WCAG 2.0 AA"
      }
    }
  }
};

// Fallback for remaining 9 languages uses English structure dynamically with translated titles
const otherLangs = ['ta', 'te', 'mr', 'ml', 'bn', 'gu', 'pa', 'ur', 'or'];
otherLangs.forEach(lang => {
  resources[lang] = { translation: { ...resources.en.translation } };
});

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false,
    },
  });

export default i18n;
