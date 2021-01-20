from flask import Flask
from flask_restful import Api,Resource,reqparse,inputs,abort

app = Flask(__name__)
api = Api(app)

def min_length(min_length):
    def validate(s):
        if len(s) >= min_length:
            return {"message":"Please enter security code less than 3"}
        raise ValidationError("String must be at least %i characters long" % min)
    return validate

fields_ = reqparse.RequestParser()
fields_.add_argument("CreditCardNumber",type=int,help="number required", required=True)
fields_.add_argument("CardHolder",type=str,help="Enter Name", required=True)
fields_.add_argument("ExpirationDate",help="Enter  ExpirationDate", required=True)
fields_.add_argument("SecurityCode",type=min_length(3), location='form',help="enter security code")
fields_.add_argument("Amount",type=float,help="Enter Amount", required=True)

payments = {}

def not_exist(payment_id):
	if payment_id not in payments:
		abort(404, message="Please enter valid payment id")

class ProcessPayment(Resource):
	def get(self,payment_id):
		not_exist(payment_id)
		if len(self.SecurityCode) == 3:
			return payments[payment_id]
		else:
			return {"Response": 400}

	def put(self,payment_id):
		argss = fields_.parse_args()
		if argss.Amount < 20:
			return {"method":"CheapPaymentGateway"}
		elif argss.Amount == range(21,500):
			return {"method":"ExpensivePaymentGateway"}
		elif argss.Amount > 500:
			return {"method":"PremiumPaymentGateway"}
		payments[payment_id] = argss
		return {"message":"success"},201

api.add_resource(ProcessPayment,"/ProcessPayment/<int:payment_id>")

if __name__ == "__main__":
    app.run(debug=True)