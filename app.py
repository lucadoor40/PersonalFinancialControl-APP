from flask import Flask,jsonify
from models.investment import Investment
from models.transaction import Transaction
from models.salary import Salary
from models.expense import Expense

app=Flask(__name__)

salary=[
    Salary('Amazon',13000)
]

transaction=[
    Transaction('imposto direto', 1300,'governo')
]

investment=[
    Investment('CDB', 78946,1300),
    Investment('BTC', 43245,460),
    Investment('Tesouro Direto', 6297,150),
    Investment('Bolsa Americana', 16896, 560)
]

expense=[
    Expense('Aluguel',2450,'moradia'),
    Expense('Condominio',320,'moradia'),
    Expense('Luz', 200,'fixo'),
    Expense('Agua',120,'fixo'),
    Expense('Internet', 100,'fixo'),
    Expense('Carro',650,'mobilidade'),
    Expense('Barbeiro',50,'estetica'),
    Expense('Academia',120,'saude'),
    Expense('Plano de Saude',400,'saude'),
    Expense('Alimentacao',1000,'comida'),
    Expense('Streaming',100,'entreterimento'),
    Expense('Cartao de Credito',1720,'lazer'),
    Expense('Cachorro',250,'pet'),
    Expense('Viagem',1200,'lazer'),
    Expense('Namorada', 300,'relacionamento'),
    Expense('Video Game',200,'entreterimento')
]

def total_salary():

    return sum(s.salary for s in salary)

def total_transaction():
    return sum(t.value for t in transaction)

def total_expense():

    return sum(e.value for e in expense)

def investment_value_total():

    return sum(i.investment_total for i in investment)

def investment_value_month():
    return sum(i.investment_month for i in investment)

def listar_expense():

    return [e.to_dict() for e in expense]

def listar_transaction():

    return [t.to_dict() for t in transaction]

def listar_investment():

    return [i.to_dict() for i in investment]

def listar_salary():

    return [s.to_dict() for s in salary]

@app.route("/Lucas")
def financeiro():

    return jsonify({
        "salary": listar_salary(),
        "expense": listar_expense(),
        "investment": listar_investment(),

        "total_salary": total_salary(),
        "total_expense": total_expense(),
        "total_investment_value_total": investment_value_total(),
        "total_investment_value_month": investment_value_month(),

        "final_balance": total_salary() - total_expense(),
        "final_balance_without_tax": (total_salary() - total_expense()) - total_transaction(),

    })





if __name__=='__main__':
    app.run(debug=True)