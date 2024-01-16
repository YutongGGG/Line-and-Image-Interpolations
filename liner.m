function yy = liner(x,y,xx)
syms t;

if(length(x)==length(y))
    n=length(x);
else
    disp('false');
    return;
end

for i=1:n-1
    yy(i)=((t-x(i+1))/(x(i)-x(i+1)))*y(i)+((t-x(i))/(x(i+1)-x(i)))*y(i+1);
end

if(nargin==3)
	nn=length(xx);
for i=1:nn
    for j=1:n-1
        if(xx(i)>x(j)&xx(i)<=x(j+1))
             yynum(i)=subs(yy(j),'t',xx(i));  
        end
    end
end    
yy=yynum;
else
    yy=collect(yy);         
    yy=vpa(yy,6);            
end
end