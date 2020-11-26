
                                                     _____  __   __ ___   ___      __    _  _   ___    __    __
                                                    |_   _| \ `v' /| _,\ | __|    /  \  | || | | __|  /  \  | _\
                                                      | |    `. .' | v_/ | _|    | /\ | | >< | | _|  | /\ | | v |
                                                      |_|     !_!  |_|   |___|   |_||_| |_||_| |___| |_||_| |__/


# Introduction

This model takes long string ,split that string into a list of 2-elem list. Finally it create a dictionary having word as key and its frequency as value.

# Folder architecture

    D:.
    │   License
    │   README.md
    │   requirements.txt
    │   server.py
    │   setup.sh
    │
    ├───db
    │       big.txt
    │
    ├───log
    │       app.log
    │
    ├───model
    │       models_compressed.pkl
    │
    └───src
            config.py
            model.py
            utils.py
            __init__.py

# How to train the model?
    # Train a model on default dataset
    import src
    src.model.train_bigtxt()
# How to predict words with same prefix?
    import src
    src.load()
    src.predict('some')
# How to predict next word?
    import src
    src.load()
    src.predict('gold',"m")
# How to host the model in production?
Open the command line and run following command
    
    python server.py

# How to access the result?
    import requests
    url= 'http://localhost:5000/TypeAhead/gold/m'
    requests.get(url).json()

# Model description

**Conditional probability model** and **Hidden markov model**

$P(A , B) = P(B | A) * P(A)$

# Author
    Ashish Kumar
# Credits
This package is deeply inspired from [autocomplete 0.0.104](https://pypi.org/project/autocomplete/#explain-like-im-5) by *Rodrigo Palacios*

# License

[MIT License](./License)

Copyright (c) 2020 Ashish Kumar
