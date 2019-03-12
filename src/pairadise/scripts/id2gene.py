import re,sys

gene_list=sys.argv[1];
annotation=sys.argv[2];#Gene Info file
ofile=sys.argv[3];
pos1=int(sys.argv[4]);#position in first file
pos2=int(sys.argv[5]);#position in second file
if len(sys.argv)>=7:#the regulation expression of level2
	level2=(sys.argv[6]);
	if level2=="":
		level2="[^\n]+";
else:
	level2="[^\n]+";
if len(sys.argv)>=8:#0 do not output the line without match
	flag=int(sys.argv[7]);
else:
	flag=1;
print(level2);print(flag);

ifile=open(gene_list);
#ifile.readline();
ilines=ifile.readlines();
gene_list=[];
for i in ilines:
	element=re.findall('[^ |\t\n]+',i);
	if len(element)<=pos1:
		gene_list.append('');continue;
	element_2=re.findall(level2,element[pos1]);
	gene_list.append(element_2[0]);
gene_line=ilines;
print(len(gene_list));print(len(gene_line));
print(gene_list[0]);print(gene_line[0]);print(element);
ifile.close();

ifile=open(annotation);
#ifile.readline();
ilines=ifile.readlines();
annotation_gene={};
for i in ilines:
	element=re.findall('[^ |\t\n]+',i);
	if len(element)<=pos2:
		continue;
	element_2=re.findall(level2,element[pos2]);
	#for j in element_2:	
	#	annotation_gene[j]=i;
	annotation_gene[element_2[0]]=i;
print(element);
print(len(ilines));
print(len(annotation_gene));
print(ilines[0]);print(annotation_gene.keys()[0]);
ifile.close();

ofile=open(ofile,'w');

for i in range(len(gene_list)):
	if gene_list[i] in annotation_gene:
		elements=re.findall('[^ "\n]+',annotation_gene[gene_list[i]]);
		ofile.write(gene_line[i][:-1]+'\t'+elements[-1]+'\n');
	else:
		if flag==1:
			ofile.write(gene_line[i][:-1]+'\n');
ofile.close();
