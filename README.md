# book-rdf-test

Steps for running the python rdf converter:
1. Install Libraries:
 pandas for reading CSV files.
 rdflib for RDF manipulation and serialization.
 datetime for manipulating date fields.

 2. Edit the fields for the csv files.
  Currently, the file is set up to convert BookData_updated.csv, included in this git depository.
  Use of the converter for other csv files requires changing this.

 3. Choose a namespace. 
  The file is set up to encode to "http://www.semanticweb.org/alexanderanderson/ontologies/bookOntology".
  This is the namespace for the toy book ontology used for this exercise.
  Change the namespace in the file to the one of your choice.

4. Define the columns to be converted.
   Define columns in the file to match those in the csv.
   
6. Edit or remove the SPARQL queries.
   Current file includes SPARQL queries which run immediately when the rdf file is created, edit or remove thise for your use case.

