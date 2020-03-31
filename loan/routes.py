from flask import render_template, flash, redirect, url_for
from loan import app, db
from loan.forms import LoanForm, MemberForm, CalculatorForm
from loan.models import Loan,  Member, Calculator


@app.route('/')
def home():
    loans = Loan.query.all()
    return render_template('home.html', loans=loans)


# @app.route('/new_member', methods=['GET', 'POST'])
# def new_member():
#     form = MemberForm()
#     if form.validate_on_submit():
#         member = Member(name=form.name.data, id_number=form.id_number.data, location=form.location.data)
#         db.session.add(member)
#         db.session.commit()
#         flash('Member added successfully !', 'success')
#         return redirect(url_for('calculator'))
#     return render_template('new_member.html', form=form)


# @app.route('/calculator', methods=['GET', 'POST'])
# def calculator():
#     form = CalculatorForm()
#     if form.validate_on_submit():
#         try:
#             total_loan = round(form.loan_amount.data * form.interest_rate.data / 100 * form.period.data)
#             amount = Calculator(loan_amount=form.loan_amount.data, interest_rate=form.interest_rate.data,
#                                 period=form.period.data, total_loan=total_loan)
#             db.session.add(amount)
#             db.session.commit()
#             flash(f'Successful')
#             return redirect(url_for('home'))
#         except ValueError:
#             return redirect(url_for('calculator'))
#     return render_template('calculator.html', form=form)


@app.route('/loan', methods=['GET', 'POST'])
def loan():
    form = LoanForm()
    if form.validate_on_submit():
        try:
            amount = Calculator(loan_amount=form.loan_amount.data, interest_rate=form.interest_rate.data,
                                period=form.period.data)
            member = Member(name=form.name.data, id_number=form.id_number.data, location=form.location.data)
            db.session.add(amount, member)
            db.session.commit()
        except ValueError:
            return redirect(url_for('loan'))
        flash(f"successful !", 'success')
        return redirect(url_for('home'))
    return render_template('loan.html', form=form)
