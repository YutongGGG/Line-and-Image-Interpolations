function [L]=Lagran1(X,Y)
[C,L,L1,l]=Lagran(X,Y);
X1=[7.0,10.5,13.0,17.5,34.0,40.5,44.5,48.0,56.0,61.0,68.5,76.5,80.5,91.0...
    96.0,101.0,104.0,106.5,111.5,118.0,123.5,136.5,142.0,146.0,150.0,157.0,158.0];
Y1=polyval(C,X1);
% plot(X,Y,'*',X1,Y1,'r');
% grid on;
% xlabel('x');
% ylabel('y');
end

function [C,L,L1,l]=Lagran(X,Y)
m=length(X);
L=ones(m,m);
for k=1:m
    v=1;
    for i=1:m
        if k~=i
            v=conv(v,poly(X(i)))/(X(k)-X(i));
        end
    end
    L1(k,:)=v;
    l(k,:)=poly2sym(v);
end
C=Y*L1;
L=Y*l;
end