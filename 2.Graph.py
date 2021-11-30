import networkx as nx
import os
import json
import matplotlib.pyplot as plt

G = nx.DiGraph()
username='elonmusk'
data_directory = "./output_friends/"
#screen_name='POTUS'

# Load the people I follow into a list
vahid_friends = []
with open(data_directory+"{username}.json".format(username=username),encoding = 'utf-8') as f:
        friends=json.loads(f.read())
        vahid_friends = [friend["screen_name"] for friend in friends]

for filename in os.listdir(data_directory):
    if (filename != "{username}.json".format(username=username)):
        with open(data_directory+filename,encoding = 'utf-8') as f:
            screen_name = filename.replace(".json","")
            friends = json.loads(f.read())
            
            G.add_node(screen_name,is_friend=True)

            # Add all of my friend's friends
            for friend in friends:
                    # If this friend is in vahid's list of friends, assign the is_friend attribute appropriately
                    if friend["screen_name"] in vahid_friends:
                        is_friend = True
                    else:
                        is_friend = False

                    G.add_node(friend["screen_name"], is_friend = is_friend)
                    G.add_edge(screen_name,friend["screen_name"])

degrees = [{"screen_name": n[0],  "degrees": list(nx.degree(G,n))[0][1]} for n in nx.get_node_attributes(G,'is_friend').items() if n[1] == False]
sorted_degrees = sorted(degrees, key=lambda k:k["degrees"], reverse=True)

# Get the top 50 (later i changed it to top 5 because of readability)
top_50 = sorted_degrees[1:6] # you can change it to more friend's suggestion
top_50

# Create a new graph that will only contain the top 50 friends of friends
G2 = nx.DiGraph()

data_directory = "./output_friends/"

# Load me into the graph
G2.add_node("{username}".format(username=username), friend_tier=0)

# Add User's Friends
with open(data_directory+"{username}.json".format(username=username),encoding = 'utf-8') as f:
        friends=json.loads(f.read())
        for friend in friends:
            G2.add_node(friend["screen_name"], friend_tier=1)
            #G2.add_edge("{username}".format(username=username),friend["screen_name"])

# Add User's Friends' Friends only if they appear in the top_5 list
for filename in os.listdir(data_directory):
    if (filename != "{username}.json".format(username=username)):
        with open(data_directory+filename,encoding = 'utf-8') as f:
            screen_name = filename.replace(".json","")
            friends = json.loads(f.read())

            for friend in friends:
                    # Add only the top_50 friends of friends
                    if any(d["screen_name"] == friend["screen_name"] for d in top_50):  
                        G2.add_node(friend["screen_name"], friend_tier=2)
                        G2.add_edge(screen_name,friend["screen_name"])

#Shells are the circles that nodes appear on the graph
shell_level_1 = []
shell_level_2 = []

# Add nodes to the appropriate circle
for n in nx.get_node_attributes(G2,'friend_tier').items():
    if n[1] == 2:
        shell_level_2.append(n[0])
    else:
        shell_level_1.append(n[0])

shells = [shell_level_1,shell_level_2]
pos = nx.shell_layout(G2,shells,scale=500)

pos["{username}".format(username=username)] =[0,0]


print("Friends Suggestion: ",top_50)
#nx.draw_networkx(G2,pos=pos,node_size=1,node_color="#cfcfcf",alpha=.3,arrowsize=1,font_size=2,width=.1,edge_color="#bdbdbd")
nx.draw_networkx(G2,pos=pos,node_size=1,node_color="blue",alpha=.5,arrowsize=1,font_size=2,width=.1,edge_color="red")
plt.savefig("{username}.png".format(username=username), dpi=1000)
plt.show()