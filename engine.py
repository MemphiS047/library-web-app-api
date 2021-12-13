from sqlalchemy import create_engine

def engine():
    connection_string="mysql://root:a1s2d3f4g5@localhost/world"
    engine= create_engine(connection_string)
    return engine

