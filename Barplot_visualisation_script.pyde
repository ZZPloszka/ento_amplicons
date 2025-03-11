add_library('pdf')


#======================================================================================
#                 This is a basic script for producing stacked barplots
#======================================================================================



#_____________________What you need to include in the input file______________________
#======================================================================================
#The input file should be a table in a .txt format with tabulation as separators
#The script assumes that the first two rows and columns contain labels:
#first row - hosts grouping category - e.g. host otu, zotu or taxonomy
#second row - sample labels - e.g. "specimen 1" or zotu if grouping category is otu
#first column - bacteria grouping category - e.g. bacteria otu, zotu or taxonomy
#second column - bacteria labels - e.g specific bacteria genotype
#The table cells should contain absolute abundance of bacteria
#======================================================================================



#___________________________________Table importing___________________________________
#======================================================================================
#Please input the path to your data file and its name below (it should be in .txt format):
input_path = "C:\Users\Walka\Downloads\Basic_Stacked_Barplot"
file_name = "data_tab1.txt"
#======================================================================================



#___________________________________Saving the PDF____________________________________
#======================================================================================
#Please input the output path for your PDF; Add "#" at the beginning to disable saving:
#beginRecord(PDF,"C:/Users/Walka/Downloads/Basic_Stacked_Barplot/Basic_Stacked_Barplot_16S.pdf")
#======================================================================================



#_____________________________________Settings________________________________________
#======================================================================================
#Bar size:
how_tall = 400
how_wide = 19
#======================================================================================
#Change gap size:
gap = 2
#======================================================================================
#Change the size of the background and its colour; background(255) for white:
size(2000,800)
background(255)
#======================================================================================
#Change offset:
x=50
y=170
#======================================================================================
#Change border colour and width or delete "#" in the last line to erase borders:
stroke(255) #border colour - 0 for black, 
strokeWeight(0.1) #border size
#noStroke()
#======================================================================================
#Change font size:
textSize(8)
#======================================================================================
#Colour pallete:
palette=("#2f4f4f","#2e8b57","#8b0000","#A0A020","#00008b","#ff0000","#ffa500","#ffff00","#00ff00","#ba55d3","#00ffff","#0000ff","#ff00ff","#1e90ff","#fa8072","#dda0dd","#ff1493","#98fb98","#87cefa","#ffe4c4","#EEEEEE")
host_palette=("#111111","#aaaaaa","#111111","#aaaaaa","#00008b","#ff0000","#ffa500","#ffff00","#00ff00","#ba55d3","#00ffff","#0000ff","#ff00ff","#1e90ff","#fa8072","#dda0dd","#ff1493","#98fb98","#87cefa","#ffe4c4","#ddff44")
#======================================================================================
#This is the number of bacteria labels shown in a single column of the legend
cut_legend=5
#This is the length of the gap between legends labels (x axis)
gap_legend=200
#======================================================================================
#This is the number of colours used:
num_col = 21
#======================================================================================
#How many bacteria do you want to keep? ! Introduces category - OTHER !
k=20
#======================================================================================
tax_group_top = 1
#======================================================================================



#OK, let's begin!



#The sacred starting ritual which imports and splits the file into rows
import os
os.chdir(input_path)
input = open(file_name,"r")
data = []
for row in input:
    Line=[]
    Line.append(row.strip().split("\t"))
    data += Line
input.close()


#This shortens the list of bacteria 
others_sum = ["Other","Other"]
summing=0
for sample in data[2:]:
    for bact in sample[2+k:]:
        summing+=float(bact)
    others_sum.append(summing)
    summing=0
#print(others_sum)
kill = len(data[0])-k
for sample in data:
    del sample[-kill:]


#This appends the "Other" group of bacteria
n=0
for sample in data:
    sample.append(others_sum[n])
    n+=1
n=0


#This makes a list - sums_in_hosts - containing the total absolute abundance of reads in each host
sums_in_hosts = []
summing = 0
for host in data[2:]:
    for bact in host[2:]:
        summing+=float(bact)
    sums_in_hosts.append(summing)
    summing=0


#variables used for later
n_sample = 0 #sets the counter for number of bacteria genotypes
n_otu=len(data[1])-1 #how many bacteria genotypes are there
n=0  #sets the universal counter
xx=x #for resetting X offset
yy=y #for resetting Y offset
nn=n #for resetting universal counters


#======================================================================================
#                     THIS PART IS FOR THE BARS AND COLOURS ORDER
#======================================================================================

"""
rel_abu=[] #this wil store the information about relative abundance of bacteria
c=0
for sample in data[1]:
    for bact in sample[2]:
        rel_abu.append(0)
for sample in data[2:]:
    for bact in sample[2:]:
        rel_abu[nn] += int(bact)/sums_in_hosts[c]
        nn+=1
    c+=1
    nn=n
c=0
rel_abu_new=[] #This will be important at the end, since the rel_abu will be deleted during counting
rel_abu_new+=rel_abu
#print(rel_abu)


positions=[] #This will store the positions of highest relative abundances in the list
for m in rel_abu:
    positions.append(rel_abu.index(max(rel_abu)))
    rel_abu[rel_abu.index(max(rel_abu))] = 0
pos_limited = positions[:num_col]
#print(positions)
"""
#GPT
#========================================================================================================================
# Calculate relative abundances
rel_abu = []  # This will store the information about the relative abundance of bacteria
c = 0
for sample in data[1]:
    for bact in sample[2:]:
        rel_abu.append(0)
for sample in data[2:]:
    for bact in sample[2:]:
        rel_abu[nn] += int(bact) / sums_in_hosts[c]
        nn += 1
    c += 1
    nn = n

