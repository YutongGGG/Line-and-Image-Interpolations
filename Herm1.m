function [L]=Herm1(X,Y,Z)
[A,C,L]=Herm2(X,Y,Z);
% X1=1:0.01:5;
% Y1=polyval(C,X1);
% plot(X,Y,'*',X1,Y1,'r');
% grid on
% xlabel('x');
% ylabel('y');

function [A,C,L]=Herm2(X,Y,Z)
s=length(X);
n=2*s;
X2=zeros(1,n);
Y2=zeros(1,n);
Z2=zeros(1,n);
A=zeros(n,n);
for m=1:s
    X2(2*m-1)=X(m);
    X2(2*m)=X(m);
    Y2(2*m-1)=Y(m);
    Y2(2*m)=Y(m);
    Z2(2*m)=Z(m);
end
A(:,1)=Y2';
s=0.0;
p=1.0;
q=1.0;
c1=1.0;
for j=2:n
    for i=j:n
        if X2(i)==X2(i-j+1)
            A(i,j)=Z2(i);
        else
        A(i,j)=(A(i,j-1)-A(i-1,j-1))/(X2(i)-X2(i-j+1));
        end
    end
    b=poly(X2(j-1));
    q1=conv(q,b);
    c1=c1*j;
    q=q1;
end
C=A(n,n);
b=poly(X2(n));
q1=conv(q1,b);
for k=(n-1):-1:1
    C=conv(C,poly(X2(k)));
    d=length(C);
    C(d)=C(d)+A(k,k);
end
L(k,:)=poly2sym(C)