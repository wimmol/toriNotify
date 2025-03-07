from app.db.models.links import SessionLocal, Link


def add_link(chat_id: int, name: str, link: str):
    """Add a new link for a chat, assigning a unique number."""
    session = SessionLocal()
    try:
        new_link = Link(chat_id=chat_id, name=name, link=link)
        session.add(new_link)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def remove_link(link_id: int):
    """Remove a link from a chat by its number."""
    session = SessionLocal()
    try:
        link = session.query(Link).filter_by(id=link_id).first()
        if link:
            session.delete(link)
            session.commit()
    finally:
        session.close()

def get_links(chat_id: int):
    """Get all links for a specific chat."""
    session = SessionLocal()
    try:
        links = session.query(Link).filter_by(chat_id=chat_id).order_by(Link.created_at).all()
        return [{"id": l.id, "name": l.name, "link": l.link, "created_at": l.created_at} for l in links]
    finally:
        session.close()
