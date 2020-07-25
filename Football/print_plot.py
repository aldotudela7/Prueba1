# print_plot.py

def unique_list(dic, column):
    raw_list = [i[column] for i in dic]
    unique = list(set(raw_list))
    return unique

def plotGoals(results, team_name):
    '''
    Print a line graph showing goals scored and goals received
    for a specific team using its 3-letter code.
    '''
    gf = []
    ga = []
    gdiff = []
    teams = []

    matchdays = [i for i in range(1, 39, 1)]
    for team in results:
        if team['name'] == team_name:
            for matchday in matchdays:
                teams.append(team['name'])
                try:
                    gf.append(team['gf_'+str(matchday)])
                    ga.append(-team['ga_'+str(matchday)])
                    gdiff.append(team['gdiff_'+str(matchday)])
                except KeyError:
                    gf.append(None)
                    ga.append(None)
                    gdiff.append(None)

    
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_ylabel('Goals')
    title = 'Goals scored per match: '+team_name
    ax.set_title(title)

    ax.plot(matchdays, gf, color='green')
    ax.plot(matchdays, ga, color='red')
    ax.plot(matchdays, gdiff, color='black')

    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(90)
        label.set_fontsize(8)
    
    plt.tight_layout()
    plt.show()

def printTable(myDict, colList=None):
   """ 
   Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   # Sorting the standings from first to last place
   myDict.sort(key=lambda s: s['points'], reverse=True)
   
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] if item[col] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))