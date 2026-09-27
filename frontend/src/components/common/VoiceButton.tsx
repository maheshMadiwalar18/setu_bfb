import React, { useState } from 'react';
import { Mic } from 'lucide-react';
import { VoiceAssistantModal } from './VoiceAssistantModal';

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
  const [isModalOpen, setIsModalOpen] = useState(false);

  const sizeClasses = {
    sm: 'w-7 h-7',
    md: 'w-9 h-9',
    lg: 'w-11 h-11',
  };

  const handleTranscriptSubmit = (text: string) => {
    onTranscript(text);
  };

  return (
    <>
      <button
        type="button"
        onClick={() => setIsModalOpen(true)}
        className={`relative flex items-center justify-center rounded-full transition-all focus:outline-hidden ${sizeClasses[size]} bg-emerald-50 hover:bg-emerald-100 text-[#00875A] border border-emerald-300 shadow-2xs ${className}`}
        title={'Voice Input (Click to open Voice Assistant)'}
        aria-label="Voice input button"
      >
        <Mic className="w-4 h-4" />
      </button>

      <VoiceAssistantModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleTranscriptSubmit}
      />
    </>
  );
};
