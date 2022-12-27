import sqlalchemy

Base = sqlalchemy.orm.declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    def __repr__(self) -> str:
        return f'Book(id={self.id}, title={self.title})'

class Chapter(Base):
    __tablename__ = 'chapter'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    body = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    book_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('book.id'))

    def __repr__(self) -> str:
        return f'Chapter(id={self.id}, title={self.title}, book_id={self.book_id}, body_snippet={self.body.slice(250)})'

