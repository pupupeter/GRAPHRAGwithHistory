# -*- coding: utf-8 -*-
"""neo4jwithhistory.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URPFphHqOHKWm8i19X_VAUNzPL0oFotC
"""

pip install neo4j

from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://92c5f014.databases.neo4j.io"
AUTH = ("neo4j", "nqIVfsyN_naa3dUAgwDkDJF5HIjkl-k26REUmiSsINE")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

pip install py2neo

from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher

records, summary, keys = driver.execute_query(
    "MATCH (a:Person)-->() RETURN a",
    database_="neo4j",
)
for person in records:
    print(person)
    # person["name"] or person["age"] are also valid

# Some summary information
print("Query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after
))

print(f"Available keys are {keys}")  # ['name', 'age']

records, summary, keys = driver.execute_query(
    "MATCH (b:Event)-->() RETURN b",
    database_="neo4j",
)
for event in records:
    print(event)
    # person["name"] or person["age"] are also valid

# Some summary information
print("Query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after
))

print(f"Available keys are {keys}")  # ['name', 'age']

records, summary, keys = driver.execute_query(
    "MATCH (c:Chunk)-->() RETURN c",
    database_="neo4j",
)
for chunk in records:
    print(chunk)
    # person["name"] or person["age"] are also valid

# Some summary information
print("Query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after
))

print(f"Available keys are {keys}")  # ['name', 'age']

records, summary, keys = driver.execute_query(
    "MATCH (d:Document)-->() RETURN d",
    database_="neo4j",
)
for document in records:
    print(document)
    # person["name"] or person["age"] are also valid

# Some summary information
print("Query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records),
    time=summary.result_available_after
))

print(f"Available keys are {keys}")  # ['name', 'age']

pip install pyvis

import neo4j
import pyvis

def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver: # Query to get a graphy result
        graph_result = driver.execute_query(
         "MATCH (a:Person)-->() RETURN a",

            result_transformer_=neo4j.Result.graph,
        )

        # Draw graph
        nodes_text_properties = {  # what property to use as text for each node
            "Person": "id",
        }
        visualize_result(graph_result, nodes_text_properties)
def visualize_result(query_graph, nodes_text_properties):
    visual_graph = pyvis.network.Network()

    for node in query_graph.nodes:
        node_label = list(node.labels)[0]
        node_text = node[nodes_text_properties[node_label]]
        visual_graph.add_node(node.element_id, node_text, group=node_label)

    for relationship in query_graph.relationships:
        visual_graph.add_edge(
            relationship.start_node.element_id,
            relationship.end_node.element_id,
            title=relationship.type
        )

    visual_graph.show('network.html', notebook=False)


if __name__ == "__main__":
    main()

def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver: # Query to get a graphy result
        graph_result = driver.execute_query(
         "MATCH (c:Chunk)-->() RETURN c",

            result_transformer_=neo4j.Result.graph,
        )

        # Draw graph
        nodes_text_properties = {  # what property to use as text for each node
            "Chunk": "fileName",
        }
        visualize_result(graph_result, nodes_text_properties)
def visualize_result(query_graph, nodes_text_properties):
    visual_graph = pyvis.network.Network()

    for node in query_graph.nodes:
        node_label = list(node.labels)[0]
        node_text = node[nodes_text_properties[node_label]]
        visual_graph.add_node(node.element_id, node_text, group=node_label)

    for relationship in query_graph.relationships:
        visual_graph.add_edge(
            relationship.start_node.element_id,
            relationship.end_node.element_id,
            title=relationship.type
        )

    visual_graph.show('f.html', notebook=False)


if __name__ == "__main__":
    main()

def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver: # Query to get a graphy result
        graph_result = driver.execute_query(
         "MATCH (a:Person)-[r1]->(b:Event)-[r2]->(c:Chunk)-[r3]->(d:Document) RETURN a, r1, b, r2, c, r3,d ",

            result_transformer_=neo4j.Result.graph,
        )
        print(f"Nodes: {list(graph_result.nodes)}")  # Debugging: Print nodes
        print(f"Relationships: {list(graph_result.relationships)}")
        # Draw graph
        nodes_text_properties = {  # what property to use as text for each node
            "Person": "name",
            "Event":"name",
            "Chunk":"fileName",
            "Document":"fileName",
        }
        visualize_result(graph_result, nodes_text_properties)
def visualize_result(query_graph, nodes_text_properties):
    visual_graph = pyvis.network.Network()

    for node in query_graph.nodes:
        node_label = list(node.labels)[0]
        node_text = node[nodes_text_properties[node_label]]
        visual_graph.add_node(node.element_id, node_text, group=node_label)

    for relationship in query_graph.relationships:
        visual_graph.add_edge(
            relationship.start_node.element_id,
            relationship.end_node.element_id,
            title=relationship.type
        )

    visual_graph.show('e.html', notebook=False)


if __name__ == "__main__":
    main()

def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver: # Query to get a graphy result
        graph_result = driver.execute_query(
         "MATCH (a:Person)-[r1]->(b:Event)<-[r2]-(c:Chunk)-[r3]->(d:Document) RETURN a, r1, b,r2,c,r3,d",

            result_transformer_=neo4j.Result.graph,
        )
        print(f"Nodes: {list(graph_result.nodes)}")  # Debugging: Print nodes
        print(f"Relationships: {list(graph_result.relationships)}")
        # Draw graph
        nodes_text_properties = {  # what property to use as text for each node
            "Person": "id",
            "Event":"id",
            "Chunk":"fileName",
            "Document":"fileName",
        }
        visualize_result(graph_result, nodes_text_properties)
def visualize_result(query_graph, nodes_text_properties):
    visual_graph = pyvis.network.Network()

    for node in query_graph.nodes:
        node_label = list(node.labels)[0]
        node_text = node[nodes_text_properties[node_label]]
        visual_graph.add_node(node.element_id, node_text, group=node_label)

    for relationship in query_graph.relationships:
        visual_graph.add_edge(
            relationship.start_node.element_id,
            relationship.end_node.element_id,
            title=relationship.type
        )

    visual_graph.show('e.html', notebook=False)


if __name__ == "__main__":
    main()

def main():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        # Query to get a graph result for specific persons mentioned in the document
        graph_result = driver.execute_query(

            "MATCH (d:Document)-->(a:Person {name: '江充'})RETURN a,d,r1",
            result_transformer_=neo4j.Result.graph,
        )

        print(f"Nodes: {list(graph_result.nodes)}")  # Debugging: Print nodes
        print(f"Relationships: {list(graph_result.relationships)}")

        # Draw graph
        nodes_text_properties = {  # what property to use as text for each node
            "Person": "name",
            "Event": "name",
            "Chunk": "fileName",
            "Document": "fileName",
        }
        visualize_result(graph_result, nodes_text_properties)

def visualize_result(query_graph, nodes_text_properties):
    visual_graph = pyvis.network.Network()

    for node in query_graph.nodes:
        node_label = list(node.labels)[0]
        node_text = node[nodes_text_properties[node_label]]
        visual_graph.add_node(node.element_id, node_text, group=node_label)

    for relationship in query_graph.relationships:
        visual_graph.add_edge(
            relationship.start_node.element_id,
            relationship.end_node.element_id,
            title=relationship.type
        )

    visual_graph.show('e.html', notebook=False)

if __name__ == "__main__":
    main()