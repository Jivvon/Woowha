from typing import List

from .image_model import ImageModel
from .utils import SQLAlchemyDBConnection

"""Table "public.images"

  Column  |          Type          | Collation | Nullable | Default
----------+------------------------+-----------+----------+---------
 filename | character varying(100) |           | not null |
 styles   | character varying[]    |           | not null |
Indexes:
    "images_pkey" PRIMARY KEY, btree (filename)

filename:  daa24daad3393865.jpg
styles:  {cartoongan_hayao, cartoongan_hosoda}
"""

class Database:
    @classmethod
    def select_all_image(cls):
        with SQLAlchemyDBConnection() as session:
            imagemodel = session.query(ImageModel)
            return imagemodel

    @classmethod
    def select_image(cls, filename: str):
        with SQLAlchemyDBConnection() as session:
            imagemodel = session.query(ImageModel).filter(ImageModel.filename == filename).first()
            print("select {} result : {}".format(filename, imagemodel))
            return imagemodel

    @classmethod
    def insert(cls, filename: str, styles: List[str]):
        with SQLAlchemyDBConnection() as session:
            session.add(ImageModel(filename, styles))

    @classmethod
    def update(cls, filename: str, style: str):
        with SQLAlchemyDBConnection() as session:
            imagemodel = session.query(ImageModel).filter(ImageModel.filename == filename).first()
            if not style in imagemodel.styles:
                imagemodel.styles.append(style)
