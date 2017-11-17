## Translation deduplication

Tools for cleaning up existing translations' bases.

#### show_duplicated_keys.py

Compares each line with previous one 
and prints if computed Levenshtein distance is lower than set 
threshold. Helps with finding same keys but with modified (inside the line or at the end) 
punctuation or numbers.

##### Usage
Accepts sorted keys as input.

Usage example with Qt translations under Ubuntu:
```bash
grep source nitrokey_en.ts  | sort -b | ./show_duplicated_keys.py
```

##### Installation
Needs Python 3. Install dependencies from `requirements.txt`:
```bash
pip3 install -r requirements.txt --user
```

##### Known issues
Bases on `sort` output. If similar lines have changed the first 
letter than tool will not find it. Each string have just two comparisons 
(with previous and next). 

##### To do
Make each vs each computation to detect strings changed at the beginning 
(eg. in case where first few letters are different).
