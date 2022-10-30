# Django_Vue
Template for Vue3 and Django Application
Reference:https://realpython.com/python-virtual-environments-a-primer/

### [ 1 ] Prepare basic project enviorment and create an virtual enviorment of python

1. Create a folder in computer to storage the project file and open a terminal in this folder:

 >git clone https://github.com/sweetbao/IRS-PM-2022-10-17-IS04FT-GRP10-Paper-Recommendation-System.git

 >cd IRS-PM-2022-10-17-IS04FT-GRP10-Paper-Recommendation-System

 >python -m venv venv

 >venv\Scripts\activate(windows) OR: source venv/bin/activate(mac)

 >pip install -r requirements.txt

3. go to download sqlite3 https://drive.google.com/file/d/1Wx-D0MNJ-t3G0dlp2LwvJEfDTWxXHP5p/view

4. Use the download file replace the old sqlite3 file in backend folder

### [ 2 ] Deploy the Paper Recommendation system locally with virtual enviorment just created

1. In project folder terminal: 
 >cd backend

 >python manage.py runserver (ignore the migrate error)

2. Open an other terminal in project folder:

 >cd frontend

 >npm install (optional:npm audit fix)

 >npm fund 

 >npm run dev
