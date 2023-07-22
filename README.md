PROJECT NAME: SAKLOLO: DISASTER MANAGEMENT WEBSITE 

Saklolo is a disaster management system that serves as a preparedness, response, and recovery aid for Filipinos. Users are able to post their own incident reports onto a feed, wherein reports from other areas can also be found. Through the website, users also gain information on disaster statuses and updates. We wanted to develop an accessible disaster management system that can reach a vast majority of Filipinos.

DEPENDENCIES AND PACKAGES:

This project uses the following dependencies and packages:
1. asgiref==3.4.1
2. Django==3.2.7
3. django-bootstrap4==3.0.1
4. django-crispy-forms==1.12.0
5. gunicorn==20.1.0
6. Pillow==8.3.1
7. psycopg2==2.9.1
8. pytz==2021.1
9. whitenoise==5.3.0


HOW TO RUN THE PROJECT (ADMIN VIEW):
1. Clone the repository to your local machine:
   - git clone https://github.com/Ayvanne/ITMGT-25.03-FINAL-PROJECT.git
2. Change into the project directory:
   - cd project/
3. Create and activate a virtual environment (optional, but recommended):
   - python -m venv env
   - source env/bin/activate
4. Install project dependencies from requirements.txt:
   - pip install -r requirements.txt
5. Apply database migrations:
   - python manage.py migrate
6. Create a superuser to access the admin panel:
   - python manage.py createsuperuser
7. Run the development server:
   - python manage.py runserver
8. Access the Admin View at:
   - http://127.0.0.1:8000/admin/

HOW TO RUN THE PROJECT (USER VIEW)
1. Follow the instructions given in the "ADMIN VIEW," but omit the sixth step.
2. Access the Customer View at:
   - (http://127.0.0.1:8000/)
