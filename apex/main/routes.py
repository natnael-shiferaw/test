from flask import render_template, Blueprint
from apex.models import Property, Agent
main = Blueprint('main', __name__)

@main.route('/')
@main.route("/home")
def home():
    # Fetches the latest 3 properties
    latest_properties = Property.query.order_by(Property.id.desc()).limit(3).all()
  # Fetch all the Agents in the database.
    agents = Agent.query.all()

  
    return render_template('home.html', latest_properties=latest_properties, agents=agents)

@main.route("/buy")
def buy():
    for_sale = Property.query.filter_by(listing_type='sale').all()
    # Query to get the total number of properties for sale
    total_properties_for_sale = Property.query.filter_by(listing_type='sale').count()
    return render_template('buy.html', for_sale=for_sale, total_properties_for_sale=total_properties_for_sale)

@main.route("/rent")
def rent():
    for_rent = Property.query.filter_by(listing_type='rent').all()
    # Query to get the total number of properties for rent
    total_properties_for_rent = Property.query.filter_by(listing_type='rent').count()
    return render_template('rent.html', for_rent=for_rent, total_properties_for_rent=total_properties_for_rent)

@main.route("/listings")
def listings():
    all_properties = Property.query.all()
    # Query to get the total number of properties for rent
    total_properties = Property.query.count()
    return render_template('listings.html', all_properties=all_properties, total_properties=total_properties)

@main.route("/property_details/<property_id>")
def property_details(property_id):
    property_details = Property.query.filter_by(id=property_id).first()
    return render_template('home_property_details.html', property_details=property_details)


@main.route("/sell")
def sell():
    return render_template('sell.html')

@main.route("/contact")
def contact():
    return render_template('contact.html')

@main.route("/about")
def about():
    return render_template('about.html')

@main.route("/agent_details/<agent_id>")
def agent_details(agent_id):
    agent_details = Agent.query.filter_by(id=agent_id).first()
    return render_template('agent_details.html', agent_details=agent_details)