# Backup the relative abundances for later use
rel_abu_new = []
rel_abu_new += rel_abu

# Determine positions of highest relative abundances
positions = []
for m in rel_abu:
    positions.append(rel_abu.index(max(rel_abu)))
    rel_abu[rel_abu.index(max(rel_abu))] = 0

# Ensure 'Other' is at the end of pos_limited
# Identify 'Other' position
other_position = positions.index(len(data[0]) - 1)  # 'Other' is added as the last element in the sample list
positions.remove(len(data[0]) - 1)  # Remove 'Other' from positions

# Limit to num_col - 1 positions, then add 'Other' at the end
pos_limited = positions[:num_col - 1] + [len(data[0]) - 1]

# Print positions for debugging
#print(positions)

# Print pos_limited for debugging
print(pos_limited)
#========================================================================================================================


xx=x #for resetting X offset
yy=y #for resetting Y offset
nn=n #for resetting counters


#======================================================================================
#                                    MAIN PART
#======================================================================================


#This part is the heart of the script, it makes the barplots
c=0
col_limit=len(palette) #This checks how many colours are in the palette in order not to count past this value
for sample in data[2:]:
    for bact in sample[2:]:
        if n_sample in pos_limited:    
            fill(palette[pos_limited.index(n_sample)])
        else:
            if c == 0:
                fill(200) #Change this to 190 or something for double color - useful without borders to show diversity of less abundant bacteria
                c=1
            else:
                fill(200)
                c=0
        rect(xx,yy,how_wide,float(bact)*how_tall/sums_in_hosts[nn])
        yy += float(bact)*how_tall/sums_in_hosts[nn]
        n_sample+=1
        if n_sample > n_otu:
            n_sample = 0
            xx+=how_wide+gap
            yy=y
            nn+=1


xx=x #for resetting X offset
yy=y #for resetting Y offset
nn=n #for resetting counters


#======================================================================================
#                                  TOP LABELS
#======================================================================================


#This gets the unique values of host otus or any other kind of grouping
unique_host_group = []
for m in data[2:]:
    if m[0] not in unique_host_group:
        unique_host_group.append(m[0])
#print(unique_host_group)


#This gets the full list of host otus or any other kind of grouping
host_grouping = []
for m in data[2:]:
    host_grouping.append(m[0])
#print(host_grouping)


#This checks how many hosts belong to specific groups
distances_hosts = []
for m in unique_host_group:
    distances_hosts.append(host_grouping.count(m))
#print(distances_hosts)


#This produces the grouping rectangles on top (and the text)
if tax_group_top != 0:
    stroke(0)
    textAlign(CENTER)
    textSize(10)
    for m in distances_hosts:
        if tax_group_top == 1:
            fill(255)
        elif tax_group_top == 2:
            fill(0)
        elif tax_group_top == 3:
            fill(host_palette[nn])
        elif tax_group_top == 4:
            fill(random(0, 255),random(0, 255),random(0, 255))
        rect(xx,yy-20,m*how_wide+gap*m-gap,15)
        fill(0)
        if tax_group_top == 1:
            text(unique_host_group[nn],xx+(m*how_wide+gap*m-gap)/2,yy-8)
        xx+=m*how_wide+m*gap
        nn+=1
    textAlign(LEFT)


xx=x #for resetting X offset
yy=y #for resetting Y offset
nn=n #for resetting counters


#This gets the list of host labels
host_labels = []
for m in data[2:]:
    host_labels.append(m[1])
#print(host_labels)


#This makes the host labels on the top of the graph
fill(0)
for m in data[2:]:
    rotate(-0.5*PI)
    text(host_labels[nn], 25-yy, xx+(0.6*how_wide))
    rotate(0.5*PI)
    nn+=1
    xx+=how_wide+gap


xx=x #for resetting X offset
yy=y #for resetting Y offset
nn=n #for resetting counters


#======================================================================================
#                                      LEGEND
#======================================================================================


#This makes the list of unique bacteria groupings names
unique_bact_group = []
for m in data[1]:
    if m not in unique_bact_group:
        unique_bact_group.append(m)
#print(unique_bact_group)


#This is the main body of the legend. It makes the squares and text at the bottom
y_legend=y+how_tall+25
y_leg=y_legend
c=0
for m in pos_limited:
    fill(palette[nn])
    rect(xx,y_leg,20,20)
    fill(0)
    text(unique_bact_group[pos_limited[nn]],xx+25,y_leg+12)
    y_leg+=20+gap
    nn+=1
    c+=1
    if c > cut_legend-1:
        xx+=gap_legend
        y_leg=y_legend
        c=0


#======================================================================================
#                               PERCENTAGE COUNTER
#======================================================================================

"""
textSize(17)
c=0
for m in pos_limited:
    c+=rel_abu_new[m]
c=c*10
round(c,8)
text(str("{:.1f}".format(c)) + "% of total relative abundance", xx, y_leg+30) #This weird :.lf is for producing a single decimal digit
#print(rel_abu_new)
"""

xx=x #for resetting X offset
yy=y #for resetting Y offset
nn=n #for resetting counters


#======================================================================================
#                                     LEFT AXIS
#======================================================================================


stroke(0)
strokeWeight(0.5)
textAlign(RIGHT)
textSize(12)
axis_labels = ('100%','80%','60%','40%','20%','0%')
for m in axis_labels:
    line(xx-15,yy,xx-5,yy)
    text(m,xx-18,yy+5)
    yy+=how_tall/(len(axis_labels)-1)


endRecord()
