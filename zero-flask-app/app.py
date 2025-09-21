# A simple Flask web server for a customer management web app.

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This list will act as a simple "in-memory database" for demonstration.
customers = []

@app.route('/')
def home():
    """
    Renders the main page of the web application.
    """
    return render_template('index.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    """
    Handles the form submission to add a new customer.
    """
    # Get the form data from the request.
    customer_name = request.form.get('name')
    customer_email = request.form.get('email')

    if customer_name and customer_email:
        # Create a new customer dictionary.
        new_customer = {
            'name': customer_name,
            'email': customer_email
        }
        customers.append(new_customer)
        print(f"Added new customer: {new_customer}")
        
        # Return a JSON response to the front-end.
        return jsonify({'success': True, 'message': customer_name+' added successfully!'})
    else:
        # Handle the case where data is missing.
        return jsonify({'success': False, 'message': 'Please provide both name and email.'}), 400

if __name__ == '__main__':
    # Run the Flask app on port 5000.
    app.run(debug=True, port=5000)
