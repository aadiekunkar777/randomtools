from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import random as rd
from datetime import date

app = Flask(__name__)

#start with begin function
#once you begin show order option
#take order
#ask for how many orders
#ask for the amount of each
#show option to change if someone has typed it incorrectly
#finalize the order
#some messege first and then we can begin everything

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    msg = request.form.get('Body')
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    # resp.message("What? didn't you see that coming?")


    def begin():
        if msg == "begin":
            resp.message("Hey There ! Would you like to order something ?\n if yes then press 'order'.")
            #asking for order
        else:
            resp.message("SORRY SIR WE DONT DO THAT HERE\nWrite message as 'begin' to get started")
            #if someone is unable to begin and types some other message



    def order():
        global order_dict
        #defining the global variable 'order_dict' for storing the orders and their amounts.
        order_dict = {}
        #creating the dictionary




    def finalord():
        if msg == 'order':
            resp.message("Alright here we go again ! Would you tell me how many orders you have")
            #asking user for total number of orders
        else:
            resp.message("SORRY SIR WE DONT DO THAT HERE\nWrite message as 'order' to start ordering")
            #reply sorry if user enters wrong input as a message



    def changeord():
        if msg == 'change':
            resp.message("Reply as\n1)'change' if you wanna change a order\n2) reply 'remove' if you want to remove your order")
            #asking the user whether he wants to change the whole order or remove some order totally
        elif msg == 'amount':
            resp.message("Name the order you want to change the amount of")
            #asing user to reply the name of the order he/she wants to change
        elif msg == 'delete':
            resp.message("Reply the name of the order you want to remove")


    def finalamount():

        if msg ==
    def placeord():
        #placing the order collected bye yes or no

















if __name__ == "__main__":
    app.run(debug=True)