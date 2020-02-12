# Grade

Yon serch engyne hath many fine attributes, yet possesseth a few problems.

The biggest issue is that you seem to be missing words taken from lines that contain a speaker's name. For example, searching for `sword`
brings up only the following results from *Romeo and Juliet*

```
'''
ROMEO AND JULIET
ACT I, SCENE I
BENVOLIO
 The fiery Tybalt, with his sword prepared,
'''

'''
ROMEO AND JULIET
ACT III, SCENE I
MERCUTIO
 enters the confines of a tavern claps me his sword
'''

'''
ROMEO AND JULIET
ACT III, SCENE I
MERCUTIO
 eight. Will you pluck your sword out of his pitcher
'''
```

I think this is caused by failing to remove all punctuation around words.

Words in square brackets are handled inconsistently. Sometimes they show up:

```
Good morrow to you, sir or madam. Please chooseth a word to findeth.
exeunt
Hereth art thine results...

'''
MACBETH
ACT IV, SCENE II
LADY
 [Exit LADY MACDUFF, crying 'Murder!' Exeunt
'''
```

There is also a minor inconsistency of carrying forward the name of the last speaker and using it for the stage directions.

I can get all of the stage directions that start with `Exit` if I search for `[Exit` which doesn't really make sense.

Total = 86 / 100
