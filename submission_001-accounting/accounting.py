import user.authentication
import transactions.journal
import banking
import sys
import requests

for i in range (1, len(sys.argv)):
    print (sys.argv[i])

user.authentication.authenticate_user()
transactions.journal.receive_income(100)
transactions.journal.pay_expense(100)
banking.fvb.reconciliation.do_reconciliation()


'''
help("modules")
'''
