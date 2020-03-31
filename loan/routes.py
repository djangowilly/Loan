from flask import render_template, flash, redirect, url_for
from loan import app
from loan.forms import *
from loan.models import *


@app.route('/')
def home():
    loans = Loan.query.all()
    return render_template('home.html', loans=loans)


@app.route('/loan', methods=['GET', 'POST'])
def loan():
    form = LoanForm()
    if form.validate_on_submit():
        try:
            total_loan = round(form.loan_amount.data * form.interest_rate.data / 100 * form.period.data)
            amount = Loan(loan_amount=form.loan_amount.data, interest_rate=form.interest_rate.data,
                          period=form.period.data, total_loan=total_loan, name=form.name.data,
                          id_number=form.id_number.data, location=form.location.data)
            db.session.add(amount)
            db.session.commit()
        except ValueError:
            return redirect(url_for('loan'))
        flash(f"successful !", 'success')
        return redirect(url_for('home'))
    return render_template('loan.html', form=form)
