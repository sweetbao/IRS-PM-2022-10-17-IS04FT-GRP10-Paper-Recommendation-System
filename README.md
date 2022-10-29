# IRS-PM-2022-10-17-IS04FT-GRP10-Paper-Recommendation-System
Read paper every day!！^0^！ The project provides a recommendation system for papers in your interest area.
## SECTION 1 : PROJECT TITLE
## Paper Recommendation System

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
Reference papers and documents are extremely important for academic research, practical operations, and rich our experience. It can not only help students or scholars to enrich their knowledge in this field and keep up with the latest research progress, but also inspire and help follow-up research or topics. According to arXiv’s Category Taxonomy, the current research types can be roughly divided into nine categories: Computer Science, Economics, Electrical Engineering and Systems Science, Mathematics, Physics, Quantitative Biology, Quantitative Finance, and Statistics. Under each category, there are multipl research directions in each field, and each research direction has dozens or even hundreds of keywords. The sheer variety of papers and the abundance of keywords in each subfield make finding interested papers in a certain field becoming a problem.

Our team wants to design a paper recommendation system. By using the system, users can select the research category they are interested in, and select the sub-field of the category, and then select the keywords. We will recommend relevant papers in this field for users to read. It also supports user registration and login, which can record user browsing records, list them as learning objects, and recommend more accurate papers for users.

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION
| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :--------------- |:---------------:| :-----| :-----|
| Bao wudi | A0261805H | System process design, Data feature extraction, Recommendation algorithm design, Model implementation, Model evaluation|E0983199@u.nus.edu  |
| Dai chujia | A0191582Y | Team Lead，Architecture and System Design，Backend Application Development，UI/UX Development，Frontend development，Testing of frontend and backend integration| E0338226@u.nus.edu |
| Du wenlei | A0243809Y | Data Acquisition,Data Processing,Django & Database development,Interface Development for backend |E0838377@u.nus.edu  |
| Huang sijie | A0261685W | UI Design, Front-end Development, Video Documentation/Presentation, Project report writing| E0983079@u.nus.edu |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO


## SECTION 5 : USER GUIDE

### [ 1 ] System Environment Requirement

1. Install [nodejs (npm)>=18.10.0](https://nodejs.org/en/download/) on the computer

2. Install [python >=3.5](https://www.python.org/downloads/)

3. Google Chrome (latest version)

### [ 2 ] Prepare basic project enviorment and create an virtual enviorment of python

1. git clone git@github.com:sweetbao/IRS-PM-2022-10-17-IS04FT-GRP10-Paper-Recommendation-System.git

2. open terminal in the project folder

 >python -m venv venv

 >venv\Scripts\activate(windows) OR: venv/Scripts/activate(mac)

 >pip install -r requirements.txt

3. go to download sqlite3 https://drive.google.com/file/d/1Wx-D0MNJ-t3G0dlp2LwvJEfDTWxXHP5p/view

4. Use the download file replace the old sqlite3 file in backend folder

### [ 3 ] Deploy the Paper Recommendation system locally

1. In project folder terminal: 
 >cd backend

 >python manage.py runserver

2. Open an other terminal in project folder:

 >cd frontend

 >npm install (optional:npm audit fix)

 >npm fund 

 >npm run dev

### [ 4 ] Run the systems on browser
Go to URL using web browser** http://localhost:5173 or http://127.0.0.1:5173
Or: Directly click the link on the frontend terminal

---
## SECTION 6 : PROJECT REPORT / PAPER
## SECTION 7 : MISCELLANEOUS
