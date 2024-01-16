function SY(X,Y,Z)
n=length(X);
Y1=zeros(n,1);
A=2*eye(n);
for i=2:n-1
    A(i,i-1)=(X(i)-X(i-1))/(X(i+1)-X(i-1));
    A(i,i+1)=1-(X(i)-X(i-1))/(X(i+1)-X(i-1));
end
A(1,2)=1;
A(n,n-1)=1;
Y1(1)=6/(X(2)-X(1))*((Y(2)-Y(1))/(X(2)-X(1))-Z(1));
Y1(n)=6/(X(n)-X(n-1))*(Z(2)-(Y(n)-Y(n-1))/(X(n)-X(n-1)));
for i=2:n-1
    Y1(i)=6/(X(i+1)-X(i-1))*((Y(i+1)-Y(i))/(X(i+1)-X(i))-(Y(i)-Y(i-1))/(X(i)-X(i-1)));
end
U=A;
L=eye(n);
for k=1:n-1
    L(k+1:n,k)=U(k+1:n,k)/U(k,k);
    U(k+1:n,k+1:n)=U(k+1:n,k+1:n)-L(k+1:n,k)*U(k,k+1:n);
    U(k+1:n,k)=zeros(n-k,1);
end
for j=1:n-1
    Y1(j)=Y1(j)/L(j,j);
    Y1(j+1:n)=Y1(j+1:n)-Y1(j)*L(j+1:n,j);
end
Y1(n)=Y1(n)/L(n,n);
for j=n:-1:2
    Y1(j)=Y1(j)/U(j,j);
    Y1(1:j-1)=Y1(1:j-1)-Y1(j)*U(1:j-1,j);
end
Y1(1)=Y1(1)/U(1,1);
syms x;
for i=1:n-1
    y=Y1(i)/6*(X(i+1)-x).^3/(X(i+1)-X(i))+Y1(i+1)/6*(x-X(i)).^3/(X(i+1)-X(i))+(Y(i)-Y1(i)/6*(X(i+1)-X(i)).^2)*(X(i+1)-x)/(X(i+1)-X(i))+(Y(i+1)-Y1(i+1)/6*(X(i+1)-X(i)).^2)*(x-X(i))/(X(i+1)-X(i))
end