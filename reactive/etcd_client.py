from charms.reactive import when

@when('db.available')
def print_con_string(db):
    print(db.connection_string())
