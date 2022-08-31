from random import choice, random, shuffle
from time import sleep
import matplotlib.pyplot as plt

freq_a = 0.3;
freq_A = 0.7;

pop = 100000;

iterations=100

entities = [];
for i in range(pop):
    if random() < freq_a:  
        allele_1 = 0;
        
    else:
        allele_1 = 1
        
    if random() < freq_a:  
        allele_2 = 0;
        
    else:
        allele_2 = 1    
    
    entities.append((allele_1, allele_2))

homo_dom_hist = [];
homo_rec_hist = [];
hetero_hist = [];


for i in range(iterations):
    print (i / iterations * 100, "%")
    
    # Count frequenties
    homo_dom = 0;
    homo_rec = 0;
    hetero = 0;

    for entity in entities:
        if entity[0] == entity[1]:
            if entity[0] == 0:
                homo_rec += 1;
            else:
                homo_dom += 1;
        else:
            hetero += 1;
            
    homo_dom_hist.append(homo_dom / pop);
    homo_rec_hist.append(homo_rec / pop)        
    hetero_hist.append(hetero / pop);        
            
    # print("homo_dom:", homo_dom / pop, "expteced:", freq_A**2);
    # print("homo_rec:", homo_rec / pop, "expteced:", freq_a**2);
    # print("hetero:", hetero / pop, "expteced:", 2*freq_A*freq_a);
    
    # Reproduce
    shuffle(entities);
    
    new_entities = [];
    
    i = 0;
    while i < len(entities):
        index1 = choice([0, 1]);
        index2 = choice([0, 1]);
        
        new_entity = (entities[i][index1], entities[i + 1][index2]);
        
        new_entities.append(new_entity)
        
        index1 = choice([0, 1]);
        index2 = choice([0, 1]);
        
        new_entity = (entities[i][index1], entities[i + 1][index2]);
        
        new_entities.append(new_entity)
        
        i += 2;
        
    entities = new_entities
    
    
fig, ax = plt.subplots();
    
ax.plot(range(iterations), homo_dom_hist, label="Homo Dom")
ax.axhline(y=freq_A**2, color="black", linestyle ="--", label="exptected")
    
ax.plot(range(iterations), homo_rec_hist, label="Homo Rec")
ax.axhline(y=freq_a**2, color="black", linestyle ="--", label="exptected")
    
ax.plot(range(iterations), hetero_hist, label="Hetero")
ax.axhline(y=2*freq_A*freq_a, color="black", linestyle ="--", label="exptected")


ax.legend()

plt.show()
    

    