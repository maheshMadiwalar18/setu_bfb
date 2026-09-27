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
    },
    {
        "id": "pm-yasasvi",
        "code": "GOI/MSJE/2024/0130",
        "name": "PM-YASASVI Scholarship Scheme",
        "name_native": "पीएम यशस्वी छात्रवृत्ति योजना (ಯಶಸ್ವಿ ವಿದ್ಯಾರ್ಥಿವೇತನ)",
        "category": "education",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Social Justice and Empowerment",
        "summary": "Merit-based scholarships up to Rs 1,25,000 per year for OBC, EBC, and DNT students studying in Top Class Schools and Colleges across India.",
        "description": "PM Young Achievers Scholarship Award Scheme for Vibrant India (PM-YASASVI) provides prestigious financial support to meritorious students from OBC, Economically Backward Class (EBC), and De-Notified Nomadic and Semi-Nomadic Tribes (DNT) categories.",
        "benefit_amount": "Rs 75,000 to Rs 1,25,000 / year",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://scholarships.gov.in",
        "min_age": 13,
        "max_age": 28,
        "gender_allowed": "any",
        "income_ceiling": 250000.0,
        "caste_eligibility": ["obc"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Student belonging to OBC, EBC, or DNT category",
            "Annual family income less than Rs 2.50 Lakh",
            "Enrolled in identified Top Class Schools (Class 9 & 11) or Top Class Colleges/Universities"
        ],
        "highlights": [
            "Class 9 and 10 students: Up to Rs 75,000 per annum",
            "Class 11 and 12 students: Up to Rs 1,25,000 per annum",
            "Top College / University students: Full tuition fee plus Rs 86,000 per annum living stipend"
        ],
        "benefits_breakdown": [
            "School Tier: Rs 75,000 to Rs 1,25,000 annual scholarship grant",
            "College Tier: 100% Tuition fee waiver + living expenses direct DBT"
        ],
        "documents_required": [
            "Aadhaar Card of the Student",
            "OBC / EBC / DNT Category Certificate",
            "Income Certificate (under Rs 2.5 Lakh)",
            "Previous Class Marksheet (min 60%)",
            "Bonafide School / College Admission Certificate"
        ],
        "application_steps": [
            "Visit National Scholarship Portal (scholarships.gov.in)",
            "Complete One Time Registration (OTR) with Aadhaar Face/OTP verification",
            "Apply under 'PM-YASASVI Central Sector Scheme'",
            "Submit online; school/college verifies and submits to ministry"
        ],
        "faqs": [
            {"q": "Is there an entrance exam?", "a": "Selection is merit-based based on Class 8/10 marks and verified NSP institutional portal criteria."}
        ],
        "last_updated": "24 Sep 2025",
        "view_count": 21500
    },
    {
        "id": "pm-vidyalaxmi",
        "code": "GOI/MoE/2024/0142",
        "name": "Prime Minister Vidyalaxmi Scheme",
        "name_native": "प्रधानमंत्री विद्यालक्ष्मी योजना",
        "category": "education",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Department of Higher Education, Ministry of Education",
        "summary": "Collateral-free, guarantor-free education loans up to Rs 7.50 Lakh with 75% Government Credit Guarantee and 3% interest subvention for higher education.",
        "description": "PM Vidyalaxmi scheme empowers youth to pursue higher education in top 860 quality Higher Education Institutions (QHEIs) by providing collateral-free education loans with government backing and full interest subsidy for family incomes up to Rs 8 Lakh.",
        "benefit_amount": "Collateral-Free Loan up to Rs 7,50,000 with 75% Govt Guarantee + Interest Subsidy",
        "benefit_type": "Loan",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://www.vidyalakshmi.co.in",
        "min_age": 17,
        "max_age": 35,
        "gender_allowed": "any",
        "income_ceiling": 800000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Admitted to top NIRF-ranked Higher Educational Institutions in India",
            "Annual family income up to Rs 8 Lakh for interest subvention",
            "Zero requirement of third-party guarantor or collateral security"
        ],
        "highlights": [
            "Loans up to Rs 7.50 Lakh receive 75% credit guarantee by Central Government",
            "3% interest subvention during moratorium period for incomes up to Rs 8 Lakh",
            "Seamless digital application linked with 40+ scheduled commercial banks"
        ],
        "benefits_breakdown": [
            "Tuition fees, hostel charges, books, and laptop costs fully financed",
            "Repayment starts only 1 year after course completion"
        ],
        "documents_required": [
            "Student Aadhaar Card & PAN Card",
            "College Admission Offer Letter & Fee Structure",
            "Family Income Certificate / ITR",
            "10th, 12th & Graduation Marksheets",
            "Student Savings Bank Account Passbook"
        ],
        "application_steps": [
            "Register on PM Vidyalaxmi Portal (vidyalakshmi.co.in)",
            "Search and choose loan scheme from 40+ partner banks with Common Educational Loan Application Form (CELAF)",
            "Upload admission letter and KYC details",
            "Bank sanctions and disburses loan amount directly to the college institution"
        ],
        "faqs": [
            {"q": "Do I need to pledge property or gold?", "a": "No, PM Vidyalaxmi loans up to Rs 7.5 Lakh are 100% collateral-free and guarantor-free."}
        ],
        "last_updated": "25 Sep 2025",
        "view_count": 19400
    },
    {
        "id": "aicte-pragati",
        "code": "GOI/AICTE/2024/0155",
        "name": "AICTE Pragati Scholarship for Girl Students",
        "name_native": "एआईसीटीई प्रगति छात्रवृत्ति (ಯುವತಿಯರಿಗೆ ಎಐಸಿಟಿಇ ಪ್ರಗತಿ ಯೋಜನೆ)",
        "category": "education",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "All India Council for Technical Education (AICTE)",
        "summary": "Financial grant of Rs 50,000 per year for girl students enrolled in technical degree or diploma courses across AICTE approved colleges.",
        "description": "Pragati Scheme aims to provide assistance for advancement of girls pursuing technical education. Up to two girl children per family are eligible for Rs 50,000 per year throughout the duration of their degree/diploma program.",
        "benefit_amount": "Rs 50,000 / year for every year of course",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://scholarships.gov.in",
        "min_age": 16,
        "max_age": 30,
        "gender_allowed": "female",
        "income_ceiling": 800000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Female student admitted to 1st year or 2nd year (lateral entry) of technical Degree/Diploma",
            "AICTE approved college or university institution",
            "Family income not exceeding Rs 8.00 Lakh per annum",
            "Maximum two girl children per family"
        ],
        "highlights": [
            "Rs 50,000 per annum towards college fee, computer purchase, books, and equipment",
            "Disbursed via DBT directly into student's Aadhaar-seeded bank account",
            "Renewable each academic year based on passing progression"
        ],
        "benefits_breakdown": [
            "Rs 50,000 per year for 4 years (Degree: Total Rs 2,00,000)",
            "Rs 50,000 per year for 3 years (Diploma: Total Rs 1,50,000)"
        ],
        "documents_required": [
            "Student Aadhaar Card (Aadhaar Seeded Bank Account)",
            "10th & 12th Marks Sheet",
            "College Admission Allotment Letter & Tuition Fee Receipt",
            "Family Income Certificate from Tehsildar/Revenue Officer",
            "Declaration of parents confirming maximum two girls"
        ],
        "application_steps": [
            "Register on National Scholarship Portal (scholarships.gov.in)",
            "Select 'AICTE - Pragati Scholarship Scheme for Girl Students'",
            "Upload admission letter and income proof",
            "College Nodal Officer approves application for central disbursement"
        ],
        "faqs": [
            {"q": "Can I receive state tuition waiver along with Pragati?", "a": "Yes, Pragati provides contingency/study grant support which can be availed alongside state tuition fee waivers."}
        ],
        "last_updated": "22 Sep 2025",
        "view_count": 14800
    },
    {
        "id": "central-sector-scholarship",
        "code": "GOI/MoE/2024/0168",
        "name": "Central Sector Scheme of Scholarships for College Students",
        "name_native": "कॉलेज और विश्वविद्यालय के छात्रों के लिए केंद्रीय क्षेत्र छात्रवृत्ति योजना",
        "category": "education",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Department of Higher Education, Ministry of Education",
        "summary": "Merit-cum-means scholarship of Rs 12,000 to Rs 20,000 per year for top 80th percentile students pursuing regular graduation and post-graduation.",
        "description": "Central Sector Scholarship provides financial assistance to meritorious students from low-income families to meet a part of their day-to-day expenses while pursuing higher studies in universities, colleges, and professional institutions.",
        "benefit_amount": "Rs 12,000 to Rs 20,000 / year (Total up to Rs 76,000)",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://scholarships.gov.in",
        "min_age": 17,
        "max_age": 26,
        "gender_allowed": "any",
        "income_ceiling": 450000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Scored above 80th percentile in Class 12 board examination",
            "Pursuing regular full-time undergraduate or postgraduate degree course",
            "Annual family income not exceeding Rs 4.50 Lakh",
            "Not availing any other government scholarship"
        ],
        "highlights": [
            "Rs 12,000 per annum for Undergraduate courses (1st to 3rd year)",
            "Rs 20,000 per annum for Postgraduate courses (4th and 5th year)",
            "Total 82,000 fresh scholarships awarded every academic year (50% reserved for girls)"
        ],
        "benefits_breakdown": [
            "UG Degree (3 Years): Rs 36,000 total scholarship",
            "PG Degree (2 Years): Rs 40,000 total scholarship"
        ],
        "documents_required": [
            "Class 12 Passing Marksheet with Roll Number",
            "Student Aadhaar Card & Mobile Number",
            "Income Certificate (under Rs 4.5 Lakh)",
            "Bonafide College Student Certificate",
            "Aadhaar-seeded Bank Passbook"
        ],
        "application_steps": [
            "Visit scholarships.gov.in and complete OTR",
            "Select 'Central Sector Scheme of Scholarships for College and University Students'",
            "Enter Class 12 board roll number and year of passing for auto-verification of 80th percentile eligibility",
            "Submit online application"
        ],
        "faqs": [
            {"q": "What is the renewal criterion?", "a": "Minimum 50% marks in annual college exams and 75% attendance are required for automatic renewal."}
        ],
        "last_updated": "24 Sep 2025",
        "view_count": 13200
    },
    {
        "id": "pm-jandhan",
        "code": "GOI/MoF/2024/0201",
        "name": "PM Jan-Dhan Yojana (PMJDY)",
        "name_native": "प्रधानमंत्री जन-धन योजना",
        "category": "banking",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Finance",
        "summary": "National mission for financial inclusion providing zero balance bank account, RuPay debit card, and Rs 2 Lakh accidental insurance cover.",
        "description": "Pradhan Mantri Jan-Dhan Yojana ensures access to financial services including banking, savings, deposit accounts, remittance, credit, insurance, and pension in an affordable manner for unbanked citizens.",
        "benefit_amount": "Zero Balance Account + Rs 2 Lakh Accident Cover + Rs 10,000 Overdraft",
        "benefit_type": "Cash",
        "application_mode": "Offline",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://pmjdy.gov.in",
        "min_age": 10,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Indian citizen without any existing bank account",
            "Minors above 10 years can open self-operated accounts"
        ],
        "highlights": [
            "No minimum balance required",
            "Free RuPay debit card with Rs 2,00,000 accidental insurance",
            "Rs 10,000 overdraft facility for eligible account holders"
        ],
        "benefits_breakdown": [
            "Direct Benefit Transfer (DBT) of all government schemes",
            "Interest earned on savings deposit",
            "Rs 2 Lakh accidental death / disability coverage"
        ],
        "documents_required": [
            "Aadhaar Card OR Passport / Voter ID / Driving License",
            "Passport size photographs",
            "Mobile number"
        ],
        "application_steps": [
            "Visit nearest bank branch or Bank Mitra / CSC kiosk",
            "Fill in PMJDY account opening form",
            "Authenticate using Aadhaar biometric authentication",
            "Receive instant RuPay Debit Card and Passbook"
        ],
        "faqs": [
            {"q": "Is minimum balance compulsory?", "a": "No, PMJDY accounts are zero-balance savings accounts with no penalty charges."}
        ],
        "last_updated": "20 Sep 2025",
        "view_count": 15400
    },
    {
        "id": "pm-jjby",
        "code": "GOI/MoF/2024/0202",
        "name": "PM Jeevan Jyoti Bima Yojana (PMJJBY)",
        "name_native": "प्रधानमंत्री जीवन ज्योति बीमा योजना",
        "category": "banking",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Finance",
        "summary": "Life insurance coverage of Rs 2,00,000 for death due to any cause at an affordable premium of Rs 436 per annum.",
        "description": "PMJJBY is a renewable one-year term life insurance scheme providing life cover to citizens aged 18 to 50 years holding a bank account.",
        "benefit_amount": "Rs 2,00,000 Life Insurance Cover",
        "benefit_type": "Insurance",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://jansuraksha.gov.in",
        "min_age": 18,
        "max_age": 50,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Bank account holder aged between 18 and 50 years",
            "Consent for auto-debit of Rs 436 annual premium"
        ],
        "highlights": [
            "Rs 2 Lakh life cover payable to nominee on death due to any reason",
            "Annual premium auto-debited in single installment every May",
            "Simple enrollment through SMS or internet banking"
        ],
        "benefits_breakdown": [
            "Rs 2,00,000 lump sum claim amount to family nominee"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Bank Passbook",
            "Nominee details"
        ],
        "application_steps": [
            "Log in to net banking or visit bank branch / CSC",
            "Select PMJJBY auto-debit consent",
            "Submit nominee name and Aadhaar details"
        ],
        "faqs": [
            {"q": "What is the annual premium?", "a": "Rs 436 per year, auto-debited automatically from your bank account."}
        ],
        "last_updated": "18 Sep 2025",
        "view_count": 9800
    },
    {
        "id": "nsap-pension",
        "code": "GOI/MoRD/2024/0203",
        "name": "National Social Assistance Programme (NSAP)",
        "name_native": "राष्ट्रीय सामाजिक सहायता कार्यक्रम",
        "category": "social",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Rural Development",
        "summary": "Monthly pension for senior citizens, widows, and persons with severe disabilities living below the poverty line.",
        "description": "NSAP fulfills the Constitutional directive of providing social security to destitute elderly citizens, widows, and severely disabled persons.",
        "benefit_amount": "Rs 1,000 - 3,000 / month pension",
        "benefit_type": "Cash",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://nsap.nic.in",
        "min_age": 60,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 150000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": True,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "BPL household senior citizen aged 60+ (IGNOAPS), widow aged 40+ (IGNWPS), or severe PwD (IGNDPS)"
        ],
        "highlights": [
            "Direct monthly benefit transfer into Aadhaar-seeded bank account",
            "Combined central and state top-up contribution"
        ],
        "benefits_breakdown": [
            "Senior Citizen Pension (60-79 yrs): Rs 1,000 - 2,000 / month",
            "Senior Citizen Pension (80+ yrs): Rs 2,500 - 3,000 / month"
        ],
        "documents_required": [
            "Aadhaar Card",
            "BPL Ration Card / Income Certificate",
            "Bank Passbook",
            "Age proof document"
        ],
        "application_steps": [
            "Apply via Gram Panchayat / Municipal Office or NSAP portal",
            "Submit BPL card and Aadhaar for verification",
            "Receive monthly direct pension transfer"
        ],
        "faqs": [
            {"q": "Is BPL card compulsory?", "a": "Yes, applicant must belong to a BPL family listed in rural/urban survey."}
        ],
        "last_updated": "15 Sep 2025",
        "view_count": 12100
    },
    {
        "id": "pm-daksh",
        "code": "GOI/MoSJE/2024/0204",
        "name": "PM-DAKSH Skill Development Scheme",
        "name_native": "पीएम दक्ष कौशल विकास योजना",
        "category": "social",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Social Justice and Empowerment",
        "summary": "Free skill training with monthly stipend of Rs 1,000 to Rs 3,000 for SC, OBC, EBC, DNT, and Sanitation Workers.",
        "description": "PM-DAKSH provides short term upskilling, reskilling, and entrepreneurial training to youth belonging to marginalized communities to enhance their wage and self-employment opportunities.",
        "benefit_amount": "Free Skill Course + Rs 1,000 - 3,000 Monthly Stipend + Free Kit",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://pmdaksh.dosje.gov.in",
        "min_age": 18,
        "max_age": 45,
        "gender_allowed": "any",
        "income_ceiling": 300000.0,
        "caste_eligibility": ["sc", "obc"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "SC, OBC, EBC, DNT youth or sanitation worker",
            "Annual family income less than Rs 3 Lakh for OBC and Rs 1 Lakh for EBC"
        ],
        "highlights": [
            "100% free government certified vocational training",
            "Monthly stipend for candidates with 80%+ attendance",
            "Placement assistance provided in private and government sectors"
        ],
        "benefits_breakdown": [
            "Stipend of Rs 1,000/month for upskilling/reskilling",
            "Stipend of Rs 1,500/month for short term training",
            "Stipend of Rs 3,000/month for apprentice training"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Caste & Income Certificate",
            "Educational Qualification Certificate",
            "Bank Account details"
        ],
        "application_steps": [
            "Register on pmdaksh.dosje.gov.in portal",
            "Choose preferred skill sector and nearest training institute",
            "Complete batch enrollment and attend classes"
        ],
        "faqs": [
            {"q": "Is training completely free?", "a": "Yes, 100% free with study materials and stipend."}
        ],
        "last_updated": "22 Sep 2025",
        "view_count": 7600
    },
    {
        "id": "pm-kusum",
        "code": "GOI/MNRE/2024/0205",
        "name": "PM-KUSUM Solar Pump Scheme",
        "name_native": "पीएम कुसुम सोलर पंप योजना",
        "category": "agriculture",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of New and Renewable Energy",
        "summary": "Up to 60% central and state capital subsidy for installing standalone off-grid solar agriculture pumps for farmers.",
        "description": "PM-KUSUM scheme aims to de-dieselize the farm sector by enabling farmers to install standalone solar agriculture pumps and solarize existing grid-connected pumps.",
        "benefit_amount": "Up to 60% Subsidy on Solar Agriculture Pumps",
        "benefit_type": "Subsidy",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2026",
        "apply_url": "https://pmkusum.mnre.gov.in",
        "min_age": 18,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": True,
        "additional_eligibility": [
            "Individual farmer, water user association, or farm producer organization (FPO)",
            "Agricultural land with borewell/openwell source"
        ],
        "highlights": [
            "30% Central Subsidy + 30% State Subsidy (Farmer pays only 10-40%)",
            "5 to 7.5 HP solar water pump installation",
            "Earn extra income by selling surplus power back to the grid"
        ],
        "benefits_breakdown": [
            "Financial subsidy up to Rs 1,50,000 on 7.5 HP solar pump",
            "Zero electricity bill for irrigation"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Land ownership Patta / RTC",
            "Bank Passbook",
            "Mobile number"
        ],
        "application_steps": [
            "Apply via State Renewable Energy Agency portal (e.g. KREDL / MEDA / UPNEDA)",
            "Select solar pump capacity and vendor",
            "Pay farmer contribution share (10%)",
            "Receive site verification and pump installation"
        ],
        "faqs": [
            {"q": "What is the farmer share?", "a": "Farmer only pays 10% to 40% of the total cost; remaining 60-90% is covered by subsidies and bank loans."}
        ],
        "last_updated": "21 Sep 2025",
        "view_count": 11200
    },
    {
        "id": "jan-aushadhi",
        "code": "GOI/MoCF/2024/0206",
        "name": "PM Bhartiya Jan Aushadhi Pariyojana",
        "name_native": "प्रधानमंत्री भारतीय जन औषधि परियोजना",
        "category": "health",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Department of Pharmaceuticals, Ministry of Chemicals & Fertilizers",
        "summary": "High quality generic medicines, surgical items, and health products available at 50% to 90% lower prices across 10,000+ Jan Aushadhi Kendras.",
        "description": "PMBJAP makes quality generic medicines accessible to all citizens at affordable prices, reducing out-of-pocket healthcare expenses significantly.",
        "benefit_amount": "50% to 90% discount on 2,000+ medicines and surgicals",
        "benefit_type": "Subsidy",
        "application_mode": "Offline",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://janaushadhi.gov.in",
        "min_age": 0,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Open to all citizens without any income or documentation barrier"
        ],
        "highlights": [
            "Over 2,000 quality WHO-GMP certified generic medicines",
            "300+ surgical equipment and medical consumables",
            "Oxo-biodegradable Sanitary Napkins (Suvidha) at Rs 1 per pad"
        ],
        "benefits_breakdown": [
            "50-90% savings compared to branded market medicines",
            "Available across 10,000+ kendras nationwide"
        ],
        "documents_required": [
            "Valid Doctor Prescription (optional for OTC items)"
        ],
        "application_steps": [
            "Locate nearest Jan Aushadhi Kendra using Jan Aushadhi Sugam Mobile App",
            "Present prescription and purchase WHO-GMP tested generic medicines"
        ],
        "faqs": [
            {"q": "Are generic medicines as effective as branded ones?", "a": "Yes, all Jan Aushadhi medicines undergo strict NABL lab quality tests and meet standard pharmacopoeia norms."}
        ],
        "last_updated": "19 Sep 2025",
        "view_count": 8300
    },
    {
        "id": "pmgdisha",
        "code": "GOI/MeitY/2024/0207",
        "name": "PMGDISHA Digital Literacy Scheme",
        "name_native": "प्रधानमंत्री ग्रामीण डिजिटल साक्षरता अभियान",
        "category": "it-science",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Electronics and Information Technology (MeitY)",
        "summary": "Free 20-hour digital literacy training for rural citizens to learn computer skills, smartphones, UPI digital payments, and e-governance.",
        "description": "Pradhan Mantri Gramin Digital Saksharta Abhiyan (PMGDISHA) empowers 6 crore rural households by imparting digital literacy skills.",
        "benefit_amount": "Free 20-Hour Digital Literacy Course + Government Certificate",
        "benefit_type": "Scholarship",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://www.pmgdisha.in",
        "min_age": 14,
        "max_age": 60,
        "gender_allowed": "any",
        "income_ceiling": 500000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Digitally illiterate person in a rural household aged between 14 and 60 years",
            "Only one person per eligible rural family"
        ],
        "highlights": [
            "Hands-on training in operating computers, tablets, and smartphones",
            "Learning BHIM UPI, net banking, email, and online government services",
            "Official MeitY Govt Certificate upon passing proctored test"
        ],
        "benefits_breakdown": [
            "Free 20-hour training course",
            "Govt certified digital badge and physical certificate"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Active Mobile Number"
        ],
        "application_steps": [
            "Visit nearest CSC (Common Service Centre) training center",
            "Provide Aadhaar for biometrics registration",
            "Complete 20 hours of training module and appear for online exam"
        ],
        "faqs": [
            {"q": "Is there any fee for training or certificate?", "a": "No, PMGDISHA is 100% free of cost funded by Government of India."}
        ],
        "last_updated": "24 Sep 2025",
        "view_count": 9100
    },
    {
        "id": "inspire-scholarship",
        "code": "GOI/DST/2024/0208",
        "name": "INSPIRE Scholarship for Higher Education (SHE)",
        "name_native": "इंस्पायर उच्च शिक्षा छात्रवृत्ति योजना",
        "category": "it-science",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Department of Science and Technology (DST)",
        "summary": "Prestigious scholarship of Rs 80,000 per year for top 1% Class 12 science graduates pursuing Natural and Basic Sciences (B.Sc / M.Sc).",
        "description": "Innovation in Science Pursuit for Inspired Research (INSPIRE) SHE scheme attracts talent to study natural and basic sciences at university degree level.",
        "benefit_amount": "Rs 80,000 / year (Rs 60,000 cash + Rs 20,000 mentorship grant)",
        "benefit_type": "Scholarship",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://online-inspire.gov.in",
        "min_age": 17,
        "max_age": 22,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": True,
        "farmer_only": False,
        "additional_eligibility": [
            "Top 1% aggregate percentile in Class 12 board examination (Science stream)",
            "Pursuing B.Sc., B.S., or 5-year Integrated M.Sc. in Natural & Basic Sciences"
        ],
        "highlights": [
            "Rs 60,000 direct annual scholarship stipend",
            "Rs 20,000 annual summer research project mentorship grant",
            "Direct mentorship by national academy scientists"
        ],
        "benefits_breakdown": [
            "Total Rs 4,00,000 support over 5 years (B.Sc + M.Sc)"
        ],
        "documents_required": [
            "Class 12 Marksheet & Board Cut-off Advisory Letter",
            "Aadhaar Card",
            "College Admission Verification Certificate",
            "Bank Account Passbook"
        ],
        "application_steps": [
            "Register on online-inspire.gov.in portal",
            "Upload Class 12 marksheet and college admission proof",
            "Submit online application before DST deadline"
        ],
        "faqs": [
            {"q": "What subjects are covered?", "a": "Physics, Chemistry, Mathematics, Biology, Statistics, Geology, Astrophysics, Botany, Zoology."}
        ],
        "last_updated": "23 Sep 2025",
        "view_count": 14100
    },
    {
        "id": "khelo-india",
        "code": "GOI/MYAS/2024/0209",
        "name": "Khelo India Youth & Talent Development Scheme",
        "name_native": "खेलो इंडिया युवा खेल विकास योजना",
        "category": "sports",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Youth Affairs and Sports",
        "summary": "Financial stipend of Rs 5 Lakh per year for 8 consecutive years awarded to 1,000 talented young athletes across India.",
        "description": "Khelo India aims to revive sports culture in India at the grass-root level by identifying young athletic talent and supporting their long-term training.",
        "benefit_amount": "Rs 5,00,000 / year for 8 years + World-Class Coaching",
        "benefit_type": "Scholarship",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://kheloindia.gov.in",
        "min_age": 10,
        "max_age": 21,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Selected through Khelo India Youth Games / School Games talent identification drive",
            "Age group U-17 and U-21"
        ],
        "highlights": [
            "Rs 5 Lakh per annum financial support for 8 years",
            "Covers diet, equipment, international training, and sports science",
            "Free admission to National Sports Academies and SAI Centers"
        ],
        "benefits_breakdown": [
            "Rs 1.2 Lakh out-of-pocket allowance",
            "Rs 3.8 Lakh academy training, lodging, and tournament travel"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Birth Certificate",
            "National / State Sports Achievement Certificates"
        ],
        "application_steps": [
            "Register on Khelo India Athlete Portal (kheloindia.gov.in)",
            "Participate in District / State talent identification trials",
            "Get empaneled under Khelo India Academy scholarship"
        ],
        "faqs": [
            {"q": "How many athletes are selected every year?", "a": "1,000 top talented athletes are selected annually across sports disciplines."}
        ],
        "last_updated": "20 Sep 2025",
        "view_count": 10500
    },
    {
        "id": "tele-law",
        "code": "GOI/MoLJ/2024/0210",
        "name": "Tele-Law Portal (NALSA Legal Aid via CSC)",
        "name_native": "टेली-लॉ सेवा (सीएससी मुफ्त कानूनी सलाह)",
        "category": "law-justice",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Law & Justice & NALSA",
        "summary": "Free pre-litigation legal advice and video/voice consultation with panel lawyers via Common Service Centres (CSCs) for marginalized citizens.",
        "description": "Tele-Law connects vulnerable citizens in rural areas with Panel Lawyers through video conferencing and telephone facilities available at CSCs.",
        "benefit_amount": "Free Lawyer Consultation + Legal Drafting Support",
        "benefit_type": "Subsidy",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "Ongoing",
        "apply_url": "https://www.tele-law.in",
        "min_age": 18,
        "max_age": 99,
        "gender_allowed": "any",
        "income_ceiling": 300000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Free for Women, Children, SC/ST, PwD, Disaster victims, and Low-income citizens (income < Rs 3L)"
        ],
        "highlights": [
            "Instant video call consultation with high court / district panel advocates",
            "Covers land disputes, marital issues, consumer cases, labor rights, and criminal grievances",
            "Free case registration at 2.5 Lakh CSC VLE centers"
        ],
        "benefits_breakdown": [
            "Zero advice fee for eligible categories",
            "Free document drafting support"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Category Proof (Caste/Income/Disability) if applicable"
        ],
        "application_steps": [
            "Visit nearest CSC center or download Tele-Law Citizen App",
            "Describe legal issue to VLE operator",
            "Connect with Panel Lawyer via video call and receive legal advice"
        ],
        "faqs": [
            {"q": "Is advice confidential?", "a": "Yes, all consultations between lawyer and citizen are strictly confidential and privileged."}
        ],
        "last_updated": "25 Sep 2025",
        "view_count": 6200
    },
    {
        "id": "pmkvy",
        "code": "GOI/MSDE/2024/0211",
        "name": "PM Kaushal Vikas Yojana 4.0 (PMKVY)",
        "name_native": "प्रधानमंत्री कौशल विकास योजना 4.0",
        "category": "employment",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Skill Development and Entrepreneurship",
        "summary": "Free industry-aligned short term skill training, Industry 4.0 courses (AI, Robotics, Drones), and NSDC certification with job placement.",
        "description": "PMKVY 4.0 empowers youth by providing industry-relevant skill training in emerging technology and manufacturing sectors.",
        "benefit_amount": "Free Skill Training + NSDC Certification + Placement Support",
        "benefit_type": "Scholarship",
        "application_mode": "Both",
        "status": "Open",
        "deadline": "31 Dec 2025",
        "apply_url": "https://www.pmkvyofficial.org",
        "min_age": 15,
        "max_age": 45,
        "gender_allowed": "any",
        "income_ceiling": 10000000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Indian school/college dropout or unemployed youth aged 15 to 45 years"
        ],
        "highlights": [
            "100% government funded training",
            "On-the-job training (OJT) and industry apprenticeship",
            "NSDC certified digital skill credential"
        ],
        "benefits_breakdown": [
            "Free short-term course (200-400 hours)",
            "Assessment and certification fee fully waived"
        ],
        "documents_required": [
            "Aadhaar Card",
            "Educational Qualification Certificate",
            "Bank Account details"
        ],
        "application_steps": [
            "Register on Skill India Digital portal (skillindiadigital.gov.in)",
            "Enroll in nearest Pradhan Mantri Kaushal Kendra (PMKK)",
            "Complete course and assessment to get certified"
        ],
        "faqs": [
            {"q": "Are drone pilot and AI courses available?", "a": "Yes, PMKVY 4.0 includes Drone Pilot Training, AI, 3D Printing, and IoT."}
        ],
        "last_updated": "22 Sep 2025",
        "view_count": 16800
    },
    {
        "id": "pmay-u",
        "code": "GOI/MoHUA/2024/0212",
        "name": "PM Awas Yojana - Urban 2.0 (PMAY-U)",
        "name_native": "प्रधानमंत्री आवास योजना - शहरी 2.0",
        "category": "housing",
        "scheme_type": "Central",
        "state": "All India",
        "ministry": "Ministry of Housing and Urban Affairs",
        "summary": "Interest subvention subsidy of Rs 1.80 Lakh to Rs 2.67 Lakh on home loans for EWS and LIG urban families.",
        "description": "Pradhan Mantri Awas Yojana - Urban 2.0 provides interest subsidy and central assistance to urban poor and middle class families to construct or purchase a pucca home.",
        "benefit_amount": "Up to Rs 2,67,000 Credit Linked Interest Subsidy",
        "benefit_type": "Housing",
        "application_mode": "Online",
        "status": "Open",
        "deadline": "31 Dec 2026",
        "apply_url": "https://pmay-urban.gov.in",
        "min_age": 18,
        "max_age": 70,
        "gender_allowed": "any",
        "income_ceiling": 900000.0,
        "caste_eligibility": ["general", "obc", "sc", "st"],
        "bpl_required": False,
        "disability_required": False,
        "student_only": False,
        "farmer_only": False,
        "additional_eligibility": [
            "Urban family that does not own a pucca house anywhere in India",
            "Annual family income up to Rs 3 Lakh (EWS) or Rs 6 Lakh (LIG)"
        ],
        "highlights": [
            "Interest subsidy up to 6.5% on housing loans up to Rs 6 Lakh",
            "Direct subsidy credited upfront to home loan account reducing EMI",
            "Female ownership / co-ownership mandatory for EWS/LIG houses"
        ],
        "benefits_breakdown": [
            "Subsidy amount up to Rs 2,67,000 credited directly to home loan principal"
        ],
        "documents_required": [
            "Aadhaar Card of all family members",
            "Income Certificate / ITR / Salary slip",
            "Approved construction plan / Home loan sanction letter",
            "Self-declaration patta of no pucca house"
        ],
        "application_steps": [
            "Apply online through PMAY-U portal or bank housing loan counter",
            "Submit Aadhaar, urban domicile, and income details",
            "Track Application status and receive CLSS subsidy in loan account"
        ],
        "faqs": [
            {"q": "How is subsidy paid?", "a": "Subsidy is credited upfront to the loan account of beneficiary by National Housing Bank (NHB), reducing monthly EMI."}
        ],
        "last_updated": "24 Sep 2025",
        "view_count": 13900
    }
]

def init_db_data(db):
    # Upsert all schemes to ensure all new schemes and scholarships are present in SQLite
    for data in SEED_SCHEMES:
        existing = db.query(Scheme).filter(Scheme.id == data["id"]).first()
        if not existing:
            scheme = Scheme(**data)
            db.add(scheme)
        else:
            for k, v in data.items():
                setattr(existing, k, v)
    db.commit()

