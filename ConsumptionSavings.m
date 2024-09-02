%%% Consumption and savings via Dynamic programming 

clear 
clf

%%%%%%%%%%%%%%%% parameters of the problem  %%%%%%%%%%%%
r = 0.06;  % interest rate 
beta = 0.9; % discount factor in the interval (0,1)
gamma = 0.5; % determines the utility function

%%%%%%%%%%%%%%%%%%%%

X=linspace(0.001,2); % state space % money in millions 
% Actions = linspace(0.001,2) %% action space % constraints are introduced below
N=20; % number of stages

%%%%%%%%%%%%%%%%%%%%%%%

valFUNCTs = zeros(N,length(X)); %value functions
valFUNCTs(N,:) = (beta)^N*X.^(1-gamma); 
OPTpolicy = zeros(N-1,length(X)); %optimal policy

for k = 1:N-1 
    for x = 1:length(X)
        A=linspace(0.00001,X(x)); %natural constraint of the problem
    [valFUNCTs(N-k,x),a]= max((beta^(N-k))*(A.^(1-gamma)) + interp1(X,valFUNCTs(N-k+1,:),(1+r)*(X(x)-A),'spline' ));
    %%% we're using a linear interpolation to approximate the values of
    %%% valFUNCTs(N-k+1,:) 
    %%% 'spline' interpolation 
    OPTpolicy(N-k,x) = A(a);
    end
end

plot(X,OPTpolicy(N-1,:),':',X,OPTpolicy(N-2,:),'--',X,OPTpolicy(1,:))
grid
xlabel('Available money x')
ylabel('Optimal withdrawal')


%%% one optimal path

x0 = 1; % initial condition

Xopt = zeros(1,N); % vector to save the optimal state path
Xopt(1) = x0;
Aopt = zeros(1,N-1)  % vector to save the optimal policy associated to x0

for k = 1:N-1
    Aopt(k) = interp1(X,OPTpolicy(k,:),Xopt(k));
    Xopt(k+1) = (1+r)*(Xopt(k)- Aopt(k));
end    

%plot(Xopt,'o')
%grid
%xlabel('Stage')
%ylabel('Optimal state path')

