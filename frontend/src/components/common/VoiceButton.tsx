import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Radio } from 'lucide-react';
import { useTranslation } from 'react-i18next';
import { SUPPORTED_LANGUAGES } from '../../i18n/config';

interface VoiceButtonProps {
  onTranscript: (text: string) => void;
  className?: string;
  size?: 'sm' | 'md' | 'lg';
}

export const VoiceButton: React.FC<VoiceButtonProps> = ({
  onTranscript,
  className = '',
  size = 'md'
}) => {
  const { i18n } = useTranslation();
  const [isRecording, setIsRecording] = useState(false);
  const [supported, setSupported] = useState(true);
  const recognitionRef = useRef<any>(null);
  const silenceTimerRef = useRef<any>(null);

  useEffect(() => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (!SpeechRecognition) {
      setSupported(false);
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;

    // Get speech language code according to current active language
    const currentLangConfig = SUPPORTED_LANGUAGES.find(l => l.code === i18n.language);
    recognition.lang = currentLangConfig?.speechCode || 'en-IN';

    recognition.onstart = () => {
      setIsRecording(true);
    };

    recognition.onresult = (event: any) => {
      clearTimeout(silenceTimerRef.current);
      let transcriptText = '';
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        transcriptText += event.results[i][0].transcript;
      }
      
      // Auto-stop after 2 seconds of silence once speech captured
      silenceTimerRef.current = setTimeout(() => {
        if (recognitionRef.current) {
          recognitionRef.current.stop();
        }
      }, 2000);

      if (event.results[0].isFinal) {
        onTranscript(transcriptText);
        setIsRecording(false);
      }
    };

    recognition.onerror = () => {
      setIsRecording(false);
    };

    recognition.onend = () => {
      setIsRecording(false);
    };

    recognitionRef.current = recognition;

    return () => {
      if (recognitionRef.current) {
        recognitionRef.current.abort();
      }
      clearTimeout(silenceTimerRef.current);
    };
  }, [i18n.language, onTranscript]);

  const toggleRecording = () => {
    if (!supported) {
      alert("Speech Recognition is not supported by your current browser. Please use Chrome, Edge, or Safari.");
      return;
    }

    if (isRecording) {
      recognitionRef.current?.stop();
      setIsRecording(false);
    } else {
      try {
        const currentLangConfig = SUPPORTED_LANGUAGES.find(l => l.code === i18n.language);
        if (recognitionRef.current) {
          recognitionRef.current.lang = currentLangConfig?.speechCode || 'en-IN';
          recognitionRef.current.start();
        }
      } catch (e) {
        console.error("Speech recognition error:", e);
      }
    }
  };

  const sizeClasses = {
    sm: 'w-8 h-8',
    md: 'w-10 h-10',
    lg: 'w-12 h-12',
  };

  return (
    <div className="relative inline-flex items-center">
      <button
        type="button"
        onClick={toggleRecording}
        className={`relative flex items-center justify-center rounded-full transition-all focus:outline-hidden ${sizeClasses[size]} ${
          isRecording
            ? 'bg-red-600 text-white animate-pulse-ring'
            : 'bg-setu-blue hover:bg-setu-blue-dark text-white shadow-xs'
        } ${className}`}
        title={isRecording ? 'Listening... Click to stop' : 'Voice Input (Speak in your language)'}
        aria-label="Voice input button"
      >
        {isRecording ? (
          <Mic className="w-5 h-5 animate-pulse" />
        ) : (
          <Mic className="w-5 h-5" />
        )}
      </button>

      {isRecording && (
        <span className="absolute -top-7 left-1/2 -translate-x-1/2 bg-red-600 text-white text-[10px] font-semibold px-2 py-0.5 rounded-md whitespace-nowrap shadow-md flex items-center space-x-1 animate-fade-in">
          <Radio className="w-2.5 h-2.5 animate-spin" />
          <span>Listening...</span>
        </span>
      )}
    </div>
  );
};
