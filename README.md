# MojoDojoCasaTeam


## Prerequisites
Install necessary dependencies:
```
pip install -r requirements.txt
```

Furthermore, if using IBM Quantum Computer API place your token 
in the .env file as follows:
```
IBM_TOKEN="your_token"
```

## Generate art 
Run following command to execute program with random initial pattern. Result will be saved to quantum.gif :
```
cd game
python main.py
```


You can use `-l` flag to load initial pattern from pattern.png. You can edit it in external program (e.g. MS Paint).
White pixel = dead cell, any other pixel = living cell:
```
python main.py -l
```

## Testing 
Run following command to execute test suite:
```
pytest .
```
