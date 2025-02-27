import subprocess
import time
import json
import os
import pygetwindow as gw

class WindowLayoutManager:
    def __init__(self, config_path="layouts.json"):
        self.config_path = config_path
        self.layouts = self.load_layouts()

    def load_layouts(self):
        """Load layouts from config file."""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}

    def save_layouts(self):
        """Save layouts to config file."""
        with open(self.config_path, 'w') as f:
            json.dump(self.layouts, f, indent=4)

    def create_layout(self, layout_name):
        """Create a new layout configuration."""
        layout = {'programs': []}
        
        while True:
            program = input("Enter program path (or 'done' to finish): ").strip()
            if program.lower() == 'done':
                break
                
            x = int(input("Enter X position: "))
            y = int(input("Enter Y position: "))
            program_name = input("Enter program substring: ")
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            
            layout['programs'].append({
                'path': program,
                'program_name': program_name,
                'position': {
                    'x': x,
                    'y': y,
                    'width': width,
                    'height': height
                }
            })
        
        self.layouts[layout_name] = layout
        self.save_layouts()
        print(f"Layout '{layout_name}' created successfully!")

    def apply_layout(self, layout_name):
        """Apply a saved layout configuration."""
        if layout_name not in self.layouts:
            print(f"Layout '{layout_name}' not found!")
            return
            
        layout = self.layouts[layout_name]
        
        # Launch programs
        for program in layout['programs']:
            try:
                subprocess.Popen(program['path'])
                # Wait for window to appear
                time.sleep(2)
                
                # Find and resize window
                windows = gw.getAllWindows()
                program_name = program['program_name'].lower()
                print(f"Looking for window with title containing '{program_name}'")
                for window in windows:
                    print(f"Checking window title: {window.title}")
                    if program_name in window.title.lower():
                        print(f"Found window: {window.title}")
                        pos = program['position']
                        window.moveTo(pos['x'], pos['y'])
                        window.resizeTo(pos['width'], pos['height'])
                        break
                        
            except Exception as e:
                print(f"Error launching {program['path']}: {str(e)}")

    def list_layouts(self):
        """List all saved layouts."""
        if not self.layouts:
            print("No layouts saved!")
            return
            
        print("\nAvailable layouts:")
        for name in self.layouts:
            print(f"- {name}")

    def delete_layout(self, layout_name):
        """Delete a saved layout."""
        if layout_name in self.layouts:
            del self.layouts[layout_name]
            self.save_layouts()
            print(f"Layout '{layout_name}' deleted successfully!")
        else:
            print(f"Layout '{layout_name}' not found!")

def main():
    manager = WindowLayoutManager()
    
    while True:
        print("\nWindow Layout Manager")
        print("1. Create new layout")
        print("2. Apply layout")
        print("3. List layouts")
        print("4. Delete layout")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter layout name: ")
            manager.create_layout(name)
        elif choice == '2':
            name = input("Enter layout name: ")
            manager.apply_layout(name)
        elif choice == '3':
            manager.list_layouts()
        elif choice == '4':
            name = input("Enter layout name to delete: ")
            manager.delete_layout(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()