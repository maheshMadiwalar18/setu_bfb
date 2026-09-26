from app.models import Scheme

SEED_SCHEMES = [
    {
        "id": "pm-kisan",
        "code": "GOI/MoAFW/2024/0001",
        "name": "PM Kisan Samman Nidhi",
        "name_native": "प्रधानमंत्री किसान सम्मान निधि (ಪಿಎಂ ಕಿಸಾನ್)",
        "category": "agriculture",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Agriculture & Farmers Welfare",
        "summary": "Direct financial support of Rs 6,000 per year provided in three equal four-monthly installments to small and marginal farmer families.",
        "description": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN) is a central sector scheme with 100% funding from the Government of India. Under the scheme, income support of Rs 6,000 per year is provided to all landholding farmer families across the country, subject to certain exclusions relating to higher income brackets.",
        "benefit_amount": "Rs 6,000 / year",
        "benefit_type": "Cash",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://pmkisan.gov.in",
        "min_age": 18,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 1000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": True,
        "additional_eligibility": [
            "Landholding farmer families with cultivable land in their names",
            "Institutional landholders and institutional government servants are excluded"
        ],
        "highlights": [
            "Rs 2,000 transferred every 4 months directly into Aadhaar-seeded bank account",
            "Covers over 11 crore farmer families across India",
            "Integrated with e-KYC and PM-KISAN portal"
        ],
        "benefits_breakdown": [
            "Installment 1 (April to July): Rs 2,000",
            "Installment 2 (August to November): Rs 2,000",
            "Installment 3 (December to March): Rs 2,000"
        ],
        "documents_required": [
            "Aadhaar Card with mobile linking",
            "Land Record (Khata/Khatoni/ROR)",
            "Bank Passbook or Account Details",
            "Active Mobile Number"
        ],
        "application_steps": [
            "Visit the official PM-KISAN portal (pmkisan.gov.in)",
            "Click on 'Farmers Corner' and select 'New Farmer Registration'",
            "Enter Aadhaar number and select state to verify OTP",
            "Fill in landholding details and active bank account details",
            "Submit the application and note down the registration number for tracking"
        ],
        "faqs": [
            {"q": "How is the assistance credited?", "a": "Payment is credited directly into bank accounts via Direct Benefit Transfer (DBT) based on Aadhaar."},
            {"q": "Is eKYC mandatory?", "a": "Yes, eKYC is mandatory for all registered PM-KISAN beneficiaries using Aadhaar OTP or biometric verification at CSCs."}
        ],
        "last_updated": "15 Sep 2025",
        "view_count": 8940
    },
    {
        "id": "gruha-lakshmi",
        "code": "KA/WCD/2024/0042",
        "name": "Gruha Lakshmi Scheme",
        "name_native": "ಗೃಹ ಲಕ್ಷ್ಮಿ ಯೋಜನೆ (गृह लक्ष्मी योजना)",
        "category": "women",
        "scheme_type": "State",
        "state": "Karnataka",
        "ministry": "Department of Women & Child Development, Karnataka",
        "summary": "Monthly financial aid of Rs 2,000 to the woman head of household in Karnataka to alleviate household living expenses.",
        "description": "Gruha Lakshmi is a flagship welfare program launched by the Government of Karnataka to empower female homemakers and heads of families by providing a direct monthly DBT allowance of Rs 2,000.",
        "benefit_amount": "Rs 2,000 / month",
        "benefit_type": "Cash",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://sevasindhu.karnataka.gov.in",
        "min_age": 18,
        "max_age": 99,
        "gender_allowed": "female",
        "income_ceiling": 500000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Permanent resident of Karnataka",
            "Must be registered as head of family in Antyodaya/BPL/APL Ration Card",
            "Neither the woman nor her spouse should be income tax or GST payees"
        ],
        "highlights": [
            "Rs 24,000 annual financial security for women homemakers",
            "Direct Benefit Transfer directly to Aadhaar-linked savings account",
            "No application processing fees across Seva Sindhu or Grama One"
        ],
        "benefits_breakdown": [
            "Monthly financial allowance: Rs 2,000 per eligible woman head"
        ],
        "documents_required": [
            "Aadhaar Card of the woman head",
            "Husband's Aadhaar Card (if married)",
            "Ration Card (APL / BPL / Antyodaya)",
            "Aadhaar linked Bank Passbook",
            "Mobile number registered with Aadhaar"
        ],
        "application_steps": [
            "Visit Seva Sindhu portal or visit nearest Grama One / Bangalore One / Bapuji Seva Kendra",
            "Provide Ration Card number to fetch eligible head woman details",
            "Authenticate with Aadhaar OTP of the beneficiary",
            "Verify Aadhaar-seeded bank account for DBT receipt",
            "Receive application acknowledgement with registration ID"
        ],
        "faqs": [
            {"q": "Can unmarried or widowed women apply?", "a": "Yes, if listed as head of the family in the ration card."},
            {"q": "What if payment is delayed?", "a": "Ensure bank account has active Aadhaar seeding (NPCI mapping) at your home bank branch."}
        ],
        "last_updated": "20 Sep 2025",
        "view_count": 14210
    },
    {
        "id": "ayushman-bharat",
        "code": "GOI/MoHFW/2024/0018",
        "name": "Ayushman Bharat PM-JAY",
        "name_native": "आयुष्मान भारत - प्रधानमंत्री जन आरोग्य योजना",
        "category": "health",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Health and Family Welfare",
        "summary": "Comprehensive health insurance cover of Rs 5 Lakh per family per year for secondary and tertiary inpatient hospital care.",
        "description": "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (PM-JAY) is the world's largest government funded healthcare assurance scheme. It provides a health cover of Rs 5 lakh per family per year for secondary and tertiary care hospitalization across public and empaneled private hospitals.",
        "benefit_amount": "Rs 5,00,000 / family / year",
        "benefit_type": "Insurance",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://pmjay.gov.in",
        "min_age": 0,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 300000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": True,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Families listed in Socio-Economic Caste Census (SECC 2011) deprivation criteria",
            "Active NFSA ration card holders or state equivalent beneficiary list",
            "All senior citizens aged 70+ (expanded universal cover)"
        ],
        "highlights": [
            "Cashless and paperless treatment at all empaneled hospitals",
            "Covers up to 3 days pre-hospitalization and 15 days post-hospitalization expenses",
            "No restriction on family size, age, or gender"
        ],
        "benefits_breakdown": [
            "Inpatient medical examinations, consultations and treatments",
            "Pre and post hospitalization care and medical consumables",
            "Coverage across 1,949 medical and surgical procedures"
        ],
        "documents_required": [
            "Aadhaar Card / Ration Card",
            "PMJAY Eligibility Letter / HH ID",
            "Identity Proof with Photo",
            "Mobile number"
        ],
        "application_steps": [
            "Check eligibility on beneficiary.nha.gov.in using Mobile or Ration card number",
            "Visit nearest Empaneled Healthcare Facility (EHCP) or Ayushman Mitra kiosk",
            "Perform Aadhaar biometric or OTP eKYC authentication",
            "Download and print the digital Ayushman Card immediately"
        ],
        "faqs": [
            {"q": "Is preexisting disease covered?", "a": "Yes, all preexisting health conditions are covered from day one of enrollment."},
            {"q": "Can I use the card in any state?", "a": "Yes, Ayushman Bharat has nationwide portability across all empaneled network hospitals."}
        ],
        "last_updated": "18 Sep 2025",
        "view_count": 18200
    },
    {
        "id": "vidyasiri-scholarship",
        "code": "KA/BCWD/2024/0071",
        "name": "Vidyasiri Scholarship (Food & Accommodation)",
        "name_native": "ವಿದ್ಯಾಸಿರಿ ವಿದ್ಯಾರ್ಥಿವೇತನ (विद्यासिरी छात्रवृत्ति)",
        "category": "education",
        "scheme_type": "State",
        "state": "Karnataka",
        "ministry": "Backward Classes Welfare Department, Karnataka",
        "summary": "Monthly stipend of Rs 1,500 for 10 months (Rs 15,000/yr) for post-matric students unable to secure government hostel seats.",
        "description": "Vidyasiri (Food and Accommodation Scheme) provides financial assistance to SC, ST, and Backward Classes students pursuing post-matriculation courses who have not secured accommodation in department-run hostels, ensuring education continuity.",
        "benefit_amount": "Rs 1,500 / month (up to Rs 15,000/yr)",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "30 Nov 2025",
        "apply_url": "https://scholarships.karnataka.gov.in",
        "min_age": 16,
        "max_age": 30,
        "gender_allowed": "any",
        "income_ceiling": 250000.0,
        "caste_eligibility": ["sc", "st", "obc"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Karnataka domicile student",
            "Admitted to recognized post-matric course (PUC, Diploma, Degree, PG)",
            "Distance between home town and college must be greater than 5 km",
            "Annual family income less than Rs 2.50 Lakh for Cat-1 and Rs 1.00 Lakh for 2A/2B/3A/3B"
        ],
        "highlights": [
            "Financial stipend directly deposited to student's bank account",
            "Covers 10 academic months per year",
            "Integrated with State Scholarship Portal (SSP)"
        ],
        "benefits_breakdown": [
            "Rs 1,500 per month for food and lodging allowance for 10 academic months"
        ],
        "documents_required": [
            "Student Aadhaar Card & College ID",
            "Caste and Income Certificate (RD Number from Nadakacheri)",
            "SSLC / 10th Marks Card & Previous Year Marks Sheet",
            "Hostel Non-Availability Certificate / Verification Form",
            "Fee Receipt and Study Certificate"
        ],
        "application_steps": [
            "Register on Karnataka State Scholarship Portal (SSP: ssp.postmatric.karnataka.gov.in)",
            "Enter student Aadhaar and Nadakacheri Caste/Income RD numbers for auto-verification",
            "Select college, course, and hostel non-availability option",
            "Submit application online and provide signed hard copy to college nodal officer"
        ],
        "faqs": [
            {"q": "What is the attendance requirement?", "a": "Minimum 75% biometric/college attendance is mandatory for monthly release of allowance."},
            {"q": "Can I receive SSP fee concession alongside Vidyasiri?", "a": "Yes, tuition fee reimbursement and Vidyasiri food allowance can be availed concurrently."}
        ],
        "last_updated": "12 Sep 2025",
        "view_count": 6430
    },
    {
        "id": "pm-awas-gramin",
        "code": "GOI/MoRD/2024/0034",
        "name": "PM Awas Yojana - Gramin",
        "name_native": "प्रधानमंत्री आवास योजना - ग्रामीण",
        "category": "housing",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Rural Development",
        "summary": "Financial grant of Rs 1.20 Lakh in plains and Rs 1.30 Lakh in hilly states for construction of permanent pucca houses.",
        "description": "Pradhan Mantri Awaas Yojana - Gramin (PMAY-G) aims to provide a pucca house with basic amenities to all houseless households and households living in kutcha and dilapidated houses in rural areas.",
        "benefit_amount": "Rs 1,20,000 - 1,30,000 grant",
        "benefit_type": "Housing",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://pmayg.nic.in",
        "min_age": 18,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 200000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": True,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Rural household without a pucca house in any part of India",
            "Identified through SECC priority list and Gram Sabha verification",
            "No motorized three/four wheelers or agricultural equipment owned"
        ],
        "highlights": [
            "Minimum house unit size of 25 sq. metres including hygienic cooking space",
            "Additional 90/95 person days of unskilled labor wage under MGNREGS",
            "Rs 12,000 incentive for toilet construction under Swachh Bharat Mission (SBM)"
        ],
        "benefits_breakdown": [
            "Phase 1 (Foundation): Rs 40,000",
            "Phase 2 (Roof Level): Rs 40,000",
            "Phase 3 (Completion & Plastering): Rs 40,000",
            "MGNREGS unskilled labor wage component: approx Rs 22,000"
        ],
        "documents_required": [
            "Aadhaar Card of all family members",
            "Bank Account Passbook (DBT enabled)",
            "MGNREGA Job Card Number",
            "Land ownership/possession certificate or Patta",
            "Self-declaration certificate of kutcha residence"
        ],
        "application_steps": [
            "Contact your Gram Panchayat Secretary or Block Development Office (BDO)",
            "Verify presence in the PMAY-G Awaas+ beneficiary waitlist",
            "Geotag existing kutcha house location through the AwaasApp",
            "Upon sanction, receive milestone-linked installments directly into your bank account"
        ],
        "faqs": [
            {"q": "Can I construct the house myself?", "a": "Yes, beneficiaries are encouraged to construct their own houses using locally available materials."},
            {"q": "Are basic services bundled?", "a": "Yes, electricity connection (Saubhagya), LPG connection (Ujjwala), and tap water (JJM) are converged."}
        ],
        "last_updated": "05 Sep 2025",
        "view_count": 9120
    },
    {
        "id": "pm-mudra-yojana",
        "code": "GOI/MoF/2024/0009",
        "name": "PM Mudra Yojana (PMMY)",
        "name_native": "प्रधानमंत्री मुद्रा योजना",
        "category": "entrepreneurship",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Finance, Department of Financial Services",
        "summary": "Collateral-free institutional micro-loans up to Rs 10 Lakh (extended up to Rs 20 Lakh) for micro and small enterprises.",
        "description": "Pradhan Mantri Mudra Yojana (PMMY) enables micro and small enterprises involved in manufacturing, processing, trading, or service sectors to secure non-farm business loans without requiring collateral or third-party guarantees.",
        "benefit_amount": "Loans from Rs 50,000 to Rs 10,00,000",
        "benefit_type": "Loan",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://www.mudra.org.in",
        "min_age": 18,
        "max_age": 65,
        "gender_allowed": "any",
        "income_ceiling": 2000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Any Indian citizen having a non-farm business plan for income generation",
            "Eligible across three categories: Shishu (up to Rs 50k), Kishore (Rs 50k - 5L), Tarun (Rs 5L - 10L)",
            "No past default history with any bank or financial institution"
        ],
        "highlights": [
            "Zero collateral security requirement",
            "Nominal processing charges and competitive interest rates (MCLR linked)",
            "Mudra Debit Card provided for working capital withdrawals"
        ],
        "benefits_breakdown": [
            "Shishu: Loans up to Rs 50,000 (ideal for starters and street vendors)",
            "Kishore: Loans from Rs 50,001 to Rs 5,00,000 (for business expansion)",
            "Tarun: Loans from Rs 5,00,001 to Rs 10,00,000 (for established units)"
        ],
        "documents_required": [
            "Aadhaar Card and PAN Card",
            "Proof of Business Address and Trade License / Udyam Registration",
            "Bank Statement of last 6 months",
            "Quotations for machinery/assets to be purchased",
            "Passport size photographs of applicant/partners"
        ],
        "application_steps": [
            "Prepare a concise business plan indicating capital cost and operational expenses",
            "Apply online through the JanSamarth Portal (jansamarth.in) or visit your local public/private bank",
            "Submit identity documents, business license, and quotation",
            "Receive in-principle approval and loan disbursal into your business current account"
        ],
        "faqs": [
            {"q": "Is collateral required?", "a": "No, loans under PMMY are covered by the Credit Guarantee Fund for Micro Units (CGFMU)."},
            {"q": "What is the repayment tenure?", "a": "Repayment tenure ranges between 3 to 5 years depending on cash flow."}
        ],
        "last_updated": "22 Sep 2025",
        "view_count": 11300
    },
    {
        "id": "sukanya-samriddhi",
        "code": "GOI/MoWCD/2024/0055",
        "name": "Sukanya Samriddhi Yojana (SSY)",
        "name_native": "सुकन्या समृद्धि योजना (ಸುಕನ್ಯಾ ಸಮೃದ್ಧಿ ಯೋಜನೆ)",
        "category": "women",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Women and Child Development",
        "summary": "High-interest savings account (8.2% p.a.) with triple tax exemption (EEE) designed to secure education and marriage of the girl child.",
        "description": "Sukanya Samriddhi Account is a government-backed savings initiative under the 'Beti Bachao Beti Padhao' campaign. Parents or legal guardians can open an account in the name of a girl child below 10 years of age.",
        "benefit_amount": "8.2% compound interest + Section 80C tax exemption",
        "benefit_type": "Subsidy",
        "application_mode": "Offline",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://www.indiapost.gov.in",
        "min_age": 0,
        "max_age": 10,
        "gender_allowed": "female",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Account can be opened for a girl child from birth up to 10 years of age",
            "Maximum two accounts per family (allowed for triplets/twins girl children)",
            "Minimum deposit of Rs 250 per financial year, maximum Rs 1,50,000"
        ],
        "highlights": [
            "Highest sovereign interest rate among all small savings schemes (currently 8.2%)",
            "Exempt-Exempt-Exempt (EEE) status under Income Tax Act 1961",
            "Operated by the girl child after reaching 18 years of age"
        ],
        "benefits_breakdown": [
            "Annual deposit from Rs 250 to Rs 1.5 Lakh",
            "Full maturity after 21 years from account opening or upon marriage after age 18",
            "50% partial withdrawal allowed for higher education after age 18"
        ],
        "documents_required": [
            "Birth Certificate of the Girl Child",
            "Aadhaar Card / PAN Card of the Parent / Guardian",
            "Address proof of Guardian",
            "Passport size photographs of Child and Guardian"
        ],
        "application_steps": [
            "Visit any Post Office branch or authorized public/private commercial bank",
            "Fill in Form-1 (Sukanya Samriddhi Account Opening Form)",
            "Submit with child birth certificate, guardian KYC documents, and initial deposit (minimum Rs 250)",
            "Receive physical passbook with account number and IFSC/branch details"
        ],
        "faqs": [
            {"q": "Can I transfer the account to another city?", "a": "Yes, SSY accounts can be freely transferred anywhere in India between post offices and banks without fee."},
            {"q": "What happens if I miss the minimum deposit?", "a": "A penalty fee of Rs 50 per year of default is applicable to regularize the account."}
        ],
        "last_updated": "10 Sep 2025",
        "view_count": 7890
    },
    {
        "id": "nsp-post-matric",
        "code": "GOI/MoSJE/2024/0088",
        "name": "National Scholarship Portal - Post-Matric Scholarship",
        "name_native": "राष्ट्रीय छात्रवृत्ति पोर्टल - उत्तर मैट्रिक छात्रवृत्ति",
        "category": "education",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Social Justice & Empowerment / MoMA",
        "summary": "Centrally sponsored scholarship covering non-refundable college fees and living maintenance allowances for SC/ST/OBC/Minority students.",
        "description": "Post-Matric Scholarship scheme provides substantial financial assistance to students belonging to underprivileged communities pursuing Class 11, Class 12, ITI, Diploma, Undergraduate, and Postgraduate degrees across recognized institutions.",
        "benefit_amount": "Rs 3,000 - 13,500 / year + Full Tuition Reimbursement",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://scholarships.gov.in",
        "min_age": 15,
        "max_age": 35,
        "gender_allowed": "any",
        "income_ceiling": 250000.0,
        "caste_eligibility": ["sc", "st", "obc"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Indian national studying in Class 11 and above in a recognized institution",
            "Annual family income not exceeding Rs 2,50,000 from all sources",
            "Student must not be receiving any other government scholarship concurrently"
        ],
        "highlights": [
            "Direct Benefit Transfer of maintenance allowance and fee reimbursement",
            "One-time registration (OTR) with Aadhaar face authentication / OTP",
            "Pan-India validity across universities, colleges, and polytechnics"
        ],
        "benefits_breakdown": [
            "Maintenance allowance for Day Scholars: Rs 2,500 to Rs 7,000 / year",
            "Maintenance allowance for Hostellers: Rs 4,000 to Rs 13,500 / year",
            "100% compulsory non-refundable tuition fees reimbursed to institution"
        ],
        "documents_required": [
            "Student Aadhaar Card (Aadhaar Seeded Bank Account)",
            "Valid Income Certificate issued by competent Revenue Authority",
            "Valid Community / Caste Certificate",
            "Previous Qualifying Exam Marksheet",
            "Current Year Fee Receipt and Institute Bonafide Certificate"
        ],
        "application_steps": [
            "Visit scholarships.gov.in and complete One Time Registration (OTR)",
            "Log in using OTR Reference Number and verify institutional AISHE/DISE code",
            "Fill academic and fee details, upload required certificates",
            "Submit online and institute nodal officer will verify and forward to state department"
        ],
        "faqs": [
            {"q": "Can renewal students apply?", "a": "Yes, renewal applications only require entering previous application ID and uploading latest mark sheet."},
            {"q": "How to verify bank account status?", "a": "Ensure your bank account is mapped to NPCI Aadhaar mapper so DBT funds reach your account without bounce."}
        ],
        "last_updated": "24 Sep 2025",
        "view_count": 16500
    },
    {
        "id": "pm-vishwakarma",
        "code": "GOI/MoMSME/2024/0102",
        "name": "PM Vishwakarma Scheme",
        "name_native": "पीएम विश्वकर्मा योजना",
        "category": "employment",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Micro, Small and Medium Enterprises",
        "summary": "Holistic support with Rs 15,000 toolkit incentive, skill training with daily Rs 500 stipend, and collateral-free credit up to Rs 3 Lakh at 5% interest.",
        "description": "PM Vishwakarma provides end-to-end support to traditional artisans and craftspeople engaged in 18 traditional trades such as carpenters, blacksmiths, goldsmiths, potters, cobblers, masons, and tailors.",
        "benefit_amount": "Rs 15,000 toolkit + Rs 3 Lakh loan at 5% interest",
        "benefit_type": "Subsidy",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://pmvishwakarma.gov.in",
        "min_age": 18,
        "max_age": 75,
        "gender_allowed": "any",
        "income_ceiling": 500000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Engaged in one of the 18 specified traditional family craft trades",
            "Minimum age 18 years on the date of registration",
            "Only one family member (husband/wife/unmarried children) can avail benefits"
        ],
        "highlights": [
            "Recognition through PM Vishwakarma Certificate and ID Card",
            "Basic training of 5-7 days and advanced training of 15 days with Rs 500/day stipend",
            "Digital transaction incentive of Rs 1 per transaction up to 100 transactions monthly"
        ],
        "benefits_breakdown": [
            "Skill verification & basic training (40 hours) with Rs 500 daily stipend",
            "Toolkit financial e-voucher: Rs 15,000",
            "First tranche collateral-free loan: Rs 1,00,000 (18 months tenure @ 5%)",
            "Second tranche collateral-free loan: Rs 2,00,000 (30 months tenure @ 5%)"
        ],
        "documents_required": [
            "Aadhaar Card and Mobile Number",
            "Bank Passbook details",
            "Ration Card or Family details document",
            "Trade skill declaration"
        ],
        "application_steps": [
            "Visit nearest Common Service Centre (CSC) for Aadhaar biometric registration",
            "Select traditional artisan trade category and verify family details",
            "Stage 1 Gram Panchayat / ULB verification, Stage 2 District committee approval",
            "Download digital PM Vishwakarma ID and join training program"
        ],
        "faqs": [
            {"q": "What are the 18 covered trades?", "a": "Carpenter, Boat Builder, Armourer, Blacksmith, Hammer and Tool Kit Maker, Locksmith, Sculptor, Goldsmith, Potter, Cobbler, Mason, Basket/Mat/Broom Maker, Doll & Toy Maker, Barber, Garland Maker, Washerman, Tailor, Fishing Net Maker."}
        ],
        "last_updated": "21 Sep 2025",
        "view_count": 8700
    },
    {
        "id": "atal-pension-yojana",
        "code": "GOI/MoF/2024/0064",
        "name": "Atal Pension Yojana (APY)",
        "name_native": "अटल पेंशन योजना (ಅಟಲ್ ಪಿಂಚಣಿ ಯೋಜನೆ)",
        "category": "senior_citizens",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Pension Fund Regulatory and Development Authority (PFRDA)",
        "summary": "Guaranteed monthly pension of Rs 1,000 to Rs 5,000 for life starting from age 60 for unorganized sector workers.",
        "description": "Atal Pension Yojana (APY) provides retirement financial security for unorganized sector workers by guaranteeing a fixed monthly pension ranging between Rs 1,000 and Rs 5,000 upon reaching 60 years of age.",
        "benefit_amount": "Rs 1,000 - 5,000 / month lifelong pension",
        "benefit_type": "Cash",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://npscra.nsdl.co.in",
        "min_age": 18,
        "max_age": 40,
        "gender_allowed": "any",
        "income_ceiling": 500000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Indian citizen aged between 18 and 40 years",
            "Must possess a savings bank account or post office savings account",
            "Must not be an income taxpayer or member of any statutory social security scheme"
        ],
        "highlights": [
            "Guaranteed minimum monthly pension backed by the Government of India",
            "In case of demise of subscriber, same pension is paid to the spouse for life",
            "Entire accumulated pension corpus returned to the nominee after spouse's demise"
        ],
        "benefits_breakdown": [
            "Option 1: Rs 1,000 / month guaranteed lifelong pension",
            "Option 2: Rs 2,000 / month guaranteed lifelong pension",
            "Option 3: Rs 3,000 / month guaranteed lifelong pension",
            "Option 4: Rs 4,000 / month guaranteed lifelong pension",
            "Option 5: Rs 5,000 / month guaranteed lifelong pension"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Active Savings Bank Account Passbook",
            "Mobile Number",
            "Nominee details"
        ],
        "application_steps": [
            "Visit your home bank branch or internet banking portal",
            "Fill in the APY registration form and choose desired monthly pension tier",
            "Authorize auto-debit of the small monthly contribution",
            "Receive APY PRAN (Permanent Retirement Account Number) card confirmation"
        ],
        "faqs": [
            {"q": "Can I increase or decrease my pension tier?", "a": "Yes, subscribers can change their pension amount choice once in a financial year during April."}
        ],
        "last_updated": "14 Sep 2025",
        "view_count": 5420
    },
    {
        "id": "divyangjan-swavalamban",
        "code": "GOI/MSJE/2024/0091",
        "name": "Divyangjan Swavalamban Yojana",
        "name_native": "दिव्यांगजन स्वावलंबन योजना",
        "category": "disability",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Department of Empowerment of Persons with Disabilities",
        "summary": "Concessional loans up to Rs 50 Lakh at low interest rates with interest rebate for women with disabilities for self-employment.",
        "description": "National Handicapped Finance and Development Corporation (NHFDC) provides financial assistance to Persons with Disabilities (PwDs) at subsidized interest rates for education, vocational training, and income-generating self-employment activities.",
        "benefit_amount": "Concessional loans up to Rs 50,00,000",
        "benefit_type": "Loan",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://www.nhfdc.nic.in",
        "min_age": 18,
        "max_age": 60,
        "gender_allowed": "any",
        "income_ceiling": 800000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": True,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Indian citizen having disability level of 40% or more (UDID card)",
            "Age between 18 and 60 years",
            "Relevant educational or vocational skill for proposed commercial venture"
        ],
        "highlights": [
            "Subsidized interest rates between 5% to 8% per annum",
            "1% special interest rebate for female borrowers and prompt repayers",
            "Loan repayment tenure up to 7 to 10 years with comfortable moratorium"
        ],
        "benefits_breakdown": [
            "Loans up to Rs 50,000 at 5% interest",
            "Loans from Rs 50,000 to Rs 5,00,000 at 6% interest",
            "Loans above Rs 5,00,000 at 7-8% interest"
        ],
        "documents_required": [
            "Unique Disability ID (UDID) Card or Disability Certificate (40%+)",
            "Aadhaar Card and Residence Certificate",
            "Income Certificate",
            "Business Project Report / Skill certificate",
            "Bank passbook copy"
        ],
        "application_steps": [
            "Submit application online at nhfdc.nic.in or through State Channelising Agencies (SCAs) / RRBs",
            "Submit project proposal along with UDID card and KYC",
            "Undergo district appraisal and credit sanction",
            "Receive funds directly into bank account for equipment purchase or business setup"
        ],
        "faqs": [
            {"q": "Is UDID card mandatory?", "a": "UDID card or medical authority disability certificate with 40%+ benchmark disability is accepted."}
        ],
        "last_updated": "08 Sep 2025",
        "view_count": 3810
    },
    {
        "id": "pm-surya-ghar",
        "code": "GOI/MNRE/2024/0115",
        "name": "PM Surya Ghar: Muft Bijli Yojana",
        "name_native": "पीएम सूर्य घर: मुफ्त बिजली योजना",
        "category": "environment",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of New and Renewable Energy",
        "summary": "Direct financial subsidy up to Rs 78,000 for installing rooftop solar panels to provide up to 300 units of free electricity monthly.",
        "description": "PM Surya Ghar: Muft Bijli Yojana provides substantial capital subsidies to households across India to install grid-connected rooftop solar systems, cutting electricity bills to zero and generating extra income from net metering.",
        "benefit_amount": "Subsidy up to Rs 78,000 + 300 units free power/month",
        "benefit_type": "Subsidy",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2026",
        "apply_url": "https://pmsuryaghar.gov.in",
        "min_age": 18,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 5000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Indian residential household with a suitable roof with solar access",
            "Must have an active domestic grid electricity connection",
            "Must not have availed another central solar subsidy for the same meter"
        ],
        "highlights": [
            "Rs 30,000 subsidy for 1 kW system",
            "Rs 60,000 subsidy for 2 kW system",
            "Rs 78,000 max subsidy for 3 kW and higher systems",
            "Low-interest collateral-free loans at 7% from leading public banks"
        ],
        "benefits_breakdown": [
            "1 kW capacity: Rs 30,000 subsidy",
            "2 kW capacity: Rs 60,000 subsidy",
            "3 kW and above: Rs 78,000 subsidy",
            "Estimated monthly electricity savings: Rs 2,000 - 3,500"
        ],
        "documents_required": [
            "Latest Electricity Bill (Consumer Number)",
            "Aadhaar Card of Electricity Account Holder",
            "Bank Passbook / Cancelled Cheque (matching electricity bill name)",
            "Roof ownership document or permission"
        ],
        "application_steps": [
            "Register on National Portal (pmsuryaghar.gov.in) with State, Discom, and Electricity Consumer Number",
            "Apply for Rooftop Solar technical feasibility approval from local Discom",
            "Select empaneled vendor and install standard solar equipment",
            "Discom inspects and installs net meter; subsidy is released to bank within 30 days"
        ],
        "faqs": [
            {"q": "How long does subsidy credit take?", "a": "Subsidy is directly credited to beneficiary bank account within 30 days of net meter commissioning."}
        ],
        "last_updated": "25 Sep 2025",
        "view_count": 10400
    }
]

def init_db_data(db):
    # Check if schemes already exist
    count = db.query(Scheme).count()
    if count == 0:
        for data in SEED_SCHEMES:
            scheme = Scheme(**data)
            db.add(scheme)
        db.commit()
