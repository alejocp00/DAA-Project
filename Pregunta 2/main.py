from src.generator import generate
from src.graph import Graph
from src.travel import travel
import time
from colorama import Fore, init

init()

while True:
    
    text_input = input(Fore.GREEN+"Do you want to generate and run a new case? (y/n): ")
    
    if text_input == 'y':
        
        print(Fore.CYAN+"Generating new case...")
        G, U = generate()
        print(Fore.BLUE+f"Case details: Vertices: {G.VerticesCount}, Edges: {G.EdgesCount}, Util Paths: {len(U)}")
        start_time = time.time()
        util_edges = travel(G, U)
        end_time = time.time()
        print(Fore.YELLOW+f"Founded {util_edges} util edges in {end_time - start_time} seconds")
    elif text_input == 'n':
        break
    else:
        print(Fore.RED+"Invalid input. Please enter 'y' or 'n'.")
