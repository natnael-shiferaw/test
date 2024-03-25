from flask import render_template, request, Blueprint
from apex.models import Property
main = Blueprint('main', __name__)

@main.route('/')
@main.route("/home")
def home():
    # Fetches the latest 3 properties
    latest_properties = Property.query.order_by(Property.id.desc()).limit(3).all()
    return render_template('home.html', latest_properties=latest_properties)

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