PROJECT NAME: SAKLOLO: DISASTER MANAGEMENT WEBSITE 

Saklolo is a disaster management system that serves as a preparedness, response, and recovery aid for Filipinos. Users are able to post their own incident reports onto a feed, wherein reports from other areas can also be found. Through the website, users also gain information on disaster statuses and updates. We wanted to develop an accessible disaster management system that can reach a vast majority of Filipinos.

DEPENDENCIES AND PACKAGES:

This project uses the following dependencies and packages:
- (For Python 3.10)
1. asgiref 3.7.2
2. Django 3.2
3. crispy-bootstrap4 2022.1
4. django-crispy-forms 2.0
5. gunicorn 21.2.0
6. Pillow 9.4.0
7. psycopg2-binary 2.9.6
8. pytz 2022.7
9. whitenoise 6.5.0

HOW TO RUN THE PROJECT (ADMIN VIEW):
1. Clone the repository to your local machine:
   - git clone https://github.com/Ayvanne/ITMGT-25.03-FINAL-PROJECT.git
2. Change into the project directory:
   - cd 'file path'
3. Install project dependencies from requirements.txt:
   - pip install -r requirements.txt
   - Note: Use this if you have python 3.10, if not, install the package version that is compatible with your python version
4. Apply database migrations:
   - python manage.py migrate
5. Create a superuser to access the admin panel:
   - python manage.py createsuperuser
6. Run the development server:
   - python manage.py runserver
7. Access the Admin View at:
   - http://127.0.0.1:8000/admin/

HOW TO RUN THE PROJECT (USER VIEW)
1. Follow the instructions in the "ADMIN VIEW," but omit the sixth step.
2. Access the User View at:
   - (http://127.0.0.1:8000/)
