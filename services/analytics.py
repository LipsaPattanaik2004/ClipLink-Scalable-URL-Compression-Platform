from database.models import SessionLocal, URL

def get_stats(short_code):
    session = SessionLocal()

    url = session.query(URL).filter_by(short_code=short_code).first()

    if not url:
        session.close()
        return None

    data = {
        "original_url": url.original_url,
        "clicks": url.clicks
    }

    session.close()
    return data
