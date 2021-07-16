#tup1 = (0,1,2)
#tup2 = ('risk','hello','shit')

#print(tup1+tup2)

num_testCases = int(input())
i = 0
final_list = []
final_dictionary = {}
score = {}
while i < num_testCases :
    i = i+1
    Str = input()
    match_name = Str.split(':')[0]#print(match_name)
    match_details = Str.split(':')[1].split(',')#print(match_details)
    temp_dict = {}
    for j in match_details:
        player_name = j.split('-')[0]
        player_score = int(j.split('-')[1])
        temp_dict.update({player_name : player_score})
        try :
            score[player_name] += player_score
        except KeyError :
            score.update({player_name : player_score})
    final_dictionary.update({match_name : temp_dict})
print(final_dictionary)
for key,value in sorted(score.items(), key=lambda x: (x[1],x[0]), reverse=True):
    final_list.append((key,value))
print(final_list)
