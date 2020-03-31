from loan import db
from datetime import datetime


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    location = db.Column(db.String(20))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    loan_amount = db.Column(db.Integer, nullable=False)
    period = db.Column(db.Integer, nullable=False)
    interest_rate = db.Column(db.Integer, nullable=False)
    total_loan = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Member('{self.id_number}, {self.name}, {self.location}, {self.date}, {self.loan_amount}," \
               f" {self.total_loan}') "
