from application import db
from application.models import Food

db.drop_all()
db.create_all()

caul = Food(
    food = "A Raw Cauliflower"
)
db.session.add(caul)

pie = Food(
    food = "A Freshly Baked Pie"
)
db.session.add(pie
)
spid = Food(
    food = "A Live, Wriggling Spider"
)
db.session.add(spid
)
chick = Food(
    food = "An Entire Roast Chicken"
)
db.session.add(chick)

oink = Food(
    food = "Bacon, Cooked or Raw"
)
db.session.add(oink)

pea = Food(
    food = "Frozen Peas"
)
db.session.add(pea
)
cake = Food(
    food = "A Victoria Sponge"
)
db.session.add(cake)

cream = Food(
    food = "Fresh Cream"
)
db.session.add(cream)

db.session.commit()
