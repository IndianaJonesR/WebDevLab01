
#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "Images/profile.jpg"
about_me = "Hey, I'm Rohit Naras. I study Computer Engineering at Georgia Tech, with interests in machine learning, quantitive finance, and startups"


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/spongebob-squarepants-44b857281/"
my_github_url = "https://github.com/IndianaJonesR"
my_email_address = "rnaras3@gatech.edu"


education_data ={
    'Degree': 'Bachelor of Science in Computer Engineering',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'May 2028',
    'GPA': 'N/A'
}
course_data = {
    "code":["CS 1301", "PHYS 2211", "MATH 1554", "ENGL 1012", "APPH 1040"], 
    "names":["Intro to CS", "Physics 1", "Linear Algebra", "English 2", "Applied Physiology"], 
    "semester_taken":["1st", "1st", "1st", "1st", "1st"],
    "skills":["Loops, Conditionals, Functions", "Kinematics, Forces, and Newton's Laws", "Row reduction, Gauss-Jordan Elimination, and Matrix Inverses", 
    "Watched TONS of movies", "Learnt how to manage time and control stress"],
    }
experience_data = {
    "Machine Learning Research Intern – Georgia Institute of Technology": (
        [
            "- Built and trained a custom CNN in PyTorch on CIFAR-10 dataset, exported to TorchScript",
            "- Integrated TorchScript model into a C++ inference pipeline and inspected forward pass with GDB",
            "- Performed runtime memory analysis of tensor objects and validated against PyTorch source structures",
            "- Captured memory with LiME and wrote a Volatility plugin to recover model internals"
        ],
        "images/ml_research.jpg"
    ),
    
    "Co-Founder & Lead Fullstack Developer – Acceptional (tryacceptional.com)": (
        [
            "- Engineered a full-stack TypeScript app with React/Vite and shadcn/Tailwind CSS",
            "- Architected a Supabase backend with PostgreSQL, RLS, and Auth for secure data management",
            "- Developed serverless booking APIs with custom Supabase Edge Functions",
            "- Integrated Stripe payment processing with webhooks for secure transaction handling"
        ],
        "images/acceptional.jpg"
    ),
    
    "Genesis Staff Member – Startup Exchange at Georgia Tech": (
        [
            "- Developed and delivered presentation slide decks for a cohort of 140+ members",
            "- Advised new builders on idea validation strategies and online engagement growth",
            "- Instructed members on leveraging AI coding tools to accelerate MVP development"
        ],
        "images/genesis.jpg"
    )
}


projects_data = {
    "Algorithmic Options Trading": (
        "Engineered a Python event-driven trading system with asyncio and aiohttp; "
        "integrated Tradier REST API endpoints for option chain retrieval, order placement, and account management; "
        "deployed natural language trade parsing via OpenAI API with Discord WebSocket alerts; "
        "built a FastAPI/Flask hybrid service for REST endpoints."
    ),
    
    "Transformer Quantum State": (
        "Extended a pre-trained Transformer model with custom embedding dimensions for new parameters; "
        "built preprocessing pipeline with Scikit-learn MinMaxScaler for high-dimensional input normalization; "
        "applied transfer learning with AdamW to reduce MSE and overfitting; "
        "implemented evaluation workflows with PyTorch Lightning for reproducibility."
    ),
    
    "TSA Time Series Forecasting": (
        "Ingested TSA daily checkpoint data with requests and aggregated volumes in Pandas; "
        "trained Facebook Prophet models capturing trend, seasonality, and holidays; "
        "evaluated predictions with Scikit-learn metrics (RMSE, MAPE) and visualized intervals in Matplotlib; "
        "generated forecast-driven signals to inform Kalshi TSA passenger volume trading strategies."
    ),
    
    "Stock Market Quiz": (
        "Developed an interactive Streamlit quiz with 5 investment-focused questions that generates a personalized summary using OpenAI."
    )
}



programming_data = {
    "Python": 90,
    "Java": 75,
    "C": 25,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}
spoken_icons = {
    "English": "🇬🇧",
    "Kannada":"🇮🇳"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "Kannada": "Fluent",
}
leadership_data = {
    "Genesis Staff Member – Startup Exchange at Georgia Tech": (
        [
            "- Developed and delivered presentation slide decks for a cohort of 140+ members",
            "- Advised new builders on idea validation strategies and methods for organic growth",
            "- Instructed members on leveraging AI coding tools to accelerate MVP development"
        ],
        "images/genesis.jpg"
    ),
}

activity_data = {
    "Tennis": [
        "- Competed recreationally and in school events, developing discipline and focus",
        "- Organized casual matches with peers to build teamwork and sportsmanship"
    ]
}