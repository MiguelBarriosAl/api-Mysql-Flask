def query_total_count():
    return """SELECT COUNT(*) FROM Simulations"""


def query_state(id_simulation: int):
    return """SELECT state FROM Simulations WHERE id_simulation = %s """ % id_simulation


def query_graph_loss(id_simulation: int):
    return """SELECT seconds,loss FROM Loss WHERE id_simulation = %s """ % id_simulation