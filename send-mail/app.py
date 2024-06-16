from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)  

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ramanandkumawat87@gmail.com'
app.config['MAIL_PASSWORD'] = 'wvciwvelpmyrngxk'  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/send-email", methods=['POST'])
def send_email():
    data = request.get_json()
    receiver_email = data.get('receiver_email')
    subject = data.get('subject')
    body_text = data.get('body_text')
    
    if not receiver_email or not subject or not body_text:
        return jsonify({"error": "Missing required fields"}), 400
    
    msg = Message(
        subject,
        sender='ramanandkumawat87@gmail.com',
        recipients=[receiver_email]
    )
    msg.body = body_text
    
    try:
        mail.send(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
