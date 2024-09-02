%%% Pollution control in a lake 

clear 
clf

%%%%%%%%%%%%%%%% parameters  %%%%%%%%%%%%
b = 0.52;
q = 2;
kappa = 0.33;
beta = 0.997; % discount factor 0.997
%%%%%%%%%%%%%%%%%%%%

X=linspace(0.001,2.5,400); % state space %800
A=linspace(0.001,0.3,200); % state space %2000
%%%%%%%%%%%%%%%%%%%%%%%


v0 = log(X)-X.^2; %initial value function
policy = X; %optimal policy
v1 = X;
distance = 1;

while distance>0.9  %0.01
  for x = 1:length(X)
    [v1(x),a]= max(log(A)-kappa*X(x)^2 + beta*interp1(X,v0,b*X(x)+(X(x))^q/(1+(X(x))^q)+A,'spline' ));
    %%%'spline' interpolation to approximate valFUNCTs(N-k+1,:)
   policy(x) = A(a);
  end
  distance = max(abs(v1-v0))
  v0=v1;
end


subplot(2,1,1);
plot(X,policy,'.')
grid
xlabel('State x')
ylabel('Optimal download')


subplot(2,1,2);
plot(X,v1,'.')
grid
xlabel('State x')
ylabel('Net utility')





