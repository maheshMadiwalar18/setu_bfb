import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, X, Globe, Radio, Play } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { SUPPORTED_LANGUAGES } from '../../i18n/config';

interface VoiceAssistantModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (transcript: string) => void;
}

export const VoiceAssistantModal: React.FC<VoiceAssistantModalProps> = ({
  isOpen,
  onClose,
  onSubmit
}) => {
  const { i18n } = useTranslation();
  const [isRecording, setIsRecording] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [interimTranscript, setInterimTranscript] = useState('');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [selectedLang, setSelectedLang] = useState(i18n.language);
  
  const recognitionRef = useRef<any>(null);

  useEffect(() => {
    setSelectedLang(i18n.language);
  }, [i18n.language]);

  useEffect(() => {
    if (!isOpen) {
      stopRecording();
      setTranscript('');
      setInterimTranscript('');
      setErrorMessage(null);
      return;
    }

    startRecording();

    return () => stopRecording();
  }, [isOpen, selectedLang]);

  const startRecording = async () => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setErrorMessage("Speech recognition not supported in this browser.");
      return;
    }

    try {
      if (recognitionRef.current) {
        recognitionRef.current.abort();
      }

      const recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      
      const currentLangConfig = SUPPORTED_LANGUAGES.find(l => l.code === selectedLang) || SUPPORTED_LANGUAGES[0];
      recognition.lang = currentLangConfig.speechCode || 'en-IN';

      recognition.onstart = () => {
        setIsRecording(true);
        setErrorMessage(null);
      };

      recognition.onresult = (event: any) => {
        let currentInterim = '';
        let currentFinal = '';

        for (let i = event.resultIndex; i < event.results.length; ++i) {
          const trans = event.results[i][0].transcript;
          if (event.results[i].isFinal) {
            currentFinal += trans + ' ';
          } else {
            currentInterim += trans;
          }
        }
        
        if (currentFinal) {
          setTranscript(prev => prev + currentFinal);
        }
        setInterimTranscript(currentInterim);
      };

      recognition.onerror = (event: any) => {
        if (event.error !== 'no-speech') {
          setErrorMessage(`Mic error: ${event.error}`);
          setIsRecording(false);
        }
      };

      recognition.onend = () => {
        setIsRecording(false);
      };

      recognitionRef.current = recognition;
      recognition.start();
    } catch (err) {
      setErrorMessage("Failed to start voice recognition.");
    }
  };

  const stopRecording = () => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
    }
    setIsRecording(false);
  };

  const handleSubmit = () => {
    const finalResult = (transcript + interimTranscript).trim();
    if (finalResult) {
      onSubmit(finalResult);
      onClose();
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-end sm:items-center justify-center bg-slate-900/50 backdrop-blur-sm transition-opacity">
      <div className="w-full max-w-md bg-white rounded-t-2xl sm:rounded-2xl shadow-2xl overflow-hidden flex flex-col transform transition-all">
        {/* Header */}
        <div className="bg-[#1A3A6B] text-white p-4 flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Globe className="w-5 h-5 text-setu-saffron" />
            <h3 className="font-bold text-lg">Voice Assistant</h3>
          </div>
          <button onClick={onClose} className="p-1 hover:bg-white/20 rounded-full transition-colors">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 flex flex-col items-center space-y-6">
          {/* Language Selector */}
          <div className="flex items-center space-x-2">
            <span className="text-sm font-medium text-slate-500">Speaking in:</span>
            <select 
              value={selectedLang}
              onChange={(e) => {
                setSelectedLang(e.target.value);
                setTranscript('');
                setInterimTranscript('');
              }}
              className="bg-slate-100 border border-slate-300 text-slate-700 text-sm rounded-lg focus:ring-[#00875A] focus:border-[#00875A] block p-2"
            >
              {SUPPORTED_LANGUAGES.map(lang => (
                <option key={lang.code} value={lang.code}>{lang.native} ({lang.name})</option>
              ))}
            </select>
          </div>

          {/* Transcript Display */}
          <div className="w-full bg-slate-50 rounded-xl p-4 min-h-[120px] max-h-[200px] overflow-y-auto border border-slate-200 shadow-inner">
            <p className="text-lg text-slate-800 font-medium">
              {transcript}
              <span className="text-slate-400">{interimTranscript}</span>
              {!transcript && !interimTranscript && !isRecording && (
                <span className="text-slate-400 italic">Tap the microphone to start speaking...</span>
              )}
            </p>
          </div>

          {/* Mic Button */}
          <div className="flex flex-col items-center">
            <button
              onClick={isRecording ? stopRecording : startRecording}
              className={`relative flex items-center justify-center rounded-full transition-all focus:outline-hidden w-20 h-20 ${
                isRecording
                  ? 'bg-red-600 hover:bg-red-700 text-white animate-pulse shadow-lg ring-4 ring-red-400'
                  : 'bg-[#00875A] hover:bg-[#00704A] text-white shadow-lg ring-4 ring-emerald-100'
              }`}
            >
              {isRecording ? <Mic className="w-10 h-10 animate-bounce" /> : <Mic className="w-10 h-10" />}
            </button>
            <div className="mt-4 flex items-center space-x-2 text-sm font-bold text-slate-600">
              {isRecording ? (
                <>
                  <Radio className="w-4 h-4 text-red-600 animate-pulse" />
                  <span className="text-red-600">Listening...</span>
                </>
              ) : (
                <span>Microphone off</span>
              )}
            </div>
            {errorMessage && <p className="text-red-500 text-xs mt-2">{errorMessage}</p>}
          </div>
        </div>

        {/* Footer */}
        <div className="bg-slate-50 p-4 border-t border-slate-200 flex justify-end space-x-3">
          <button
            onClick={onClose}
            className="px-4 py-2 text-slate-600 font-semibold hover:bg-slate-200 rounded-lg transition-colors"
          >
            Cancel
          </button>
          <button
            onClick={handleSubmit}
            disabled={!transcript && !interimTranscript}
            className="px-6 py-2 bg-[#00875A] text-white font-bold rounded-lg hover:bg-[#00704A] disabled:opacity-50 disabled:cursor-not-allowed shadow-sm transition-colors"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  );
};
