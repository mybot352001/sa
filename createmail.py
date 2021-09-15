# -*- coding: UTF-8 -*-
import os, sys, glob, shutil

abspath = os.path.dirname(__file__)
sys.path.append(abspath)

if abspath == '':
    os.chdir(sys.path[0])
else:
    os.chdir(abspath)

search_str = 'client_email'
i = 0
emails_list = []

if __name__ == '__main__':
    All_in_File = glob.glob(r'accounts/*.json')
    if len(All_in_File) > 0:
        for infile in All_in_File:
            read_all_lines_list = open(infile, 'r').readlines()
            one_fetch_line_list = [j for j in read_all_lines_list if j.find(search_str) > 0]
            one_fetch_line_str = ''.join(one_fetch_line_list)
            emails_str = one_fetch_line_str.replace('  "client_email": "', '').replace('",', '')
            emails_list.append(emails_str)
            i += 1
            print('Extracting: %d/%d\r' %(i,len(All_in_File)), end='')
            if i % 100 == 0:
                emails_list.append('(' + str(i) + '/' + str(len(All_in_File)) + ')')
                emails_list.append('\n''\n')

    out_txt = open('email.txt', 'w')
    out_txt.writelines(emails_list)
    out_txt.close()

