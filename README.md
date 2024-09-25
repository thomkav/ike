# Iterative Knowledge Extractor (IKE)

IKE is an advanced system designed to extract, accumulate, and refine knowledge from a corpus of documents using large language models (LLMs). The core innovation of IKE lies in its iterative approach, allowing it to build a dynamic, self-improving knowledge base that becomes more accurate and comprehensive over time.

## Table of Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Scalable framework for processing large sets of documents
- LLM-powered information extraction techniques
- Adaptive knowledge base with built-in conflict resolution
- Context-aware re-extraction for continuous knowledge refinement
- Interactive dashboard for visualizing and querying the knowledge base

## Technology Stack
- Python 3.9+
- Django 5.1.1
- PostgreSQL 14.x
- Neo4j 5.24.0
- Anthropic API (Claude)
- Django Rest Framework 3.15.2
- Streamlit 1.38.0

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-organization/ike.git
   cd ike
   ```
2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up the databases:
   - Install and configure PostgreSQL
   - Install and configure Neo4j
5. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file with your database credentials and Anthropic API key.
6. Run migrations:
   ```
   python manage.py migrate
   ```

## Usage
1. Start the Django development server:
   ```
   python manage.py runserver
   ```
2. Access the Django admin interface at `http://localhost:8000/admin`
3. For the Streamlit dashboard:
   ```
   streamlit run dashboard/app.py
   ```
   Access the dashboard at `http://localhost:8501`

## Project Structure
```
ike/
├── ike/                 # Django project directory
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/                 # Django app for API
│   ├── views.py
│   ├── serializers.py
│   └── models.py
├── core/                # Core IKE logic
│   ├── extractor/
│   ├── knowledge_base/
│   └── refinement/
├── dashboard/           # Streamlit dashboard
├── tests/               # Unit and integration tests
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── README.md            # This file
```

## Contributing
We welcome contributions to the IKE project. Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to submit issues, feature requests, and pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.