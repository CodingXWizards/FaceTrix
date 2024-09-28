from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db import Base

# Association table for many-to-many relationship
detected = Table(
    'detected',
    Base.metadata,
    Column('criminal_id', UUID(as_uuid=True), ForeignKey('criminal.id')),
    Column('camera_id', UUID(as_uuid=True), ForeignKey('camera.id'))
)