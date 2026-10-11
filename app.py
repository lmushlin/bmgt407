from flask import Flask, render_template

app = Flask(__name__)

# Customer/Public Routes

@app.route('/')
def homepage():
    return "This is Elcys Website."

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/customize/<item_id>')
def customize(item_id):
    return render_template('customize_item_id.html')

@app.route('/process-order', methods=['POST'])
def process_order():
    return render_template('process_order.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/order-confirmation/<order_id>')
def order_confirmation(order_id):
    return render_template('order_confirmation_order_id.html')

# Authentication Routes
# GET = show loging page; POST = submit login credentials

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    return render_template('logout.html')

# Kitchen/Staff Routes

@app.route('/kitchen/queue')
def kitchen_queue():
    return render_template('kitchen_queue.html')

@app.route('/update-order-status', methods=['POST'])
def update_order_status():
    return render_template('update_order_status.html')

@app.route('/kitchen/ticket/<order_id>')
def kitchen(order_id):
    return render_template('kitchen_ticket_order_id.html')

@app.route('/kitchen/pause-controls')
def kitchen_pause_controls():
    return render_template('kitchen_pause_controls.html')

@app.route('/update-pause-status', methods=['POST'])
def update_pause_status():
    return render_template('update_pause_status.html')

# Admin Routes

@app.route('/admin/menu')
def admin_menu():
    return render_template('admin_menu.html')

@app.route('/admin/menu/update', methods=['POST'])
def admin_menu_update():
    return render_template('admin_menu_update.html')

@app.route('/admin/analytics')
def admin_analytics():
    return render_template('admin_analytics.html')

@app.route('/admin/ai-chat', methods=['POST'])
def admin_ai_chat():
    return render_template('admin_ai_chat.html')

if __name__ == '__main__':
    app.run(debug=True)