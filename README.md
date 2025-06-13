# 💧 Smart Water Network

**Smart Water Network** is a Django-based web application designed to analyze, optimize, and control water distribution systems using advanced algorithms such as Genetic Algorithm (GA), Particle Swarm Optimization (PSO), Ant Colony Optimization (ACO), and Model Predictive Control (MPC). It leverages the `wntr` toolkit for hydraulic simulation.

---

## 🚀 Features

- Upload and visualize EPANET .inp files
- Run hydraulic simulations using the WNTR toolkit
- Optimize network performance using:
  - Genetic Algorithm (GA)
  - Particle Swarm Optimization (PSO)
  - Ant Colony Optimization (ACO)
  - Model Predictive Control (MPC)
- Display analytical results with graphical plots
- User authentication and session-based analysis storage

---

## 🛠️ Technologies Used

- Python 3.13
- Django 5.1.7
- WNTR (Water Network Tool for Resilience)
- NumPy, SciPy, Matplotlib
- Gunicorn, Whitenoise
- PostgreSQL (Render-hosted DB recommended)

---

## 📦 Installation

```bash
git clone https://github.com/eKidenge/smartwater.git
cd smartwater
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt


 Environment Variables
Set the following in your .env or Render dashboard:
SECRET_KEY=your-django-secret-key
DEBUG=False
DJANGO_SETTINGS_MODULE=smartwater.settings
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=your_postgres_db_url_if_any



Running Locally:
python manage.py migrate
python manage.py runserver
