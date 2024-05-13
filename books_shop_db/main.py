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


def info_salle(publisher_):


    q = (session.query(Publisher, Book.title, Shop.name, Sale.price, Sale.date_sale)
         .join(Book)
         .join(Stock)
         .join(Shop)
         .join(Sale)
         )
    if publisher_.isdigit():
        res = q.filter(Publisher.id == publisher_).all()
    else:
        res = q.filter(Publisher.name.like(publisher_)).all()
    for i in res:
        print(f"{i.title: <40} | {i.name: <10} | {i.price: <8} | {i.date_sale.strftime("%d-%m-%Y")}")

session.close()
if __name__ == "__main__":

    info_ = input("Введите id или имя издателя: ")
    info_salle(info_)