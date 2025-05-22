import os

def update_path_attributes(directory='.'):
    search_str = '<path class="svg-wb" fill="param(fill)" stroke="param(fill)" stroke-width="param(outline-width)" stroke-linejoin="round" stroke-miterlimit="10" d'
    replacement_str = '<path class="svg-wb" fill="param(fill)" stroke="param(fill)" stroke-width="param(outline-width)" stroke-linejoin="round" stroke-linecap="round" stroke-miterlimit="10" d'
    
    for filename in os.listdir(directory):
        if filename.lower().endswith('.svg'):
            svg_path = os.path.join(directory, filename)
            with open(svg_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace(search_str, replacement_str)
            
            with open(svg_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated {filename}")

if __name__ == "__main__":
    update_path_attributes()