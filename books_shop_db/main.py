import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from books_shop_db.models import create_tables, Publisher, Book, Shop, Stock, Sale
login = input("Введите логин PSQL: ")
password = input("Введите пароль PSQL: ")
DSN = f"postgresql://{login}:{password}@localhost:5432/books_db"
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

with open("tests_data.json", "r") as fd:
    data = json.load(fd)
    for add_ in data:
        model = {
            "publisher": Publisher,
            "book": Book,
            "shop": Shop,
            "stock": Stock,
            "sale": Sale,
        }[add_.get("model")]
        session.add(model(id=add_.get("pk1"), **add_.get("fields")))
session.commit()

def info_sale(id_=input("Введите ID писателя:")):
    str_ = ""
    q = (session.query(Publisher, Book.title, Shop.name, Sale.price, Sale.date_sale)
         .join(Book)
         .join(Stock)
         .join(Shop)
         .join(Sale)
         .filter(Publisher.id == id_)
         )

    for c in q.all():
        str_ += f"{c.title} | {c.name} | {c.price} | {c.date_sale} \n"
    return str_
print(info_sale())
session.close()
