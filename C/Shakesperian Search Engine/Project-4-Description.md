# Project Description

## Overview

***You may work with a partner on this project and you may code it in JAVA.***

***Due Sunday, 4/22, at 11:59 PM.***

In this project, you're going to write a Shakespearean Search Engine.

Your program will take as input the texts of the Shakespeare's plays and build an *index* data structure. The index will allow you to look
up the play, act, scene, character, and line where a given word occurs in Shakespeare's plays.

For example, a query for the word *wherefore* would output an entry formatted like so,

```
Romeo and Juliet
Act II, Scene II
Juliet
JULIET	O Romeo, Romeo! wherefore art thou Romeo?
```

The fourth line of the output is the line taken from the play's script that contains this instance of the word *wherefore*.

The word *wherefore* occurs in other locations as well (five total times in *Romea and Juliet*) and your program must be able to print
similarly formatted entries for each unique occurrence.

## Details

The main challenge of this project is interpereting the spec and making appropriate design decisions. Therefore, you have pretty broad
freedom to structure your solutions that way you wish, but I'll give you a few tips to get started.

Don't procrastinate! You're going to need some time to think about your design! Ask me if you need clarifications!

Develop incrementally! Start with a small program that does the simplest possible thing: open a file and print its lines, perhaps. Then
make a small change to get slightly more functionality. Don't write more than 10-20 lines without compiling and testing. You can't write
a program this complex in one go.

Don't put all your code in one gigantic method.

### Classes

You should make a class called `SearchEngine` that implements the index. It should methods to build an index from a set of files and to 
lookup the entries in the index associated with a given word.

Create a `Driver` class with a `main` method to test your engine. I'm not providing automated tests, so you'll need to think about how
to test your solution. Think about edge cases! For example, what if the index receives a query for a word that it doesn't contain?

You'll probably also need an `Entry` class to represent a single mapping stored in the index. This is basically a state blob that
stores the play, act, scene, etc. for a given occurrence of a word.

### Files and Text

The `texts` directory contains scripts for three plays. You may assume that the engine will automatically build an index for any
`.txt` files in that directory. Do not hardcode in paths for the three given files.

The name of the play will always be the first line of the file.

The act and scenes will always be identified by `ACT` and `SCENE` appearing at the beginning of a line.

Character names appear at the beginning of a line.

Lines that continue a speech begun by a character are always indented by a single tab (`\t`).

Using these facts, you should be able to parse out the acts, scenes, and character names as you read through each line in the file.

Use the `Scanner` class to read through a file. I recommend using one `Scanner` to read over the lines of the file, then creating a
second `Scanner` to tokenize the words in each line. Relevant methods are `hasNext`, `next`, `hasNextLine`, and `nextLine`.

Ignore all punctutation other than apostrophes, which you should treat as part of a word. Hint: the `String` class has a `replaceAll`
method that can be used to remove all characters matching a regular expression. Try using it on a line after you've read it with
`Scanner`.

**For convenience, you may ignore all words with fewer than four letters**.

### Indexing

The index should be a `map: string --> list of index entries`. That is, for a given word, the index map should store a list
of index entry objects containing the information on all the occurrences of that word.

There are multiple `Map` classes: `TreeMap` and `HashMap` are good options. `ArrayList` or `LinkedList` can be used for the inner
list.

### Future Work

This is Phase I of a two-phase project. The second phase will involve putting your search engine onto a server and giving it a web-based
interface. It will be epic.

