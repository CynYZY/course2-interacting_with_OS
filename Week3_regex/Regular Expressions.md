# Regular expressions

> Allows us to search a text for strings matching a specific pattern

#### Basic Matching with `grep`

- Reserved characters
  - A dot matches any character
  - `grep`
  - case-sensitive

`grep s.ing` any words like "sling" or "sting" etc.

`grep ^fruit` any words start with fruit

`grep cat$` any words end with cat

`r""` represents raw string

> It's a good idea to always use raw strings for regular expressions in Python.



#### Simply match

- Simply match`.`

  > ```python
  > >>> print(re.search(r"p.g", "pig"))
  > <re.Match object; span=(0, 3), match='pig'>
  > ```



#### Wildcard& Character classes

- Wildcard

  > more than 1 character

- Character classes

  - square brackets`[]`

    > written inside square brackets and let us list the characters we want to match inside of those brackets.

  - Circumflex inside the square brackets`[^]`

    > match any characters that aren't in a group
    >
    > 
    >
    > ```python
    > >>> print(re.search(r"[^a-zA-Z]","This is a sentence with spaces."))
    > <re.Match object; span=(4, 5), match=' '>
    > ```

    > ```python
    > >>> print(re.search(r"[^a-zA-Z]","This is a sentence with spaces."))
    > <re.Match object; span=(4, 5), match=' '>
    > ```

  - pipe`|`

    > list alternative options that can get matched
    >
    > ```python
    > >>> print(re.search(r"cat|dog", "I like cats."))
    > <re.Match object; span=(7, 10), match='cat'>
    > ```

  - `re.findall()`

    > ```python
    > >>> print(re.findall(r"cat|dog", "I like both dogs and cats"))
    > ['dog', 'cat']
    > ```

  

  #### Repetition Qualifiers

  - `.*`

    > It matches any character repeated as many times as possible including zero.
    >
    > ```python
    > >>> print(re.search(r"Py.*n", "Pygmalion"))
    > <re.Match object; span=(0, 9), match='Pygmalion'>
    > ```
    >
    > 
    >
    > **`*` takes as many characters as possible.**
    >
    > > *Greedy*
    >
    > ```python
    > >>> print(re.search(r"Py.*n", "Python Programming"))
    > <re.Match object; span=(0, 17), match='Python Programmin'>
    > ```
    >
    > ```python
    > >>> print(re.search(r"Py[a-z]*n", "Python Programming"))
    > <re.Match object; span=(0, 6), match='Python'>
    > ```

    

  - `+`

    > It matches one or more occurrences of the character that comes before it.
    >
    > ```python
    > >>> print(re.search(r"o+l+", "wooolly"))
    > <re.Match object; span=(1, 6), match='oooll'>
    > ```
    >
    > `+` VS. ` *` 
    >
    > - `+` -> at least 1 times
    > - `*` -> 0+ times

    

  - `?`

    > It means either zero or one occurrence of the character before it. 
    >
    > ```python
    > >>> print(re.search(r"p?each", "To each their own"))
    > <re.Match object; span=(3, 7), match='each'>
    > ```

  

  #### Escaping characters

  - Slash`\`

    > ```python
    > >>> print(re.search(r"\.com", "Welcome"))
    > None
    > 
    > >>> print(re.search(r".com", "Welcome"))
    > <re.Match object; span=(2, 6), match='lcom'>
    > ```

  | Unicode |      Mean       |
  | :-----: | :-------------: |
  |  `\d`   |     `[0-9]`     |
  |  `\D`   |    `[^0-9]`     |
  |  `\s`   | `[\t\n\r\f\v]`  |
  |  `\S`   | `[^\t\n\r\f\v]` |
  |  `\w`   | `[a-zA-Z0-9_]`  |
  |  `\W`   | `[^a-zA-Z0-9_]` |

  ```python
  >>> print(re.search(r"\w*", "This is an example"))
  <re.Match object; span=(0, 4), match='This'>
  
  >>> print(re.search(r"\w*", "And_this_is_another"))
  <re.Match object; span=(0, 19), match='And_this_is_another'>
  ```

  

  #### Regular Expressions in Action

  ```python
  import re
  def check_sentence(text):
    result = re.search(r"^[A-Z][a-z\s]*\W$", text)
    return result != None
  
  print(check_sentence("Is this is a sentence?")) # True
  print(check_sentence("is this is a sentence?")) # False
  print(check_sentence("Hello")) # False
  print(check_sentence("1-2-3-GO!")) # False
  print(check_sentence("A star is born.")) # True
  ```

  

  #### Capturing Groups
  
  > portions of the pattern that are enclosed in parentheses
  >
  > ```python
  > >>> import re
  > >>> result = re.search(r"^(\w*), (\w*)$", "lovelace, Ada")
  > >>> print(result)
  > <re.Match object; span=(0, 13), match='lovelace, Ada'>
  > >>> print(result.groups())
  > ('lovelace', 'Ada')
  > ```
  >
  > ```python
  > >>> print(result[0])
  > lovelace, Ada
  > >>> print(result[1])
  > lovelace
  > >>> print(result[2])
  > Ada
  > ```
  >
  > 

#### Numeric repetition qualifiers`{}`

> ```python
> >>> print(re.search(r"[a-zA-Z]{5}", "a ghost"))
> <re.Match object; span=(2, 7), match='ghost'>
> ```
>
> ```python
> >>> print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
> ['scary', 'ghost', 'appea']
> ```
>
> ```python
> # use `\b`
> >>> print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
> ['scary', 'ghost']
> ```
>
> ```python
> >>> print(re.findall(r"\w{5,10}", "I really like strawberries"))
> ['really', 'strawberri']
> ```
>
> ```python
> >>> print(re.search(r"s\w{,20}", " I really like stawberries"))
> <re.Match object; span=(15, 26), match='stawberries'>
> ```



### `re.sub()`

> `re.sub(pattern, repl, string, count=0, flags=0)`
>
> 找到`text`中与`pattern`所匹配的形式，把`text`中与`pattern`所匹配的形式以外的用`repl`代替。

```python
import re


def transform_record(record):
    new_record = re.sub(r',', ',+1-', record, 1)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer
```

### `re.split()`

> `re.split(pattern, string, maxsplit=0, flags=0)`

```python
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```

