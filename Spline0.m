
function yy = Spline0(x, y, xx)

n = length(x);

a = y(1 : end - 1);

b = zeros(n - 1, 1);

d = zeros(n - 1, 1);

dx = diff(x);

dy = diff(y);

A = zeros(n);

B = zeros(n, 1);

A(1, 1) = 1;

A(n, n) = 1;

for i = 2 : n - 1

    A(i, i - 1) = dx(i - 1);

    A(i, i) = 2*(dx(i - 1) + dx(i));

    A(i, i + 1) = dx(i);

    B(i) = 3*(dy(i) / dx(i) - dy(i - 1) / dx(i - 1));

end

c = A \ B;

for i = 1 : n - 1

    d(i) = (c(i + 1) - c(i)) / (3 * dx(i));

    b(i) = dy(i) / dx(i) - dx(i)*(2*c(i) + c(i + 1)) / 3;

end

[mm, nn] = size(xx);

yy = zeros(mm, nn);

for i = 1 : mm*nn

    for ii = 1 : n - 1

        if xx(i) >= x(ii) && xx(i) < x(ii + 1)

            j = ii;

            break;

        elseif xx(i) == x(n)

            j = n - 1;

        end

    end

    yy(i) = a(j) + b(j)*(xx(i) - x(j)) + c(j)*(xx(i) - x(j))^2 + d(j)*(xx(i) - x(j))^3;

end
