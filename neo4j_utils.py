from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "neo4j"
password = "Drones4dayz"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Define a query
query = "MATCH (f:FACULTY)" "WHERE f.position = 'Assistant Professor'" "RETURN count(f) AS assistant_professors"

# Run the query
with driver.session(database="academicworld") as session:
    result = session.run(query)
    for record in result:
        print(record)

# Close the connection
driver.close()