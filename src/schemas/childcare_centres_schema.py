from main import ma

class ChildcareCentreSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "cost_per_day", "maximum_capacity", "phone_number", "email_address", "description", "user", "user_id")
        load_only = ["user_id"]

    user = ma.Nested("UserSchema", exclude=["childcare_centre"])


childcare_centre_schema = ChildcareCentreSchema()
childcare_centres_schema = ChildcareCentreSchema(many=True)
