#!/usr/bin/env python3

import pandas as pd

def cities():
    data = [[643272, 715.48], [279044, 528.03], [231853, 689.59], [223027, 240.35], [201810, 3817.52]]
    cities = pd.DataFrame(data, index=['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu'], columns=['Population', 'Total area'])
    return cities
    
def main():
    print(cities())
    return
    
if __name__ == "__main__":
    main()
