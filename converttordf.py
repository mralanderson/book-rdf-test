import pandas as pd
import rdflib
from rdflib.namespace import RDF, RDFS, XSD
from datetime import datetime

# Define the ontology IRI
ONTOLOGY_IRI = "http://www.semanticweb.org/alexanderanderson/ontologies/bookOntology/"

# Define RDF properties and classes for the ontology
BOOK_CLASS = rdflib.URIRef(ONTOLOGY_IRI + "Novel")
TITLE_PROPERTY = rdflib.URIRef(ONTOLOGY_IRI + "novelTitle")
AUTHOR_PROPERTY = rdflib.URIRef(ONTOLOGY_IRI + "novelAuthor")
PUBLISHER_PROPERTY = rdflib.URIRef(ONTOLOGY_IRI + "novelPublisher")
PUBLICATION_DATE_PROPERTY = rdflib.URIRef(ONTOLOGY_IRI + "novelPublicationDate")

# Load CSV data using pandas
csv_file = 'bookData_updated.csv'
df = pd.read_csv(csv_file)


# Create an RDF graph
g = rdflib.Graph()

# Define a namespace for convenience
namespace = rdflib.Namespace(ONTOLOGY_IRI)
g.bind('ont', namespace)

# Convert each row to RDF triples
for index, row in df.iterrows():
    book_id = rdflib.URIRef(ONTOLOGY_IRI + f"Book_{index}")
    g.add((book_id, RDF.type, BOOK_CLASS))
    g.add((book_id, TITLE_PROPERTY, rdflib.Literal(row['Title'])))
    g.add((book_id, AUTHOR_PROPERTY, rdflib.Literal(row['Author'])))
    g.add((book_id, PUBLISHER_PROPERTY, rdflib.Literal(row['Publisher'])))
    g.add((book_id, PUBLICATION_DATE_PROPERTY, rdflib.Literal(row['Publication Date'], datatype=XSD.date)))



# Serialize the RDF graph to Turtle format
ttl_file = 'bookData.ttl'
g.serialize(destination=ttl_file, format='turtle')

print(f"RDF data has been successfully converted and stored in {ttl_file}")

# Define SPARQL queries
def sparql_query(graph, query):
    return graph.query(query)

# Query to find all books by "Tolkien, J.R.R."
query_books_by_author = """
PREFIX ont: <http://www.semanticweb.org/alexanderanderson/ontologies/bookOntology/>
SELECT ?book ?title
WHERE {
    ?book rdf:type ont:Novel .
    ?book ont:novelAuthor "Rowling, J.K." .
    ?book ont:novelTitle ?title .
}
"""
results_books_by_author = sparql_query(g, query_books_by_author)
print("Books by 'Rowling, J.K.':")
for row in results_books_by_author:
    print(f"Title: {row.title}")

# Query to find all publishers and the titles of books they published
query_publishers_and_books = """
PREFIX ont: <http://www.semanticweb.org/alexanderanderson/ontologies/bookOntology/>
SELECT ?publisher ?title
WHERE {
    ?book rdf:type ont:Novel .
    ?book ont:novelPublisher ?publisher .
    ?book ont:novelTitle ?title .
}
"""
results_publishers_and_books = sparql_query(g, query_publishers_and_books)
print("\nPublishers and their books:")
for row in results_publishers_and_books:
    print(f"Publisher: {row.publisher}, Title: {row.title}")

# Query to find all books published within a certain date range (e.g., 1900 to 1990)
start_date = "1900-01-01"
end_date = "1999-12-31"
query_books_in_date_range = f"""
PREFIX ont: <http://www.semanticweb.org/alexanderanderson/ontologies/bookOntology/>
SELECT ?book ?title ?publicationDate
WHERE {{
    ?book rdf:type ont:Novel .
    ?book ont:novelPublicationDate ?publicationDate .
    ?book ont:novelTitle ?title .
    FILTER (?publicationDate >= "{start_date}"^^xsd:date && ?publicationDate <= "{end_date}"^^xsd:date)
}}
"""
results_books_in_date_range = sparql_query(g, query_books_in_date_range)
print(f"\nBooks published between {start_date} and {end_date}:")
for row in results_books_in_date_range:
    print(f"Title: {row.title}, Publication Date: {row.publicationDate}")
