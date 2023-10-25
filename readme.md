# STLS Z-Height Sorter

Python script to sort a folder of STLs depending on Z-height and then move them to corresponding folders for easy plate creation of similar height models.

Right now the script will just look for the biggest diff in Z height and split the STLs at that height. A more elaborate algorithm migth be added in the future.


## How to use
1. Install requirements
    ```
    pip install -r requirements.txt
    ```
2. Add your stl files in a folder named STLs in the same folder as main.py. Voron usually release their stls in folders named STLs so you can just add a folder directly from a Voron repo. 
3. Run main.py
    ```
    python main.py
    ```
    or
    ```
    python3 main.py
    ```
4. Sorted folder is created with stls storted by type (main, accent, other) and in to subfolders (short, tall) depending on their Z height.
    ```
    Sorted
        main
            short
            tall
        accent
            short
            tall
        other
            short
            tall
    ```
