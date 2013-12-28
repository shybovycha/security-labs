# Lab #1

## Task

Ваша задача дешифрувати останній шифротекст. (Зашифровані тексти записані англійською мовою).

## Solution

Let's create a program, which will help us to do the most of work. First of all, one should read 
the data given from the text file. Then it must get all the possible combinations of applying
the XOR operation to all text pairs. Then we'll just take the letters out of those pairs and xor 
them with the space character. To get the key, all we need is to find the letter that was hit
most times at the same place in all the XOR'red pairs.

## Explanation

    key:        66396e89c9dbd8 ?? 9874 ?? 2acd6395102eaf
    cipher[2]:  32510ba9a7b2bb a9 b800 5d 43a304b5714cc0
    text[2]:    The nice thing about...
    decoded[2]: The nicb t<ing abo

    key:        66 39 6e 89 c9 db d8 cb 98 74 61 2a cd 63 95 10 2e af
    cipher:     32 51 0b a9 a7 b2 bb a9 b8 00 5d 43 a3 04 b5 71 4c c0
    decoded:    T  h  e     n  i  c  b     t  <  i  n  g     a  b  o
    origin:     T  h  e     n  i  c  e     t  h  i  n  g     a  b  o


So, `'a9'.decode(hex) ^ 'cb'.decode(hex)` is `'b'` whilst should be `'e'` (hexadecimal ord is `65`).
Thus, we have an equation: `'a9' ^ X = '65'`. solving this, `X = 'cc'`.
And so for the `'h'` (`hex(ord('h')) == 68`): `'5d' ^ X = '68'`; `X = '35'`.

Replace these in the key:

    key:        66 39 6e 89 c9 db d8 cc 98 74 35 2a cd 63 95 10 2e af
    cipher:     32 51 0b a9 a7 b2 bb a9 b8 00 5d 43 a3 04 b5 71 4c c0
    decoded:    The nice thing abo
    origin:     The nice thing abo

---

So we can find mistakes, fix them, XOR them with the correspondent key fixes and go on...

    You don t #ant to
    You don't want to

    The cipoer ext pro
    The cipher_ext project

    Euler whul0 probab
    Euler while probably

    We can aac or the
    We can a?c?or the

    There aue  wo type
    There are two types

    We can teetthe poi
    We can see the point

    A (privfteykey)  e
    A (private key)  e

    The Coici'e Oxfor
    The Coi?i'? Oxford

Yet, adding the target text to the program' input does the most job:

    key (hex): 66396e89c9dbd8cb9874352acd6395102eafce78aa7fed28a06e6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba9a577335daefcecd59c433a6b268b60bf4ef03c9a611095bb9a3161edc704a33922cfd2d2c954376ea8c2027c2461e2a10845021b501089a1ba6025781145e902c4aba98aa8c0d1324c

    text[0]: We can aactor the number  5 with quantum computers. We can �& `�vt֮_6�H�=����?cK~����   ye�c��  ���P/�2c���"�e�����HBax    ���q�SG

    text[1]: Euler whuld probably enjoh that now his theorem becomes a cornGr stone of crypto - Acn��)�E�h���Xn:���f��O=*

    text[2]: The nicb thing about Keey}oq is now we cryptographers can drivG a lot of fancy cars   ��>�h�uX

    text[3]: The cipoertext produced bh a weak encryption algorithm looks aQ good as ciphertext po��3�N�yD���no$��C�P|��Y,.Tg�    nx��EA�Ƽ�0

    text[4]: You don t want to buy a stt of car keys from a guy who specialKzes in stealing cars   ��"
    �tI䔒xi1��K�Xw��I?gT?i�

    text[5]: There aue two types of crhptography - that which will keep secPets safe from your liyt��p�C�oX���|u2��L�A2��0g Kk�  Zup��e��&Fl

    text[6]: There aue two types of cyatography: one that allows the GovernOent to use brute forch ��p�X�zV�x;5��A�s��6"^ �    og��Ee����/U)

    text[7]: We can tee the point whert the chip is unhappy if a wrong bit Ks sent and consumes mbr�� �]�i爟p;"���[d��O5"TQKA�@)nt��

    text[8]: A (privfte-key)  encrypti~n scheme states 3 algorithms, namelya procedure for generlt��7�A�bN�ڑ=k$��A�@`��F*gp�*5��1��/@)

    text[9]:  The Coicise OxfordDictioary (2006) deﬁnes crypto as the arV of  writing o r solvdnË3�N�h�

    text[10]: The secuet message is: Whtn using a stream cipher, never use tJe key more than once

As you can see, we almost guessed the key:

    last key:    66396e89c9dbd8cb9874352acd6395102eafce78aa7fed28a06e6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba9a577335daefcecd59c433a6b268b60bf4ef03c9a611095bb9a3161edc704a33922cfd2d2c954376ea8c2027c2461e2a10845021b501089a1ba6025781145e902c4aba98aa8c0d1324c

    guessed key: 66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a06e6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba9a577335daefcecd59c433a6b268b60bf4ef03c9a611095bb9a3161edc704a33922cfd2d2c954376ea8c2027c2461e2a10845021b501089a1ba6025781145e902c4aba98aa8c0d1324c

We can fix the mistakes in the last message. Yet, the meaning we got:

    The secret message is: When using a stream cipher, never use the key more than once