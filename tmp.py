from database.config import session_local
from database.models import * 

db = session_local()

q = {
    "subject":["Plan 1️⃣" ,"Plan 2️⃣", "Plan 3️⃣", "Plan 4️⃣", "Plan 5️⃣"],
    "region":["Ireland" ,"England", "America", "Iraq", "France"],
    "volume":[100, 30, 20, 10, 5],
    "price":[800000, 100000, 30000, 20000, 15000, 10000]
}

for i in range(len(q) + 1):
    new = Product(subject=q["subject"][i], region=q["region"][i], volume=q["volume"][i], price=q["price"][i])
    db.add(new)
    db.commit()
    print(i)
    

# db.query(Product).delete()
# db.commit()

# new = Product(subject="Plan 1", region="germany", volume=20)
# db.add(new)
# db.commit()
# db.close()

# d = db.query(User).filter(User.id==1).first()
# d.is_admin = True
# db.commit()
