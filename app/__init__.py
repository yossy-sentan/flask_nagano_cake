from flask import Flask
# from flask_bootstrap import Bootstrap
from lib.db import init_db
from flask_login import LoginManager

app = Flask(__name__, static_folder='static')
app.config.from_object('app.config.config')
app.config.from_object('app.config.admin.config')
app.config.from_object('lib.config')

# bootstrap = Bootstrap(app)

init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'public_session.new'

from .views.admin import homes, sessions, genres, items, customers, orders, order_items
app.register_blueprint(homes.home)
app.register_blueprint(sessions.admin_session)
app.register_blueprint(genres.genre)
app.register_blueprint(items.item)
app.register_blueprint(customers.customer)
app.register_blueprint(orders.order)
app.register_blueprint(order_items.order_item)

from .views.public import homes, customers, sessions, items, carts, orders, addresses
app.register_blueprint(homes.home)
app.register_blueprint(customers.customer)
app.register_blueprint(sessions.public_session)
app.register_blueprint(items.item)
app.register_blueprint(carts.cart)
app.register_blueprint(orders.order)
app.register_blueprint(addresses.address)