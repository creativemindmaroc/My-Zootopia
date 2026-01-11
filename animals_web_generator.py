import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal_data):
    """ Serializes a single animal into HTML """
    output = '<li class="cards__item">'
    
    # Name
    output += f"Name: {animal_data['name']}<br/>\n"
    
    # Diet (if exists)
    if 'diet' in animal_data.get('characteristics', {}):
        output += f"Diet: {animal_data['characteristics']['diet']}<br/>\n"
    
    # Location (first one, if exists)
    if 'locations' in animal_data and len(animal_data['locations']) > 0:
        output += f"Location: {animal_data['locations'][0]}<br/>\n"
    
    # Type (if exists)
    if 'type' in animal_data.get('characteristics', {}):
        output += f"Type: {animal_data['characteristics']['type']}<br/>\n"
    
    output += '</li>\n'
    return output

def main():
    # Load data
    animals_data = load_data('animals_data.json')
    
    # Generate animals HTML
    animals_html = ''
    for animal in animals_data:
        animals_html += serialize_animal(animal)
    
    # Read template
    with open('animals_template.html', 'r') as handle:
        template_content = handle.read()
    
    # Replace placeholder
    final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)
    
    # Write output
    with open('animals.html', 'w') as handle:
        handle.write(final_html)
    
    print("HTML file generated successfully!")

if __name__ == "__main__":
    main()
