### Installing and creating virtual env
step 1 - Installing virtualenv

    pip install virtualenv

step 2 - Creating virtualenv

    virtualenv -p python3 <virtualenv_name>

step 3 - Activating virtualenv

    source <virtualenv_name>/bin/activate

### Starting the application
After activating the virtualenv do the following

step 1 - Move to project directory
    
    cd WeatherAPI

step 2 - Installing the requirements
    
    pip install -r requirement.txt

step 3 - Run Django server 

    python manage.py runserver

step 3 - For results, go to browser 

    http://127.0.0.1:8000/search/<city>/<country>

    
### Running the test cases:

Run the following command on terminal - 

    python manage.py test --pattern='test_*.py'

### Technologies Used:

Language: Python 3
Framework : Django
