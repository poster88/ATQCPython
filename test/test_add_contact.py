from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Second uncle", middlename="Bob", email="uncle.bob@gmail.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", email=""))
