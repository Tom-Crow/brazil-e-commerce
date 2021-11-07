# brazil-e-commerce

Personal project looking at Brazilian e-commerce data provided by Olist. Dataset and information is available [here](https://www.kaggle.com/olistbr/brazilian-ecommerce).

## Setup
The project uses Python 3.8. To run and set up a virtual environment locally, run:
```bash
python3.8 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

cp .env.example .env
```

There is a script to set up a Dockerised postgres database. To do this run:
```bash
scripts/init_db.sh
```
and input "brazilpw" on all prompts.

To populate the database, activate the virtual environment and run:
```bash
PYTHONPATH=. python scripts/init_db.py
```

The database schema is as below:
![Database Schema](https://i.imgur.com/HRhd2Y0.png "Database Schema")
