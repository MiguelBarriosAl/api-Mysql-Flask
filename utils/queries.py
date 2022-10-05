def query_total_count():
    return """SELECT COUNT(*) FROM Simulations"""


def query_by_state(state: str):
    return """SELECT id_simulation, state  FROM Simulations WHERE state = \"%s\"""" % str(state)


def query_graph_loss(id_simulation: int):
    return """SELECT seconds,loss FROM Loss WHERE id_simulation = %s """ % id_simulation