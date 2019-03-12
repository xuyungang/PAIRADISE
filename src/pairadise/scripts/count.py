#This script calculates the inclusion level of RNA-Seq reads

import re,os,sys

#Inc.txt
ofile=open(sys.argv[2],'w');
ofile.write('IncLevel1\tIncLevel2\tIncLevelDifference\n');

def vec2float(vec):
	res=[];
	for i in vec:
		res.append(float(i));
	return(res);

def vecprod(vec):
	res=1;
	for i in vec:
		res=res*i;
	return(res);

def vec2psi(inc,skp,effective_inclusion_length,effective_skipping_length):
	psi=[];
	inclusion_length=effective_inclusion_length;
	skipping_length=effective_skipping_length;
	for i in range(len(inc)):
		if (float(inc[i])+float(skp[i]))==0:
			psi.append("NA");
		else:
			psi.append(str(round(float(inc[i])/inclusion_length/(float(inc[i])/inclusion_length+float(skp[i])/skipping_length),3)));
	return(psi);

#Data.txt
ifile=open(sys.argv[1]);
ifile.readline();
ilines=ifile.readlines();
for i in ilines:
	element=re.findall('[^\t\n]+',i);
	inc1=re.findall('[^,]+',element[1]);
	skp1=re.findall('[^,]+',element[2]);
	inc2=re.findall('[^,]+',element[3]);
	skp2=re.findall('[^,]+',element[4]);
	inc1=vec2float(inc1);
	skp1=vec2float(skp1);
	inc2=vec2float(inc2);
	skp2=vec2float(skp2);
	effective_inclusion_length=int(element[5]);
	effective_skipping_length=int(element[6]);
	psi1=vec2psi(inc1,skp1,effective_inclusion_length,effective_skipping_length);
	psi2=vec2psi(inc2,skp2,effective_inclusion_length,effective_skipping_length);
	psi1text='';psi2text='';sum1=0;sum2=0;count1=0;count2=0;
	total1=[];total2=[];
	for j in range(len(psi1)):
		psi1text+=psi1[j]+',';
		if psi1[j]!="NA":
			sum1+=float(psi1[j]);
			count1+=1;
			total1.append(inc1[j]+skp1[j]);
	for j in range(len(psi2)):
		psi2text+=psi2[j]+',';
		if psi2[j]!="NA":
			sum2+=float(psi2[j]);
			count2+=1;
			total2.append(inc2[j]+skp2[j]);
	if (count1*count2)==0:
		diff="NA";psi1="NA";psi2="NA";
	else:
		diff=str(round(sum1/count1-sum2/count2,3));
		psi1=str(round(sum1/count1,3));
		psi2=str(round(sum2/count2,3));
	if (len(total1)*len(total2))==0:
		continue;
	ofile.write(i[:-1]+'\t'+psi1text[:-1]+'\t'+psi2text[:-1]+'\t'+psi1+'\t'+psi2+'\t'+diff+'\t'+str(sum(total1)/len(total1))+'\t'+str(sum(total2)/len(total2))+'\n');
ofile.close();
