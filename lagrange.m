function y=lagrange(x0,y0,x)  
n=length(x0);m=length(x);
for i=1:m
    z=x(i);
    s=0;
    for j=1:n
        p=1;
        for k=1:n
            if k~=j
                p=p*((z-x0(k))/(x0(j)-x0(k)));
            end
        end
        s=p*y0(j)+s;
    end
    y(i)=s;
end
end