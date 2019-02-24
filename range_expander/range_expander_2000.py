# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:20:28 2019

@author: awohl
"""

def expand_ranges(row):
    rang = row
    
    assert len(str(rang[0])) and len(str(rang[1])) == 5, "Bad code length"
    
    def char_range(c1,c2):
        for c in range(ord(c1),ord(c2)+1):
            yield chr(c)
    
    #check if we have a numeric range only
    
    ####################Category I HCPCS/CPT##########################
    if rang[0].isdigit() and rang[1].isdigit():
        start = int(rang[0])
        end = int(rang[1])
        codes = []
        for num in range(start,end+1):
            if len(str(num)) < 2:
                code = '000' + str(num)
                codes.append(code)
            elif len(str(num)) < 3:
                code = '00' + str(num)
                codes.append(code)
            elif len(str(num)) < 4:
                code = '0' + str(num)
                codes.append(code)
            else:
                code = str(num)
                codes.append(code)
    else:
    #check if first character is a letter else assume last letter
    
    ############Category II HCPCS J9000 or K9020####################
        if (rang[0][0]).isalpha():
            
            #get the starting and ending letter of the ranges
            a = rang[0][0]
            b = rang[1][0]
            #make sure the alphabet isn't going backwards
            assert a < b,'Bad range detected'
            
            start_num = int(rang[0][1:])
            end_num = int(rang[1][1:])
            
            #check and see if they are the same
            if a != b:
                chrs = char_range(a,b)
                
                codes = []
                start = start_num
                end = 10000
                for category in chrs:
                    if category == b:
                        end = end_num
                    for num in range(start,end):
                        if len(str(num)) < 2:
                            code = category + '000' + str(num)
                            codes.append(code)
                        elif len(str(num)) < 3:
                            code = category + '00' + str(num)
                            codes.append(code)
                        elif len(str(num)) < 4:
                            code = category + '0' + str(num)
                            codes.append(code)
                        else:
                            code = category + str(num)
                            codes.append(code)
                    start = 0
                
            else:
                codes = []
                for num in range(start_num, end_num +1):
                    if len(str(num)) < 2:
                        code = category + '000' + str(num)
                        codes.append(code)
                    elif len(str(num)) < 3:
                        code = category + '00' + str(num)
                        codes.append(code)
                    elif len(str(num)) < 4:
                        code = category + '0' + str(num)
                        codes.append(code)
                    else:
                        code = category + str(num)
                        codes.append(code)
                
        else:
            #Category III CPT
            a = rang[0][-1]
            b = rang[1][-1]
            
            assert a < b,'Bad range detected'
            
            start_num = int(rang[0][:-1])
            end_num = int(rang[1][:-1]) 
            #check and see if they are the same
            if a != b:
                chrs = char_range(a,b)
                codes = []
                start = start_num
                end = 10000
                for category in chrs:
                    if category == b:
                        end = end_num
                    for num in range(start,end):
                        if len(str(num)) < 2:
                            code = '000' + str(num) + category
                            codes.append(code)
                        elif len(str(num)) < 3:
                            code = '00' + str(num) + category
                            codes.append(code)
                        elif len(str(num)) < 4:
                            code = '0' + str(num) + category
                            codes.append(code)
                        else:
                            code = str(num) + category
                            codes.append(code)
                    start = 0
                
            else:
                codes = []
                for num in range(start_num, end_num +1):
                    if len(str(num)) < 2:
                        code = '000' + str(num) + category
                        codes.append(code)
                    elif len(str(num)) < 3:
                        code = '00' + str(num) + category
                        codes.append(code)
                    elif len(str(num)) < 4:
                        code = '0' + str(num) + category
                        codes.append(code)
                    else:
                        code = str(num) + category
                        codes.append(code)
                        
    return codes

