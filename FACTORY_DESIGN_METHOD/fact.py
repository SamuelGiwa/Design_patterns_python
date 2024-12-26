import json
import xml.etree.ElementTree as etree

class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
    @property
    def parsed_data(self):
        return self.data
    

class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
    @property
    def parsed_data(self):
         return self.tree
     
    def dataextraction_factory(filepath):
        if filepath.endswith('json'):
         extractor = JSONDataExtractor
        elif filepath.endswith('xml'):
            extractor = XMLDataExtractor
        else:
            raise ValueError('Cannot extract data from {}'.format(filepath))
        return extractor(filepath)

def main():
    sqlite_factory = extract_data_from('data/person.sq3')
    print()
 
json_factory = extract_data_from('data/movies.json')
json_data = json_factory.parsed_data
print(f'Found: {len(json_data)} movies')
for movie in json_data:
 print(f"Title: {movie['title']}")
 year = movie['year']
 if year:
 print(f"Year: {year}")
 director = movie['director']
 if director:
 print(f"Director: {director}")
 genre = movie['genre']
 if genre:
 print(f"Genre: {genre}")
 print()
