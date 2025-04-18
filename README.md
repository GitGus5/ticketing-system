# Ticketing System
     
     A ticketing system with potential AI integration, built with Django and React, deployed on cloud.gov.
     
     ## Prerequisites
     - Python 3.8+
     - Node.js 16+
     - Git
     - cloud.gov account
     
     ## Setup
     1. Clone the repository:

        git clone https://github.com/your-username/ticketing-system.git
        cd ticketing-system
        
     2. Set up the backend:

        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        cd backend
        python manage.py migrate
     

     3. Set up the frontend:

        ./scripts/build_frontend.sh

     4. Run locally:

        cd backend
        python manage.py runserver

     ## Deployment

     - Push to the `main` branch to trigger GitHub Actions deployment to cloud.gov.
     - Ensure GitHub Secrets are configured for cloud.gov credentials.
