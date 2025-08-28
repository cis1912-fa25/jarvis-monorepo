from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def create_database_engine(database_url: str):
    """Create SQLAlchemy engine with appropriate settings"""
    if database_url.startswith("sqlite"):
        engine = create_engine(
            database_url, connect_args={"check_same_thread": False}
        )
    else:
        # For PostgreSQL and other databases
        engine = create_engine(database_url)
    return engine

def create_session_local(engine):
    """Create SessionLocal class for database sessions"""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_database_dependency(SessionLocal):
    """Create database dependency function"""
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    return get_db


# Base class for all models
Base = declarative_base()
# Create engine and session
engine = create_database_engine("sqlite:///auth.db")
SessionLocal = create_session_local(engine)

# Create database dependency
get_db = get_database_dependency(SessionLocal)

def create_tables(engine):
    """Create all tables for the auth service"""
    Base.metadata.create_all(bind=engine)