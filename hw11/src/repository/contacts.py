from datetime import date, datetime
from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel, ContactName

async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    return contact


async def get_contacts(db: Session):
    return db.query(Contact).all()


async def get_contact_by_id(contact_id: int, db: Session):
    return db.query(Contact).filter_by(id = contact_id).first()


async def update_contact(body: ContactModel, contact_id, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.birthday = body.birthday
        contact.phone = body.phone
        contact.description = body.description
        db.commit()
    return contact


async def remove_contact(contact_id, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def search_contacts(query: str, db: Session):
    contacts = db.query(Contact).filter(
        (Contact.first_name.contains(query)) |
        (Contact.last_name.contains(query)) |
        (Contact.email.contains(query))
    ).all()
    return contacts


async def get_contacts_by_birthdays(db: Session):
    contacts = db.query(Contact).all()
    contacts_list = []
    for contact in contacts:
        if 0 <= await validate_birthday(contact.birthday) <= 7:
            contacts_list.append(contact)
    return contacts_list