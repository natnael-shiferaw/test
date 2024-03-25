from flask import render_template, request, Blueprint
from apex.models import Property
main = Blueprint('main', __name__)

@main.route('/')
@main.route("/home")
def home():
    # Fetch all properties for sale
    for_sale = Property.query.filter_by(listing_type='sale').all()

    # Fetch all properties for rent
    for_rent = Property.query.filter_by(listing_type='rent').all()
    return render_template('home.html', for_sale=for_sale, for_rent=for_rent)

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

@main.route("/property_details")
def property_details():
    return render_template('property_details.html')