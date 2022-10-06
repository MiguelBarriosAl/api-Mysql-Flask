def query_total_count():
    return """SELECT COUNT(*) FROM Simulations"""


def query_by_state(state: str):
    return """SELECT id_simulation, state  FROM Simulations WHERE state = \"%s\"""" % str(state)


def query_order_by(term: str):
    return """SELECT id_simulation, state, created_at, updated_at  FROM Simulations ORDER BY %s  """ % term


def query_graph_loss(id_simulation: int):
    return """SELECT seconds,loss FROM Loss WHERE id_simulation = %s """ % id_simulation


def query_list_fixtures():
    return """SELECT id_fixture, fixture FROM Fixtures"""