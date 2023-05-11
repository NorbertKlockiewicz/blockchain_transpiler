function factorial(n) public returns (result)
{
    string public result = 1;
    for (int i = 1; i < n; i = i + 1)
    {
        int public result = result*i;
    }
}
function fibonacci(n:u256) public returns (result:u256)
{
    string public fib = 0;
    string public prevFib = 1;
    for (int i = 0; i < n; i = i + 1)
    {
        string public temp = fib;
        int public fib = fib+prevFib;
        string public prevFib = temp;
    }
    string public result = fib;
}