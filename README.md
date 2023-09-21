# Replication-system-demonstration

Replication of methodology in scientific research involves a process of independently re-executing an experiment or study, following the same procedures and protocols of the original investigation with the goal of validating or confirming the initial findings. 

However, many obstacles can be observed that can limit the reproducibility of an experiment including inadequate documentation of the original methodology, resource constraints, the introduction of variability from environmental factors and equipment, and the need for precise equipment calibration and maintenance. 

Despite these difficulties, replication is essential for validating and enhancing the credibility of scientific findings.
This project presents a comprehensive  Natural Language Processing (NLP) approach, specifically designed to aid in  replicating scientific methodologies. The primary goal is to preserve specific aspects of reproducibility by establishing an easily accessible list of reagents, equipment, and items for independent groups, thereby enabling standardized replication and verification.
We have developed an NLP software capable of extracting key elements, including items, reagents, and materials from scholarly texts. To achieve this, we employed the Doccano platform for rigorous document labeling, distinguishing items with the 'ITEM' tag,  and experiments with the 'EXPERIMENT' tag. The labeled dataset was then meticulously transformed to train an empty spaCy NLP model, which includes a Named Entity Recognition (NER) pipeline.

The process begins with extracting text from the PDF document. This extracted text then undergoes a content summarization phase, identifying and isolating key sentences crucial to the paper's core concepts. Following this, text analysis is conducted to specifically identify multiple significant named entities: **'ITEM-ANIMAL'**, **‘ITEM-MATERIAL'**, **‘ITEM-METHOD’**, **‘ITEM-EQUIPMENT’**, **‘EXPERIMENT-TYPE’**,  **‘EXPERIMENT-DATA TYPE’**, **‘EXPERIMENT-PROTOCOL’**. 

These entities are pivotal in comprehending the content of the paper. 
Subsequently, the identified items and experiments are compiled, leading to the generation of experiment titles along with their corresponding items. 
These are then organized and formatted into a structured output, which may take the form of a JSON file or be stored in a website NoSQL database, ready for rendering. 
In the subsequent phase of our workflow, the compiled lists of items are stored in JSON files within a NoSQL database.

Our JavaScript application is designed to efficiently query these JSON files, extracting experiment titles along with their respective lists of items. 
This information is then seamlessly integrated into HTML code, allowing for customized styling through CSS and enabling seamless rendering on web platforms. This streamlined process ensures the efficient handling and accessibility of scholarly content for further analysis and utilization.

We retrieved a total of 2000 papers using the (Hugging Face API).
Data labels are:
- ITEM-ANIMAL (i.e. mice)
- ITEM-MATERIAL (i.e. Antibodies)
- ITEM-METHOD (i.e. Modified Testing Procedure)
- ITEM-EQUIPMENT (i.e. rotarod)
- EXPERIMENT-TYPE (i.e behavioral test)
- EXPERIMENT-PROTOCOL (i.e. motor coordination)
- EXPERIMENT-DATA TYPE (20-25RPM)

The fine-tuned model exhibited high accuracy for the ITEM tag when tested on previously unseen papers with F1-Score about 95% and precision 94% and recall 95%. Future endeavors include expanding and diversifying the dataset to improve prediction on EXPERIMENT tag and generalize the predictions, implementing an API for streamlined predictions in JSON format, integrating a PDF parser for improved text extraction from PDF files, and enhancing labeling through detailed item categorization. This work underscores a systematic and thorough approach to advancing NLP capabilities in scientific contexts, with potential applications in various domains.


![Items-Lists generator workflow](https://github.com/Abdelrahman4983/Replication-system-demonstration/assets/96976680/534cf582-0806-43ac-8fec-219caa12e4cf)
