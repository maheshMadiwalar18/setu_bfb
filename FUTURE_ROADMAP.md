# Future Roadmap

While SETU is currently a highly functional prototype, the roadmap to a production-grade national deployment includes several key phases.

## Phase 1: Production Hardening
- **Database Migration:** Move from SQLite to PostgreSQL.
- **Caching Layer:** Implement Redis cluster for caching heavy AI responses and scraped data.
- **Auth Integration:** Replace mock DigiLocker OAuth with actual DigiLocker API integration.
- **CI/CD:** Set up GitHub Actions for automated testing and deployment.

## Phase 2: Enhanced Intelligence
- **RAG Implementation:** Implement Retrieval-Augmented Generation using a vector database (e.g., Pinecone/Milvus) indexing all PDF guidelines of government schemes.
- **Voice TTS:** Add Text-to-Speech (TTS) using Bhashini APIs so the assistant can speak back to the user in regional languages.
- **WhatsApp Integration:** Deploy the conversational agent as a WhatsApp bot, as WhatsApp is the most accessible platform in rural India.

## Phase 3: Ecosystem Integration
- **UMANG App API:** Integrate with UMANG to allow direct application submission from within SETU.
- **DBT Bharat Portal:** Connect to the Direct Benefit Transfer tracking APIs for real-time payment status.
- **Grievance (CPGRAMS):** Route submitted grievances directly to the CPGRAMS API.

## Phase 4: Offline & Edge
- **CSC Kiosks:** Package SETU as a desktop application for Common Service Centres with offline-first capabilities, syncing data when connectivity is restored.
- **Local LLMs:** Explore running quantized local models (e.g., Llama 3 8B) on edge servers in CSC centers to reduce API costs and latency.
