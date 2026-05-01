from database.models import SessionLocal, URL
from utils.encoder import encode

def create_short_url(original_url):
    session = SessionLocal()

    existing = session.query(URL).filter_by(original_url=original_url).first()
    if existing:
        session.close()
        return existing.short_code

    new_url = URL(original_url=original_url)
    session.add(new_url)
    session.commit()

    short_code = encode(new_url.id)
    new_url.short_code = short_code
    session.commit()

    session.close()
    return short_code

def get_original_url(short_code):
    session = SessionLocal()

    url = session.query(URL).filter_by(short_code=short_code).first()

    if url:
        url.clicks += 1
        session.commit()
        result = url.original_url
    else:
        result = None

    session.close()
    return result
