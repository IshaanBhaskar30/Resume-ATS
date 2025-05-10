📄 ATS Resume Analyzer with Gemini

🎯 Project Overview

This Streamlit-based application evaluates resumes against job descriptions using Google’s Gemini 1.5 Flash model. It mimics both a seasoned technical recruiter and an advanced Applicant Tracking System (ATS), offering deep insight into resume-job fit and keyword alignment — all through an intuitive UI.

The app supports modern PDF resumes and job descriptions, analyzes them semantically, and outputs structured feedback such as resume strengths, weaknesses, missing keywords, and match percentage — helping users improve their chances of clearing automated HR screening systems.

🧰 Key Features

✅ Upload your resume in PDF format for instant analysis

🧠 Gemini-powered reasoning to evaluate how well your resume aligns with your job description

📊 ATS-style score breakdown, including match percentage and missing keywords

🧾 Human-style evaluation that highlights your strengths and areas to improve

🔐 Secure API key input for using Gemini models


⚙️ How It Works

->The user provides a job description and uploads their resume.

->The resume is internally converted from PDF to image for Gemini multi-modal input.

->The app offers two modes:

    o Resume Fit Evaluation: A qualitative assessment like a hiring manager would provide.

    o ATS Percentage Match: A quantitative breakdown with a match score and keyword analysis.

->Gemini 1.5 Flash processes both resume and JD to generate results in seconds.

🖥️ UI Overview

->Sidebar:

    o Google API Key input

    o App stops gracefully if no key is provided

->Main Panel:

    o Text area for job description input

    o File uploader for resume (PDF format)

    o Two buttons:

        o “🔍 Evaluate Resume Fit”

        o “📊 Percentage Match (ATS Style)”

    o Rich output display: HR-style feedback or ATS-style match score

    o Interactive and user-friendly interface with success indicators

🚀 Deployment Note for Streamlit Cloud

->To ensure smooth deployment on Streamlit Cloud, the app includes a packages.txt file with the following entry:

    o poppler-utils

This ensures that Poppler, which is required by the pdf2image library to convert PDFs to images, is installed automatically in the Streamlit Cloud environment. Without it, the resume parsing feature will not function properly.

    o ✅ No manual setup is required—Streamlit Cloud will detect packages.txt and install the necessary dependency.
