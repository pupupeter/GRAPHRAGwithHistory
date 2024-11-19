# GRAPHRAGwithHistory
The introduction of the GraphRAG with History 


# Demonstration

# Project Description
This open-source software is designed to assist institutions and researchers in the field of history by embedding historical documents or case reports into a graph database (such as Neo4j), enabling advanced search and retrieval functionality through GraphRAG (Graph-based Retrieval-Augmented Generation). The integration of AI capabilities enhances the system's scalability and value, making historical data more efficient to search and analyze. This system supports historical research and education by providing rich historical data, helping scholars to delve deeper into historical events, figures, and connections, thus facilitating more precise historical research and teaching.
# Project Directory Structure


```


GraphRagwith history/
│
│
├── templates/
│   ├── person.html       # person nodes
│   ├── file.html        # file nodes
│   ├── personandevent.html       # person relate event nodes
│   └── personaboutjiangchong.html        # jiangchong  nodes
├── neo4j-for-nodes.py               # neo4j code
│
└── README.md            # Project description file
```

# Installation Guide
Please use VScode jupyter notebook google colab and other interactive computing platform to show codes.


 **Suggesting using google colab to fulfill with the project**

**1.** Install Required Packages
```
pip install neo4j

```


**2.** Call Required Packages

```
from neo4j import GraphDatabase
from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher
import neo4j
import pyvis
```








# Usage Instructions

**please enroll and login neo4j in advance.**

website: https://llm-graph-builder.neo4jlabs.com/

I had already put the theories on github, you could try choose our theories or just use your files to do.

![image](https://github.com/user-attachments/assets/fa5681da-f933-4bd0-9b42-0c0164ff781d)



**1. connect neo4j**



![image](https://github.com/user-attachments/assets/116d427c-05f0-4756-aa55-f3112cd2809c)


**2. put the files on**



![image](https://github.com/user-attachments/assets/83ce949b-abc9-4618-8468-5458da1562f2)




**3. click Generate Graph**



![image](https://github.com/user-attachments/assets/7e380299-7267-4dbf-9ca9-8e8af3020366)



**4. Use RAG-bot to ask question( optionally )**



![image](https://github.com/user-attachments/assets/26ce4f6f-80f5-47f7-bcf2-35cf058d406f)

**5. get back to the interactive computing platform to excuate your code for the files**



  **you could just download my code to modify**

```
https://github.com/pupupeter/GRAPHRAGwithHistory/blob/main/%E6%9C%89%E6%88%90%E5%8A%9Fneo4j%E7%9A%84%E6%9D%B1%E8%A5%BF.py
```





#  Contact Information
  fFor any questions, please contact:

Email: peter20040512@gmail.com

Email: shimodesu0829@gmail.com

Email: pecu@ntnu.edu.tw
