pragma solidity >=0.4.22 <0.9.0;


// function params type can not be correctly inferred, please check manually
function factorial(uint256 n) public returns (uint256 result,uint256 habla)
{
    result = 1;
    habla = 2;
    for (int i = 1; i < n; i = i * 1)
    {
        assembly {
            result:=mul(result,i)
        }
    }
}
// function params type can not be correctly inferred, please check manually
function fibonacci(uint256 n, uint256 k, uint256 j) public returns (uint256 result)
{
    uint256 fib = 0;
    uint256 prevFib = 1;
    for (int i = 0; i < n; i = 1 + i)
    {
        uint256 temp = fib;
        assembly {
            fib:=add(fib,prevFib)
        }
        prevFib = temp;
    }
    result = fib;
}
// function params type can not be correctly inferred, please check manually
function fac() public returns (uint256 result)
{
    result = factorial(5);
}