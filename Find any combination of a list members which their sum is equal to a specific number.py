def jam(l,x):
  
  n=len(l)
  out=[]
  sum=0
  ls=[]


  for i in range (n):
    j=i

    while j<n and sum<x:
      sum=sum+l[j]
      j=j+1

    if sum==x:
      k=i

      while k<j:
       ls.append(l[k])
       k=k+1

      out.append(ls)


    sum=0
    ls=[]

  return out
