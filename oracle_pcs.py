#!/usr/bin/python

import re
import os
import sys
debug = True

lines = sys.stdin.readlines()
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
lemma = sys.argv[1]

# INPUT:
# - lines contain a list of "%i:goal" where "%i" is the index of the goal
# - lemma contain the name of the lemma under scrutiny
# OUTPUT:
# - (on stdout) a list of ordered index separated by EOL


for line in lines:
    num = line.split(':')[0]

       
    if "attackerCannotGetLeakAfter2Iters" in lemma:
        print ("applying oracle to "+lemma)
        if re.match('.*State.*',line): l1.append(num)
        elif re.match('.*OldK1.*',line): l2.append(num)
        elif re.match('.*OldK2.*',line): l3.append(num)
        elif re.match('.*OldK3.*',line): l3.append(num)


        
    elif "compromiseK3" in lemma:
        print ("applying oracle to "+lemma)
        if re.match('.*Leak.*',line): l1.append(num)
        elif re.match('.*Update.*',line): l1.append(num)
        elif re.match('.*Secret.*',line): l1.append(num)
        elif re.match('.*OldK3.*',line): l2.append(num)
        elif re.match('.*OldK2.*',line): l2.append(num)
        elif re.match('.*OldK1.*',line): l3.append(num)
        elif re.match('.*State_3.*',line): l4.append(num)
        elif re.match('.*State_2.*',line): l5.append(num)
        elif re.match('.*State_1.*',line): l5.append(num)



        
    elif "leaks_can_happen" in lemma:
        print ("applying oracle to "+lemma)
        if re.match('.*Secret.*',line): l1.append(num)
        elif re.match('.*KU\( Rel.*',line): l1.append(num)
        elif re.match('.*Leak.*',line): l1.append(num)
        elif re.match('.*State.*',line): l2.append(num)
        elif re.match('.*OldK1.*',line): l3.append(num)
        elif re.match('.*OldK2.*',line): l4.append(num)
        elif re.match('.*OldK3.*',line): l5.append(num)

    elif "knowledge_implies_leakage" in lemma:
        print ("applying oracle to "+lemma)
        if re.match('.*Secret.*',line): l1.append(num)
        elif re.match('.*KU\( .*',line): l1.append(num)
        elif re.match('.*Leak.*',line): l1.append(num)
        elif re.match('.*OldK3.*',line): l2.append(num)
        elif re.match('.*OldK2.*',line): l2.append(num)
        elif re.match('.*OldK1.*',line): l3.append(num)
        elif re.match('.*State_3.*',line): l4.append(num)
        elif re.match('.*State_2.*',line): l5.append(num)
        elif re.match('.*State_1.*',line): l5.append(num)    

    elif "attackerRequiresLeak" in lemma:
        print ("applying oracle to "+lemma)
        if re.match('.*Secret.*',line): l1.append(num)
        elif re.match('.*KU\( .*',line): l1.append(num)
        elif re.match('.*Leak.*',line): l1.append(num)
        elif re.match('.*OldK3.*',line): l2.append(num)
        elif re.match('.*OldK2.*',line): l2.append(num)
        elif re.match('.*OldK1.*',line): l3.append(num)
        elif re.match('.*State_3.*',line): l4.append(num)
        elif re.match('.*State_2.*',line): l5.append(num)
        elif re.match('.*State_1.*',line): l5.append(num)    
        

    else:
        print ("applying standard heuristic to "+lemma)
        exit(0)

# Ordering all goals by ranking (higher first)
ranked=l1+l2+l3+l4+l5+l6
for goal in ranked:
    print (goal)
